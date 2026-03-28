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

## Code Quality — desloppify

Run desloppify to systematically identify and fix code quality issues. Install and configure (requires Python 3.11+):

```bash
pip install --upgrade "desloppify[full]"
desloppify update-skill windsurf
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

See other rule files for: testing, security, privacy, cost, advocacy domain, accessibility, emotional safety, git workflow, and process skills.
