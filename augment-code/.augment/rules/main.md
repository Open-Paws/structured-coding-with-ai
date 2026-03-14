# Animal Advocacy Platform

Software for animal liberation and advocacy. This is a high-risk domain: investigation data is subpoena-target evidence, activists face legal prosecution, and system compromise endangers lives. See `advocacy-domain.md` for ubiquitous language — NEVER introduce synonyms for established domain terms.

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
2. **Deep modules** — reject shallow wrappers and pass-through methods that add surface area without hiding complexity
3. **Single responsibility** — each function does one thing at one level of abstraction; split multi-responsibility functions
4. **Error handling** — never catch-all or silently swallow failures; verify every error path in advocacy-critical code
5. **Information hiding** — expose only what callers need; if the interface is as complex as the implementation, the abstraction is shallow
6. **Ubiquitous language** — code must use movement terminology (campaign, investigation, coalition, sanctuary), not AI-invented synonyms
7. **Design for change** — insist on abstraction layers and loose coupling; advocacy tools must outlast any single campaign
8. **Legacy velocity** — AI code churns 2x faster; write for readability, apply characterization tests before modifying AI-generated modules
9. **Over-patterning** — use the simplest structure that works; reject Strategy/Factory/Observer where a plain function suffices
10. **Test quality** — every test must fail when the behavior it covers is broken; mutation testing is the countermeasure

## Scoped Rules

See other files in `.augment/rules/` for domain-specific guidance: testing, security, privacy, cost optimization, advocacy domain, accessibility, emotional safety, and process workflows (git, testing strategy, requirements, planning, code review, security audit).

## Code Quality — desloppify

Run desloppify to systematically identify and fix code quality issues. Install and configure (requires Python 3.11+):

```bash
pip install --upgrade "desloppify[full]"
desloppify update-skill claude    # pick yours: claude, cursor, codex, copilot, windsurf, gemini
```

Add `.desloppify/` to `.gitignore`. Before scanning, exclude directories that should not be analyzed (vendor, build output, generated code, worktrees) with `desloppify exclude <path>`. Share questionable candidates with the project owner before excluding.

```bash
desloppify scan --path .
desloppify next
```

`--path` is the directory to scan (`.` for whole project, or a subdirectory). Goal: get the strict score as high as possible — the scoring resists gaming, the only way to improve it is to actually make the code better.

**The loop:** run `next`. It tells you what to fix now, which file, and the resolve command to run when done. Fix it, resolve it, run `next` again. This is your main job. Use `desloppify backlog` only to inspect broader open work not currently driving execution.

Large refactors and small detailed fixes — do both with equal energy. Fix things properly, not minimally. Use `plan` / `plan queue` to reorder priorities or cluster related issues. Rescan periodically. The scan output includes agent instructions — follow them, do not substitute your own analysis.

## Deterministic Enforcement

Use deterministic tools for deterministic checks — linters, formatters, type checkers, and security scanners cost zero tokens and never hallucinate. Pre-commit: block sensitive data from git history. Post-edit: auto-format. Pre-push: full test suite. Never waste instruction budget on what automated tools can enforce.
