<!-- trigger: model_decision -->
# Git Workflow

## When to Use
Before committing, branching, or creating a pull request. After an AI agent has generated changes needing logical decomposition.

## Step 1: Ephemeral Branch
Create a short-lived branch for the task. Trunk-based development remains the goal — this branch is a safety net. If the agent has not produced mergeable work in one session, delete the branch and reconsider. Name for the task, not a feature epic.

## Step 2: One Subtask at a Time
Break the task into smallest logical subtasks. Each subtask = one commit. "Extract interface, implement adapter, update callers" = three commits, not one. Never let the agent complete an entire multi-step task before committing.

## Step 3: Test Before Commit
Run relevant tests before each commit. Every commit must leave the codebase passing. For advocacy code handling investigation or evidence data, verify no sensitive data leaked into test output, logs, or error messages.

## Step 4: Commit Message
Explain WHY, not WHAT — code shows what. First line: 50 chars, imperative mood. Reference the issue. Add AI attribution trailers for agent-generated code.

## Step 5: Repeat
Implement subtask, test, commit. Each commit independently understandable.

## Step 6: Curate the PR
PR curation is the critical human skill. AI adoption inflated PR size 154%. Do not submit full agent output as one PR:
- Target under 200 lines changed, ideally under 100
- Stacked PRs for large changes (PR1 > PR2 > PR3, each independently reviewable)
- Each PR tells a story with clear description

## Step 7: Tag and Review
- Tag every PR with AI-generated code as **AI-Assisted**
- Two human approvals for primarily AI-generated PRs
- Flag security boundaries, error handling, investigation/coalition code for close review

## Step 8: Quality Signals
- **Code Survival Rate** — AI code remaining 48 hours after merge. Low = agent generating throwaway code
- **Suggestion acceptance rate** — healthy range 25-35%. Higher may indicate over-reliance

## Merge Strategy
Squash-merge ephemeral branches. Delete immediately after merge. Branch alive longer than one session? Reconsider the approach.
