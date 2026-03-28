# Rules Directory

Contains 18 files: 5 mode-specific rules, 7 cross-cutting concerns, and 6 skill definitions. Roo Code loads `rules-{mode}.md` based on the active mode. Concern and skill files are referenced within mode rules as needed.

## Mode Rules (5)

Each file is loaded when its corresponding mode is active:

- `rules-architect.md` -- Design and planning. Proposes architecture, writes specifications, enforces bounded context separation. No implementation.
- `rules-code.md` -- Implementation. Read-plan-code-test-verify workflow with AI code review checklist and two-failure rule.
- `rules-debug.md` -- Structured debugging: reproduce, hypothesize, isolate, fix, verify. Checks for data leak vectors in error paths.
- `rules-review.md` -- Layered code review (custom mode). Automated checks first, then AI failure patterns, then advocacy-specific concerns. Distinguishes blocking issues from suggestions.
- `rules-interview.md` -- Requirements interview (custom mode). One question at a time across five areas: threat model, legal exposure, coalition needs, user safety, technical constraints.

## Concern Files (7)

Cross-cutting rules applied across modes:

- `testing.md` -- Assertion quality, spec-first generation, AI test anti-patterns.
- `security.md` -- Zero-retention APIs, encrypted storage, slopsquatting defense, device seizure readiness.
- `privacy.md` -- Data minimization, metadata stripping, real deletion, consent management.
- `cost-optimization.md` -- Model routing, token budgets, vendor lock-in avoidance.
- `advocacy-domain.md` -- Ubiquitous language dictionary and bounded context definitions.
- `accessibility.md` -- Internationalization, offline-first, low-bandwidth support.
- `emotional-safety.md` -- Progressive disclosure of traumatic content, content warnings.

## Skill Files (6)

Inline skill definitions (not subdirectories -- each is a single markdown file):

- `git-workflow.md` -- Atomic commits, ephemeral branches, PR curation, AI-Assisted tagging.
- `testing-strategy.md` -- Spec-first test generation, mutation testing, assertion quality review.
- `requirements-interview.md` -- Structured stakeholder interview producing specification documents.
- `plan-first.md` -- Read-plan-code-verify workflow with spec writing and subtask decomposition.
- `code-review.md` -- Layered review pipeline with Ousterhout red flags and AI failure pattern detection.
- `security-audit.md` -- Dependency verification, zero-retention compliance, device seizure readiness.

## Boomerang Task Chain

The modes are designed to delegate work in sequence:

**Interview** --> **Architect** --> **Code** --> **Review** --> **Code**

Interview gathers requirements, Architect designs, Code implements, Review audits, and Code addresses any findings from Review.
