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

## Code Quality — desloppify

Run desloppify to systematically identify and fix code quality issues. Install and configure (requires Python 3.11+):

```bash
pip install --upgrade "desloppify[full]"
desloppify update-skill copilot
```

Add `.desloppify/` to `.gitignore`. Before scanning, exclude directories that should not be analyzed (vendor, build output, generated code, worktrees) with `desloppify exclude <path>`. Share questionable candidates with the project owner before excluding.

```bash
desloppify scan --path .
desloppify next
```

`--path` is the directory to scan (`.` for whole project, or a subdirectory). Goal: get the strict score as high as possible — the scoring resists gaming, the only way to improve it is to actually make the code better.

**The loop:** run `next`. It tells you what to fix now, which file, and the resolve command to run when done. Fix it, resolve it, run `next` again. This is your main job. Use `desloppify backlog` only to inspect broader open work not currently driving execution.

Large refactors and small detailed fixes — do both with equal energy. Fix things properly, not minimally. Use `plan` / `plan queue` to reorder priorities or cluster related issues. Rescan periodically. The scan output includes agent instructions — follow them, do not substitute your own analysis.

## Scoped Guidance

See `.github/instructions/` for domain-specific rules: testing, security, privacy, cost optimization, advocacy domain, accessibility, emotional safety. See `.github/prompts/` for invocable workflows. See `.github/skills/` for detailed process guidance.
