# Animal Advocacy Platform

Software for animal liberation and advocacy. High-risk domain: investigation data is subpoena-target evidence, activists face legal prosecution, system compromise endangers lives. See `advocacy-domain.md` in this directory for ubiquitous language — NEVER introduce synonyms for established domain terms.

## Plan Mode First — ALWAYS

Use Plan Mode before Act Mode on every task. Read existing code, understand the structure, identify what already exists. AI agents duplicate code at 4x the normal rate because they skip this step. Plan Mode is read-only exploration — no file changes, no commands. Build your attack plan, then switch to Act Mode to execute it.

## Workflow

- Read existing code before writing anything — search for existing functions before creating new ones
- Spec-first: write requirements before implementation
- Test-first: write failing tests before writing code
- Two-failure rule: after two failed fix attempts, stop and re-approach with a better prompt
- Break work into small subtasks — implement, test, and verify one at a time

## Constraints

- NEVER log, store, or transmit activist personally identifiable information
- NEVER send data to external APIs without explicit project-owner approval
- ALWAYS use zero-retention configurations for any third-party service
- ALWAYS apply progressive disclosure for traumatic content (investigation footage, slaughter documentation)
- Abstract all vendor dependencies behind project-owned interfaces — vendor lock-in is a movement risk
- Assume adversarial legal discovery: investigation data is court-subpoena material
- Encrypted local storage; no telemetry to third parties

## Review Checklist — Top 10 AI-Violated Principles

Before finishing any task, verify output against these failure modes:

1. **DRY** — search the codebase before writing anything new; AI clones at 4x normal rate
2. **Deep modules** — reject shallow wrappers and pass-through methods (Ousterhout red flags)
3. **Single responsibility** — one thing per function at one abstraction level; split immediately
4. **Error handling** — never catch-all or suppress errors; verify every error path
5. **Information hiding** — if the interface is as complex as the implementation, the abstraction is shallow
6. **Ubiquitous language** — use movement terminology (campaign, investigation, coalition, sanctuary)
7. **Design for change** — abstraction layers and loose coupling over "works now"
8. **Legacy velocity** — AI code churns 2x faster; write for readability, apply characterization tests
9. **Over-patterning** — simplest structure that works; reject unnecessary Strategy/Factory/Observer
10. **Test quality** — every test must fail when behavior breaks; mutation testing over coverage

For investigation or evidence code: security review for data leakage, PII exposure, and ag-gag legal risk.

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

## Scoped Rules

See other files in this `.clinerules/` directory for domain-specific guidance on: testing, security, privacy, cost optimization, advocacy domain, accessibility, emotional safety, git workflow, testing strategy, requirements interview, plan-first development, code review, and security audit.
