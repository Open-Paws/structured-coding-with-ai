#!/usr/bin/env python3
"""
Checks instruction files for hidden Unicode characters that could manipulate AI behavior.

Rules File Backdoor attack: attackers embed zero-width spaces, directional overrides,
or other invisible characters in .md/.yaml instruction files. When AI assistants
read these files, the hidden characters carry hidden instructions that override visible
content -- a supply chain attack against any project that copies these files.

This repo distributes instruction files to thousands of projects, making it a
high-value target. This script is the first line of defense.

Exit codes:
  0 -- no suspicious characters found
  1 -- one or more violations found (details printed to stdout)
"""

import sys
import os
from pathlib import Path
from typing import Iterator


# Characters explicitly allowed (standard whitespace used in all text files)
ALLOWED_WHITESPACE = {
    0x0009,  # TAB
    0x000A,  # LINE FEED (newline)
    0x000D,  # CARRIAGE RETURN
    0x0020,  # SPACE
}

# Suspicious Unicode ranges and codepoints that have no legitimate use
# in plain-text instruction files but are commonly used in backdoor attacks.
#
# Each entry is (codepoint_or_range, description).
# Ranges are (start, end) inclusive tuples; single codepoints are plain ints.
SUSPICIOUS: list[tuple[int | tuple[int, int], str]] = [
    # Zero-width / invisible characters
    (0x00AD, "SOFT HYPHEN — invisible in most renderers"),
    (0x200B, "ZERO WIDTH SPACE"),
    (0x200C, "ZERO WIDTH NON-JOINER"),
    (0x200D, "ZERO WIDTH JOINER"),
    (0x2060, "WORD JOINER (invisible separator)"),
    (0x2061, "FUNCTION APPLICATION (invisible)"),
    (0x2062, "INVISIBLE TIMES"),
    (0x2063, "INVISIBLE SEPARATOR"),
    (0x2064, "INVISIBLE PLUS"),
    (0xFEFF, "ZERO WIDTH NO-BREAK SPACE / BOM"),
    # Bidirectional text overrides — used to reverse visible text
    ((0x202A, 0x202E), "BIDI OVERRIDE (U+202A–U+202E)"),
    ((0x2066, 0x2069), "BIDI ISOLATE (U+2066–U+2069)"),
    (0x200E, "LEFT-TO-RIGHT MARK"),
    (0x200F, "RIGHT-TO-LEFT MARK"),
    (0x061C, "ARABIC LETTER MARK"),
    # Variation selectors — can silently alter glyph rendering
    ((0xFE00, 0xFE0F), "VARIATION SELECTOR (U+FE00–U+FE0F)"),
    ((0xE0100, 0xE01EF), "VARIATION SELECTOR SUPPLEMENT"),
    # Tag characters — invisible ASCII lookalikes used in prompt injection
    ((0xE0000, 0xE007F), "TAGS BLOCK (invisible ASCII lookalikes)"),
    # Private Use Area — no legitimate use in shared instruction files
    ((0xE000, 0xF8FF), "PRIVATE USE AREA (BMP)"),
    ((0xF0000, 0xFFFFF), "SUPPLEMENTARY PRIVATE USE AREA-A"),
    ((0x100000, 0x10FFFF), "SUPPLEMENTARY PRIVATE USE AREA-B"),
    # C0 / C1 control characters (excluding standard whitespace handled above)
    ((0x0001, 0x0008), "C0 CONTROL (non-printable, non-whitespace)"),
    ((0x000B, 0x000C), "C0 CONTROL (vertical tab / form feed)"),
    ((0x000E, 0x001F), "C0 CONTROL (non-printable)"),
    (0x007F, "DELETE (DEL)"),
    ((0x0080, 0x009F), "C1 CONTROL CHARACTERS"),
]


def is_suspicious(codepoint: int) -> str | None:
    """Return a description if the codepoint is suspicious, else None."""
    if codepoint in ALLOWED_WHITESPACE:
        return None
    for entry, description in SUSPICIOUS:
        if isinstance(entry, tuple):
            start, end = entry
            if start <= codepoint <= end:
                return description
        elif codepoint == entry:
            return description
    return None


def scan_file(path: Path) -> list[tuple[int, int, str, str]]:
    """
    Scan a single file for suspicious Unicode characters.

    Returns a list of (line_number, column, hex_code, description) tuples.
    Line numbers are 1-based; columns are 0-based character offsets within the line.
    """
    violations: list[tuple[int, int, str, str]] = []
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError as exc:
        print(f"WARNING: cannot read {path}: {exc}", file=sys.stderr)
        return violations

    for line_num, line in enumerate(text.splitlines(keepends=True), start=1):
        for col, char in enumerate(line):
            description = is_suspicious(ord(char))
            if description is not None:
                hex_code = f"U+{ord(char):04X}"
                violations.append((line_num, col, hex_code, description))

    return violations


def find_instruction_files(root: Path) -> Iterator[Path]:
    """Yield all instruction files that should be scanned."""
    extensions = {".md", ".yaml", ".yml", ".json", ".cursorrules", ".mdc"}
    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        # Skip the .git directory
        if ".git" in path.parts:
            continue
        if path.suffix.lower() in extensions or path.name in {
            ".cursorrules",
            ".roomodes",
        }:
            yield path


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    if not root.is_dir():
        print(f"ERROR: {root} is not a directory", file=sys.stderr)
        return 2

    total_violations = 0
    files_scanned = 0

    for path in find_instruction_files(root):
        files_scanned += 1
        violations = scan_file(path)
        if violations:
            for line_num, col, hex_code, description in violations:
                rel = path.relative_to(root)
                print(f"{rel}:{line_num}:{col}: {hex_code} — {description}")
            total_violations += len(violations)

    if total_violations:
        print(
            f"\nFAIL: {total_violations} suspicious character(s) found "
            f"across {files_scanned} file(s) scanned.",
            file=sys.stderr,
        )
        print(
            "These characters have no legitimate use in instruction files and may "
            "indicate a Rules File Backdoor attack.\n"
            "Remove them or open an issue if you believe this is a false positive.",
            file=sys.stderr,
        )
        return 1

    print(
        f"OK: {files_scanned} file(s) scanned. No suspicious Unicode characters found."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
