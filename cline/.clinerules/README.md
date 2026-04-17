# Cline Rules Directory

Contains 14 files: one global rule file and 13 scoped files for concerns and skills. Cline loads `main.md` on every interaction. The scoped files are referenced from `main.md` and provide detailed rules for specific areas.

## Files

### Global Rules

- `main.md` -- Core rules, always loaded. Defines the Plan/Act workflow, read-before-write discipline, two-failure rule, security constraints, and references to concern and skill files.

### Concern Files (7)

- `testing.md` -- Assertion quality, spec-first generation, AI test anti-patterns.
- `security.md` -- Zero-retention APIs, encrypted storage, slopsquatting defense, device seizure readiness.
- `privacy.md` -- Data minimization, metadata stripping, real deletion, consent management.
- `cost-optimization.md` -- Model routing, token budgets, vendor lock-in avoidance.
- `advocacy-domain.md` -- Ubiquitous language dictionary and bounded context definitions.
- `accessibility.md` -- Internationalization, offline-first, low-bandwidth support.
- `emotional-safety.md` -- Progressive disclosure of traumatic content, content warnings.

### Skill Files (6)

- `git-workflow.md` -- Issue-first GitHub workflow: worktree-per-task, plan→review→implement loops, desloppify gate, PR monitoring until merged.
- `testing-strategy.md` -- Spec-first test generation, mutation testing, assertion quality review.
- `requirements-interview.md` -- Structured stakeholder interview producing specification documents.
- `plan-first.md` -- Read-plan-code-verify workflow with spec writing and subtask decomposition.
- `code-review.md` -- Layered review pipeline with Ousterhout red flags and AI failure pattern detection.
- `security-audit.md` -- Dependency verification, zero-retention compliance, device seizure readiness.
