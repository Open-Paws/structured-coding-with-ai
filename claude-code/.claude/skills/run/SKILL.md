---
name: run
description: On-demand operator drive of the 14-stage Open Paws pipeline. Walks pipeline-tracked issues + PRs across in-scope Open-Paws repos, dispatches the right subagent per stage label, classifies every touched item into one outcome bucket, and writes a structured report to ~/.claude/orchestrator-log/run-<UTC-timestamp>.md that /merge and /unblock consume. Idempotent and interruptible — partial runs leave nothing in a corrupt half-stage. Operator-only — never auto-invoked.
disable-model-invocation: true
argument-hint: "[--repo <name>] [--since <duration>] [--stage <name>] [--fix-mode]"
allowed-tools: Bash(gh:*), Bash(git:*), Bash(ls:*), Bash(date:*), Bash(mkdir:*), Read, Grep, Glob, Write, Task
model: opus
agent: general-purpose
---

# /run — operator drive of the pipeline

Operator HUD on top of the same machinery `~/.claude/scheduled-tasks/op-pipeline-orchestrator/SKILL.md` runs on cron. Same wave gates, same subagents, same hard-nevers. Only differences: invoked on demand, scoped by flags, produces a report consumed downstream by `/merge` and `/unblock`.

Read these every fire (they auto-load via `InstructionsLoaded`; cite by name in the report's preamble):

- `~/.claude/rules/pipeline-nevers.md` — never apply override labels, never wildcard `git add`, never write production code before tests, never fold scope creep
- `~/.claude/rules/parallelization.md` — wave gates, file ownership, worktree isolation, orchestrator cwd preflight, subagent recovery
- `~/.claude/rules/context-repo.md` — sensitivity taxonomy, org-wide read test, STAGE 13 confidentiality leak
- `~/.claude/rules/git-identity.md` — `Original Gary <276612211+OpenGaryBot@users.noreply.github.com>` for any commit a recovered subagent left behind
- `~/.claude/rules/cost-optimization.md` — Haiku/Sonnet/Opus routing inside dispatched subagents

## Argument parsing

`$ARGUMENTS` is the raw flag string. Parse:

- `--repo <name>` — single-repo scope (matches `Open-Paws/<name>`)
- `--since <duration>` — only items with `pushedAt`/`updatedAt` inside the window (e.g. `30m`, `2h`, `1d`)
- `--stage <name>` — drain only items currently sitting at the named stage label (e.g. `stage:plan-approved`)
- `--fix-mode` — emit ONLY the credential-gated section + summary; suppress everything else (use after rotating a credential, to confirm the unblock cleared the queue)

Default scope: every Open-Paws repo OpenGaryBot has push access to, every pipeline-tracked item, no time filter.

## Delegation: orchestrate inside a subagent, not in main context

Per the `agent: general-purpose` directive, the first thing this skill does is delegate the orchestration sweep to a `general-purpose` subagent via the `Task` tool. Per-stage subagent dispatches happen inside *that* subagent's context, not in main session — keeps the operator's main thread clean for follow-up questions.

Spawn one Task call with `subagent_type: general-purpose`, hand it the parsed args + the algorithm below + the load-bearing report format, instruct it to write the report file and return the path. Main session reads the report and surfaces it to the operator.

## Algorithm (the subagent runs this)

### 1. Discover scope

```bash
# All in-scope repos. Cache once per fire.
gh repo list Open-Paws --limit 200 --json name,pushedAt,defaultBranchRef
```

If `--repo <name>` set, filter to that one. If `--since <duration>` set, drop repos whose `pushedAt` is older than the window — no point walking quiet repos.

For each repo, list pipeline-tracked items:

```bash
# Issues with any pipeline label
gh issue list --repo Open-Paws/<repo> --state open --label 'stage:*' --json number,title,labels,updatedAt,url --limit 200
gh issue list --repo Open-Paws/<repo> --state open --label 'auto:*'  --json number,title,labels,updatedAt,url --limit 200
# PRs with any pipeline label
gh pr    list --repo Open-Paws/<repo> --state open --json number,title,labels,updatedAt,url,statusCheckRollup,reviewDecision --limit 200
```

Dedupe (an issue can have both `stage:*` and `auto:*`). If `--since` set, additionally filter on `updatedAt`. If `--stage` set, filter to items currently carrying that label.

### 2. Identify current stage from labels

Stage label is the source of truth. The full taxonomy lives in `$OP_CONTEXT_REPO/.github/labels.yaml` and the stage-by-stage dispatch table is in `~/.claude/scheduled-tasks/op-pipeline-orchestrator/SKILL.md` — re-read that table before dispatching, do not duplicate it here.

### 3. Attempt advancement (one Task per item, never reimplement stage logic inline)

For each item, dispatch the correct subagent via the `Task` tool using the dispatch table in op-pipeline-orchestrator. Use `subagent_type` matching the agent name (`scout`, `triage`, `planner`, `plan-reviewer`, `test-writer`, `test-reviewer`, `implementer`, `verifier`, `desloppifier`, `adversarial`, `persona-qa`).

**Wave gate discipline:** advance a stage only when the prior stage's subagent posted a completion comment AND the label transition makes sense. Don't force it.

**Worktree-isolated subagents** (`test-writer`, `implementer`, `desloppifier`) require cwd to be inside a git repo. Before dispatching, `cd` into the repo's checkout (e.g. `~/Desktop/Open-Paws/<repo>`). Verify with `git rev-parse --show-toplevel` — if it returns nothing, classify the item as `stopped-at-human-gate` with reason `cwd preflight failed: <repo> not checked out at expected path` and continue.

**Idempotency:** every stage commits its output (label transition, completion comment) before advancement is recorded. If interrupted (Ctrl-C, token cap, wallclock), the next `/run` picks up cleanly from the last committed state — no half-stage corruption.

**Token + wallclock cap:** soft 22 minutes wallclock, ~200k tokens (matches the cron orchestrator's cap). On approach: finish current dispatch cleanly, write the partial report with whatever's classified, exit. Do not start new dispatches past the cap.

### 4. Classification

Every touched item lands in exactly one bucket. Don't double-classify.

| Outcome | Triggered by |
|---|---|
| `advanced` | Subagent succeeded, label transitioned forward, completion comment posted |
| `stopped-at-human-gate` | `auto:requires-human` was applied; OR subagent classified the item as needing judgment; OR `stage:awaiting-human-review`; OR a subagent invocation FAILED (subagent failure: <error>); OR cwd preflight failed for a worktree-isolated stage |
| `stopped-at-credential-gate` | Subagent reported a missing credential / IAM role / API key / secret it cannot self-resolve |
| `stopped-at-ci` | PR has failing CI checks (`statusCheckRollup` shows FAIL/ERROR), no other forward-motion possible until CI clears |
| `stopped-at-decision-conflict` | Subagent flagged that proceeding would silently resolve an open `$OP_CONTEXT_REPO/proposals/*.md` OR contradict `$OP_CONTEXT_REPO/decisions.md` |
| `no-action-needed` | Item already at terminal stage (`stage:ready-for-merge` — humans only); OR walked but no advancement possible this fire (still inside another wave) |

### 5. Hard rules (never violate)

- **Never apply override labels.** `override:skip-adversarial` and `override:allow-score-drop` are human-only per `pipeline-nevers.md`. If a subagent thinks an override is warranted, classify the item as `stopped-at-human-gate` with the override request as the reason.
- **Never merge PRs.** `/run` advances stages; merging is `/merge`'s job and is human-confirmed. Items at `stage:ready-for-merge` are `no-action-needed`.
- **Never modify files outside `~/.claude/orchestrator-log/`.** This skill's only filesystem write is the report file. Any code changes happen inside dispatched subagents' worktrees.
- **Never silently resolve open decisions.** If a planner dispatch would touch `$OP_CONTEXT_REPO/decisions.md` or `$OP_CONTEXT_REPO/proposals/*.md` content, classify as `stopped-at-decision-conflict`.
- **Sensitivity gate (context-repo only).** Issues in `Open-Paws/context` lacking `sensitivity:public-ok` or `sensitivity:staff-ok` cannot advance past triage. `sensitivity:private` items get a redirect comment + close — they're `no-action-needed`, not advanced.
- **Subagent failure ≠ retry.** If a Task invocation fails, log the item under `stopped-at-human-gate` with `reason: subagent failure: <one-line error>`. Don't retry inline. Operator decides.

## Report format (LOAD-BEARING — `/merge` and `/unblock` parse this verbatim)

The report is markdown but the section headers and per-row formats are stable contracts. Do not change them. If a future need requires a new field, add a new section rather than mutating an existing one.

Write to `~/.claude/orchestrator-log/run-<UTC-ISO8601-timestamp>.md`. Filename example: `run-2026-04-25T19:42:13Z.md`. Use `Write` tool. Create the parent dir if missing (it should already exist).

````markdown
## /run report — <ISO timestamp> — scope: <args summary>

### Preamble
- Repos walked: N
- Items inspected: N
- Subagents dispatched: <count by name>
- Rules read: pipeline-nevers, parallelization, context-repo, git-identity, cost-optimization
- Cap hit: yes/no <reason if yes>
- Total runtime: <duration>

### Advanced (N)
- <repo>#<num> — <stage from> → <stage to> — <one-line title> — <html_url>

### Stopped at human gate (N)
- <repo>#<num> — sitting at <stage> — needs: <one-line reason> — <html_url>

### Stopped at credential gate (N)
- <repo>#<num> — sitting at <stage> — missing: <specific credential name / IAM role / secret name> — <html_url>

### Stopped at CI (N)
- <repo>#<num> — failing: <check name> — <html_url> — <CI run URL>

### Stopped at decision conflict (N)
- <repo>#<num> — conflicts with: <decision-id or proposal filename from $OP_CONTEXT_REPO> — <html_url>

### No action needed (N)
- <repo>#<num> — at <stage> — <one-line reason> — <html_url>

### Summary
Advanced: N | Human-gated: N | Credential-gated: N | CI-stuck: N | Decision-conflict: N | No-action: N
Total runtime: <duration>
````

Empty sections still render with `(0)` count and one line: `- none`. Do not omit empty sections — `/merge` and `/unblock` parse by section header presence.

## --fix-mode

When `--fix-mode` is set, the report contains ONLY:
- A short preamble line: `## /run report (fix-mode) — <ISO timestamp> — scope: <args summary>`
- The `### Stopped at credential gate (N)` section
- The `### Summary` line (still includes all six counts so the operator can confirm zero credential-gated remain)

All other sections are suppressed from the file. Use this immediately after rotating a credential to confirm the unblock cleared the queue without re-emitting the full report.

## Persistence + log discovery

`/merge` and `/unblock` find the latest run by `ls -t ~/.claude/orchestrator-log/run-*.md | head -1`. Make sure the filename sorts correctly — UTC ISO8601 with `Z` suffix sorts lexicographically. Do not write partial files under the same name; if the report is incomplete because of a cap hit, write it anyway with the partial classifications + cap-hit preamble line. Subsequent `/run` produces a new file.

## Surfacing the report to the operator

After the subagent returns the report path:

1. Confirm the file exists: `ls -lh <path>`
2. Print the report verbatim to the operator (Read the file, output its contents).
3. Note the path explicitly: `Report written to <absolute path>` so the operator can hand it to `/merge` or `/unblock` later.
