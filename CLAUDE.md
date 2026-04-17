# Structured Coding with AI

Ready-to-use AI coding instruction files for 12 tools, tailored for animal advocacy software. Copy a tool directory into any project root and the AI assistant immediately understands advocacy-domain constraints, security threat models, testing standards, and process workflows. Part of the Open Paws developer pipeline.

## Organizational Context

**Role in flywheel:** This repo is the canonical source for AI coding methodology across all Open Paws projects. It feeds two downstream consumers: `graze-cli` bundles selected guides into its binary, and `desloppify` generates agent skill files from the same content. It is also curriculum content for the bootcamp — developers learn these 7 concerns and 6 process skills through the training pipeline.

**Layer:** 1 — Strengthen. Lever: Strengthen.

**External contribution safety (2026-04-01):** All 12 tool directories now include `external-contribution-safety.md` (or equivalent for the tool's format). This file teaches the two-state identity model: advocacy mode for Open Paws repos, neutral mode (org identity suppressed, commit hygiene enforced) for external repos. The `agents-md/AGENTS.md` is the vendor-neutral version of the same. This was implemented in PR #13.

**Clean-room agent architecture rollout (2026-04-09):** The clean-room reuse pattern (closed decision 2026-04-01) is being rolled out across the ecosystem using instruction files from this repo. Status: PCC#13 merged, platform#42 merged, docs#7 merged. Tools-Platform#1 repo verification is still pending — do not mark the rollout complete until that PR is verified.

**Unicode integrity (CI):** A CI action checks all instruction files for hidden Unicode characters (Rules File Backdoor attack). The `scripts/check-unicode-integrity.py` script is the underlying tool.

**Strategy references:**
- `open-paws-strategy/ecosystem/repos.md` — structured-coding-with-ai entry with full breakdown
- `open-paws-strategy/closed-decisions.md` — 2026-04-01 external contribution safety decision
- `open-paws-strategy/programs/developer-training-pipeline/guild/operations.md` — bootcamp curriculum context

## Quick Start

No build step. Pick a tool directory, copy its files into your project:

```bash
# Example: Claude Code
cp claude-code/CLAUDE.md your-project/
cp claude-code/hooks-template.md your-project/
cp -r claude-code/.claude your-project/
```

See README.md for copy commands for all 12 tools.

## Architecture

```
claude-code/       CLAUDE.md + hooks-template.md + .claude/ (rules/ + skills/)
cursor/            .cursorrules + .cursor/rules/ (.mdc files)
github-copilot/    .github/ (copilot-instructions.md + instructions/ + prompts/ + skills/ + chat-modes/)
windsurf/          .windsurf/rules/ (trigger-type rules, 6K/12K char limits)
kilo-code/         .kilocode/ (rules/ mode files + Memory Bank + skills/)
cline/             .clinerules/ (Plan/Act paradigm — all rules as flat files)
roo-code/          .roomodes + .roo/rules/ (JSON modes + mode rules)
augment-code/      .augment/rules/ (concern rules + process skills)
aider/             CONVENTIONS.md (all-in-one)
gemini-cli/        GEMINI.md (all-in-one)
jetbrains-junie/   README.md (references .junie/guidelines.md pattern)
agents-md/         AGENTS.md (vendor-neutral, 20+ tools)
scripts/           check-unicode-integrity.py (instruction file integrity checker)
```

137 files total across 12 tool directories.

## Key Files

| File | Purpose |
|------|---------|
| `README.md` | Full tool comparison, copy commands, content coverage |
| `claude-code/CLAUDE.md` | Claude Code root instruction file |
| `claude-code/hooks-template.md` | Pre-commit/post-edit/pre-push hook setup guide |
| `claude-code/.claude/rules/external-contribution-safety.md` | Two-state identity model for external repos |
| `agents-md/AGENTS.md` | Universal vendor-neutral fallback for any unsupported tool |
| `scripts/check-unicode-integrity.py` | Detects hidden Unicode in instruction files (Rules File Backdoor defense) |

## Content Coverage

All 12 tools cover the same 7 concerns and 6 process skills:

**Concerns:** Testing, Security, Privacy, Cost optimization, Advocacy domain, Accessibility, Emotional safety

**Skills:** git-workflow, testing-strategy, requirements-interview, plan-first-development, code-review, security-audit

Each tool also includes: external-contribution-safety (two-state identity model for external repos).

## Development

- **No dependencies** — pure markdown/JSON instruction files
- **Adding a new tool:** Create `tool-name/` directory, implement the 7 concerns + 6 skills in the tool's native format, add external-contribution-safety content
- **Editing content:** Each tool was independently authored for its format — changes to one do not auto-propagate to others
- **Integrity check:** Run `python scripts/check-unicode-integrity.py` before committing any instruction file edits
- **CI:** Unicode integrity check runs on all PRs via GitHub Action

## Development Standards

### 10-Point Review Checklist (ranked by AI violation frequency)

Apply to every PR:

1. **DRY** — AI clones code at 4x the human rate. Search before writing anything new
2. **Deep modules** — Reject shallow wrappers and pass-through methods. Interface must be simpler than implementation (Ousterhout)
3. **Single responsibility** — Each function does one thing at one level of abstraction
4. **Error handling** — Never catch-all. AI suppresses errors and removes safety checks. Every catch block must handle specifically
5. **Information hiding** — Don't expose internal state. Mask API keys (last 4 chars only)
6. **Ubiquitous language** — Use movement terminology consistently. Never let AI invent synonyms for domain terms
7. **Design for change** — Abstraction layers and loose coupling. Tools must outlast individual campaigns
8. **Legacy velocity** — AI code churns 2x faster. Use characterization tests before modifying existing code
9. **Over-patterning** — Simplest structure that works. Three similar lines of code is better than a premature abstraction
10. **Test quality** — Every test must fail when the covered behavior breaks. Mutation score over coverage percentage

### Quality Gates

**Desloppify** — Target score: ≥ 85 (all other repos).

```bash
pip install "git+https://github.com/Open-Paws/desloppify.git#egg=desloppify[full]"
desloppify scan --path .
desloppify next
```

**Speciesist language** — Run `semgrep --config semgrep-no-animal-violence.yaml` on all `.md` edits.

**Instruction file integrity** — Run `python scripts/check-unicode-integrity.py` before pushing. CI also runs this automatically.

**Two-failure rule** — After two failed fixes on the same problem, stop and restart with a better approach.

### Plan-First Development

Read existing files → identify what changes → write specification → break into subtasks → implement and verify each → commit per subtask

### Structured Coding Reference

For tool-specific AI coding instructions, copy the corresponding directory from this repo into your project root. This repo IS the reference.

### Seven Concerns — repo-specific implications

All 7 always apply. Critical for this repo:

1. **Testing** — Content changes must not break the downstream consumers (graze-cli bundling, desloppify skill generation). Verify content renders correctly in the target tool's format
2. **Security** — Instruction file integrity is a first-class concern. Hidden Unicode in instruction files is the Rules File Backdoor attack. Every PR runs the Unicode check
3. **Privacy** — No activist data or operational details in example code or sample prompts
4. **Cost** — Instruction files are loaded into every AI session that uses them. Keep them lean — every token counts at scale across the bootcamp
5. **Advocacy domain** — This repo IS the canonical source for advocacy domain language. Never introduce synonyms for established terms
6. **Accessibility** — Instruction files must work in editors with no syntax highlighting, screen readers, and plain-text terminals
7. **Emotional safety** — Sample prompts and example scenarios must not include graphic investigation content

### Advocacy Domain Language

Use these terms consistently. Never introduce synonyms:
- **Campaign** — organized advocacy effort (not "project" or "initiative")
- **Investigation** — covert documentation (not "research" or "audit")
- **Coalition** — multi-org alliance
- **Sanctuary** — permanent animal care facility (not "shelter" or "foster")
- **Farmed animal** — not the industry commodity term
- **Factory farm** — not "farm" or "facility"
- **Ag-gag** — laws criminalizing undercover agricultural investigation
- **Companion animal** — not "pet"
- **Direct action** — physical intervention with specific legal status