"""Tests for pipeline_watchdog.py.

The watchdog strips the status:done label from GitHub issues that were marked
done without a closing PR or commit evidence. This suite encodes the three
fixed behaviours introduced by the bug fix:

1. Label mutation happens before the strip-comment is posted.
2. The strip-comment is suppressed when the label mutation fails.
3. The strip-comment is posted when the label mutation succeeds.
4. Failed mutations are written to the orchestrator log as structured entries.
5. The drift-repair pass re-attempts label removal on any issue that already
   has the strip-comment but still carries status:done.

Each test names the rule it encodes and specifies the mutation that kills it.
"""

from __future__ import annotations

import json
import os
import stat
import subprocess
import sys
import textwrap
from pathlib import Path

import pytest

# ---------------------------------------------------------------------------
# Load module under test
# ---------------------------------------------------------------------------

import importlib.util

_watchdog_path = Path(__file__).parent.parent / "pipeline_watchdog.py"
_spec = importlib.util.spec_from_file_location("pipeline_watchdog", _watchdog_path)
_watchdog = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_watchdog)

strip_status_done = _watchdog.strip_status_done
drift_repair_pass = _watchdog.drift_repair_pass


# ---------------------------------------------------------------------------
# Mock gh binary helpers
# ---------------------------------------------------------------------------

def _write_mock_gh(path: Path, exit_code_for_edit: int, labels: list[str], comments: list[str]) -> None:
    """Write a mock gh binary that records calls and returns configurable exit codes.

    The mock records every invocation (argv) into a JSON-lines call log at
    <path>.calls. Responses vary by sub-command:

    - `gh issue edit ... --remove-label ...`  → exit_code_for_edit
    - `gh issue comment ...`                  → exit 0 (always)
    - `gh issue view ... --json labels,comments` → stdout JSON, exit 0
    """
    labels_json = json.dumps(labels)
    comments_json = json.dumps(comments)

    # Build the mock script content
    script = textwrap.dedent(f"""\
        #!/usr/bin/env python3
        import json, sys, os

        argv = sys.argv[1:]
        log_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "gh.calls")
        with open(log_path, "a") as f:
            f.write(json.dumps(argv) + "\\n")

        if "issue" in argv and "edit" in argv and "--remove-label" in argv:
            sys.exit({exit_code_for_edit})
        elif "issue" in argv and "comment" in argv:
            sys.exit(0)
        elif "issue" in argv and "view" in argv and "--json" in argv:
            labels = {labels_json}
            comments = {comments_json}
            print(json.dumps({{"labels": labels, "comments": comments}}))
            sys.exit(0)
        else:
            sys.exit(0)
    """)

    path.write_text(script, encoding="utf-8")
    path.chmod(path.stat().st_mode | stat.S_IEXEC | stat.S_IXGRP | stat.S_IXOTH)


def _read_calls(mock_gh_path: Path) -> list[list[str]]:
    """Return all recorded call argument lists."""
    calls_file = mock_gh_path.parent / "gh.calls"
    if not calls_file.exists():
        return []
    lines = calls_file.read_text(encoding="utf-8").strip().splitlines()
    return [json.loads(line) for line in lines if line.strip()]


# ---------------------------------------------------------------------------
# Test 1 — Mutation-first behaviour
#
# Rule: gh issue edit --remove-label is called before gh issue comment.
# Mutation: swap call order in strip_status_done — mutation causes this test
# to fail because comment call appears before edit call in the log.
# ---------------------------------------------------------------------------

def test_mutation_first_behaviour(tmp_path: Path) -> None:
    mock_gh = tmp_path / "gh"
    _write_mock_gh(mock_gh, exit_code_for_edit=0, labels=["status:done"], comments=[])
    log_path = tmp_path / "orchestrator.log"

    env = {**os.environ, "PATH": str(tmp_path) + os.pathsep + os.environ.get("PATH", "")}
    strip_status_done(
        repo="Open-Paws/structured-coding-with-ai",
        issue_number=46,
        log_path=log_path,
        gh_path=str(mock_gh),
    )

    calls = _read_calls(mock_gh)
    # Find positions of edit and comment calls
    edit_positions = [i for i, c in enumerate(calls) if "edit" in c and "--remove-label" in c]
    comment_positions = [i for i, c in enumerate(calls) if "comment" in c]

    assert edit_positions, "gh issue edit --remove-label was not called"
    assert comment_positions, "gh issue comment was not called"
    # The mutation (label removal) must precede the comment
    assert edit_positions[0] < comment_positions[0], (
        "label mutation must happen before strip-comment is posted"
    )


# ---------------------------------------------------------------------------
# Test 2 — Comment suppressed on mutation failure
#
# Rule: when gh issue edit exits non-zero, gh issue comment is never called.
# Mutation: remove the exit-code guard in strip_status_done — mutation causes
# this test to fail because comment call appears in the log.
# ---------------------------------------------------------------------------

def test_comment_suppressed_on_mutation_failure(tmp_path: Path) -> None:
    mock_gh = tmp_path / "gh"
    _write_mock_gh(mock_gh, exit_code_for_edit=1, labels=["status:done"], comments=[])
    log_path = tmp_path / "orchestrator.log"

    strip_status_done(
        repo="Open-Paws/structured-coding-with-ai",
        issue_number=46,
        log_path=log_path,
        gh_path=str(mock_gh),
    )

    calls = _read_calls(mock_gh)
    comment_calls = [c for c in calls if "comment" in c]
    assert not comment_calls, (
        "strip-comment must not be posted when label mutation fails"
    )


# ---------------------------------------------------------------------------
# Test 3 — Comment posted on mutation success
#
# Rule: when gh issue edit exits 0, gh issue comment IS called.
# Mutation: invert the success guard (post comment only on failure) — mutation
# causes this test to fail because comment call is absent in the log.
# ---------------------------------------------------------------------------

def test_comment_posted_on_mutation_success(tmp_path: Path) -> None:
    mock_gh = tmp_path / "gh"
    _write_mock_gh(mock_gh, exit_code_for_edit=0, labels=["status:done"], comments=[])
    log_path = tmp_path / "orchestrator.log"

    strip_status_done(
        repo="Open-Paws/structured-coding-with-ai",
        issue_number=46,
        log_path=log_path,
        gh_path=str(mock_gh),
    )

    calls = _read_calls(mock_gh)
    comment_calls = [c for c in calls if "comment" in c]
    assert comment_calls, (
        "strip-comment must be posted when label mutation succeeds"
    )


# ---------------------------------------------------------------------------
# Test 4 — Failure logged on non-zero exit
#
# Rule: when gh issue edit exits non-zero, a structured error entry is written
# to the orchestrator log containing repo, issue number, and exit code.
# Mutation: remove the log-write call from the failure branch — mutation causes
# this test to fail because no log entry is present.
# ---------------------------------------------------------------------------

def test_failure_logged_on_nonzero_exit(tmp_path: Path) -> None:
    mock_gh = tmp_path / "gh"
    _write_mock_gh(mock_gh, exit_code_for_edit=1, labels=["status:done"], comments=[])
    log_path = tmp_path / "orchestrator.log"

    strip_status_done(
        repo="Open-Paws/context",
        issue_number=82,
        log_path=log_path,
        gh_path=str(mock_gh),
    )

    assert log_path.exists(), "orchestrator log must be written on failure"
    log_content = log_path.read_text(encoding="utf-8")

    # Parse each line as a JSON entry
    entries = []
    for line in log_content.strip().splitlines():
        try:
            entries.append(json.loads(line))
        except json.JSONDecodeError:
            pass

    assert entries, "log must contain at least one structured JSON entry"
    entry = entries[-1]

    # The entry must encode the three required fields
    assert "repo" in entry and "Open-Paws/context" in str(entry["repo"]), (
        "log entry must contain repo field"
    )
    assert "issue" in entry and entry["issue"] == 82, (
        "log entry must contain issue number"
    )
    assert "exit_code" in entry and entry["exit_code"] != 0, (
        "log entry must contain non-zero exit code"
    )


# ---------------------------------------------------------------------------
# Test 5 — Drift-repair pass fires on stale comment
#
# Rule: when an issue already has the strip-comment AND still has status:done,
# drift_repair_pass must call gh issue edit --remove-label for that issue.
# Mutation: remove the drift-repair scan from drift_repair_pass — mutation
# causes this test to fail because no edit call appears in the log.
# ---------------------------------------------------------------------------

STRIP_COMMENT_BODY = "[pipeline-watchdog] Stripped `status:done`"


def test_drift_repair_fires_on_stale_comment(tmp_path: Path) -> None:
    mock_gh = tmp_path / "gh"
    stale_comments = [{"body": STRIP_COMMENT_BODY}]
    _write_mock_gh(
        mock_gh,
        exit_code_for_edit=0,
        labels=["status:done"],
        comments=stale_comments,
    )
    log_path = tmp_path / "orchestrator.log"

    drift_repair_pass(
        repos_and_issues=[("Open-Paws/context", 82)],
        log_path=log_path,
        gh_path=str(mock_gh),
    )

    calls = _read_calls(mock_gh)
    edit_calls = [c for c in calls if "edit" in c and "--remove-label" in c]
    assert edit_calls, (
        "drift-repair pass must call gh issue edit --remove-label on stale issues"
    )


# ---------------------------------------------------------------------------
# Test 6 — Drift-repair is a no-op when label already removed
#
# Rule: when an issue has the strip-comment but does NOT have status:done,
# drift_repair_pass must NOT call gh issue edit --remove-label (already clean).
# Mutation: remove the label-presence check — mutation causes this test to
# fail because an edit call appears even for already-clean issues.
# ---------------------------------------------------------------------------

def test_drift_repair_noop_when_label_absent(tmp_path: Path) -> None:
    mock_gh = tmp_path / "gh"
    # Issue has strip-comment but status:done is already gone
    stale_comments = [{"body": STRIP_COMMENT_BODY}]
    _write_mock_gh(
        mock_gh,
        exit_code_for_edit=0,
        labels=[],  # status:done already removed
        comments=stale_comments,
    )
    log_path = tmp_path / "orchestrator.log"

    drift_repair_pass(
        repos_and_issues=[("Open-Paws/context", 82)],
        log_path=log_path,
        gh_path=str(mock_gh),
    )

    calls = _read_calls(mock_gh)
    edit_calls = [c for c in calls if "edit" in c and "--remove-label" in c]
    assert not edit_calls, (
        "drift-repair pass must not call gh issue edit when status:done is already removed"
    )
