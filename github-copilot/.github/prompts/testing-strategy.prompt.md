# Testing Strategy for AI-Assisted Advocacy Development

You are guiding a developer through writing or reviewing tests for an animal advocacy project. In advocacy software, silent test failures mean lost evidence or exposed activists. Follow these steps in order.

## Step 1: Read the Specification

Before writing any test, identify the specification or acceptance criteria for the behavior under test. If no spec exists, write one — even a brief description of what the code should do and what constitutes failure. Without a spec, AI generates tests that mirror the implementation rather than the intent, producing circular validation.

## Step 2: Write Failing Tests from the Spec

Generate tests from the specification BEFORE writing implementation. Each test should encode a business rule you can state in words. For advocacy software: "investigation records must be anonymized before export," "coalition data must not cross organizational boundaries without explicit agreement," "graphic content must never display without a content warning." Write the test. Verify it fails.

## Step 3: Verify Tests Fail for the Right Reason

A failing test is only useful if it fails because the behavior is absent — not because of a setup error or typo. Read each failure message. Confirm it describes the missing behavior, not a broken test.

## Step 4: Implement Until Tests Pass

Write the minimum implementation that makes the failing tests pass. Do not write more code than the tests demand.

## Step 5: Review Assertions Against the Spec

This is the critical step for AI-generated tests. Ask three questions of every assertion:
1. **Does this test fail if the code is wrong?** If you break the implementation and the test still passes, it is worthless.
2. **Does the assertion encode a domain rule?** If you cannot name the rule, it is a snapshot, not a test.
3. **Would mutation testing kill this?** If changing `+` to `-` leaves the test green, the assertion is weak.

NEVER accept tautological assertions — tests that assert output equals the output of the same function call.

## Step 6: Run Mutation Testing

Run a mutation testing tool against the suite. Surviving mutants reveal assertions that look thorough but verify nothing. Feed surviving mutants to the AI and ask it to write tests that kill them. Mutation score is the primary quality metric — not coverage percentage.

## Step 7: Fix Weak Tests

For each surviving mutant, write a targeted test that kills it. This closes the loop between test generation and test quality.

## Five Anti-Patterns to Reject on Sight

1. **Snapshot trap** — tests that snapshot current output and assert against it. They verify nothing about correctness.
2. **Mock everything** — over-mocked tests verify mock behavior, not real code. Mock only at system boundaries.
3. **Happy path only** — AI tests overwhelmingly test success. Explicitly request error path, boundary condition, and adversarial input tests. In advocacy software, error paths are where people get hurt.
4. **Test-after-commit** — writing tests after code is committed defeats the feedback loop.
5. **Coverage theater** — chasing coverage numbers with meaningless assertions.

## Advocacy-Specific Testing

- Contract tests at every service boundary, especially coalition cross-organization APIs
- Test adversarial inputs: SQL injection through investigation search, XSS through testimony display, path traversal through evidence uploads
- Verify progressive disclosure: graphic content must not render without explicit opt-in
- Test offline behavior: what happens when connectivity drops during evidence sync
