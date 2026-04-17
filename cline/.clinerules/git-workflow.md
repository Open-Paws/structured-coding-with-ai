# GitHub Workflow for AI-Assisted Advocacy Development

## When to Use
- Before starting any coding task on a GitHub repository
- Before committing, branching, or creating a pull request
- When multiple agents are running in parallel on the same repo
- After an AI agent has generated a batch of changes

## Hard Rules — No Exceptions

- **Never commit or push directly to `main`** — always work on a branch
- **Never merge to `main` directly** — always submit a pull request
- **Never share a branch between parallel agents** — each agent gets its own worktree

## Process

### Step 0: Start with a GitHub Issue

Before writing any code, verify there is a documented issue:

```bash
gh issue list --search "keywords describing the task"
```

- **Issue exists:** note the issue number — every branch, commit, and PR must reference it.
- **No issue exists:** create one before starting. A good issue includes:
  - Clear problem description and context
  - Acceptance criteria (what "done" looks like)
  - Affected files or components (if known)
  - Security, privacy, or advocacy-domain considerations
  - Any constraints (performance, compatibility, etc.)

```bash
gh issue create --title "Fix: short description" --body "..."
```

Do not begin implementation until the issue is documented.

### Step 1: One Worktree Per Task

Every task — especially in parallel agent swarms — gets its own git worktree. This isolates in-progress changes and prevents one agent's work from affecting another's.

```bash
git worktree add ../worktrees/<branch-name> -b <branch-name>
cd ../worktrees/<branch-name>
```

Branch naming: `fix/<issue-number>-short-description` or `feat/<issue-number>-short-description`. Under 50 characters. Reference the issue number. No advocacy language in external repos.

**Critical for multi-agent work:** When spawning parallel sub-agents, each agent MUST receive its own unique branch name and worktree path. Pass these explicitly — agents sharing a branch will produce conflicts and corrupted history.

### Step 2: Read and Understand the Codebase

Before planning, read the codebase. This is mandatory — AI agents violate DRY at 4x the normal rate because they skip this step.

Required reading:
- Every file in the affected module(s)
- Existing utilities, patterns, and conventions relevant to the change
- Test files for the affected code
- Recent git log for the affected files: `git log --oneline -10 -- <file>`
- How data flows through the affected path

Do not begin planning until you can describe the current behavior in your own words.

### Step 3: Write a Plan

Write a detailed implementation plan before touching any code:
- The specific change stated in one sentence
- Which files change and why
- Subtask decomposition — each subtask is one commit
- Test strategy: which existing tests run, what new tests are needed
- Security and privacy considerations
- desloppify score impact: does this touch code quality hotspots?

The plan is an artifact — write it out explicitly. Do not keep it in your head.

### Step 4: Review the Plan (Loop Until Approved)

The plan must pass review before implementation begins. Review it yourself against the issue's acceptance criteria, or spawn a sub-agent to review it with full codebase context.

Review checks:
- Does the plan fully address the issue's acceptance criteria?
- Does it avoid duplicating existing code?
- Does it follow the codebase's naming conventions and architectural patterns?
- Are security and privacy implications addressed?
- Is each subtask atomic and independently committable?

**Loop:** revise the plan → review again → until all concerns are resolved. Do not begin implementing on a plan with unresolved review concerns.

### Step 5: Implement One Subtask at a Time

Work through subtasks in order. For each subtask:
1. Implement the change
2. Run the relevant test subset
3. Verify no sensitive data leaked into test output, logs, or error messages
4. Commit with a message that explains WHY, not WHAT:
   `git commit -m "fix(#<issue>): <imperative-mood description>"`

Every commit must leave the codebase passing. Never push broken commits.

### Step 6: Review the Implementation (Loop Until Approved)

After all subtasks are implemented, review the full diff against the plan:
- Does the implementation match what the plan described?
- Are all acceptance criteria from the issue met?
- Did any scope creep occur? (If yes, revert it — scope creep belongs in a separate PR)
- Are the tests meaningful — do they fail when the covered behavior breaks?
- Are all safety checks from the original code preserved?

Spawn a sub-agent to review if available. **Loop:** fix → review → until clean.

### Step 7: Run desloppify (Score Must Not Drop)

Before opening a PR, run desloppify on the repo:

```bash
desloppify scan --path .
desloppify next   # loop: next → fix → resolve → next
```

**Critical rule:** The desloppify score after your changes must be equal to or higher than before. A score drop means the PR is not ready — fix the issues desloppify raises and rescan.

**If the repo has no published desloppify score:** Run a baseline scan first, record the score, then implement and rescan. The post-implementation score must be ≥ the baseline.

Minimum scores: Gary ≥80 · Platform repos ≥75 · All other repos ≥70

### Step 8: Submit the Pull Request

```bash
gh pr create \
  --title "fix: <description> (closes #<issue>)" \
  --body "$(cat <<'EOF'
## Summary
<1-3 bullet points describing what changed and why>

## Closes
#<issue-number>

## Test Plan
- [ ] <what was tested>
- [ ] <any new tests added>

## desloppify Score
Before: <score>  After: <score>

## Notes
<security/privacy notes if applicable>
EOF
)"
```

- Target under 200 lines changed per PR, ideally under 100
- Use stacked PRs for large changes (each independently reviewable)
- Add the **AI-Assisted** label if the code is primarily agent-generated
- Require two human approvals for primarily AI-generated PRs

### Step 9: Monitor and Respond (Loop Until Merged)

After submitting, the task is not done. Periodically check the PR:

```bash
gh pr view <number>       # overall status
gh pr checks <number>     # CI/CD status
gh pr comments <number>   # review comments
```

**CI/CD failures:** Investigate immediately. Identify the root cause, fix on the same branch, push, and verify checks go green. Do not leave a PR with failing checks unattended.

**Review comments:** Respond to every comment. For blocking issues, implement the fix on the same branch and push. For discussion comments, reply with your reasoning. Re-request review when fixes are pushed.

**Loop:** check → fix → push → check until the PR is merged, CI is green, and all review comments are resolved.

**The task is not done until the PR is merged.**

## Quality Signals

- **Code Survival Rate** — how much AI-generated code remains unchanged 48 hours after merge. Low survival means the agent generates code humans immediately rewrite.
- **Suggestion acceptance rate** — healthy range 25-35%; higher may indicate over-reliance without critical review. In advocacy projects, over-reliance means unreviewed security assumptions.

## Merge Strategy

Squash-merge ephemeral branches. Delete branches immediately after merge. If a branch has lived longer than one working session, evaluate whether the approach needs to change.
