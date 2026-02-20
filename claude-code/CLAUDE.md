# Project Instructions

Animal advocacy and liberation technology. Use the project's ubiquitous language — never introduce synonyms for established domain terms. See domain glossary if one exists.

## Workflow

Read existing code before writing anything. Plan before code: read, plan, code, verify. Never create files or functions that duplicate existing ones — search first. Write a specification or interface before implementation. Write a failing test before writing the code that passes it. After two failed fix attempts, stop and re-approach with a better prompt rather than compounding errors.

## Constraints

- NEVER log, store, or transmit activist personally identifiable information
- NEVER send data to external APIs without explicit project-owner approval
- ALWAYS use zero-retention configurations for any third-party service
- ALWAYS apply progressive disclosure for traumatic content (investigation footage, slaughter documentation)
- Abstract all vendor dependencies behind project-owned interfaces so providers can be swapped without code changes
- Assume adversarial legal discovery, not just hackers — investigation data is court-subpoena targets
- Encrypted local storage; no telemetry to third parties

## Review Checklist

Before finishing any task, check for:

- **Shallow modules** — reject thin wrappers that add surface area without hiding complexity
- **DRY violations** — AI-generated code clones existing logic at 4x the normal rate; search before writing
- **Suppressed errors** — never catch-all or silently swallow failures; handle errors at the right level
- **Over-patterning** — use the simplest structure that works; don't force design patterns where a plain function suffices
- **Leaked internals** — hide implementation details; expose only what callers need
- **Test quality** — every test must fail when the behavior it covers is broken; delete tests that verify nothing
- **Legacy velocity** — AI-written code churns 2x faster; optimize for readability and changeability, not cleverness
- **AI-Assisted tags** — mark AI-generated or AI-modified code per project convention

For investigation or evidence-handling code, run a security review focused on data leakage, PII exposure, and ag-gag legal risk.

## Scoped Rules

Context-specific rules live in `.claude/rules/`. These activate automatically based on file path or task type and keep this main file short.

## Hooks

See `hooks-template.md` for deterministic enforcement via shell hooks. Hooks run before or after agent actions and catch issues that instructions alone cannot enforce reliably:

- **Pre-commit** — block sensitive data from reaching git history
- **Post-edit** — auto-format files after every edit
- **Pre-push** — run the full test suite before any push

## MCP Servers

Self-host MCP servers when handling sensitive advocacy data. Every MCP connection extends the attack surface — audit each server's data access, network calls, and retention policy before enabling it.
