# Git Workflow for AI-Assisted Advocacy Development

You are guiding a developer through the git workflow for an animal advocacy project. AI-generated code requires stricter commit and PR discipline because AI adoption inflated PR size by 154% and review time by 91%. Follow these steps in order.

## Step 1: Create an Ephemeral Branch

Create a short-lived branch for this task. Trunk-based development is the goal — this branch is a safety net, not a long-lived workspace. If the work is not mergeable within one session, delete the branch and reconsider the approach. Name the branch for the specific task, not a feature epic.

## Step 2: Decompose into Subtasks

Break the work into the smallest logical subtasks. Each subtask becomes one commit. If the task decomposes into "extract interface, implement adapter, update callers," those are three separate commits. Never batch the entire task into one commit.

## Step 3: Implement One Subtask

Write the code for exactly one subtask. Do not move ahead to the next subtask.

## Step 4: Test Before Committing

Run the relevant test subset before each commit. Every commit must leave the codebase in a passing state. For advocacy code handling investigation or evidence data, also verify that no sensitive data has leaked into test output, logs, or error messages.

## Step 5: Write the Commit Message

Write a commit message that explains WHY, not WHAT — the code shows what changed. First line: 50 characters max, imperative mood. Reference the issue or ticket. Add AI attribution trailers so the team knows which code was agent-generated.

## Step 6: Repeat for Each Subtask

Cycle: implement one subtask, test, commit. Each commit should be independently understandable. If you read it in isolation six months from now, you should know what it does and why.

## Step 7: Curate the Pull Request

PR curation is the critical human skill. Do not submit the full output as one PR. Split into reviewable chunks:
- Target under 200 lines changed per PR, ideally under 100
- Use stacked PRs for large changes (PR1, PR2, PR3 — each independently reviewable)
- Each PR tells a coherent story with a clear description explaining the reasoning

## Step 8: Tag and Request Review

- Tag every PR containing AI-generated code as **AI-Assisted**
- Require two human approvals for primarily AI-generated PRs
- Call out areas needing close review — especially security boundaries, error handling, and any code touching investigation or coalition data

## Step 9: Track Quality Signals

- **Code Survival Rate** — how much AI-generated code remains unchanged 48 hours after merge. Low survival means the agent is generating code that humans immediately rewrite.
- **Suggestion acceptance rate** — healthy range is 25-35%. Higher may indicate over-reliance without critical review.

## Merge Strategy

Squash-merge ephemeral branches to keep trunk history clean. Delete branches immediately after merge. If a branch has lived longer than one working session, evaluate whether the approach needs to change.
