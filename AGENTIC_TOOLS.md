# The complete guide to agentic coding tools and instruction patterns in 2025

**Every major AI coding tool has converged on the same core mechanism: Markdown files committed to your repo that tell agents how to work in your codebase.** This convergence is striking — from Anthropic's Claude Code to Cursor, Copilot, and a dozen others, the instruction file has become the highest-leverage artifact in modern development. The differences between tools are mostly superficial (file names, frontmatter syntax, activation modes), while the deep patterns — hierarchical scoping, progressive disclosure, and context budgeting — are now universal. This report maps the entire landscape: every tool, every instruction format, and the hard-won best practices that separate effective agent-directed coding from frustrating prompt wrestling.

## The tool landscape: thirteen ways to direct a coding agent

The agentic coding space has exploded into a rich ecosystem. Each tool takes a slightly different approach to autonomy, interface, and instruction discovery, but all share the fundamental loop of **read context → plan → execute → verify**.

**Claude Code** (Anthropic) is a terminal-first CLI that reads entire codebases and autonomously executes multi-step tasks. It supports VS Code, Cursor, and JetBrains extensions, a desktop app, and a web interface at claude.ai/code. Users interact through natural language in the terminal, with special affordances: the `#` key saves instructions to CLAUDE.md, `@` mentions reference files, and "think" keywords ("think hard," "ultrathink") trigger deeper reasoning. Claude Code's distinctive strength is its **subagent architecture** — it can spawn parallel agents that work simultaneously on different parts of a codebase, each with their own context window. Its permission model is conservative by default, requiring approval for system-modifying actions unless running with `--dangerously-skip-permissions` in sandboxed environments.

**Cursor** has evolved from a code editor into an **AI-native IDE** built on VS Code. Cursor 2.0 introduced Composer, a proprietary frontier model trained specifically for agentic interactions, and an agent loop using the ReAct pattern (reasoning + tool actions). It supports up to **8 background agents running in parallel**, a browser tool for testing UI work, and sandboxed terminal execution. Cursor's `.cursor/rules/*.mdc` system is the most sophisticated rule-activation mechanism in the ecosystem, with four distinct modes: Always Apply, Auto Attached (glob-triggered), Agent Requested (AI decides based on description), and Manual (user invokes with `@`).

**Windsurf** (formerly Codeium) differentiates through its **Cascade** engine, which operates in Write, Chat, and Turbo modes. Turbo mode is fully autonomous — it runs terminal commands without confirmation. Windsurf enforces a hard **6,000-character limit per rule file** and a **12,000-character combined ceiling**, making it the most constrained system for instruction content. It also generates persistent "memories" about your codebase that survive across sessions.

**GitHub Copilot** now operates in two distinct agentic modes: an **IDE agent** (VS Code) that proposes multi-file edits, runs tests, and self-corrects in a loop, and a **GitHub.com coding agent** that can be assigned to Issues, creates PRs autonomously in GitHub Actions environments, and runs security analysis before finalizing. Copilot supports the richest instruction hierarchy: repository-wide instructions, path-specific instructions with `applyTo` globs, reusable prompt files, and custom chat modes.

**Kilo Code** (founded by GitLab co-founder Sid Sijbrandij, launched March 2025) takes the most explicitly **multi-agent approach** with five built-in modes — Ask, Architect, Code, Debug, and Orchestrator — each with controlled tool access. Its Memory Bank system (structured markdown files in `.kilocode/rules/memory-bank/`) provides persistent project context across `brief.md`, `context.md`, and `history.md`. The Orchestrator mode coordinates multi-step workflows across other modes, and an experimental Ensemble Mode runs multiple AI models in parallel via separate git worktrees.

**Cline** (formerly Claude Dev, 5M+ developers) pioneered the **Plan/Act paradigm** that many tools have since adopted. Plan Mode is read-only exploration to build an attack plan; Act Mode executes it. Cline uses "agentic search" — rather than indexing the codebase via embeddings, it agentically explores by reading file structures, ASTs, and running regex searches. **Roo Code**, forked from Cline, adds sticky models per mode (assign o3 for architecture, Claude Sonnet for coding), checkpoint systems for reverting changes, and "Boomerang Tasks" for delegation patterns.

**Aider** is the most git-native tool — every change is automatically committed with sensible messages, and it builds a compact "repo map" of the entire codebase for context. Its three chat modes (`/ask`, `/code`, `/architect`) mirror the plan-then-execute pattern. Aider's CONVENTIONS.md approach is the simplest instruction mechanism: a single markdown file loaded as read-only context.

**Devin** (Cognition AI, $73M ARR by June 2025) takes the most autonomous approach, operating in its own **sandboxed cloud environment** with shell, editor, and browser. It interfaces primarily through Slack and a web-based IDE. There are no local instruction files — instructions flow through conversation and "playbooks." **OpenHands** (38,800+ GitHub stars) provides a composable Python SDK for defining agents that run in Docker containers, with an event-stream architecture and hierarchical delegation primitives.

## Every instruction file format, mapped and compared

The instruction file format landscape looks fragmented on the surface but is remarkably uniform underneath. Every format is Markdown. Every format supports some form of hierarchical scoping. The differences are in naming, frontmatter syntax, and activation mechanisms.

| Tool | Primary File | Location | Format | Scoping Mechanism |
|------|-------------|----------|--------|-------------------|
| Claude Code | `CLAUDE.md` | Project root, `~/.claude/`, `.claude/rules/` | Markdown + optional YAML `paths:` | Ancestor walking + on-demand descendant loading |
| Cursor | `.cursor/rules/*.mdc` | `.cursor/rules/` directory | MDC (YAML frontmatter + Markdown) | 4 activation modes with `globs:` |
| GitHub Copilot | `.github/copilot-instructions.md` | `.github/` + `.github/instructions/` | Markdown with `applyTo:` | Path-specific `.instructions.md` files |
| Windsurf | `.windsurf/rules/*.md` | `.windsurf/rules/` + `~/.windsurf/rules/` | Plain Markdown | 4 modes: Manual, Always On, Model Decision, Glob |
| JetBrains/Junie | `.junie/guidelines.md` | `.junie/` directory | Plain Markdown | Always on |
| Kilo Code | Memory Bank + Skills | `.kilocode/rules/memory-bank/` | Markdown + YAML frontmatter | Mode-specific + progressive disclosure |
| Cline | `.clinerules` | Project root or `.clinerules/` directory | Plain Markdown | Global → workspace override |
| Aider | `CONVENTIONS.md` | Project root (configurable) | Plain Markdown | Single file, loaded read-only |
| Gemini CLI | `GEMINI.md` | Project root | Plain Markdown | Simple root-level |
| Augment Code | `.augment/rules/*.md` | `.augment/rules/` directory | Markdown | Directory-based |
| AGENTS.md | `AGENTS.md` | Project root + nested dirs | Plain Markdown | Nearest-file-wins hierarchy |

**AGENTS.md** has emerged as the vendor-neutral standard, co-created by OpenAI, Google, Cursor, Sourcegraph, and Factory, and now stewarded by the Agentic AI Foundation under the Linux Foundation. Over **60,000 open-source projects** on GitHub have adopted it. It's natively supported by OpenAI Codex, Google Jules, GitHub Copilot, Cursor, and 20+ other tools. Claude Code uses CLAUDE.md instead but the two coexist via symlinks or import references.

For teams using multiple tools, the **symlink strategy** provides a single source of truth:

```bash
# Create AGENTS.md as canonical source
ln -s AGENTS.md CLAUDE.md
ln -s AGENTS.md .cursorrules
ln -s AGENTS.md .windsurfrules
```

## How agents discover instructions: the three-tier hierarchy

All tools have converged on a **three-tier hierarchical model** for instruction discovery, varying only in implementation details.

**Tier 1 (Global/User)** contains personal preferences that apply across all projects — your preferred coding style, identity, general workflow preferences. These live in user home directories (`~/.claude/CLAUDE.md`, `~/.windsurf/rules/`, Cursor Settings > Rules for AI) and are **never committed to Git**.

**Tier 2 (Project/Root)** is the core instruction file — tech stack, architecture, build commands, testing conventions, team coding standards. This lives at the project root (`CLAUDE.md`, `AGENTS.md`, `.cursorrules`) and **is committed to Git**, making it the primary mechanism for team alignment.

**Tier 3 (Directory/Scoped)** provides package-specific or domain-specific overrides for monorepos or complex projects. Claude Code loads subdirectory CLAUDE.md files **on demand** when the agent works in those directories (preventing context bloat). Cursor uses glob patterns in frontmatter to auto-attach rules only when matching files are referenced. Claude Code also supports a `.claude/rules/` directory with path-scoped YAML frontmatter:

```yaml
---
paths:
  - "src/api/**/*.ts"
---
# API-specific rules that only load when working on API files
```

**Precedence flows from general to specific**: global rules are overridden by project rules, which are overridden by directory-level rules, which are overridden by inline chat directives. Claude Code wraps all CLAUDE.md content with a system reminder: *"IMPORTANT: this context may or may not be relevant to your tasks. You should not respond to this context unless it is highly relevant."* This means the agent **actively ignores** instructions it deems irrelevant — a critical design choice that punishes bloated instruction files.

## The SKILL.md pattern and progressive disclosure

The **SKILL.md pattern** represents the most sophisticated approach to instruction management and has been adopted across Claude Code, GitHub Copilot, OpenAI Codex, and Kilo Code. A skill is a self-contained directory packaging domain expertise:

```
skill-name/
├── SKILL.md          # Required: YAML frontmatter + instructions
├── scripts/          # Optional: executable automation
├── templates/        # Optional: document/code templates
├── references/       # Optional: reference materials
└── resources/        # Optional: additional files
```

The SKILL.md file itself uses YAML frontmatter for metadata and Markdown for instructions:

```markdown
---
name: api-design
description: RESTful API design patterns using Express and Zod validation
---
# API Design Skill

## When to Use
- Creating new API endpoints
- Refactoring existing route handlers

## Instructions
[Detailed step-by-step guidance for the agent]
```

The key mechanism is **progressive disclosure** — a four-stage loading process that respects context budgets:

1. **Discovery**: The agent sees only the `name` and `description` of all installed skills
2. **Matching**: The agent evaluates its current task against skill descriptions
3. **Loading**: Full SKILL.md instructions load into context only when the agent determines relevance
4. **Execution**: Referenced scripts, templates, and resources load on demand

Skills live in tool-specific directories (`.claude/skills/`, `.github/skills/`, `.kilocode/skills/`) with both global (`~/.claude/skills/`) and project-level locations. They can be invoked explicitly ("use the api-design skill") or implicitly (the agent matches task to description automatically). Anthropic provides official skills for processing PDFs, DOCX, PPTX, and XLSX files.

This progressive disclosure pattern appears everywhere in different forms: Cursor's "Agent Requested" rule type (AI reads description, decides whether to load full content), Kilo Code's Memory Bank (metadata always loaded, details on demand), and Claude Code's descendant CLAUDE.md loading (child directory files loaded only when working in those directories).

## What actually works: empirically validated best practices

The most important finding across all sources is that **the instruction file is a scarce resource with a hard budget**. HumanLayer's research established that frontier LLMs can reliably follow approximately **150–200 instructions**. Claude Code's built-in system prompt already consumes ~50 of these. This leaves room for only ~100–150 user instructions before performance degrades — and critically, **degradation is uniform**. The agent doesn't just forget bottom-of-file rules; it starts following *all* rules slightly worse, randomly skipping conventions and hallucinating plausible-but-wrong patterns.

**Keep root instruction files under 150 lines, ideally under 60.** HumanLayer's own CLAUDE.md is under 60 lines. Anthropic's guidance emphasizes the same: "Find the smallest set of high-signal tokens that maximize the likelihood of your desired outcome." Every line in your instruction file must earn its place — if the agent already does something correctly without being told, delete that instruction.

**Separate rules by concern into individual files.** VirtusLab's research found the strongest signal: "Rules only work when they are small, narrow, and scoped." Never mix unit test conventions and integration test conventions in the same file. Use one file per responsibility: general project context, language-specific patterns, testing conventions, API patterns, security boundaries. Cursor's `.mdc` system and Claude Code's `.claude/rules/` directory both support this natively.

**Use strong language for critical rules.** "NEVER," "ALWAYS," "IMPORTANT," **bold text**, and ALL CAPS measurably improve compliance on non-negotiable constraints. Weak language like "prefer," "try to," or "maybe" effectively delegates the decision to the AI. One practitioner found that running CLAUDE.md through a prompt improver and adding emphasis to critical instructions noticeably improved agent behavior.

**Use deterministic tools for deterministic checks.** The universal anti-pattern is using LLM instructions for code formatting and style enforcement. Linters (ESLint, Biome), formatters (Prettier), and type checkers cost zero tokens and never hallucinate. Claude Code's hook system executes shell commands before/after agent actions — auto-format after edits, lint before commits, block edits on protected branches. This is strictly superior to writing "always format with Prettier" in your instruction file.

**The Plan-First workflow reduces rework dramatically.** The read → plan → code → verify cycle is empirically validated across every tool. Use Plan Mode (Shift+Tab in Claude Code, Plan Mode in Cline) to restrict to read-only exploration before any code changes. Anthropic engineers report "big drops in re-work when steps one and two are never skipped." Spec-driven development — writing `requirements.md → design.md → tasks.md` before coding — extends this further, creating durable artifacts that survive context window limits.

**Arize AI proved rules can be systematically optimized.** Their research used "Prompt Learning" to automatically optimize `.clinerules` files for Cline, improving SWE-bench accuracy by **10–15%**. The optimization loop: run agent → evaluate against ground truth → generate rich feedback → meta-prompt generates improved rules → iterate. This demonstrates that instruction files aren't just documentation — they're tunable parameters.

## The universal instruction file anatomy

Analysis across hundreds of real instruction files reveals a consistent structure that works regardless of tool:

**Project summary** (1–3 sentences) establishes domain vocabulary. Even a simple "This is a Cinema Reservation System" dramatically reduces ambiguity. **Tech stack** prevents framework hallucination — without explicit "Backend: Kotlin + Spring Boot," agents may generate Express.js. **Directory map** grounds the agent in physical code organization. **Commands** must be specific and copy-pasteable: not "run tests" but `pytest -x --tb=short`. **Coding conventions** should focus on non-obvious patterns — naming schemes, forbidden patterns, architectural boundaries. **Workflows** describe the expected process for features, PRs, and testing. **Safety/permissions** explicitly state what the agent can do without asking versus what requires confirmation.

A real-world Claude Code example demonstrating this anatomy:

```markdown
# Build commands
- npm run build: Build the project
- npm run typecheck: Run the typechecker
- npm test -- --run path/to/test: Run a single test

# Code style
- ES modules (import/export), not CommonJS (require)
- Destructure imports when possible
- TypeScript strict mode; NEVER use `any`

# Workflow
- Always typecheck after a series of code changes
- Run single tests during development, not the full suite
- Read existing code before making changes — NEVER create duplicate functions

# Do Not
- Do not edit src/legacy/
- Do not commit directly to main
```

The **progressive disclosure pattern** extends this by keeping the root file lean and pointing to detailed docs:

```
agent_docs/
├── building_the_project.md
├── running_tests.md
├── code_conventions.md
├── service_architecture.md
└── database_schema.md
```

The root CLAUDE.md references these with brief descriptions, instructing the agent to read relevant files before starting specific tasks.

## Anti-patterns that waste your instruction budget

**Never auto-generate instruction files.** Tools like Claude Code's `/init` command prioritize comprehensiveness over restraint, producing bloated files that burn instruction budget on generic guidance the agent already knows. Hand-curate every line.

**Never embed code snippets.** They go stale immediately. Use capability descriptions instead: "authentication logic is in the auth module" rather than pointing to specific file paths. Domain concepts are more durable than file paths, and file paths are more durable than inline code. If you must reference code, use `file:line` pointers to the authoritative source.

**Never stuff contradictory rules into one file.** "Use mocks" (for unit tests) and "avoid mocks" (for integration tests) in the same file guarantees confusion. Separate by concern and use path-scoped activation so each rule set loads only when relevant.

**Watch for context pollution in long sessions.** Agents lose coherence as conversations grow. Practitioners recommend starting fresh sessions for each major feature, manually compacting at ~50% context usage (Claude Code's `/compact` command), and summarizing current state before continuing. Break work into subtasks that complete within less than half the context window.

## Convergent evolution across all tools

Ten patterns have independently emerged across every major tool, representing genuine convergent evolution toward optimal agent instruction:

**Markdown as universal format** — no tool uses JSON, YAML, or any structured schema for the instruction body. LLMs parse Markdown naturally, it's human-readable, and it diffs cleanly in Git. **Hierarchical three-tier scoping** (global → project → directory) appears in every tool. **Path-based conditional loading** started in Cursor's glob system and has been adopted by Claude Code, Windsurf, and Copilot. **Progressive disclosure** (show metadata first, load details on demand) appears in skills, directory-level rules, and agent-requested activation modes. **Rules-as-code** — storing instruction files in Git alongside source code — is the universal distribution mechanism. **Plan-then-execute** workflows are native in Cline, Aider, Claude Code, and Kilo Code. **Deterministic hooks over LLM instructions** for mechanical checks is recommended by every tool's documentation. **Multi-agent delegation** with separate context windows is available in Claude Code, Cursor, Kilo Code, and Cline. **The instruction budget concept** — finite capacity for rules before degradation — is acknowledged by all tool vendors. And **MCP (Model Context Protocol)**, donated to the Linux Foundation in December 2025, has become the standard for extending agent capabilities with external tools.

## Conclusion

The agentic coding landscape in 2025 is less fragmented than it appears. Strip away the branding and every tool is fundamentally the same machine: an LLM in a loop, reading Markdown instructions from your repo, planning changes, executing them, and verifying results. The real differentiators are in **autonomy level** (Devin's full cloud sandbox versus Cline's human-in-the-loop approval), **multi-agent capability** (Claude Code and Kilo Code's parallel subagents versus single-agent tools), and **instruction sophistication** (Cursor's four activation modes versus Aider's single file).

The most actionable insight is that **instruction quality dominates tool choice**. A well-crafted 60-line CLAUDE.md with progressive disclosure, path-scoped rules, deterministic hooks, and a plan-first workflow will dramatically outperform a 500-line auto-generated instruction file in any tool. The instruction budget is real, degradation is uniform, and every line must earn its place. AGENTS.md is emerging as the universal standard for teams using multiple tools, but the format matters far less than the content discipline: be specific, be concise, separate concerns, and let linters handle what linters handle.