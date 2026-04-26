---
name: merge
description: Ranked merge queue with honest confidence scoring. Replaces "open 12 PR tabs" with one table. Pulls open PRs from gh, filters to `stage:ready-for-merge` (plus all-gates-green PRs without a blocking stage label), runs its own per-PR evaluation, computes calibrated HIGH/MED/LOW confidence, emits a markdown table with clickable PR links and copy-paste merge commands. Read-only — never merges, never invokes subagents. Operator-only.
disable-model-invocation: true
argument-hint: "[--risky] [--repo <name>]"
allowed-tools: Bash(gh:*), Bash(head:*), Bash(ls:*), Bash(date:*), Bash(stat:*), Read, Grep, Glob
model: opus
---

# /merge — ranked merge queue, no auto-merge

Read-only operator HUD. Pulls open PRs directly from gh, filters to `stage:ready-for-merge` (and all-gates-green PRs without a blocking stage label), runs its own per-PR evaluation against the calibration rules below, emits clickable PR links and copy-paste merge commands the operator runs themselves.

`/merge` does NOT merge. It does NOT drive the pipeline (that's `/run`). It does NOT invoke subagents. It does NOT depend on the latest `/run` report — gh is the source of truth, and this command does its own eval.

Read these every fire (auto-load via `InstructionsLoaded`; cite by name in any followup question):

- `~/.claude/rules/pipeline-nevers.md` — `override:skip-adversarial`, `override:allow-score-drop` are MED-cap signals (never HIGH); never merges to main directly
- `~/.claude/rules/context-repo.md` — sensitivity:private files in a PR cap confidence at MED
- `~/.claude/rules/advocacy-domain.md` — bounded contexts list (used to detect scope-creep)

## Argument parsing

`$ARGUMENTS`:
- `--risky` — invert sort to ascending (LOW first); default sort is descending (HIGH first)
- `--repo <name>` — single-repo scope (`Open-Paws/<name>`)

## Algorithm

### 1. Pull candidate PRs from gh (primary path — always run this)

The canonical input is `gh pr list`, not the run log. Always derive live.

**Step A — labelled `stage:ready-for-merge` PRs:**

```bash
gh pr list --repo Open-Paws/<repo> --state open \
  --label 'stage:ready-for-merge' \
  --json number,title,labels,url,statusCheckRollup,reviewDecision,mergeStateStatus,mergeable,headRefName,additions,deletions,changedFiles \
  --limit 100
```

**Step B — all-gates-green sweep** (catches PRs that are functionally ready but missing the label, e.g. label-application drift):

```bash
gh pr list --repo Open-Paws/<repo> --state open \
  --json number,title,labels,url,statusCheckRollup,reviewDecision,mergeStateStatus,mergeable \
  --limit 200
```

Client-side filter: keep PRs where `statusCheckRollup` is all-SUCCESS AND labels contain none of `stage:plan-in-progress`/`stage:tests-in-progress`/`stage:impl-in-progress`/`stage:fix-needed`/`stage:adversarial-pending`. Tag these as "no label, all green" in the source column so the operator knows they came in via the sweep, not the official label.

**Repo scope:**

- `--repo <name>` set → just that repo
- Not set → walk every Open-Paws repo where `OpenGaryBot` has push access. Get the list with `gh repo list Open-Paws --limit 100 --json name,viewerPermission` and keep entries where `viewerPermission` is `WRITE` or `ADMIN`.

**Deduplicate** between Step A and Step B by `(repo, number)`.

### 1b. Optional: cross-reference the latest run log (secondary signal only)

```bash
LATEST=$(ls -t ~/.claude/orchestrator-log/run-*.md 2>/dev/null | head -1)
```

If `LATEST` exists AND its mtime is within the last 30 minutes, read it ONLY to harvest two specific signals that are otherwise expensive to recompute live:

- Adversarial subagent verdicts mentioned per-PR (cheap signal for the LOW caps below)
- Decision-conflict flags raised by the planner / plan-reviewer

Do NOT use the run log to determine which PRs are candidates. Do NOT inherit the run log's HIGH/MED/LOW classification — recompute from scratch against the rules below. The run log is a hint store; gh is the source of truth.

If `LATEST` is stale or missing, skip this step entirely. The eval still works; you just lose the prior-context shortcut.

### 2. Per-PR signals to gather

For each candidate PR, fetch:

```bash
gh pr view <repo>/<num> --json number,title,labels,url,statusCheckRollup,reviewDecision,mergeStateStatus,mergeable,headRefName,additions,deletions,changedFiles,files,comments,body
```

Plus, if the PR touches a deployed surface, look for "live HTTP check" evidence in PR comments — search for `gh pr view --comments` output containing patterns like `curl -i`, `health check`, `200 OK`, `live check passed`. If none, the deployed-surface MED-cap fires.

### 3. Confidence calibration (read carefully — calibration is half the value of this command)

**A PR is NEVER HIGH if any of the following are true** (these always cap at MED or lower):

- Label `override:skip-adversarial` is present
- Label `override:allow-score-drop` is present
- PR deploys application code AND no live HTTP check post-build is recorded in PR comments
  - Detect deployed service via files matched: `Dockerfile`, `cloudrun*.yaml`, `vercel.json`, `supabase/functions/`, `.github/workflows/deploy*.yml`, etc.
  - **Workflow-only carve-out:** If the ONLY deploy-surface files in the PR are themselves the deploy mechanism (e.g., the PR adds or modifies `.github/workflows/deploy*.yml` or a `Dockerfile`) AND no application code files are touched (no `src/`, `app/`, `lib/`, `pages/`, `components/`, `*.ts`/`*.tsx`/`*.py`/`*.go` etc. outside `tests/`), the cap does NOT fire. Adding the deploy mechanism doesn't deploy anything until the next code change merges. Live HTTP checks become relevant when the PR after this one ships actual code.
- Files touched include any path tagged `sensitivity:private` per `context-repo.md`
- CodeRabbit found anything above informational severity (parse PR comments for `**Issue:**`/`**Refactor:**`/`**Bug:**`/`**Note:**` blocks; the `chill` profile uses `Note:` for informational, so anything else is above-informational)
- Any test in the PR was classified as `skip:flaky` by test-reviewer (look for that label OR comment from `test-reviewer` mentioning the classification)
- Time since `stage:verified` was applied (or last `verifier` completion comment) exceeds 24h (stale verification)
- PR touches a UI surface (`*.tsx`, `*.jsx`, `*.vue`, `*.svelte`, `app/`, `pages/`, `components/`) AND no `persona-qa` completion comment is present on the PR
- `reviewDecision == CHANGES_REQUESTED` (a reviewer — CodeRabbit or human — flagged a change still unaddressed; merging now ignores that feedback)
- `mergeStateStatus == BEHIND` (head ref out of date; merge command will bounce until the branch is rebased onto base — content may be clean but the operation can't complete)
- `mergeStateStatus == BLOCKED` (branch protection blocks direct merge — content may be clean, but a required check is missing, the branch needs an admin override, or branch-protection criteria aren't met).

**A PR is LOW if any of the following are true:**

- `mergeable == CONFLICTING` or `mergeStateStatus == DIRTY` (actual merge conflict — needs manual rebase + conflict resolution before any merge command will work, regardless of content quality)
- Multiple of the MED-cap conditions above stack (count ≥ 2)
- The `adversarial` subagent flagged anything as `needs-human-review` (look for that phrase in adversarial completion comment)
- PR conflicts with a closed decision in `$OP_CONTEXT_REPO/decisions.md` (cross-reference any decision-conflict entry from the run log; on direct derivation, scan PR body + diff for keywords against `$OP_CONTEXT_REPO/decisions.md` headings)
- Files touched span more than 3 of the bounded contexts in `~/.claude/rules/advocacy-domain.md` (Investigation Operations / Public Campaigns / Coalition Coordination / Legal Defense). Use heuristic: any file under `*/investigations/*` → Investigation Operations; under `*/campaigns/*` or `*/petitions/*` → Public Campaigns; under `*/coalitions/*` or `*/partners/*` → Coalition Coordination; under `*/legal/*` or `*/cases/*` → Legal Defense. Probable scope creep.

**Otherwise: HIGH.**

### 4. Calibration intent (this is why the score is useful)

The score answers ONE question: *is this PR safe to merge right now with no further pipeline action?* If a required check is missing, branch protection is unsatisfied, or the merge command will bounce, the answer is no — and that drops confidence by design. The score is mechanical, not aspirational.

A clean bot-authored PR — CI green, no CodeRabbit issues, adversarial cleared, no merge conflict, no stale verifier, no UI-without-persona-qa, no deploy-without-live-check, AND `mergeStateStatus` is mergeable (not BLOCKED, BEHIND, or DIRTY) — is HIGH. If `mergeStateStatus == BLOCKED` for any reason — missing required check, missing required approval, branch-protection criteria unmet — that's a MED cap, no exceptions. The cap fires on the mechanical state regardless of why it's blocked.

The MED-cap conditions exist to surface real content concerns: reviewer flagged unaddressed changes, deployed surface lacks a live HTTP check, UI lacks persona-qa, override label bypassed adversarial. When the operator sees MED, it means "look at this — there's something the pipeline noticed but couldn't resolve." When they see HIGH, it means "the pipeline thinks this is clean; your call."

If you find yourself reasoning "this PR is fine, let's call it HIGH despite a MED-cap firing" — STOP. The score is mechanical. Don't soften it. Surface the cap reason in the "Top reason not HIGH" column and let the operator decide.

## Output format

```markdown
## /merge queue — <ISO timestamp> — N PRs ready

| Conf | Repo | PR | Title | Top reason not HIGH | Approve+merge command |
|------|------|----|----|---------------------|-----------------------|
| HIGH | <repo> | [#<num>](<url>) | <title 60ch> | — | gh pr review --approve <url> && gh pr merge --squash --delete-branch <url> |
| MED  | <repo> | [#<num>](<url>) | <title 60ch> | <one-line reason> | gh pr review --approve <url> && gh pr merge --squash --delete-branch <url> |
| LOW  | <repo> | [#<num>](<url>) | <title 60ch> | <one-line reason> | gh pr review --approve <url> && gh pr merge --squash --delete-branch <url> |

Distribution: HIGH: N | MED: N | LOW: N
Source: live gh derivation (<N> repos walked, <M> PRs evaluated). Run-log cross-reference: <used / skipped — stale / skipped — none>.
```

**PR column always renders as `[#<num>](<url>)`, never bare `#<num>`** — clickable links per the standing operator-output rule. Same goes for any followup answer that names a PR.

Default sort: descending — HIGH first, MED second, LOW last. With `--risky`: ascending — LOW first.

Title truncation: hard 60-char limit. Suffix with `…` if truncated. Don't try to be clever; truncation is fine because the merge command has the full URL.

The "Top reason not HIGH" column for HIGH PRs is **always em-dash (`—`), never a sycophantic comment**. If you find yourself writing "looks clean!" or "all gates green ✓" — that's wrong. Em-dash is the contract.

If only one cap fires for a MED, write the one cap. If multiple cap conditions fire on a LOW, write the most decision-relevant one (typically: adversarial flag > decision conflict > scope creep > stacked MED-caps). Reserve the long explanation for follow-up questions; the column is a glance.

Merge command always uses `--squash --delete-branch` per `pipeline-reference.md` STAGE 14.

The chained `gh pr review --approve <url> && gh pr merge ...` lets the operator paste once. If they've already approved the PR via the UI, the first half is a benign re-approval; if they haven't, it satisfies branch protection's "review required" gate immediately before the merge attempt. Caveat: on a MED with `reviewDecision == CHANGES_REQUESTED`, the operator pasting this is explicitly overriding the reviewer's flagged concerns — the cap reason is in column 5 to make that visible. If they want to handle the change first, they don't paste; that's the whole point of MED.

## Hard rules

- **Never actually merge.** `/merge` is read-only. It produces copy-paste commands the operator runs.
- **Never invoke subagents.** This skill reads existing pipeline state. Driving the pipeline is `/run`'s job.
- **Never apply labels.** Including `ready-for-merge` itself.
- **HIGH means HIGH.** Don't soften the calibration to make the report feel friendlier. The whole value of the column is that it discriminates.

## Followup questions

After surfacing the table, the operator can ask "why is platform#118 LOW?" — answer from the data already gathered, citing the specific cap conditions that fired. Stay in main session for these followups; that's why this skill has no `agent:` field.
