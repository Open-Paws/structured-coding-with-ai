# Rules Directory

Contains mode-specific rule files, cross-cutting concern files, and a memory bank subdirectory. Kilo Code loads the appropriate mode file based on the active mode, and concern files are referenced by modes as needed.

## Mode Rules

Each file defines the behavior, constraints, and workflow for one operational mode:

- `ask-mode.md` -- Read-only exploration. Explains code, traces data flow, identifies design issues. Cannot modify files.
- `architect-mode.md` -- Design and planning. Proposes architecture, writes specifications, decomposes features. No implementation.
- `code-mode.md` -- Implementation. Reads, writes, runs tests. Follows a read-plan-code-test-verify workflow with an AI code review checklist.
- `debug-mode.md` -- Structured debugging. Reproduce, gather context, form hypotheses, binary search, fix, verify.
- `orchestrator-mode.md` -- Workflow coordination. Decomposes tasks, delegates to other modes, tracks progress, enforces process gates.

## Concern Files (7)

Cross-cutting rules that apply across multiple modes:

- `testing.md` -- Assertion quality, spec-first test generation, mutation testing, AI-specific test anti-patterns.
- `security.md` -- Zero-retention APIs, encrypted storage, slopsquatting defense, device seizure readiness.
- `privacy.md` -- Data minimization, metadata stripping, consent management, real deletion.
- `cost-optimization.md` -- Model routing, token budget management, vendor lock-in avoidance.
- `advocacy-domain.md` -- Ubiquitous language dictionary and bounded context definitions.
- `accessibility.md` -- Internationalization, offline-first, low-bandwidth, assistive technology support.
- `emotional-safety.md` -- Progressive disclosure of traumatic content, content warnings, user control.

## Subdirectory

- `memory-bank/` -- Three template files for progressive project context (brief, architecture, decision history).
