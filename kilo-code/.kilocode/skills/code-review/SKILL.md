---
name: code-review
description: Layered code review pipeline — automated checks first, then AI-assisted review, then human review focused on Ousterhout red flags, AI failure patterns, silent failures, and advocacy-specific concerns
---
# Code Review

## When to Use
- Reviewing any code before merge — especially AI-generated code
- Preparing your own code for review
- When a PR is tagged AI-Assisted
- When changes touch investigation data, coalition boundaries, or emotional safety features

## Process

### Layer 1: Automated Checks (Zero Human Effort)
Before any human looks at the code, verify these pass:
- Formatting and linting — automated, enforced in CI, not discussed in review
- Static analysis and type checking — structural issues, type errors, known vulnerability patterns
- Security scanning — hardcoded secrets, known vulnerabilities, dependency issues
- Test suite — all tests pass, no regressions

If any automated check fails, fix before requesting review. No "I'll fix the tests later" PRs.

### Layer 2: AI-Assisted First-Pass Review
AI catches well: inconsistent error handling, missing null checks, unused imports, common security patterns, convention deviations, performance anti-patterns. AI misses: whether the approach is correct, whether business logic matches requirements, maintainability, whether tests verify meaningful properties, subtle concurrency issues. Treat AI flags as suggestions, not verdicts.

### Layer 3: Human Review — Design Quality Red Flags
Walk the Ousterhout red flags checklist — structural problems most common in AI-generated code:
- **Shallow module** — interface as complex as implementation; abstraction hides nothing
- **Information leakage** — implementation details escape through interface; callers depend on internals
- **Temporal decomposition** — structured by execution order rather than conceptual boundaries
- **Pass-through method** — does nothing except call another method with same signature
- **Repetition** — same logic in multiple places; AI duplicates at 4x normal rate
- **Special-general mixture** — general-purpose code polluted with special cases

### Layer 4: Human Review — AI-Specific Failure Patterns
- **DRY violations** — duplicates something already in the codebase? Search before accepting.
- **Multi-responsibility functions** — does more than one thing at one abstraction level? Split.
- **Suppressed errors** — removed safety checks, caught too broadly, silently swallowed? Review every error path.
- **Hallucinated APIs** — calls libraries, methods, or endpoints that do not exist? Verify every external dependency.
- **Over-patterning** — Strategy, Factory, Observer where a function and conditional suffice?
- **Silent failure pattern** — AI may remove safety checks to make code appear to work, create fake output matching desired formats, or edit tests to pass rather than fixing code. Verify ALL safety checks from original code are preserved. Compare error handling between old and new versions explicitly.

### Layer 5: Advocacy-Specific Review
- **Data leak vectors** — new path for sensitive data to leave the system? Check logging, error messages, telemetry, API responses, serialization for investigation data, witness identities, or activist PII.
- **Surveillance surface area** — new metadata footprint? Timestamps, access logs, IP recording, device fingerprinting that could identify activists under legal discovery.
- **Emotional safety** — content displayed to users respects progressive disclosure? Graphic content behind explicit opt-in? Content warnings specific enough?
- **Coalition boundary violations** — data crossing org boundaries without anti-corruption layer? AI optimizes for expedience and imports directly across bounded contexts.

### Render Verdict
Summarize findings by layer. Distinguish blocking issues (security vulnerabilities, data leaks, silent failures, broken tests) from suggestions (style, naming, refactoring). For primarily AI-generated PRs, require two human approvals.
