<!-- trigger: always_on -->
# Animal Advocacy Platform

Software for animal liberation and advocacy. High-risk domain: investigation data is subpoena-target evidence, activists face prosecution, system compromise endangers lives.

## Workflow

- Read existing code before writing anything — NEVER create duplicates
- Plan before code: read, plan, code, verify
- Spec-first: write requirements before implementation
- Test-first: write failing tests before code
- Two-failure rule: after two failed fixes, restart with a better approach
- Commit after each logical subtask, not after entire tasks

## Constraints

- NEVER log, store, or transmit activist personally identifiable information
- NEVER send data to external APIs without explicit project-owner approval
- ALWAYS use zero-retention configurations for third-party services
- ALWAYS apply progressive disclosure for traumatic content
- Abstract all vendor dependencies — vendor lock-in is a movement risk
- Assume adversarial legal discovery: investigation data is court-subpoena material
- Encrypted local storage; no telemetry to third parties

## Review Checklist — Top 10 AI Failure Modes

1. **DRY** — AI clones at 4x normal rate; search before writing
2. **Deep modules** — reject shallow wrappers and pass-through methods
3. **Single responsibility** — split multi-responsibility functions
4. **Error handling** — never catch-all or swallow failures silently
5. **Information hiding** — expose only what callers need
6. **Ubiquitous language** — use movement terms, not AI synonyms
7. **Design for change** — abstraction layers and loose coupling
8. **Legacy velocity** — characterization tests before modifying AI code
9. **Over-patterning** — simplest structure that works
10. **Test quality** — every test must fail when behavior breaks

## Scoped Rules

See other rule files for: testing, security, privacy, cost, advocacy domain, accessibility, emotional safety, git workflow, and process skills.
