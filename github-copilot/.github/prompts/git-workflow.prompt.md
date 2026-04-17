# GitHub Workflow for AI-Assisted Advocacy Development

You are guiding a developer through the GitHub workflow for an animal advocacy project. AI-generated code requires stricter commit and PR discipline because AI adoption inflated PR size by 154% and review time by 91%. Follow these steps in order. Never skip steps. Never work directly on main.

## Hard Rules — No Exceptions

- **Never commit or push directly to `main`** — always work on a branch
- **Never merge to `main` directly** — always submit a pull request
- **Never share a branch between parallel agents** — each agent gets its own worktree

## Step 0: Start with a GitHub Issue

Before writing any code, verify there is a documented issue:

```bash
gh issue list --search "keywords describing the task"
```

If an issue exists, note its number — every branch, commit, and PR must reference it. If no issue exists, create one first:

```bash
gh issue create --title "Fix: short description" --body "..."
```

A good issue includes: problem description, acceptance criteria, affected files or components, security and privacy considerations, and any constraints. Do not begin implementation until the issue is documented.

## Step 1: Create a Worktree

Every task — especially in parallel agent swarms — gets its own git worktree:

```bash
git worktree add ../worktrees/<branch-name> -b <branch-name>
cd ../worktrees/<branch-name>
```

Branch naming: `fix/<issue-number>-short-description` or `feat/<issue-number>-short-description`. Under 50 characters. Reference the issue number.

**Critical for multi-agent work:** When spawning parallel sub-agents, each agent MUST receive its own unique branch name and worktree path. Pass these explicitly — agents sharing a branch will produce conflicts and corrupted history.

## Step 2: Read the Codebase

Before planning, read the codebase. This is mandatory.

- Read every file in the affected module(s)
- Search for existing utilities, patterns, and conventions
- Read test files for the affected code
- Check recent git log: `git log --oneline -10 -- <file>`

Do not begin planning until you can describe the current behavior in your own words.

## Step 3: Write a Plan

Write a detailed implementation plan before touching any code:
- The specific change in one sentence
- Which files change and why
- Subtask decomposition (each subtask = one commit)
- Test strategy: which tests run, what new tests are needed
- Security and privacy considerations
- desloppify score impact

## Step 4: Review the Plan

Review the plan against the issue's acceptance criteria. Check: fully addresses criteria? No duplicate code? Follows naming conventions? Security/privacy addressed? Each subtask atomic?

**Loop:** revise → review → until all concerns resolved. Do not begin implementing on unresolved concerns.

## Step 5: Implement One Subtask

Write code for exactly one subtask. Then:
1. Run the relevant test subset
2. Verify no sensitive data leaked into test output, logs, or error messages
3. Commit: `git commit -m "fix(#<issue>): <imperative-mood WHY description>"`

Every commit must leave the codebase passing. Never push broken commits.

## Step 6: Repeat for Each Subtask

Continue: implement one subtask, test, commit. Then move to the next.

## Step 7: Review the Implementation

After all subtasks are done, review the full diff against the plan:
- Matches the plan?
- All acceptance criteria met?
- No scope creep? (Revert any — it belongs in a separate PR)
- Tests fail when covered behavior breaks?
- All original safety checks preserved?

**Loop:** fix → review → until clean.

## Step 8: Run desloppify

Before opening a PR:

```bash
desloppify scan --path .
desloppify next   # loop: next → fix → resolve → next
```

**Critical rule:** The score after your changes must be ≥ the score before. A drop means the PR is not ready.

**No published score:** Run a baseline scan first, record it, then implement and rescan. Post-implementation score must be ≥ baseline.

Minimum scores: Gary ≥80 · Platform repos ≥75 · All other repos ≥70

## Step 9: Submit the Pull Request

```bash
gh pr create \
  --title "fix: <description> (closes #<issue>)" \
  --body "$(cat <<'EOF'
## Summary
<1-3 bullet points>

## Closes
#<issue-number>

## Test Plan
- [ ] <what was tested>
- [ ] <new tests added>

## desloppify Score
Before: <score>  After: <score>

## Notes
<security/privacy notes if applicable>
EOF
)"
```

- Target under 200 lines changed, ideally under 100
- Use stacked PRs for large changes
- Add **AI-Assisted** label for primarily agent-generated code
- Require two human approvals for primarily AI-generated PRs

## Step 10: Monitor Until Merged

After submitting, the task is not done. Check periodically:

```bash
gh pr view <number>       # overall status
gh pr checks <number>     # CI/CD status
gh pr comments <number>   # review comments
```

**CI/CD failures:** Fix immediately on the same branch, push, verify green.

**Review comments:** Respond to every comment. Fix blocking issues on the same branch and push. Re-request review when fixes are pushed.

**Loop:** check → fix → push → check until the PR is merged, CI is green, and all comments are resolved.

**The task is not done until the PR is merged.**

## Quality Signals

- **Code Survival Rate** — how much AI code remains unchanged 48 hours after merge. Low survival = throwaway code.
- **Suggestion acceptance rate** — healthy range 25-35%; higher may indicate over-reliance without critical review.

## Merge Strategy

Squash-merge ephemeral branches. Delete branches immediately after merge. If a branch has lived longer than one working session, evaluate whether the approach needs to change.
