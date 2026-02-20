# Code Review Checklist for AI-Assisted Advocacy Development

This is the full code review checklist — a structured process for reviewing code. Distinct from the Review custom mode (which defines the reviewer's persona and access controls), this file documents the complete layered review methodology and specific items to check.

## When to Use
- Reviewing any code before merge — especially AI-generated code
- Preparing your own code for review
- When a PR is tagged AI-Assisted
- When changes touch investigation data, coalition boundaries, or emotional safety features

## Layered Review Pipeline

### Layer 1: Automated Checks (Zero Human Effort)
Before any human looks at the code, verify these pass:
- Formatting and linting — automated, enforced in CI, not discussed in review
- Static analysis and type checking — structural issues, type errors, known vulnerability patterns
- Security scanning — hardcoded secrets, known vulnerabilities, dependency issues
- Test suite — all tests pass, no regressions

If any automated check fails, fix it before requesting review. Do not submit "I'll fix the tests later" PRs.

### Layer 2: AI-Assisted First-Pass Review
Use AI to flag potential issues. AI catches well: inconsistent error handling, missing null checks, unused imports, common security patterns, deviations from project conventions, performance anti-patterns. AI misses: whether the approach is correct, whether business logic matches requirements, whether the code will be maintainable, whether tests verify meaningful properties, subtle concurrency issues. Treat AI review flags as suggestions, not verdicts.

### Layer 3: Human Review — Design Quality Red Flags
Walk through the Ousterhout red flags checklist:

- **Shallow module** — interface as complex as the implementation; the abstraction hides nothing
- **Information leakage** — implementation details escape through the interface
- **Temporal decomposition** — code structured by execution order rather than conceptual boundaries
- **Pass-through method** — method does nothing except call another method with the same signature
- **Repetition** — same logic in multiple places; AI duplicates at 4x the normal rate
- **Special-general mixture** — general-purpose code polluted with special-case handling
- **Overexposure** — interface more complex than the implementation it wraps
- **Vague name** — name does not precisely describe the entity
- **Hard to describe** — if the interface is hard to describe, the design is probably wrong

### Layer 4: Human Review — AI-Specific Failure Patterns
Check specifically for AI-introduced patterns:

- **DRY violations** — does this duplicate something already in the codebase?
- **Multi-responsibility functions** — does any function do more than one thing?
- **Suppressed errors** — has the AI removed safety checks, caught too broadly, swallowed failures?
- **Hallucinated APIs** — does the code call libraries, methods, or endpoints that do not exist?
- **Over-patterning** — Strategy/Factory/Observer where a function and conditional would suffice?
- **Silent failure pattern** — AI may remove safety checks to make code appear to work, create fake output matching desired formats, or edit tests to pass rather than fixing code. Verify ALL safety checks from original code are preserved. Compare error handling between old and new versions explicitly.

### Layer 5: Advocacy-Specific Review

- **Data leak vectors** — does this change create any path for sensitive data to leave the system? Check logging, error messages, telemetry, API responses, serialization for investigation data, witness identities, activist PII.
- **Surveillance surface area** — does this increase the metadata footprint? New timestamps, access logs, IP recording, device fingerprinting that could identify activists under legal discovery.
- **Emotional safety** — if this code displays content, does it respect progressive disclosure? Is graphic content behind explicit opt-in? Are content warnings specific enough?
- **Coalition boundary violations** — does data cross organizational boundaries without an anti-corruption layer?

### Layer 6: Test Quality Review
- Do tests fail if the code is wrong? (Not tautological)
- Do assertions encode domain rules you can name?
- Would mutation testing kill these tests?
- Are error paths tested, not just happy paths?
- Are adversarial inputs tested for advocacy attack surfaces?

## Verdict
Summarize findings by layer. Classify as:
- **Blocking** — security vulnerabilities, data leaks, silent failures, broken tests, missing encryption, exposed witness identities, coalition boundary violations
- **Suggestion** — style, naming, refactoring, documentation

For primarily AI-generated PRs, require two human approvals.
