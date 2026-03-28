# Augment Code Rules Directory

Contains 14 files: one core rule file and 13 concern and skill files. All files are loaded together on every interaction -- there is no conditional loading or mode selection.

## Files

### Core Rules

- `main.md` -- Project identity, workflow (read-plan-code-verify), security constraints, two-failure rule, and development guidelines. References the concern and skill files below.

### Concern Files (7)

- `testing.md` -- Assertion quality, spec-first generation, AI test anti-patterns.
- `security.md` -- Zero-retention APIs, encrypted storage, slopsquatting defense, device seizure readiness.
- `privacy.md` -- Data minimization, metadata stripping, real deletion, consent management.
- `cost-optimization.md` -- Model routing, token budgets, vendor lock-in avoidance.
- `advocacy-domain.md` -- Ubiquitous language dictionary and bounded context definitions.
- `accessibility.md` -- Internationalization, offline-first, low-bandwidth support.
- `emotional-safety.md` -- Progressive disclosure of traumatic content, content warnings.

### Skill Files (6)

- `git-workflow.md` -- Atomic commits, ephemeral branches, PR curation, AI-Assisted tagging.
- `testing-strategy.md` -- Spec-first test generation, mutation testing, assertion quality review.
- `requirements-interview.md` -- Structured stakeholder interview producing specification documents.
- `plan-first.md` -- Read-plan-code-verify workflow with spec writing and subtask decomposition.
- `code-review.md` -- Layered review pipeline with Ousterhout red flags and AI failure pattern detection.
- `security-audit.md` -- Dependency verification, zero-retention compliance, device seizure readiness.
