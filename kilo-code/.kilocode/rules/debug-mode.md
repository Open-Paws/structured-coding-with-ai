# Debug Mode — Investigation and Fix

Debug mode is for finding and fixing bugs. You can read files, run tests, inspect state, and apply targeted fixes. Follow the structured debugging workflow — do not guess randomly.

## Debugging Workflow

### Step 1: Reproduce Reliably
Before anything else, establish a reliable reproduction. A failing test, a set of steps that triggers the bug, or a minimal reproduction case. Without reliable reproduction, you will guess — and guesses compound. Give me a failing test or reproduction steps before asking me to investigate.

### Step 2: Gather Full Context
Collect: the error message or stack trace, the relevant code, what was expected versus what happened, and what has already been tried. The more context I have, the better my hypotheses. Include the bounded context (Investigation Operations, Public Campaigns, Coalition Coordination, Legal Defense) the bug exists in.

### Step 3: Form Hypotheses — Do Not Jump to Fixes
Ask "what could cause this?" before "how do I fix this?" Generate multiple hypotheses ranked by likelihood. Resist the urge to apply the first plausible fix — multiple hypotheses let you test systematically.

### Step 4: Binary Search to Isolate
Narrow the problem space. Given a stack trace, identify which module is most likely responsible. Use bisection: disable half the suspect code, check if the bug persists, narrow further. This is faster and more reliable than reading every line.

### Step 5: Apply the Fix
Write the minimum change that addresses the root cause, not just the symptom. AI-generated fixes frequently address the symptom (making the error disappear) without fixing the underlying issue.

### Step 6: Verify the Fix
After applying a fix, ask:
- Does the original reproduction case pass?
- Could this fix mask a deeper problem?
- What other code paths could be affected by this root cause?
- Do all existing tests still pass?
- Is a regression test needed to prevent recurrence?

Write a test that would have caught this bug. The Pragmatic Programmer principle: find bugs once.

## Two-Failure Rule

After two failed fix attempts, STOP. The current approach is likely wrong. Clear the conversation and restart with better context. Switching to a different AI model can also break through blind spots — different models have different failure patterns.

## Advocacy-Specific Debugging

When debugging network or storage code, check for data leak vectors:
- Does the error path log sensitive data (investigation records, witness identities, activist PII)?
- Does the fallback behavior transmit data to an external service?
- Do error messages contain information that could identify activists under legal discovery?
- Does the debug output include unencrypted investigation content?
- If this is sync/replication code, does a failure leave decrypted data on disk?

When debugging coalition or cross-org code:
- Does the bug allow data to cross bounded context boundaries without anti-corruption layers?
- Could the bug expose one coalition partner's data to another partner with a different risk profile?

## What You Must Not Do

- Do not make speculative changes without hypotheses — every change must have a reason
- Do not "fix" tests by weakening assertions to match broken behavior
- Do not suppress errors to make symptoms disappear
- Do not introduce new code paths without tests
- Do not ignore security implications of debug output (no investigation data in logs)
