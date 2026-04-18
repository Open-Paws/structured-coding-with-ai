# Structured Coding Library for Animal Advocacy

> **Status: 🟢 Production** — actively maintained, all 12 tool directories stable, CI running on every PR.
> Part of the [Open Paws](https://github.com/Open-Paws) developer ecosystem.

Ready-to-use instruction file sets for 12 AI coding tools, designed for anyone building software for animal advocacy and liberation. Each tool directory is self-contained: copy it into your project root and your AI assistant immediately understands advocacy-domain constraints, security threat models, testing standards, and process workflows. No external dependencies, no shared config, no setup beyond copying files.

---

## Why This Exists

Generic AI coding setups treat every codebase the same. Advocacy software is not generic. It operates under a three-adversary threat model (state surveillance, industry infiltration, AI model bias), handles data that is potential evidence under ag-gag statutes, and serves users who face genuine legal risk. The instruction files in this repo encode all of that — so every AI session starts with the right constraints rather than having to re-explain them.

This repo is the **canonical source for AI coding methodology** across all Open Paws projects. It feeds two downstream consumers:
- **[graze-cli](https://github.com/Open-Paws/graze-cli)** — bundles selected instruction files into its binary for advocacy-aware agentic coding
- **[desloppify](https://github.com/Open-Paws/desloppify)** — generates agent skill files from the same content

It also serves as curriculum for the Open Paws developer training bootcamp, where developers learn the 7 concerns and 6 process skills through hands-on project work.

---

## Quick Start

Pick your tool. Copy the files into your project root.

```bash
# Claude Code
cp claude-code/CLAUDE.md your-project/
cp claude-code/hooks-template.md your-project/
cp -r claude-code/.claude your-project/

# Cursor
cp cursor/.cursorrules your-project/
cp -r cursor/.cursor your-project/

# GitHub Copilot
cp -r github-copilot/.github your-project/

# Windsurf
cp -r windsurf/.windsurf your-project/

# Kilo Code
cp -r kilo-code/.kilocode your-project/

# Cline
cp -r cline/.clinerules your-project/

# Roo Code
cp roo-code/.roomodes your-project/
cp -r roo-code/.roo your-project/

# Augment Code
cp -r augment-code/.augment your-project/

# Aider
cp aider/CONVENTIONS.md your-project/

# Gemini CLI
cp gemini-cli/GEMINI.md your-project/

# JetBrains / Junie
cp -r jetbrains-junie/.junie your-project/

# AGENTS.md (universal, works with 20+ tools)
cp agents-md/AGENTS.md your-project/
```

After copying, add your project's own build commands, linting configuration, language conventions, and tech stack details. These files provide principles and methodology — they do not replace project-specific setup.

---

## What's Included

| Tool | Directory | Files | Format Notes |
|------|-----------|------:|--------------|
| Claude Code | `claude-code/` | 17 | CLAUDE.md + 8 scoped rules + 7 skills + hooks template |
| Cursor | `cursor/` | 14 | .cursorrules + 13 .mdc files with 4 activation modes |
| GitHub Copilot | `github-copilot/` | 23 | copilot-instructions.md + 7 instructions + 6 prompts + 2 chat modes + 7 skills |
| Windsurf | `windsurf/` | 14 | 14 .md files in .windsurf/rules/ with 4 trigger types, within 6K/12K char limits |
| Kilo Code | `kilo-code/` | 21 | 5 mode files + 3 Memory Bank files + 7 concerns + 6 skills |
| Cline | `cline/` | 14 | 14 .md files in .clinerules/ with Plan/Act paradigm |
| Roo Code | `roo-code/` | 19 | .roomodes JSON + 5 mode rules + 7 concerns + 6 skills |
| Augment Code | `augment-code/` | 14 | 14 .md files in .augment/rules/ |
| Aider | `aider/` | 1 | Single CONVENTIONS.md with all content as sections |
| Gemini CLI | `gemini-cli/` | 1 | Single GEMINI.md with all content as sections |
| JetBrains / Junie | `jetbrains-junie/` | 1 | Single .junie/guidelines.md, always loaded |
| AGENTS.md | `agents-md/` | 1 | Single vendor-neutral file, supported by 20+ tools |
| **Total** | | **140** | |

---

## Content Coverage

Every tool covers the same material, adapted to its native format. Tools with multi-file support break content into separate files with appropriate activation triggers. Single-file tools condense everything into clearly-headed sections.

### 7 Concerns (present in every tool)

- **Testing** — Assertion quality, spec-first generation, property-based testing, mutation testing, adversarial input testing
- **Security** — Zero-retention APIs, ag-gag legal exposure, supply chain verification, device seizure preparation, three-adversary threat model
- **Privacy** — Activist identity protection, coalition data sharing, whistleblower protection, GDPR/CCPA compliance, data minimization
- **Cost optimization** — Model routing, token budgets, prompt caching, vendor lock-in as movement risk, nonprofit budget allocation
- **Advocacy domain** — Ubiquitous language dictionary, bounded contexts (investigation ops / public campaigns / coalition coordination / legal defense), entity definitions
- **Accessibility** — i18n, offline-first, low-bandwidth, low-literacy design, mesh networking, device seizure resilience
- **Emotional safety** — Progressive disclosure of traumatic content, configurable detail levels, content warnings, secondary trauma mitigation

### 6 Process Skills (workflow guides invoked on demand)

- **git-workflow** — Issue-first GitHub workflow: worktree-per-task, plan-then-review-then-implement loops, desloppify gate, PR monitoring until merged
- **testing-strategy** — Spec-first generation, five anti-patterns to avoid (snapshot trap, mock everything, happy path only, test-after-commit, coverage theater), mutation-guided improvement
- **requirements-interview** — Structured stakeholder questions covering threat model, coalition needs, user safety, budget constraints
- **plan-first-development** — Spec, design, decompose, implement one subtask at a time, generation-then-comprehension pattern
- **code-review** — Layered review pipeline, Ousterhout red flags, AI-specific failure patterns, advocacy-specific data leak checks
- **security-audit** — Advocacy threat model assessment, slopsquatting defense, prompt injection / rules file backdoor detection, MCP server security

### External Contribution Safety

All 12 tool directories include external contribution safety content. This teaches the two-state identity model: **advocacy mode** for Open Paws repos (full domain context, movement terminology, seven concerns active), and **neutral mode** for external open-source repos (org identity suppressed, commit hygiene enforced, no advocacy-specific framing in commits or PRs). This prevents AI agents from inadvertently identifying contributors or leaking organizational context when contributing to third-party projects.

---

## Tool-by-Tool Reference

**Claude Code** — `CLAUDE.md` at project root (under 60 lines), scoped rules in `.claude/rules/` with optional `paths:` frontmatter for file-targeted activation, process skills in `.claude/skills/` with YAML frontmatter (prefixed `advocacy-` to avoid shadowing global skills). Supports hooks for deterministic enforcement of formatting, linting, and security scanning. See `hooks-template.md` for hook configuration.

**Cursor** — `.cursorrules` at project root (always loaded), scoped rules in `.cursor/rules/*.mdc` using MDC format with four activation modes: Always Apply, Auto Attached (glob-triggered), Agent Requested (description-triggered), and Manual (user invokes with @).

**GitHub Copilot** — The richest instruction hierarchy of any tool covered. `.github/copilot-instructions.md` (repo-wide), `.github/instructions/` (path-specific with `applyTo:`), `.github/prompts/` (reusable user-invocable workflows), `.github/chat-modes/` (persistent agent personas for advocacy review and requirements interviewing), `.github/skills/` (process skill packages).

**Windsurf** — `.windsurf/rules/*.md` with four trigger types: Always On, Model Decision, Glob, and Manual. Hard constraint of 6,000 characters per file and 12,000 characters combined. Always On files budgeted to ~8K total to leave headroom for contextually loaded files. Note: Windsurf generates persistent memories about your codebase — review and clear these regularly for sensitive projects.

**Kilo Code** — `.kilocode/rules/` with five mode-specific rule files (Ask, Architect, Code, Debug, Orchestrator), a Memory Bank (`brief.md`, `context.md`, `history.md`) for progressive context disclosure, seven concern files, and seven process skills in `.kilocode/skills/`.

**Cline** — `.clinerules/` directory with 14 Markdown files. Emphasizes Cline's Plan/Act paradigm: explore in Plan Mode before changing anything in Act Mode. All concern and skill content as separate rule files.

**Roo Code** — `.roomodes` JSON defining custom modes (Review and Interview) with tool restrictions and model assignments, plus `.roo/rules/` containing five mode-specific rule files (Architect, Code, Debug, Review, Interview), seven concern files, and seven skill files. Supports Boomerang Task delegation between modes.

**Augment Code** — `.augment/rules/*.md` with a `main.md` core file plus 13 concern and skill files. All files loaded as directory-based rules.

**Aider** — Single `CONVENTIONS.md` file loaded as read-only context. All seven concerns and seven skills condensed into clearly-headed sections. Adapted for Aider's `/architect` and `/code` mode workflow.

**Gemini CLI** — Single `GEMINI.md` file at project root. All content as sections in one self-contained file.

**JetBrains / Junie** — Single `.junie/guidelines.md` file, always loaded. All content as sections.

**AGENTS.md** — Single `AGENTS.md` file following the vendor-neutral standard supported by 20+ tools. The most comprehensive single-file option. Use this as a universal fallback or when your tool is not otherwise listed.

---

## Advocacy-Specific Adaptations

These instruction files differ from generic AI coding setups in several concrete ways:

**Threat model** — Generic setups address common security concerns. These files encode the advocacy-specific three-adversary model: state surveillance using ag-gag statutes and device seizure, industry infiltration through social engineering, and AI model bias encoding speciesist defaults. Every security decision is evaluated against all three adversaries.

**Domain language** — AI models default to generic or industry terminology. These files provide a ubiquitous language dictionary that prevents AI from substituting "livestock" for "farmed animal," "facility" for "slaughterhouse," or "project" for "campaign." This is enforced through explicit term lists and anti-synonym rules.

**Bounded contexts** — Advocacy work spans four distinct contexts (investigation operations, public campaigns, coalition coordination, legal defense) that must not bleed into each other. Investigation data flowing into public campaign tooling is a legal liability. These files make that boundary explicit.

**Identity protection** — Activist identity is a genuine safety concern, not a compliance checkbox. The privacy rules require pseudonymous identifiers, real deletion (not soft delete), and zero-knowledge architecture for whistleblower protection. The external contribution safety content ensures agents do not inadvertently expose organizational affiliation.

**Emotional safety** — Developers working in this domain encounter traumatic content. The emotional safety concern encodes progressive disclosure patterns, configurable detail levels, and secondary trauma mitigation requirements — including the use of abstract test data (no graphic content in CI/CD pipelines).

**Instruction file integrity** — AI instruction files are themselves an attack surface. The Rules File Backdoor attack embeds hidden Unicode characters that alter AI behavior invisibly. This repo runs a CI check (`scripts/check-unicode-integrity.py`) on every PR to detect such tampering.

---

## Open Paws Ecosystem Integration

```
structured-coding-with-ai  (this repo — canonical AI methodology)
        |
        +-- graze-cli          bundles instruction files into CLI binary
        |
        +-- desloppify         generates agent skill files from content
        |
        +-- gary               autonomous agent uses these as base instructions
        |
        +-- platform           copies claude-code/ into project root
        |
        +-- (all Open Paws     copy the relevant tool directory into
             project repos)    their own project roots
```

The `CLAUDE.md` at the root of this repo documents the repo's own role in the ecosystem and its downstream consumers. When editing content here, verify the change does not break graze-cli bundling or desloppify skill generation.

---

## Customization

After copying a tool directory, add your own:

- Build and run commands
- Linting and formatting configuration
- Language-level code conventions (naming, structure, idioms)
- Project-specific entity names and architecture details
- Tech stack details (frameworks, databases, deployment targets)
- Domain-specific entity definitions beyond the advocacy baseline

These files are stack-agnostic starting points. They contain principles and methodology, not language-specific commands.

---

## Adding a New Tool

1. Create a new directory: `tool-name/`
2. Implement all 7 concerns in the tool's native format
3. Implement all 6 process skills in the tool's native format
4. Add external contribution safety content (two-state identity model)
5. Add a `README.md` inside the directory describing the files and copy commands
6. Add a row to the table in this README
7. Run `python scripts/check-unicode-integrity.py` before opening a PR
8. Each tool must be independently authored for its format — do not copy content verbatim from another tool and relabel it

---

## Integrity Checking

All instruction files are checked for hidden Unicode characters (the Rules File Backdoor attack) before every merge. Run the check locally before pushing any edits to instruction files:

```bash
python scripts/check-unicode-integrity.py
```

CI runs this automatically on all PRs via GitHub Action.

---

## Source Material

The content across all 12 tool sets was derived from a knowledge base covering: empirical research on AI-assisted development (code quality metrics, comprehension effects, failure patterns), software design principles (Ousterhout, Feathers, DDD), testing strategy (mutation testing, property-based testing, contract testing), git workflow for AI-generated code, and operational security for the animal advocacy domain. Each tool's content was independently authored to maximize use of its native format and activation mechanisms — this is not a template applied 12 times.

---

## License

[MIT](LICENSE) — copy freely, modify for your context, no attribution required.
