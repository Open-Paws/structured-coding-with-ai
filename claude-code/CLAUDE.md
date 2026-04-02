# Claude Code — Animal Advocacy Instructions

Software for animal liberation and advocacy. This is a high-risk domain: investigation data is subpoena-target evidence, activists face legal prosecution, and system compromise endangers lives. See `.claude/rules/advocacy-domain.md` for ubiquitous language — NEVER introduce synonyms for established domain terms.

## Usage

Copy this directory into any Open Paws project root:

```bash
cp CLAUDE.md your-project/
cp hooks-template.md your-project/
cp -r .claude your-project/
```

The `.claude/rules/` files are scoped by filename and activate contextually. The `.claude/skills/` files are invoked by slash commands or agent prompts. See `hooks-template.md` for pre-commit/post-edit/pre-push hook setup.

## Workflow

Read existing code before writing anything. Plan before code: read, plan, code, verify. Never create files or functions that duplicate existing ones — search first. Write a specification before implementation. Write a failing test before writing code. After two failed fix attempts, stop and re-approach with a better prompt rather than compounding errors.

## Constraints

- NEVER log, store, or transmit activist personally identifiable information
- NEVER send data to external APIs without explicit project-owner approval
- ALWAYS use zero-retention configurations for any third-party service
- ALWAYS apply progressive disclosure for traumatic content (investigation footage, slaughter documentation)
- Abstract all vendor dependencies behind project-owned interfaces — vendor lock-in is a movement risk
- Assume adversarial legal discovery: investigation data is court-subpoena material, not just hacker targets
- Encrypted local storage; no telemetry to third parties

## Review Checklist

Before finishing any task, verify AI output against these ranked failure modes:

1. **DRY** — AI clones existing logic at 4x the normal rate; search the codebase before writing anything new
2. **Deep modules** — reject shallow wrappers and pass-through methods that add surface area without hiding complexity (Ousterhout red flags: shallow module, overexposure, pass-through)
3. **Single responsibility** — each function does one thing at one level of abstraction; split multi-responsibility functions immediately
4. **Error handling** — never catch-all or silently swallow failures; AI suppresses errors and removes safety checks — verify every error path in advocacy-critical code where silent failure means evidence loss
5. **Information hiding** — expose only what callers need; if the interface is as complex as the implementation, the abstraction is shallow
6. **Ubiquitous language** — code must use movement terminology (campaign, investigation, coalition, sanctuary), not AI-invented synonyms; language drift in advocacy software causes miscommunication across coalition partners
7. **Design for change** — insist on abstraction layers and loose coupling; AI optimizes for "works now" over "works later," but advocacy tools must outlast any single campaign
8. **Legacy velocity** — AI code churns 2x faster; write for readability and changeability, apply characterization tests before modifying AI-generated modules
9. **Over-patterning** — use the simplest structure that works; reject Strategy/Factory/Observer where a plain function suffices
10. **Test quality** — every test must fail when the behavior it covers is broken; mutation testing is the countermeasure for tautological AI-generated assertions

For investigation or evidence-handling code: security review for data leakage, PII exposure, and ag-gag legal risk.

## Scoped Rules

See `.claude/rules/` for domain-specific guidance: testing, security, privacy, cost optimization, advocacy domain, accessibility, and emotional safety. These activate based on file path or task context.

## Hooks

See `hooks-template.md`. Hooks execute shell commands before/after agent actions — strictly superior to instruction-based enforcement for deterministic checks. Pre-commit: block sensitive data from git history. Post-edit: auto-format. Pre-push: full test suite.

## Code Quality

See `.claude/rules/desloppify.md` for desloppify setup and usage.

## External Contribution Safety

When working in a repository that is NOT part of the Open Paws organization, switch to neutral mode:
- Match the target repo's commit style — read the last 5 commits first
- Do not mention Open Paws, advocacy context, or movement terminology in commits, PRs, or comments
- Do not include Co-Authored-By trailers or "Generated with" attribution
- Write PR descriptions proportional to diff size, human-style

Repo classification: `git remote get-url origin` — if the owner is `Open-Paws`, use advocacy mode. Otherwise, neutral mode. Absent positive confirmation, default to neutral (safe).

See `.claude/rules/external-contribution-safety.md` for the full two-state identity model.

## MCP Servers

Any MCP server handling sensitive advocacy data MUST be self-hosted. MCP extends agent capabilities but also extends the attack surface — audit each server's data access, network calls, and retention policy before enabling.
