<!-- trigger: glob: **/*.test.*,**/*.spec.* -->
# Testing Strategy

## When to Use
Writing or generating tests, reviewing AI-generated tests, setting up test infrastructure, when suite quality is in question.

## Process

### Read the Specification First
Before writing any test, identify the spec or acceptance criteria. If none exists, write one. Without a spec, AI generates tests mirroring implementation — circular validation.

### Spec-First Generation (Preferred)
Generate tests from the specification BEFORE implementation. Each test encodes a business rule stated in words: "investigation records must be anonymized before export," "coalition data must not cross org boundaries without agreement," "graphic content must never display without warning." Write the test. Verify it fails. Then implement.

### Review Assertions Against the Spec, Not the Code
Three questions for every assertion:
1. Does this test fail if the code is wrong?
2. Does the assertion encode a domain rule you can name?
3. Would mutation testing kill this?

NEVER accept tautological assertions. Mutation score is the primary quality metric — not coverage.

### Run Mutation Testing
Surviving mutants reveal weak assertions. Feed them to the AI to generate targeted tests that kill them. This closes the generation/quality loop.

## Five Generation Patterns
1. **Implementation-first** — tests from existing code. Dangerous: mirrors code, not intent. Use only for characterization.
2. **Spec-first** — tests from specification before coding. Preferred. Encodes intent.
3. **Edge-case generation** — ask AI for: empty inputs, boundaries, null/undefined, unicode, timezones, concurrency, overflow. AI excels here.
4. **Characterization tests** — capture current behavior of legacy/AI code before changing. Cover before you change.
5. **Mutation-guided** — run mutation testing, feed survivors to AI, generate targeted tests.

## Five Anti-Patterns to Reject
1. **Snapshot trap** — snapshots of current output. Pass today, break on correct changes. Verify nothing.
2. **Mock everything** — over-mocked tests verify mocks, not code. Mock only at system boundaries.
3. **Happy path only** — AI tests overwhelmingly test success. Explicitly request error paths, boundaries, adversarial inputs. In advocacy, error paths are where harm occurs.
4. **Test-after-commit** — tests after code is committed defeats the feedback loop. Tests must exist during development.
5. **Coverage theater** — meaningless assertions chasing numbers. Covered without assertion = not tested.

## Advocacy-Specific
- Contract tests at every coalition cross-org API boundary
- Adversarial inputs: SQL injection through investigation search, XSS through testimony display, path traversal through evidence uploads
- Progressive disclosure verification: graphic content must not render without opt-in
- Offline behavior: what happens when connectivity drops during evidence sync
- Fast execution: 10-min suite across 15 AI iterations = 2.5 hours wasted
