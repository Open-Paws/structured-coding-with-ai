---
name: testing-strategy
description: Spec-first test generation, assertion quality review, mutation testing, five anti-patterns to avoid — for AI-assisted advocacy development where silent test failures mean lost evidence or exposed activists
---
# Testing Strategy

## When to Use
- Writing or generating any tests
- Reviewing AI-generated test code
- Setting up test infrastructure for a new feature
- When test suite quality is in question (flaky tests, low mutation scores, false confidence)

## Process

### Step 1: Read the Specification
Before writing any test, identify the specification or acceptance criteria. If no spec exists, write one — even a brief description of intended behavior and failure conditions. Without a spec, AI generates tests that mirror implementation rather than intent, producing circular validation.

### Step 2: Write Failing Tests from the Spec (Spec-First Pattern)
Generate tests from the specification BEFORE writing implementation. Each test should encode a business rule stated in words. For advocacy software: "investigation records must be anonymized before export," "coalition data must not cross organizational boundaries without explicit agreement," "graphic content must never display without a content warning." Write the test. Verify it fails.

### Step 3: Verify Tests Fail for the Right Reason
A failing test is only useful if it fails because the behavior is absent — not setup error, typo, or misconfigured environment. Read each failure message. Confirm it describes missing behavior, not a broken test.

### Step 4: Implement Until Tests Pass
Write the minimum implementation to make failing tests pass. Do not write more code than tests demand.

### Step 5: Review Assertions Against the Spec, Not the Code
The critical step for AI-generated tests. Ask three questions of every assertion:
1. **Does this test fail if the code is wrong?** If you break the implementation and the test still passes, it is worthless.
2. **Does the assertion encode a domain rule?** If you cannot name the rule, it is a snapshot, not a test.
3. **Would mutation testing kill this?** If changing `+` to `-` leaves the test green, the assertion is weak.

NEVER accept tautological assertions — tests that assert output equals the same function call.

### Step 6: Run Mutation Testing
Run a mutation testing tool. Surviving mutants reveal assertions that look thorough but verify nothing. Feed surviving mutants to the AI to write tests that kill them. Mutation score is the primary quality metric — not coverage percentage.

### Step 7: Fix Weak Tests
For each surviving mutant, write a targeted test that kills it. This closes the loop between generation and quality.

## Five Generation Patterns
1. **Implementation-first** — tests from existing code. Dangerous: mirrors code, not intent. Use only for characterization tests.
2. **Spec-first** — tests from spec before coding. Preferred. Produces tests encoding intent.
3. **Edge-case generation** — ask AI for: empty inputs, boundary values, null/undefined, unicode, timezone boundaries, concurrent access, overflow.
4. **Characterization tests** — capture current behavior of untested code before changing it.
5. **Mutation-guided improvement** — run mutation testing, feed survivors to AI, generate targeted tests.

## Five Anti-Patterns to Reject on Sight
1. **Snapshot trap** — tests snapshotting output and asserting against it. Pass today, break on any correct change. Verify nothing.
2. **Mock everything** — over-mocked tests verify mock behavior, not real code. Mock only at system boundaries.
3. **Happy path only** — AI tests overwhelmingly cover success. Explicitly request error, boundary, and adversarial input tests. In advocacy, error paths are where people get hurt.
4. **Test-after-commit** — tests after code is committed defeats the feedback loop.
5. **Coverage theater** — meaningless assertions chasing numbers. A "covered" line with no assertion is not tested.

## Advocacy-Specific Testing
- Contract tests at every service boundary, especially coalition cross-org APIs
- Adversarial inputs: SQL injection through investigation search, XSS through testimony display, path traversal through evidence uploads
- Progressive disclosure verification: graphic content must not render without explicit opt-in
- Offline behavior: what happens when connectivity drops during evidence sync
- Fast execution non-negotiable for AI agent loops — 10-minute suite across 15 iterations burns 2.5 hours
