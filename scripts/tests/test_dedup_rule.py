"""
Tests for the open-PR de-duplication rule inserted at Step 0 of git-workflow
instruction files and in kilo-code/orchestrator-mode.md.

Behaviour under test: an agent following Step 0 of git-workflow MUST halt before
dispatching planner work when an open PR already references the target issue.

All assertions encode domain rules and are mutation-resistant: deleting or
softening the rule text in ANY target file will fail the corresponding test.
"""

import subprocess
import sys
from pathlib import Path

import pytest

# ---------------------------------------------------------------------------
# Repo root — tests run from the repo root or from anywhere via pytest discovery
# ---------------------------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parents[2]

# ---------------------------------------------------------------------------
# The 10 target files that must carry the dedup rule
# ---------------------------------------------------------------------------

GIT_WORKFLOW_FILES = [
    REPO_ROOT / "claude-code" / ".claude" / "skills" / "git-workflow" / "SKILL.md",
    REPO_ROOT / "kilo-code" / ".kilocode" / "skills" / "git-workflow" / "SKILL.md",
    REPO_ROOT / "github-copilot" / ".github" / "skills" / "git-workflow" / "SKILL.md",
    REPO_ROOT / "augment-code" / ".augment" / "rules" / "git-workflow.md",
    REPO_ROOT / "cline" / ".clinerules" / "git-workflow.md",
    REPO_ROOT / "cursor" / ".cursor" / "rules" / "git-workflow.mdc",
    REPO_ROOT / "windsurf" / ".windsurf" / "rules" / "git-workflow.md",
    REPO_ROOT / "roo-code" / ".roo" / "rules" / "git-workflow.md",
    REPO_ROOT / "agents-md" / "AGENTS.md",
]

ORCHESTRATOR_MODE_FILE = (
    REPO_ROOT / "kilo-code" / ".kilocode" / "rules" / "orchestrator-mode.md"
)

ALL_CHANGED_FILES = GIT_WORKFLOW_FILES + [ORCHESTRATOR_MODE_FILE]

# ---------------------------------------------------------------------------
# Canonical strings that MUST appear in every target file
# ---------------------------------------------------------------------------

# The executable command string (not the full bash block, just the identifiable part)
GH_PR_LIST_COMMAND = "gh pr list --state open"

# The halt / no-duplicate-PR instruction
HALT_INSTRUCTION = "Do not open a new PR"

# The reroute option
REROUTE_INSTRUCTION = "plan-reviewer"


# ---------------------------------------------------------------------------
# Helper
# ---------------------------------------------------------------------------

def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


# ---------------------------------------------------------------------------
# Test 1: dedup rule block is present in all target files
#
# Behaviour: the dedup rule exists in every tool instruction surface.
# Mutation kill: deleting the block from any file fails this test.
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("filepath", ALL_CHANGED_FILES, ids=[p.name for p in ALL_CHANGED_FILES])
def test_dedup_rule_present(filepath: Path) -> None:
    """Every target file must contain the open-PR dedup rule."""
    assert filepath.exists(), f"File not found: {filepath}"
    content = read_text(filepath)
    assert "Open PR already exists" in content or "open PR" in content.lower(), (
        f"Dedup rule not found in {filepath.relative_to(REPO_ROOT)}\n"
        "Expected text signalling the open-PR check (e.g. 'Open PR already exists')"
    )


# ---------------------------------------------------------------------------
# Test 2: the gh pr list command is present in all git-workflow files
#
# Behaviour: the check is executable — an agent can copy/run the command.
# Mutation kill: removing the command string fails this test.
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("filepath", ALL_CHANGED_FILES, ids=[p.name for p in ALL_CHANGED_FILES])
def test_dedup_rule_contains_gh_pr_list_command(filepath: Path) -> None:
    """Every target file must contain the gh pr list --state open command."""
    assert filepath.exists(), f"File not found: {filepath}"
    content = read_text(filepath)
    assert GH_PR_LIST_COMMAND in content, (
        f"'{GH_PR_LIST_COMMAND}' not found in {filepath.relative_to(REPO_ROOT)}\n"
        "The dedup rule must include an executable gh pr list command."
    )


# ---------------------------------------------------------------------------
# Test 3: the halt instruction is present in all target files
#
# Behaviour: agents are explicitly directed not to open a duplicate PR.
# Mutation kill: softening "Do not open a new PR" to "consider not opening"
#               would fail this test.
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("filepath", ALL_CHANGED_FILES, ids=[p.name for p in ALL_CHANGED_FILES])
def test_dedup_rule_contains_halt_instruction(filepath: Path) -> None:
    """Every target file must explicitly prohibit opening a new PR when one exists."""
    assert filepath.exists(), f"File not found: {filepath}"
    content = read_text(filepath)
    assert HALT_INSTRUCTION in content, (
        f"Halt instruction '{HALT_INSTRUCTION}' not found in "
        f"{filepath.relative_to(REPO_ROOT)}\n"
        "The dedup rule must explicitly state 'Do not open a new PR'."
    )


# ---------------------------------------------------------------------------
# Test 4: the reroute option is present in all git-workflow files
#
# Behaviour: agents have a documented reroute path (delegate to plan-reviewer
#            with the existing PR as input) rather than only hard-halting.
# Mutation kill: removing the reroute sentence fails this test.
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("filepath", ALL_CHANGED_FILES, ids=[p.name for p in ALL_CHANGED_FILES])
def test_dedup_rule_contains_reroute_option(filepath: Path) -> None:
    """Every target file must mention rerouting to plan-reviewer with the existing PR."""
    assert filepath.exists(), f"File not found: {filepath}"
    content = read_text(filepath)
    assert REROUTE_INSTRUCTION in content, (
        f"Reroute instruction '{REROUTE_INSTRUCTION}' not found in "
        f"{filepath.relative_to(REPO_ROOT)}\n"
        "The dedup rule must document the reroute path to plan-reviewer."
    )


# ---------------------------------------------------------------------------
# Test 5: orchestrator-mode.md Process Enforcement section has the open-PR rule
#
# Behaviour: the orchestrator-level enforcement exists independently of the
#            per-tool git-workflow files.
# Mutation kill: removing from orchestrator-mode.md only fails THIS test,
#                not the parametrised tests above (which also cover that file).
# ---------------------------------------------------------------------------

def test_orchestrator_mode_contains_open_pr_check() -> None:
    """orchestrator-mode.md Process Enforcement section must list the open-PR hard rule."""
    assert ORCHESTRATOR_MODE_FILE.exists(), f"File not found: {ORCHESTRATOR_MODE_FILE}"
    content = read_text(ORCHESTRATOR_MODE_FILE)

    # The Process Enforcement section must exist
    assert "## Process Enforcement" in content, (
        "orchestrator-mode.md must have a '## Process Enforcement' section."
    )

    # Within that section, the open-PR rule must appear
    enforcement_start = content.index("## Process Enforcement")
    # Grab everything from that section to the next heading (or end of file)
    after_section = content[enforcement_start:]
    next_heading = after_section.find("\n## ", 3)
    section_body = after_section if next_heading == -1 else after_section[:next_heading]

    assert GH_PR_LIST_COMMAND in section_body, (
        f"'{GH_PR_LIST_COMMAND}' not found in the Process Enforcement section of "
        f"orchestrator-mode.md.\n"
        "The open-PR check must be a hard rule in the Process Enforcement section."
    )


# ---------------------------------------------------------------------------
# Test 6: unicode integrity — no hidden characters in changed files
#
# Behaviour: no zero-width spaces, BIDI overrides, or tag-block characters.
# Mutation kill: injecting a zero-width space (U+200B) into any changed file
#                causes the check-unicode-integrity.py script to exit 1.
# ---------------------------------------------------------------------------

def test_unicode_integrity_all_changed_files() -> None:
    """check-unicode-integrity.py must exit 0 for all changed files."""
    script = REPO_ROOT / "scripts" / "check-unicode-integrity.py"
    assert script.exists(), f"check-unicode-integrity.py not found at {script}"

    violations = []
    for filepath in ALL_CHANGED_FILES:
        if not filepath.exists():
            continue
        result = subprocess.run(
            [sys.executable, str(script), str(filepath.parent)],
            capture_output=True,
            text=True,
        )
        # The script accepts a directory; filter stdout to lines mentioning this file
        file_rel = filepath.name
        file_violations = [
            line for line in result.stdout.splitlines()
            if file_rel in line and "U+" in line
        ]
        violations.extend(file_violations)

    assert not violations, (
        "Hidden Unicode characters found in changed files:\n"
        + "\n".join(violations)
    )


# ---------------------------------------------------------------------------
# Test 7: no speciesist language introduced in changed files
#
# Behaviour: the dedup rule text must not introduce language that normalises
#            animal violence (e.g. "kill two birds with one stone").
# Mutation kill: adding a prohibited idiom to any file fails this test.
#
# Implementation note: requires semgrep + the NAV config. If semgrep is not
# available in the environment, the test is skipped rather than erroring, to
# avoid blocking CI on machines without semgrep installed.
# ---------------------------------------------------------------------------

SEMGREP_CONFIG = REPO_ROOT / "semgrep-no-animal-violence.yaml"


@pytest.mark.skipif(
    not SEMGREP_CONFIG.exists(),
    reason="semgrep-no-animal-violence.yaml not found — NAV check skipped",
)
def test_no_speciesist_language_introduced() -> None:
    """semgrep NAV check must pass on all changed files."""
    semgrep_result = subprocess.run(
        [
            "semgrep",
            "--config", str(SEMGREP_CONFIG),
            "--error",
            "--quiet",
        ] + [str(f) for f in ALL_CHANGED_FILES if f.exists()],
        capture_output=True,
        text=True,
    )
    assert semgrep_result.returncode == 0, (
        "Speciesist language detected in changed files:\n"
        + semgrep_result.stdout
        + semgrep_result.stderr
    )
