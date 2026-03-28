<!-- trigger: manual -->
# Code Review

## When to Use
Reviewing code before merge (especially AI-generated), preparing code for review, PR tagged AI-Assisted, changes touching investigation data, coalition boundaries, or emotional safety.

## Layer 1: Automated Checks (Zero Human Effort)
Verify these pass before any human review:
- Formatting/linting — automated, enforced in CI
- Static analysis and type checking
- Security scanning — hardcoded secrets, known vulnerabilities, dependencies
- Test suite — all passing, no regressions

Fix failures before requesting review. No "fix tests later" PRs.

## Layer 2: AI-Assisted First Pass
AI catches well: inconsistent error handling, missing null checks, unused imports, security patterns, convention deviations, performance anti-patterns. AI misses: whether the approach is correct, business logic accuracy, maintainability, meaningful test properties, concurrency issues. Treat AI flags as suggestions.

## Layer 3: Design Quality — Ousterhout Red Flags
- **Shallow module** — interface as complex as implementation; abstraction hides nothing
- **Information leakage** — implementation details escape through interface
- **Temporal decomposition** — structured by execution order, not concepts
- **Pass-through method** — calls another method with same signature, adds nothing
- **Repetition** — same logic in multiple places; AI duplicates at 4x rate
- **Special-general mixture** — general code polluted with special cases

## Layer 4: AI-Specific Failure Patterns
- **DRY violations** — does this duplicate existing code? Search before accepting
- **Multi-responsibility functions** — doing more than one thing? Split
- **Suppressed errors** — safety checks removed, exceptions caught too broadly, failures swallowed silently
- **Hallucinated APIs** — libraries, methods, endpoints that do not exist? Verify every dependency
- **Over-patterning** — Strategy/Factory/Observer where a function and conditional suffice
- **Silent failure** — AI removes safety checks to appear working, creates fake output matching formats, edits tests to pass rather than fixing code. Verify ALL original safety checks preserved. Compare error paths between old and new

## Layer 5: Advocacy-Specific
- **Data leak vectors** — new paths for sensitive data to leave? Check logging, error messages, telemetry, API responses, serialization
- **Surveillance surface** — new metadata (timestamps, access logs, IP, fingerprints) usable to identify activists under legal discovery
- **Emotional safety** — content display respects progressive disclosure? Graphic content behind opt-in? Warnings specific?
- **Coalition boundaries** — data crossing org boundaries without anti-corruption layer? AI imports directly across contexts

## Verdict
Summarize by layer. Distinguish blocking (security, data leaks, silent failures, broken tests) from suggestions. Two human approvals for AI-generated PRs.
