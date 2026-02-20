# Cursor Scoped Rules (MDC Format)

These are `.mdc` rule files for Cursor. Each file has YAML frontmatter that determines how and when Cursor loads it.

## MDC Format

Each file starts with YAML frontmatter specifying its activation mode, followed by `---`, then markdown content. The four activation modes are:

- **alwaysApply** -- `alwaysApply: true` in frontmatter. Loaded into every conversation.
- **autoAttached** -- `globs: ["pattern"]` in frontmatter. Loaded when the active file matches.
- **agentRequested** -- `description: "..."` in frontmatter. The agent reads the description and decides whether to load the rule based on the current task.
- **manual** -- `description: "..."` in frontmatter (with wording indicating manual invocation). User invokes with `@` in chat.

## Files

| File | Activation Mode | Details |
|------|----------------|---------|
| `testing.mdc` | alwaysApply | Testing assertion quality, spec-first generation, mutation testing |
| `security.mdc` | alwaysApply | Zero-retention APIs, encrypted storage, supply chain, ag-gag exposure |
| `advocacy-domain.mdc` | alwaysApply | Ubiquitous language dictionary, bounded contexts, anti-corruption layers |
| `privacy.mdc` | agentRequested | Data minimization, activist identity protection, GDPR/CCPA, anonymization |
| `cost-optimization.mdc` | agentRequested | Model routing, token budgets, vendor lock-in, self-hosted inference |
| `accessibility.mdc` | agentRequested | Internationalization, low-bandwidth, offline-first, mesh networking |
| `emotional-safety.mdc` | agentRequested | Progressive disclosure, content warnings, investigation footage handling |
| `git-workflow.mdc` | agentRequested | Atomic commits, ephemeral branches, PR curation, AI-Assisted tagging |
| `plan-first.mdc` | agentRequested | Read-plan-code-verify workflow, spec writing, subtask decomposition |
| `testing-strategy.mdc` | autoAttached | Globs: `**/*.test.*`, `**/*.spec.*`. Spec-first test generation, five anti-patterns |
| `requirements-interview.mdc` | manual | Structured stakeholder interview for advocacy projects |
| `code-review.mdc` | manual | Layered code review: Ousterhout red flags, AI failure patterns, advocacy concerns |
| `security-audit.mdc` | manual | Dependency audit, API retention, encrypted storage, ag-gag exposure assessment |
