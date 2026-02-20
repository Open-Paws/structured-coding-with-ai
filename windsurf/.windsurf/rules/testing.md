<!-- trigger: always_on -->
# Testing Rules

Testing is the keystone of AI-assisted advocacy development. Without tests, agents drift silently — and silent drift means lost evidence, exposed activists, or traumatic content displayed without safeguards.

## Assertion Quality — Non-Negotiable

NEVER accept tautological assertions — tests asserting output equals the same function call. Every assertion must encode a business rule you can state in words.

Three questions for every AI-generated test:
1. Does this test fail if the code is wrong?
2. Does the assertion encode a domain rule you can name?
3. Would mutation testing kill this?

**Mutation score over coverage percentage.** 90% coverage with 40% mutation score is false security.

## Spec-First Generation

ALWAYS generate tests from specs before implementation. Tests from existing code mirror implementation, not intent — circular validation. Write the test, verify it fails, then implement.

## Property-Based Testing

Use property-based tests for invariants: anonymization irreversibility, encryption not leaking plaintext length, coalition data boundaries holding under arbitrary inputs.

## Test Error Paths

AI tests overwhelmingly cover happy paths. In advocacy software, error paths are where people get hurt. Test: failed encryption, leaked identity, broken anonymization, missing content warnings, network drop during evidence upload, storage seizure mid-write.

## Contract Tests at Boundaries

AI hallucinates APIs — ~20% of recommended packages do not exist. Use consumer-driven contract tests at every service boundary, especially coalition cross-org APIs.

## Infrastructure

Fast execution is non-negotiable — 10-min suite across 15 iterations burns 2.5 hours. Parallel execution, test isolation, no shared state. Flaky tests poison the AI feedback loop. Test-to-code ratio 1:1 or higher.

## Adversarial Input Testing

Test: SQL injection through investigation search, XSS through testimony display, path traversal through evidence uploads, oversized payloads against offline sync.
