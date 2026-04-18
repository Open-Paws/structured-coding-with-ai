# AGENTS.md — structured-coding-with-ai

This repo contains ready-to-use AI coding instruction files for 12 tools, tailored for animal advocacy software development. It is the canonical source for AI coding methodology across all Open Paws projects. If you are an AI agent reading this file, you are operating inside a library of instruction files that other AI agents will copy and use — content changes here propagate across the entire Open Paws developer ecosystem.

**Status: 🟢 Production** — all 12 tool directories stable, CI running on every PR.

---

## What This Means for You

This repo is unusual: it is instruction files whose consumers are other AI agents. A change to `claude-code/.claude/rules/security.md` affects every Claude Code session across all Open Paws projects that have copied those files. A change to `agents-md/AGENTS.md` affects 20+ AI tools. Treat content edits with the same care you would treat changes to a shared library used in production.

Two downstream consumers depend on this repo's content directly:
- **graze-cli** — bundles selected instruction files into its binary; content changes require verifying the bundled output still renders correctly
- **desloppify** — generates agent skill files from the same content; structural changes to skill files may break the generation pipeline

---

## Directory Structure

```
structured-coding-with-ai/
├── README.md                          Human-facing overview, copy commands, tool comparison table
├── CLAUDE.md                          Repo-level context for Claude Code (ecosystem role, downstream consumers)
├── AGENTS.md                          This file — context for AI agents working in this repo
├── LICENSE                            MIT
├── scripts/
│   ├── check-unicode-integrity.py     Detects hidden Unicode characters in instruction files (Rules File Backdoor defense)
│   └── tests/                         Tests for the integrity checker
├── .github/                           CI workflows (Unicode integrity check runs on all PRs)
├── .desloppify/                       Desloppify configuration for this repo
├── .pre-commit-config.yaml            Pre-commit hooks (includes speciesist language check)
│
├── claude-code/                       Claude Code — 17 files
│   ├── CLAUDE.md                      Root instruction file (under 60 lines, links to rules/)
│   ├── hooks-template.md              Pre-commit / post-edit / pre-push hook configuration guide
│   └── .claude/
│       ├── rules/                     8 scoped rule files (always-loaded and path-targeted)
│       │   ├── testing.md
│       │   ├── security.md
│       │   ├── privacy.md
│       │   ├── cost-optimization.md
│       │   ├── advocacy-domain.md
│       │   ├── accessibility.md
│       │   ├── emotional-safety.md
│       │   ├── external-contribution-safety.md
│       │   ├── desloppify.md
│       │   └── geo-seo.md
│       └── skills/                    7 process skill directories (invoked on demand)
│           ├── advocacy-code-review/
│           ├── advocacy-testing-strategy/
│           ├── geo-seo-audit/
│           ├── git-workflow/
│           ├── plan-first-development/
│           ├── requirements-interview/
│           └── security-audit/
│
├── cursor/                            Cursor — 14 files (.cursorrules + .cursor/rules/*.mdc)
├── github-copilot/                    GitHub Copilot — 23 files (richest hierarchy of any tool)
├── windsurf/                          Windsurf — 14 files (6K/12K char limits enforced)
├── kilo-code/                         Kilo Code — 21 files (Memory Bank pattern)
├── cline/                             Cline — 14 files (Plan/Act paradigm)
├── roo-code/                          Roo Code — 19 files (.roomodes JSON + mode rules)
├── augment-code/                      Augment Code — 14 files
├── aider/                             Aider — 1 file (CONVENTIONS.md)
├── gemini-cli/                        Gemini CLI — 1 file (GEMINI.md)
├── jetbrains-junie/                   JetBrains / Junie — 1 file (.junie/guidelines.md)
└── agents-md/                         AGENTS.md standard — 1 file (vendor-neutral, 20+ tools)
```

---

## How to Use These Files

### If you are adding a new feature to an instruction file

1. Read the existing file in full before editing. Each tool was independently authored — do not assume the structure matches other tools.
2. Identify which tools need the same change. A content update typically needs to propagate across all 12 tool directories. Check whether the change is concept-level (needs propagating everywhere) or format-level (specific to one tool's mechanism).
3. Run `python scripts/check-unicode-integrity.py` after any edit. This is also enforced by CI.
4. Run `semgrep --config semgrep-no-animal-violence.yaml` on all edited `.md` files before committing.
5. Keep instruction files lean. Every token in these files is loaded into every AI session that uses them. Across the bootcamp cohort, token cost compounds — do not add content without justification.

### If you are adding a new tool directory

1. Create `tool-name/` at repo root.
2. Implement all 7 concerns: testing, security, privacy, cost-optimization, advocacy-domain, accessibility, emotional-safety.
3. Implement all 6 process skills: git-workflow, testing-strategy, requirements-interview, plan-first-development, code-review, security-audit.
4. Add external-contribution-safety content (two-state identity model: advocacy mode vs. neutral mode).
5. Add a `README.md` inside the directory with the copy command and file list.
6. Add a row to the table in `README.md` at the repo root.
7. Update `CLAUDE.md` architecture section if the new directory changes the overall structure.
8. Do not copy content verbatim from another tool directory and relabel it. Each tool must be independently authored for its native format and activation mechanisms.

### If you are reviewing a PR

The most common failure modes in this repo are:
- Introducing synonyms for established domain terms (see advocacy-domain language dictionary in `CLAUDE.md`)
- Adding graphic investigation content to example prompts or test scenarios (violates emotional-safety concern)
- Copying content across tool directories rather than independently authoring for each format
- Edits that break the structural assumptions of downstream consumers (graze-cli bundling, desloppify skill generation)
- Hidden Unicode characters introduced through copy-paste from external sources

---

## Most Important Files by Task

| Task | Key files |
|------|-----------|
| Understand the repo's role in the ecosystem | `CLAUDE.md` |
| Copy instructions for a specific tool | `README.md` (copy commands section) |
| Claude Code implementation reference | `claude-code/CLAUDE.md`, `claude-code/.claude/rules/`, `claude-code/.claude/skills/` |
| Universal / tool-agnostic reference | `agents-md/AGENTS.md` |
| Security rule for advocacy context | `claude-code/.claude/rules/security.md` |
| Domain language enforcement | `claude-code/.claude/rules/advocacy-domain.md` |
| External contribution workflow | `claude-code/.claude/rules/external-contribution-safety.md` |
| Git workflow (issue-first, worktrees, desloppify gate) | `claude-code/.claude/skills/git-workflow/` |
| Instruction file integrity defense | `scripts/check-unicode-integrity.py` |
| Hook configuration | `claude-code/hooks-template.md` |

---

## Content Architecture

All 12 tool sets cover the same conceptual content, implemented in each tool's native format:

**7 Concerns** (always active — loaded into every AI session using these files):
1. Testing
2. Security
3. Privacy
4. Cost optimization
5. Advocacy domain
6. Accessibility
7. Emotional safety

**6 Process Skills** (invoked on demand — triggered by user request or task type):
1. git-workflow
2. testing-strategy
3. requirements-interview
4. plan-first-development
5. code-review
6. security-audit

**1 Cross-cutting rule** (always active):
- external-contribution-safety (two-state identity model)

Tools with multi-file support (Claude Code, Cursor, GitHub Copilot, Windsurf, Kilo Code, Cline, Roo Code, Augment Code) implement concerns and skills as separate files with appropriate activation triggers. Single-file tools (Aider, Gemini CLI, JetBrains/Junie, AGENTS.md) condense all content into clearly-headed sections.

---

## Security Notes for This Repo

**Instruction file integrity** — Hidden Unicode characters in instruction files are the Rules File Backdoor attack vector. An attacker who can inject such characters into these files can invisibly alter the behavior of every AI agent that copies and uses them. The CI Unicode integrity check (`scripts/check-unicode-integrity.py`) is a first-class security control, not optional linting.

**Content provenance** — Do not copy instruction file content from external sources without review. This includes AI-generated content that you have not audited character by character. Always run the integrity check after any content that passed through an external system.

**No activist data in examples** — Example prompts, sample scenarios, and test fixtures must not contain real investigation details, activist identities, coalition information, or operational details. Abstract test data only.

---

## Quality Gates

Before opening a PR:

```bash
# Instruction file integrity
python scripts/check-unicode-integrity.py

# Speciesist language
semgrep --config semgrep-no-animal-violence.yaml .

# Desloppify (target score ≥ 85)
pip install "git+https://github.com/Open-Paws/desloppify.git#egg=desloppify[full]"
desloppify scan --path .
```

---

## Known Issues and TODOs

- The file count in `README.md` shows 140 — the actual count across all tool directories should be verified as new files are added. The canonical count is whatever `find . -name "*.md" -o -name "*.mdc" -o -name "*.json" | grep -v ".github\|scripts\|README\|CLAUDE\|AGENTS\|LICENSE" | wc -l` returns at HEAD.
- Windsurf's persistent memory feature requires manual review for sensitive projects. Consider adding a warning in the Windsurf `README.md` specific to investigation operations.
- The `geo-seo.md` rule file in `claude-code/.claude/rules/` is significantly larger than other rule files (36K vs ~5K). This may warrant splitting or summarizing for token-efficiency at bootcamp scale.
- Tools-Platform#1 repo verification is still pending (as of 2026-04-09 clean-room agent architecture rollout). Do not mark that rollout complete until that PR is verified.
