"""Tests for check-unicode-integrity.py.

Validates detection of hidden Unicode characters that indicate a Rules File
Backdoor attack in instruction files.
"""

import importlib.util
import sys
from pathlib import Path

# The script uses hyphens in the filename — must use importlib to load it
_script_path = (
    Path(__file__).parent.parent / "check-unicode-integrity.py"
)
_spec = importlib.util.spec_from_file_location(
    "check_unicode_integrity", _script_path
)
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)

is_suspicious = _module.is_suspicious
scan_file = _module.scan_file
find_instruction_files = _module.find_instruction_files
main = _module.main


# ---------------------------------------------------------------------------
# is_suspicious
# ---------------------------------------------------------------------------

class TestIsSuspicious:
    def test_regular_ascii_clean(self):
        assert is_suspicious(ord("a")) is None

    def test_standard_newline_clean(self):
        assert is_suspicious(0x000A) is None

    def test_standard_space_clean(self):
        assert is_suspicious(0x0020) is None

    def test_tab_clean(self):
        assert is_suspicious(0x0009) is None

    def test_zero_width_space_flagged(self):
        result = is_suspicious(0x200B)
        assert result is not None
        assert "ZERO WIDTH" in result

    def test_zero_width_joiner_flagged(self):
        assert is_suspicious(0x200D) is not None

    def test_bidi_override_flagged(self):
        # U+202A BIDI override
        assert is_suspicious(0x202A) is not None

    def test_bidi_override_end_of_range_flagged(self):
        # U+202E is the end of the range
        assert is_suspicious(0x202E) is not None

    def test_bidi_outside_range_clean(self):
        # U+202F is just above the bidi range — should be clean
        assert is_suspicious(0x202F) is None

    def test_variation_selector_flagged(self):
        assert is_suspicious(0xFE00) is not None

    def test_tags_block_flagged(self):
        assert is_suspicious(0xE0000) is not None

    def test_private_use_area_flagged(self):
        assert is_suspicious(0xE001) is not None

    def test_c0_control_flagged(self):
        # U+0001 (non-printable control)
        assert is_suspicious(0x0001) is not None

    def test_delete_char_flagged(self):
        assert is_suspicious(0x007F) is not None

    def test_soft_hyphen_flagged(self):
        assert is_suspicious(0x00AD) is not None

    def test_bom_flagged(self):
        assert is_suspicious(0xFEFF) is not None


# ---------------------------------------------------------------------------
# scan_file
# ---------------------------------------------------------------------------

class TestScanFile:
    def test_clean_file_returns_empty(self, tmp_path):
        f = tmp_path / "clean.md"
        f.write_text("# Hello\nThis is clean text.\n", encoding="utf-8")
        assert scan_file(f) == []

    def test_file_with_zero_width_space_flagged(self, tmp_path):
        f = tmp_path / "sneaky.md"
        # Embed a zero-width space after 'Hello'
        content = "Hello\u200BWorld\n"
        f.write_bytes(content.encode("utf-8"))
        violations = scan_file(f)
        assert len(violations) == 1
        line_num, col, hex_code, description = violations[0]
        assert line_num == 1
        assert col == 5
        assert hex_code == "U+200B"
        assert "ZERO WIDTH" in description

    def test_file_with_multiple_violations(self, tmp_path):
        f = tmp_path / "multi.md"
        content = "A\u200BB\u200CC\n"  # two zero-width chars on same line
        f.write_bytes(content.encode("utf-8"))
        violations = scan_file(f)
        assert len(violations) == 2

    def test_missing_file_returns_empty(self, tmp_path):
        # OSError on unreadable — returns empty list without crashing
        result = scan_file(tmp_path / "nonexistent.md")
        assert result == []

    def test_violation_on_second_line(self, tmp_path):
        f = tmp_path / "second_line.md"
        content = "Clean first line\nSecond\u200B line\n"
        f.write_bytes(content.encode("utf-8"))
        violations = scan_file(f)
        assert len(violations) == 1
        assert violations[0][0] == 2  # line number


# ---------------------------------------------------------------------------
# find_instruction_files
# ---------------------------------------------------------------------------

class TestFindInstructionFiles:
    def test_yields_md_files(self, tmp_path):
        (tmp_path / "rules.md").write_text("# rules")
        found = list(find_instruction_files(tmp_path))
        assert any(f.name == "rules.md" for f in found)

    def test_yields_yaml_files(self, tmp_path):
        (tmp_path / "config.yaml").write_text("key: val")
        found = list(find_instruction_files(tmp_path))
        assert any(f.name == "config.yaml" for f in found)

    def test_skips_python_files(self, tmp_path):
        (tmp_path / "script.py").write_text("x = 1")
        found = list(find_instruction_files(tmp_path))
        assert not any(f.suffix == ".py" for f in found)

    def test_skips_git_directory(self, tmp_path):
        git_dir = tmp_path / ".git"
        git_dir.mkdir()
        (git_dir / "config.md").write_text("git config")
        found = list(find_instruction_files(tmp_path))
        assert not any(".git" in str(f) for f in found)

    def test_yields_json_files(self, tmp_path):
        (tmp_path / "config.json").write_text("{}")
        found = list(find_instruction_files(tmp_path))
        assert any(f.name == "config.json" for f in found)


# ---------------------------------------------------------------------------
# main (integration)
# ---------------------------------------------------------------------------

class TestMain:
    def test_clean_directory_returns_zero(self, tmp_path):
        (tmp_path / "readme.md").write_text("# Clean\n")
        sys.argv = ["check-unicode-integrity.py", str(tmp_path)]
        assert main() == 0

    def test_directory_with_violation_returns_one(self, tmp_path):
        f = tmp_path / "sneaky.md"
        f.write_bytes("Hello\u200BWorld".encode("utf-8"))
        sys.argv = ["check-unicode-integrity.py", str(tmp_path)]
        assert main() == 1

    def test_nonexistent_directory_returns_two(self, tmp_path):
        missing = str(tmp_path / "nonexistent")
        sys.argv = ["check-unicode-integrity.py", missing]
        assert main() == 2
