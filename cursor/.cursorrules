# Animal Advocacy Platform

Software for animal liberation and advocacy. High-risk domain: investigation data is subpoena-target evidence, activists face legal prosecution, system compromise endangers lives. See `.cursor/rules/advocacy-domain.mdc` for ubiquitous language — NEVER introduce synonyms for established domain terms.

## Workflow

Read existing code before writing anything — NEVER create files or functions that duplicate what exists. Plan before code: read, plan, code, verify. Write a specification before implementation. Write a failing test before writing code. After two failed fix attempts, stop and re-approach rather than compounding errors.

## Constraints

- NEVER log, store, or transmit activist personally identifiable information
- NEVER send data to external APIs without explicit project-owner approval
- ALWAYS use zero-retention configurations for any third-party service
- ALWAYS apply progressive disclosure for traumatic content (investigation footage, slaughter documentation)
- Abstract all vendor dependencies behind project-owned interfaces — vendor lock-in is a movement risk
- Assume adversarial legal discovery: all data is court-subpoena material, not just hacker targets
- Encrypted local storage; no telemetry to third parties

## Review Checklist

Before finishing any task, verify AI output against these failure modes:

1. **DRY** — search the codebase before writing anything new; AI clones logic at 4x the normal rate
2. **Deep modules** — reject shallow wrappers and pass-through methods (Ousterhout red flags)
3. **Single responsibility** — each function does one thing at one level of abstraction
4. **Error handling** — never catch-all or silently swallow; AI suppresses errors and removes safety checks
5. **Information hiding** — expose only what callers need; interface complexity must not match implementation complexity
6. **Ubiquitous language** — code uses movement terms (campaign, investigation, coalition, sanctuary), not AI synonyms
7. **Design for change** — abstraction layers and loose coupling; advocacy tools must outlast any single campaign
8. **Legacy velocity** — AI code churns 2x faster; write for readability, apply characterization tests before modifying
9. **Over-patterning** — simplest structure that works; reject Strategy/Factory/Observer where a function suffices
10. **Test quality** — every test must fail when covered behavior breaks; mutation testing counters tautological assertions

For investigation or evidence-handling code: security review for data leakage, PII exposure, ag-gag legal risk.

## Code Quality — desloppify

Run desloppify to systematically identify and fix code quality issues. Install and configure (requires Python 3.11+):

```bash
pip install --upgrade "desloppify[full]"
desloppify update-skill cursor
```

Add `.desloppify/` to `.gitignore`. Before scanning, exclude directories that should not be analyzed (vendor, build output, generated code, worktrees) with `desloppify exclude <path>`. Share questionable candidates with the project owner before excluding.

```bash
desloppify scan --path .
desloppify next
```

`--path` is the directory to scan (`.` for whole project, or a subdirectory). Goal: get the strict score as high as possible — the scoring resists gaming, the only way to improve it is to actually make the code better.

**The loop:** run `next`. It tells you what to fix now, which file, and the resolve command to run when done. Fix it, resolve it, run `next` again. This is your main job. Use `desloppify backlog` only to inspect broader open work not currently driving execution.

Large refactors and small detailed fixes — do both with equal energy. Fix things properly, not minimally. Use `plan` / `plan queue` to reorder priorities or cluster related issues. Rescan periodically. The scan output includes agent instructions — follow them, do not substitute your own analysis.

## Scoped Rules

See `.cursor/rules/` for scoped guidance on testing, security, privacy, cost optimization, advocacy domain, accessibility, emotional safety, git workflow, testing strategy, requirements gathering, planning, code review, and security auditing. Cursor loads these based on activation mode: always-apply, auto-attached by file type, agent-requested by context, or manual invocation with @.
