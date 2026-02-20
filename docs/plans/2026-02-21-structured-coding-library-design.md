# C4C Structured Coding Library — Design Document

**Date:** 2026-02-21
**Purpose:** A library of ready-to-use instruction file sets for 12 AI coding tools, tailored for animal advocacy students at Code for Compassion Campus.

---

## Design Decisions

1. **Approach: Independent per-tool authoring.** Each tool gets independently authored content maximally optimized for its native features. No shared canonical source — content is written fresh for each tool's format and activation mechanisms.

2. **Stack-agnostic.** No specific build commands, linting tools, or language-level code conventions. All content is at the principle/methodology level. Students fill in their own tech stack.

3. **Standalone.** Each tool directory is 100% self-contained. Students don't need the knowledge base documents (AI_CODING.md, TESTING.md, etc.). All relevant principles are distilled into the instruction files.

4. **Under-60-line main files.** Every tool's primary instruction file stays under 60 lines, respecting the empirically validated instruction budget (~150-200 instructions, ~50 consumed by system prompts, leaving ~100-150 for user instructions).

5. **6 process skills.** Skills are workflow/methodology guidance, not domain-specific micro-tools: git-workflow, testing-strategy, requirements-interview, plan-first-development, code-review, security-audit.

6. **All 12 tools covered.** Claude Code, Cursor, GitHub Copilot, Windsurf, Kilo Code, Cline, Roo Code, Aider, Gemini CLI, JetBrains/Junie, Augment Code, plus universal AGENTS.md.

---

## Content Architecture

### 7 Scoped Concerns (present in every tool)

| Concern | Focus | Advocacy-Specific Angle |
|---------|-------|------------------------|
| **Testing** | Assertion quality, property-based testing, mutation testing, spec-first | Adversarial input testing, emotional content classification accuracy, offline behavior verification |
| **Security** | Zero-retention, input validation, supply chain, encrypted storage | Ag-gag legal exposure, state surveillance countermeasures, adversarial legal discovery, plausible deniability |
| **Privacy** | GDPR/CCPA, data minimization, consent, anonymization | Activist identity protection, coalition data sharing across risk profiles, whistleblower protection |
| **Cost optimization** | Model routing, token budgets, caching, compute allocation | Nonprofit budgets, self-hosted inference for critical paths, vendor lock-in as movement risk |
| **Advocacy domain** | DDD ubiquitous language, bounded contexts, entity definitions | Movement terminology, campaign lifecycle, investigation workflow, coalition coordination |
| **Accessibility** | i18n, low-bandwidth, offline-first, low-literacy | Hostile infrastructure, mesh networking, device seizure risk, multi-language activist networks |
| **Emotional safety** | Trauma-informed design, content warnings, configurable detail | Investigation footage handling, witness testimony, burnout prevention, secondary trauma |

### 6 Process Skills (adapted to each tool's format)

| Skill | Purpose | Invocation Trigger |
|-------|---------|-------------------|
| **git-workflow** | Commits, branches, PRs — atomic commits for AI work, ephemeral branches, squash-merge, PR curation | About to commit, branch, or create PR |
| **testing-strategy** | Spec-first generation, assertion quality, mutation testing, property-based, "test your tests" | Writing or generating tests |
| **requirements-interview** | Structured stakeholder questions — threat modeling, coalition needs, user safety, budget constraints | Starting new feature, needs clarification |
| **plan-first-development** | Spec → design → tasks workflow, read before write, decompose, verify each step | Starting significant changes |
| **code-review** | AI code review checklist — Ousterhout red flags, advocacy concerns (data leaks, surveillance, emotional safety) | Reviewing or preparing code for review |
| **security-audit** | Advocacy threat model — ag-gag check, zero-retention, supply chain, encrypted storage, plausible deniability | Touching security-sensitive code |

---

## Per-Tool Format Specifications

### 1. Claude Code
**Format:** CLAUDE.md + .claude/rules/ + .claude/skills/ + hooks config
**Activation:** Ancestor walking + on-demand descendant loading
**Scoped rules:** Markdown with optional YAML `paths:` frontmatter
**Skills:** YAML frontmatter (name, description) + Markdown body
**Hooks:** Shell commands executing before/after agent actions (pre-commit security scan, post-edit format, etc.)
```
claude-code/
├── CLAUDE.md                    (~60 lines)
├── .claude/
│   ├── rules/                   (7 scoped concern files)
│   │   ├── testing.md
│   │   ├── security.md
│   │   ├── privacy.md
│   │   ├── cost-optimization.md
│   │   ├── advocacy-domain.md
│   │   ├── accessibility.md
│   │   └── emotional-safety.md
│   └── skills/                  (6 process skill packages)
│       ├── git-workflow/SKILL.md
│       ├── testing-strategy/SKILL.md
│       ├── requirements-interview/SKILL.md
│       ├── plan-first-development/SKILL.md
│       ├── code-review/SKILL.md
│       └── security-audit/SKILL.md
└── hooks-template.md            (stack-agnostic hooks configuration guide)
```
Note: hooks-template.md is documentation, not an executable config. It describes which hook slots to configure (pre-commit, post-edit, pre-push) with placeholder descriptions. Students fill in their own commands. Claude Code's hook system is strictly superior to writing "always format" or "always lint" in instruction files — use deterministic tools for deterministic checks.

### 2. Cursor
**Format:** .cursorrules + .cursor/rules/*.mdc
**Activation:** 4 modes — Always Apply, Auto Attached (glob), Agent Requested, Manual
**Scoped rules:** MDC format (YAML frontmatter with description, globs, activation mode + Markdown body)
```
cursor/
├── .cursorrules                 (~60 lines, always loaded)
└── .cursor/
    └── rules/                   (7 concerns + 6 skills = 13 .mdc files)
        ├── testing.mdc          (alwaysApply)
        ├── security.mdc         (alwaysApply)
        ├── privacy.mdc          (agentRequested)
        ├── cost-optimization.mdc (agentRequested)
        ├── advocacy-domain.mdc  (alwaysApply)
        ├── accessibility.mdc    (agentRequested)
        ├── emotional-safety.mdc (agentRequested)
        ├── git-workflow.mdc     (agentRequested)
        ├── testing-strategy.mdc (autoAttached, globs: test/spec files)
        ├── requirements-interview.mdc (manual)
        ├── plan-first.mdc       (agentRequested)
        ├── code-review.mdc      (manual)
        └── security-audit.mdc   (manual)
```

### 3. GitHub Copilot
**Format:** .github/copilot-instructions.md + .github/instructions/ + .github/prompts/ + .github/skills/ + custom chat modes
**Activation:** Repository-wide + path-specific with applyTo + reusable prompt files + custom chat modes
**Note:** Copilot supports the richest instruction hierarchy of any tool — 5 elements total.
```
github-copilot/
└── .github/
    ├── copilot-instructions.md  (~60 lines, repo-wide)
    ├── instructions/            (7 concern files with applyTo directives)
    │   ├── testing.md
    │   ├── security.md
    │   ├── privacy.md
    │   ├── cost-optimization.md
    │   ├── advocacy-domain.md
    │   ├── accessibility.md
    │   └── emotional-safety.md
    ├── prompts/                 (6 reusable prompt files for process skills)
    │   ├── git-workflow.prompt.md
    │   ├── testing-strategy.prompt.md
    │   ├── requirements-interview.prompt.md
    │   ├── plan-first.prompt.md
    │   ├── code-review.prompt.md
    │   └── security-audit.prompt.md
    ├── chat-modes/              (2 custom chat mode definitions)
    │   ├── advocacy-reviewer.yml
    │   └── requirements-interviewer.yml
    └── skills/                  (6 process skill packages)
        ├── git-workflow/SKILL.md
        ├── testing-strategy/SKILL.md
        ├── requirements-interview/SKILL.md
        ├── plan-first-development/SKILL.md
        ├── code-review/SKILL.md
        └── security-audit/SKILL.md
```
Prompt files are reusable, user-invocable workflows. Custom chat modes define persistent agent personas (advocacy-reviewer: code review focused on advocacy concerns; requirements-interviewer: structured stakeholder interview).

### 4. Windsurf
**Format:** .windsurf/rules/*.md
**Activation:** 4 modes — Manual, Always On, Model Decision, Glob
**HARD CONSTRAINT:** 6,000 chars per file, 12,000 chars combined
```
windsurf/
└── .windsurf/
    └── rules/                   (7 concerns + 6 skills = 13 files, ruthlessly concise)
        ├── main.md              (Always On, ~2000 chars)
        ├── testing.md           (Always On)
        ├── security.md          (Always On)
        ├── privacy.md           (Model Decision)
        ├── cost-optimization.md (Model Decision)
        ├── advocacy-domain.md   (Always On)
        ├── accessibility.md     (Model Decision)
        ├── emotional-safety.md  (Model Decision)
        ├── git-workflow.md      (Model Decision)
        ├── testing-strategy.md  (Glob: test files)
        ├── requirements.md      (Manual)
        ├── plan-first.md        (Model Decision)
        ├── code-review.md       (Manual)
        └── security-audit.md    (Manual)
```
**12K ceiling scope:** AGENTIC_TOOLS.md says "12,000-character combined ceiling" without qualifying which files count. Conservative interpretation: budget as if ALL currently-loaded files count (Always On + any triggered Model Decision/Glob files). This means Always On files alone should stay well under 12K to leave room for contextually loaded files. Budget: 4 Always On files at ~2,000 chars each = ~8K, leaving 4K headroom for Model Decision files that load alongside them.

**Privacy concern:** Windsurf generates persistent "memories" about your codebase that survive across sessions. For advocacy projects handling sensitive data (investigation footage, witness identities), review and clear memories regularly. Do not rely on Windsurf for projects involving sensitive investigation or witness data without understanding what it persists.

### 5. Kilo Code
**Format:** .kilocode/rules/ with memory-bank/ + mode-specific rules + skills/
**Activation:** Mode-specific + progressive disclosure via Memory Bank
**Modes:** Ask, Architect, Code, Debug, Orchestrator
```
kilo-code/
└── .kilocode/
    ├── rules/
    │   ├── memory-bank/
    │   │   ├── brief.md         (Project identity + advocacy domain)
    │   │   ├── context.md       (Architecture + threat model)
    │   │   └── history.md       (Decision log template)
    │   ├── ask-mode.md          (Rules for Ask mode)
    │   ├── architect-mode.md    (Rules for Architect mode)
    │   ├── code-mode.md         (Rules for Code mode)
    │   ├── debug-mode.md        (Rules for Debug mode)
    │   ├── orchestrator-mode.md (Rules for Orchestrator mode)
    │   ├── testing.md
    │   ├── security.md
    │   ├── privacy.md
    │   ├── cost-optimization.md
    │   ├── advocacy-domain.md
    │   ├── accessibility.md
    │   └── emotional-safety.md
    └── skills/                  (6 process skill packages)
        ├── git-workflow/SKILL.md
        ├── testing-strategy/SKILL.md
        ├── requirements-interview/SKILL.md
        ├── plan-first-development/SKILL.md
        ├── code-review/SKILL.md
        └── security-audit/SKILL.md
```

### 6. Cline
**Format:** .clinerules (root) + .clinerules/ directory
**Activation:** Global → workspace override
```
cline/
├── .clinerules                  (~60 lines, global rules)
└── .clinerules/                 (7 concerns + 6 skills = 13 files)
    ├── testing.md
    ├── security.md
    ├── privacy.md
    ├── cost-optimization.md
    ├── advocacy-domain.md
    ├── accessibility.md
    ├── emotional-safety.md
    ├── git-workflow.md
    ├── testing-strategy.md
    ├── requirements-interview.md
    ├── plan-first.md
    ├── code-review.md
    └── security-audit.md
```

### 7. Roo Code
**Format:** .roomodes (JSON) + .roo/rules/ with mode-specific rules
**Activation:** Custom mode definitions + mode-specific rule files
```
roo-code/
├── .roomodes                    (JSON: custom mode definitions)
└── .roo/
    └── rules/
        ├── rules-architect.md   (Architect mode rules)
        ├── rules-code.md        (Code mode rules)
        ├── rules-debug.md       (Debug mode rules)
        ├── rules-review.md      (Custom Review mode rules)
        ├── rules-interview.md   (Custom Interview mode rules)
        ├── testing.md
        ├── security.md
        ├── privacy.md
        ├── cost-optimization.md
        ├── advocacy-domain.md
        ├── accessibility.md
        ├── emotional-safety.md
        ├── git-workflow.md
        ├── testing-strategy.md
        ├── plan-first.md
        ├── code-review.md
        └── security-audit.md
```
.roomodes defines custom modes with:
- Specific model assignments (e.g., o3 for architect, Sonnet for code)
- Tool restrictions per mode
- Custom modes: Review, Interview

### 8. Aider
**Format:** CONVENTIONS.md (single file, read-only context)
```
aider/
└── CONVENTIONS.md               (Self-contained, all content as sections)
```
All 7 concerns + 6 skills embedded as clearly-headed sections in one file. Most constrained format.

### 9. Gemini CLI
**Format:** GEMINI.md (single root-level file)
```
gemini-cli/
└── GEMINI.md                    (Self-contained, all content as sections)
```
Similar to Aider — single file, skills as sections.

### 10. JetBrains/Junie
**Format:** .junie/guidelines.md (always-on)
```
jetbrains-junie/
└── .junie/
    └── guidelines.md            (Self-contained, all content as sections)
```
Single file, always loaded. Skills as sections.

### 11. Augment Code
**Format:** .augment/rules/*.md (directory-based)
```
augment-code/
└── .augment/
    └── rules/                   (7 concerns + 6 skills = 13 files + main)
        ├── main.md
        ├── testing.md
        ├── security.md
        ├── privacy.md
        ├── cost-optimization.md
        ├── advocacy-domain.md
        ├── accessibility.md
        ├── emotional-safety.md
        ├── git-workflow.md
        ├── testing-strategy.md
        ├── requirements-interview.md
        ├── plan-first.md
        ├── code-review.md
        └── security-audit.md
```

### 12. AGENTS.md (Universal)
**Format:** AGENTS.md at root + optional nested AGENTS.md
**Activation:** Nearest-file-wins hierarchy
```
agents-md/
└── AGENTS.md                    (Comprehensive, vendor-neutral)
```
Supported by 20+ tools. The "works everywhere" fallback.

---

## Animal Advocacy Domain Content (embedded in every tool)

### Threat Model (baked into security + privacy rules)
- **Ag-gag legal exposure:** Investigation footage is discoverable evidence. Zero-retention APIs, encrypted local storage with plausible deniability
- **Three adversaries:** State surveillance, industry infiltration, AI model bias
- **Adversarial legal discovery:** Not just hackers — legal proceedings can compel data disclosure
- **Hostile infrastructure:** Unreliable internet, device seizure risk, mesh networking

### Operational Concerns (baked into cost + accessibility + emotional safety rules)
- Nonprofit budgets: cheap models, resource-efficient code, vendor lock-in as movement risk
- Multi-language users: i18n from day one, low-literacy patterns
- Traumatic content: progressive disclosure, configurable detail levels, secondary trauma mitigation
- Coalition data sharing: organizations with different risk profiles sharing data safely

### Domain Language (baked into advocacy-domain rules)
- Campaign, investigation, coalition, witness testimony, sanctuary, rescue
- Ubiquitous language defined explicitly so AI uses movement terminology, not its own
- Bounded contexts: investigation operations vs. public campaigns vs. coalition coordination

---

## Success Criteria

1. Student copies one tool directory → gets complete working setup
2. Every main instruction file ≤ 60 lines
3. Progressive disclosure via scoped rules/skills
4. Animal advocacy concerns are structural, not afterthoughts
5. Each tool's native format is used correctly (activation modes, frontmatter syntax, character limits)
6. Process skills guide methodology, not implementation specifics
7. Stack-agnostic — no language-specific commands or conventions
8. 100% self-contained — no external dependencies on knowledge base docs

---

## File Count Summary

| Tool | Main | Concern files | Skill files | Mode files | Other | Total |
|------|------|--------------|-------------|------------|-------|-------|
| Claude Code | 1 | 7 | 6 | — | 1 (hooks-template) | 15 |
| Cursor | 1 | 7 | 6 | — | — | 14 |
| GitHub Copilot | 1 | 7 | 6 | — | 8 (6 prompts + 2 chat modes) | 22 |
| Windsurf | — | 7 | 6 | — | 1 (main) | 14 |
| Kilo Code | — | 7 | 6 | 5 | 3 (memory bank) | 21 |
| Cline | 1 | 7 | 6 | — | — | 14 |
| Roo Code | — | 7 | 6 | 5 | 1 (.roomodes) | 19 |
| Aider | 1 | — | — | — | — | 1 |
| Gemini CLI | 1 | — | — | — | — | 1 |
| JetBrains/Junie | 1 | — | — | — | — | 1 |
| Augment Code | — | 7 | 6 | — | 1 (main) | 14 |
| AGENTS.md | 1 | — | — | — | — | 1 |
| **Total** | | | | | | **137 files** |

Plus 1 README.md = **138 files total**.
