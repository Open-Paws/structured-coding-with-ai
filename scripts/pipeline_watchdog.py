#!/usr/bin/env python3
"""Pipeline watchdog — strips status:done labels from GitHub issues applied
without commit or PR evidence.

Operation ordering (the fix):
  1. Attempt label mutation first: ``gh issue edit --remove-label status:done``
  2. Only post the strip-announcement comment if mutation exits 0.
  3. On non-zero exit, write a structured JSON entry to the orchestrator log.

The previous (buggy) ordering posted the comment first, then attempted the
mutation. When the mutation failed silently the comment became the only
durable trace, leaving the label in place.

Drift-repair pass:
  Re-scans a list of known (repo, issue) pairs. For each issue that still
  carries the strip-comment AND the status:done label, re-attempts label
  removal. This heals issues left in the broken state by the original bug.

Usage (programmatic):
    from pipeline_watchdog import strip_status_done, drift_repair_pass

    strip_status_done(
        repo="Open-Paws/context",
        issue_number=82,
        log_path=Path("pipeline/watchdog.log"),
    )

    drift_repair_pass(
        repos_and_issues=[("Open-Paws/context", 82)],
        log_path=Path("pipeline/watchdog.log"),
    )

Usage (CLI):
    python scripts/pipeline_watchdog.py strip --repo Open-Paws/context \\
        --issue 82 --log pipeline/watchdog.log

    python scripts/pipeline_watchdog.py drift-repair \\
        --log pipeline/watchdog.log \\
        Open-Paws/context:82 Open-Paws/platform:87
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Sequence

# The exact prefix that the watchdog embeds in strip-announcement comments.
# Used by the drift-repair pass to detect stale comment+label combinations.
STRIP_COMMENT_MARKER = "[pipeline-watchdog] Stripped `status:done`"

_DEFAULT_GH = "gh"


# ---------------------------------------------------------------------------
# Core operations
# ---------------------------------------------------------------------------


def strip_status_done(
    repo: str,
    issue_number: int,
    log_path: Path,
    gh_path: str = _DEFAULT_GH,
) -> bool:
    """Attempt to remove the status:done label, then post the announcement.

    Returns True when the label mutation succeeded and the comment was posted,
    False when the mutation failed (comment suppressed, failure logged).
    """
    # Step 1 — mutate label FIRST
    result = subprocess.run(
        [gh_path, "issue", "edit", str(issue_number),
         "--repo", repo,
         "--remove-label", "status:done"],
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        # Mutation failed — log the failure, suppress the comment
        _log_failure(
            log_path=log_path,
            repo=repo,
            issue=issue_number,
            exit_code=result.returncode,
            stderr=result.stderr.strip(),
        )
        return False

    # Step 2 — mutation succeeded, now post the announcement
    subprocess.run(
        [gh_path, "issue", "comment", str(issue_number),
         "--repo", repo,
         "--body",
         f"{STRIP_COMMENT_MARKER} — applied without commit/PR evidence "
         "(no closing PR, no `Closes #N` reference on default branch). "
         "Re-walking through triage/plan/impl on next /run."],
        capture_output=True,
        text=True,
    )
    return True


def drift_repair_pass(
    repos_and_issues: Sequence[tuple[str, int]],
    log_path: Path,
    gh_path: str = _DEFAULT_GH,
) -> int:
    """Re-attempt label removal for issues in a known-broken state.

    A broken state means: the issue has the strip-comment AND still carries
    status:done. This is the signature of the original bug.

    Returns the count of issues where repair was attempted.
    """
    repaired = 0
    for repo, issue_number in repos_and_issues:
        if _is_stale(repo, issue_number, gh_path):
            strip_status_done(
                repo=repo,
                issue_number=issue_number,
                log_path=log_path,
                gh_path=gh_path,
            )
            repaired += 1
    return repaired


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _is_stale(repo: str, issue_number: int, gh_path: str) -> bool:
    """Return True if the issue has the strip-comment AND status:done label."""
    result = subprocess.run(
        [gh_path, "issue", "view", str(issue_number),
         "--repo", repo,
         "--json", "labels,comments"],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        return False

    try:
        data = json.loads(result.stdout)
    except json.JSONDecodeError:
        return False

    labels = [lbl if isinstance(lbl, str) else lbl.get("name", "") for lbl in data.get("labels", [])]
    has_done_label = "status:done" in labels

    comments = data.get("comments", [])
    has_strip_comment = any(
        STRIP_COMMENT_MARKER in (c.get("body", "") if isinstance(c, dict) else str(c))
        for c in comments
    )

    return has_done_label and has_strip_comment


def _log_failure(
    log_path: Path,
    repo: str,
    issue: int,
    exit_code: int,
    stderr: str,
) -> None:
    """Append a structured JSON entry to the orchestrator log."""
    entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "event": "watchdog_label_mutation_failed",
        "repo": repo,
        "issue": issue,
        "exit_code": exit_code,
        "stderr": stderr,
    }
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with log_path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="pipeline_watchdog",
        description="Pipeline watchdog — strips status:done labels applied without evidence.",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    strip_cmd = sub.add_parser("strip", help="Strip status:done from a single issue.")
    strip_cmd.add_argument("--repo", required=True, help="owner/repo")
    strip_cmd.add_argument("--issue", type=int, required=True, help="issue number")
    strip_cmd.add_argument("--log", required=True, help="path to orchestrator log file")
    strip_cmd.add_argument("--gh", default=_DEFAULT_GH, help="path to gh binary")

    repair_cmd = sub.add_parser("drift-repair", help="Re-attempt removal for stale issues.")
    repair_cmd.add_argument("--log", required=True, help="path to orchestrator log file")
    repair_cmd.add_argument("--gh", default=_DEFAULT_GH, help="path to gh binary")
    repair_cmd.add_argument(
        "issues",
        nargs="+",
        metavar="OWNER/REPO:NUMBER",
        help="repo:issue pairs to scan, e.g. Open-Paws/context:82",
    )

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)

    if args.command == "strip":
        ok = strip_status_done(
            repo=args.repo,
            issue_number=args.issue,
            log_path=Path(args.log),
            gh_path=args.gh,
        )
        return 0 if ok else 1

    if args.command == "drift-repair":
        pairs: list[tuple[str, int]] = []
        for item in args.issues:
            repo, _, num = item.rpartition(":")
            if not repo or not num.isdigit():
                print(f"Invalid format (expected OWNER/REPO:NUMBER): {item}", file=sys.stderr)
                return 2
            pairs.append((repo, int(num)))
        count = drift_repair_pass(
            repos_and_issues=pairs,
            log_path=Path(args.log),
            gh_path=args.gh,
        )
        print(f"drift-repair: {count} issue(s) re-attempted")
        return 0

    return 1


if __name__ == "__main__":
    sys.exit(main())
