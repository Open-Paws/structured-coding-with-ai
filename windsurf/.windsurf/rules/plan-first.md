<!-- trigger: model_decision -->
# Plan-First Development

## When to Use
Starting any significant work, beginning a new session, tasks spanning multiple files, context approaching 50% usage.

## Step 1: Read Existing Code
Before writing anything, read the relevant code. Understand structure, naming, utilities, and patterns. AI agents duplicate at 4x normal rate because they lack codebase awareness. Searching first prevents this.

## Step 2: State the Change
Describe the change in one sentence. If you cannot, the task needs further decomposition. For advocacy projects: identify which bounded context is affected and whether the change crosses context boundaries.

## Step 3: Write a Specification
Requirements before implementation. Include: what the code does, inputs, outputs, error conditions, security/safety properties. For advocacy: data sensitivity classification, device seizure behavior, coalition boundary constraints.

## Step 4: Decompose into Subtasks
Each subtask should complete within half the remaining context window and produce a testable, committable result. Follow conceptual boundaries, not execution order — temporal decomposition is an Ousterhout red flag.

## Step 5: Execute Each Subtask
For each subtask:
1. **Plan** — describe what it will do
2. **Test** — write a failing test encoding expected behavior
3. **Implement** — minimum code to pass the test
4. **Verify** — run tests, confirm in context

Do not start the next subtask until current one passes and is committed.

## Step 6: Comprehension Check
After AI generates code, explain what it does in your own words before committing. AI-assisted developers score 17 percentage points lower on comprehension (Anthropic study). Use the **generation-then-comprehension pattern**: generate code, ask AI to explain it, verify your understanding matches. If you cannot explain the code, do not commit it.

## Context Management
- Start sessions fresh rather than extending degraded conversations
- Compact at ~50% context usage
- Break work into chunks completing within half the context window
- Two-failure rule: after two failed fixes, clear and restart with better prompt
