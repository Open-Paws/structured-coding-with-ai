---
name: merge
description: Ranked merge queue with honest confidence scoring. Replaces "open 12 PR tabs" with one table. Reads the latest /run report (if <30min old) or derives ready-for-merge state via gh, computes a calibrated HIGH/MED/LOW confidence per PR, emits a markdown table with copy-paste merge commands. Read-only — never merges, never invokes subagents. Operator-only.
disable-model-invocation: true
argument-hint: "[--risky] [--repo <name>]"
allowed-tools: Bash(gh:*), Bash(head:*), Bash(ls:*), Bash(date:*), Bash(stat:*), Read, Grep, Glob
model: opus
---

# /merge — ranked merge queue, no auto-merge

Read-only operator HUD. Lists every PR currently at `stage:ready-for-merge` (or all-gates-green with no stage label blocking), ranks by calibrated confidence, emits copy-paste merge commands the operator runs themselves.

`/merge` does NOT merge. It does NOT drive the pipeline (that's `/run`). It does NOT invoke subagents. It reads existing pipeline state and surfaces it.

Read these every fire (auto-load via `InstructionsLoaded`; cite by name in any followup question):

- `~/.claude/rules/pipeline-nevers.md` — `override:skip-adversarial`, `override:allow-score-drop` are MED-cap signals (never HIGH); never merges to main directly
- `~/.claude/rules/context-repo.md` — sensitivity:private files in a PR cap confidence at MED
- `~/.claude/rules/advocacy-domain.md` — bounded contexts list (used to detect scope-creep)

## Argument parsing

`$ARGUMENTS`:
- `--risky` — invert sort to ascending (LOW first); default sort is descending (HIGH first)
- `--repo <name>` — single-repo scope (`Open-Paws/<name>`)

## Algorithm

### 1. Find the input

```bash
LATEST=$(ls -t ~/.claude/orchestrator-log/run-*.md 2>/dev/null | head -1)
```

If `LATEST` exists AND its mtime is within the last 30 minutes:
- Read it. Pull every PR mentioned in `### Advanced` (where `stage to == stage:ready-for-merge`) and `### No action needed` (where row contains `stage:ready-for-merge`).
- Also pull every PR from `### Stopped at human gate` whose `needs:` reason is "human approval (non-last-pusher branch protection)" — those are gate-clear from the bot's side.

Otherwise (no recent log, or `--repo` set forcing fresh derivation):
- Derive directly via `gh pr list --repo Open-Paws/<repo> --state open --label 'stage:ready-for-merge' --json number,title,labels,url,statusCheckRollup,reviewDecision,headRefName,additions,deletions,changedFiles --limit 100`
- Plus a sweep of all-gates-green PRs without a blocking stage label: `gh pr list --repo Open-Paws/<repo> --state open --json number,title,labels,url,statusCheckRollup,reviewDecision --limit 200` then filter client-side for `statusCheckRollup` all-SUCCESS and labels containing none of `stage:plan-in-progress`/`stage:tests-in-progress`/`stage:impl-in-progress`/`stage:fix-needed`/`stage:adversarial-pending`.

If `--repo` not set, walk all Open-Paws repos for which OpenGaryBot has push access.

### 2. Per-PR signals to gather

For each candidate PR, fetch:

```bash
gh pr view <repo>/<num> --json number,title,labels,url,statusCheckRollup,reviewDecision,headRefName,additions,deletions,changedFiles,files,comments,body
```

Plus, if the PR touches a deployed surface, look for "live HTTP check" evidence in PR comments — search for `gh pr view --comments` output containing patterns like `curl -i`, `health check`, `200 OK`, `live check passed`. If none, the deployed-surface MED-cap fires.

### 3. Confidence calibration (read carefully — calibration is half the value of this command)

**A PR is NEVER HIGH if any of the following are true** (these always cap at MED or lower):

- Label `override:skip-adversarial` is present
- Label `override:allow-score-drop` is present
- PR touches a deployed service (Cloud Run, Vercel project, Edge Function, etc.) AND no live HTTP check post-build is recorded in PR comments
  - Detect deployed service via files matched: `Dockerfile`, `cloudrun*.yaml`, `vercel.json`, `supabase/functions/`, `.github/workflows/deploy*.yml`, etc.
- Files touched include any path tagged `sensitivity:private` per `context-repo.md`
- CodeRabbit found anything above informational severity (parse PR comments for `**Issue:**`/`**Refactor:**`/`**Bug:**`/`**Note:**` blocks; the `chill` profile uses `Note:` for informational, so anything else is above-informational)
- Any test in the PR was classified as `skip:flaky` by test-reviewer (look for that label OR comment from `test-reviewer` mentioning the classification)
- Time since `stage:verified` was applied (or last `verifier` completion comment) exceeds 24h (stale verification)
- PR touches a UI surface (`*.tsx`, `*.jsx`, `*.vue`, `*.svelte`, `app/`, `pages/`, `components/`) AND no `persona-qa` completion comment is present on the PR

**A PR is LOW if any of the following are true:**

- Multiple of the MED-cap conditions above stack (count ≥ 2)
- The `adversarial` subagent flagged anything as `needs-human-review` (look for that phrase in adversarial completion comment)
- PR conflicts with a closed decision in `$OP_CONTEXT_REPO/decisions.md` (cross-reference any decision-conflict entry from the run log; on direct derivation, scan PR body + diff for keywords against `$OP_CONTEXT_REPO/decisions.md` headings)
- Files touched span more than 3 of the bounded contexts in `~/.claude/rules/advocacy-domain.md` (Investigation Operations / Public Campaigns / Coalition Coordination / Legal Defense). Use heuristic: any file under `*/investigations/*` → Investigation Operations; under `*/campaigns/*` or `*/petitions/*` → Public Campaigns; under `*/coalitions/*` or `*/partners/*` → Coalition Coordination; under `*/legal/*` or `*/cases/*` → Legal Defense. Probable scope creep.

**Otherwise: HIGH.**

### 4. Calibration intent (this is why the score is useful)

If the first day of running this surfaces 80% HIGH, the calibration is too lax — the operator stops reading the column because everything looks identical. The MED-cap conditions exist specifically to push the median to MED, not HIGH. Most PRs in flight will hit at least one MED-cap (deployed-surface-no-live-check, or UI-no-persona-qa, or stale-verifier). When the operator sees HIGH, it should mean "this one really is clean — the column actually distinguishes".

If you find yourself reasoning "this PR is fine, let's call it HIGH despite a MED-cap firing" — STOP. The score is mechanical. Don't soften it. Surface the cap reason in the "Top reason not HIGH" column and let the operator decide.

## Output format

```markdown
## /merge queue — <ISO timestamp> — N PRs ready

| Conf | Repo | PR | Title | Top reason not HIGH | Merge command |
|------|------|----|----|---------------------|---------------|
| HIGH | <repo> | #<num> | <title 60ch> | — | gh pr merge --squash --delete-branch <url> |
| MED  | <repo> | #<num> | <title 60ch> | <one-line reason> | gh pr merge --squash --delete-branch <url> |
| LOW  | <repo> | #<num> | <title 60ch> | <one-line reason> | gh pr merge --squash --delete-branch <url> |

Distribution: HIGH: N | MED: N | LOW: N
Source: <log path> (mtime: <H>m ago)  OR  Source: live gh derivation (no recent run log)
```

Default sort: descending — HIGH first, MED second, LOW last. With `--risky`: ascending — LOW first.

Title truncation: hard 60-char limit. Suffix with `…` if truncated. Don't try to be clever; truncation is fine because the merge command has the full URL.

The "Top reason not HIGH" column for HIGH PRs is **always em-dash (`—`), never a sycophantic comment**. If you find yourself writing "looks clean!" or "all gates green ✓" — that's wrong. Em-dash is the contract.

If only one cap fires for a MED, write the one cap. If multiple cap conditions fire on a LOW, write the most decision-relevant one (typically: adversarial flag > decision conflict > scope creep > stacked MED-caps). Reserve the long explanation for follow-up questions; the column is a glance.

Merge command always uses `--squash --delete-branch` per `pipeline-reference.md` STAGE 14.

## Hard rules

- **Never actually merge.** `/merge` is read-only. It produces copy-paste commands the operator runs.
- **Never invoke subagents.** This skill reads existing pipeline state. Driving the pipeline is `/run`'s job.
- **Never apply labels.** Including `ready-for-merge` itself.
- **HIGH means HIGH.** Don't soften the calibration to make the report feel friendlier. The whole value of the column is that it discriminates.

## Followup questions

After surfacing the table, the operator can ask "why is platform#118 LOW?" — answer from the data already gathered, citing the specific cap conditions that fired. Stay in main session for these followups; that's why this skill has no `agent:` field.
