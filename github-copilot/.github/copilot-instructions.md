# Animal Advocacy Platform

Software for animal liberation and advocacy. High-risk domain: investigation data is subpoena-target evidence, activists face legal prosecution, system compromise endangers lives. See `.github/instructions/advocacy-domain.md` for ubiquitous language — NEVER introduce synonyms for established domain terms.

## Workflow

Read existing code before writing anything. Plan before code: read, plan, code, verify. Never create files or functions that duplicate existing ones — search first. Write a specification before implementation. Write a failing test before writing code. After two failed fix attempts, stop and re-approach rather than compounding errors.

## Constraints

- NEVER log, store, or transmit activist personally identifiable information
- NEVER send data to external APIs without explicit project-owner approval
- ALWAYS use zero-retention configurations for any third-party service
- ALWAYS apply progressive disclosure for traumatic content (investigation footage, slaughter documentation)
- Abstract all vendor dependencies behind project-owned interfaces — vendor lock-in is a movement risk
- Assume adversarial legal discovery: investigation data is court-subpoena material
- Encrypted local storage; no telemetry to third parties

## Review Checklist

Before finishing any task, verify AI output against these ranked failure modes:

1. **DRY** — search the codebase before writing anything new; AI duplicates at 4x the normal rate
2. **Deep modules** — reject shallow wrappers and pass-through methods (Ousterhout red flags)
3. **Single responsibility** — each function does one thing at one level of abstraction
4. **Error handling** — never catch-all or silently swallow; AI suppresses errors and removes safety checks
5. **Information hiding** — expose only what callers need
6. **Ubiquitous language** — use movement terminology, not AI-invented synonyms
7. **Design for change** — abstraction layers and loose coupling over "works now"
8. **Legacy velocity** — AI code churns 2x faster; write for readability, apply characterization tests
9. **Over-patterning** — use simplest structure that works; reject unnecessary patterns
10. **Test quality** — every test must fail when the behavior it covers is broken

## Scoped Guidance

See `.github/instructions/` for domain-specific rules: testing, security, privacy, cost optimization, advocacy domain, accessibility, emotional safety. See `.github/prompts/` for invocable workflows. See `.github/skills/` for detailed process guidance.
