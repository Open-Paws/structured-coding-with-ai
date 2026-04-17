<!-- trigger: model_decision -->
# GitHub Workflow

## When to Use
Before starting any coding task on a GitHub repository. Before committing, branching, or creating a pull request. When multiple agents run in parallel on the same repo. After an AI agent has generated a batch of changes.

## Hard Rules

- **Never commit or push directly to `main`** — always work on a branch
- **Never merge to `main` directly** — always submit a pull request
- **Never share a branch between parallel agents** — each agent gets its own worktree

## Step 0: GitHub Issue First

Before writing any code, verify there is a documented issue:

```bash
gh issue list --search "keywords describing the task"
```

Issue exists → note the number; every branch, commit, and PR must reference it.
No issue → create one first. Include: problem description, acceptance criteria, affected files/components, security/privacy considerations, and constraints.

```bash
gh issue create --title "Fix: short description" --body "..."
```

Do not begin implementation until the issue is documented.

## Step 1: One Worktree Per Task

Every task — especially in parallel agent swarms — gets its own git worktree:

```bash
git worktree add ../worktrees/<branch-name> -b <branch-name>
cd ../worktrees/<branch-name>
```

Branch naming: `fix/<issue-number>-short-description` or `feat/<issue-number>-short-description`. Under 50 characters. Reference the issue number.

**Critical for multi-agent work:** When spawning parallel sub-agents, each agent MUST receive its own unique branch name and worktree path. Agents sharing a branch will produce conflicts and corrupted history.

## Step 2: Read the Codebase

Before planning, read every file in the affected module(s), existing utilities and patterns, test files, and recent git log. Do not begin planning until you can describe the current behavior in your own words.

## Step 3: Write a Plan

Write an explicit implementation plan: specific change in one sentence, which files change and why, subtask decomposition (each subtask = one commit), test strategy, security/privacy considerations, desloppify score impact.

## Step 4: Review Plan (Loop Until Approved)

Review against the issue's acceptance criteria. Check: fully addresses acceptance criteria? No duplicate code? Follows naming conventions? Security/privacy addressed? Each subtask atomic?

**Loop:** revise → review → until all concerns resolved. No implementation on unresolved concerns.

## Step 5: Implement One Subtask at a Time

For each subtask: implement, run relevant tests, verify no data leakage, commit WHY not WHAT:
`git commit -m "fix(#<issue>): <imperative-mood description>"`

Every commit must leave the codebase passing. No broken commits.

## Step 6: Review Implementation (Loop Until Approved)

Review full diff against plan: matches plan? Acceptance criteria met? No scope creep? Tests fail when behavior breaks? All safety checks preserved?

**Loop:** fix → review → until clean.

## Step 7: desloppify (Score Must Not Drop)

```bash
desloppify scan --path .
desloppify next   # loop: next → fix → resolve → next
```

**Critical rule:** Score after changes must be ≥ score before. Score drop = PR not ready.

**No published score:** Establish baseline scan first, then implement, then rescan. Post-implementation score must be ≥ baseline.

Minimum scores: Gary ≥80 · Platform repos ≥75 · All other repos ≥70

## Step 8: Submit PR

```bash
gh pr create \
  --title "fix: <description> (closes #<issue>)" \
  --body "## Summary
<bullet points>

## Closes
#<issue>

## Test Plan
- [ ] <tested>

## desloppify Score
Before: <score>  After: <score>"
```

Under 200 lines changed, ideally under 100. Stacked PRs for large changes. **AI-Assisted** label for primarily agent-generated code. Two human approvals required.

## Step 9: Monitor Until Merged

```bash
gh pr view <number>
gh pr checks <number>
gh pr comments <number>
```

**CI failures:** fix on same branch, push, verify green. Do not leave failing checks unattended.

**Review comments:** respond to every comment. Fix blocking issues on same branch and push. Re-request review when fixes are pushed.

**Loop:** check → fix → push → check until merged, CI green, all comments resolved.

**The task is not done until the PR is merged.**

## Quality Signals

- **Code Survival Rate** — AI code remaining unchanged 48 hours after merge. Low = throwaway code.
- **Suggestion acceptance rate** — healthy range 25-35%. Higher may indicate over-reliance.

## Merge Strategy

Squash-merge ephemeral branches. Delete immediately after merge. Branch alive longer than one session? Reconsider the approach.
