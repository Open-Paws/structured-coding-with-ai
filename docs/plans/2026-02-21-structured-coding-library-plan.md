# C4C Structured Coding Library — Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Create 137 instruction files across 12 AI coding tool directories, each self-contained and optimized for animal advocacy development at C4C Campus.

**Architecture:** Independent per-tool authoring. Each tool directory is a standalone package students copy into their project root. Content is stack-agnostic, principle-level, advocacy-focused. No shared canonical source — each tool gets fresh content optimized for its native format and activation mechanisms.

**Design Doc:** `docs/plans/2026-02-21-structured-coding-library-design.md`

---

## Phasing Strategy

- **Phase 1:** Claude Code (most complex, 15 files) — establishes content depth
- **Phase 2:** Multi-file tools in parallel (Cursor, Copilot, Kilo Code, Roo Code, Cline, Augment Code, Windsurf) — 7 tools, 118 files
- **Phase 3:** Single-file tools in parallel (Aider, Gemini CLI, JetBrains/Junie, AGENTS.md) — 4 tools, 4 files
- **Phase 4:** README.md — 1 file

**Parallelization:** All tools within a phase are independent and can be built by separate subagents simultaneously.

---

## Content Reference: What Every File Draws From

These are the principles distilled from the knowledge base. Every file writer should internalize these before writing.

### Advocacy Threat Model (→ security.md, privacy.md)
- Ag-gag legal exposure: investigation footage = discoverable evidence
- Three adversaries: state surveillance, industry infiltration, AI model bias
- Adversarial legal discovery (not just hackers)
- Hostile infrastructure (unreliable internet, device seizure risk)
- Zero-retention APIs, no telemetry to third parties
- Self-hosted inference for critical paths
- Encrypted local storage with plausible deniability
- Input validation against industry sabotage

### Advocacy Operations (→ cost-optimization.md, accessibility.md, emotional-safety.md)
- Nonprofit budgets: cheap models, resource-efficient, vendor lock-in = movement risk
- Multi-language users: i18n day one, low-literacy patterns
- Traumatic content: progressive disclosure, configurable detail, secondary trauma
- Coalition data sharing: orgs with different risk profiles
- Offline-capable, mesh networking, graceful degradation

### Advocacy Domain Language (→ advocacy-domain.md)
- Terms: campaign, investigation, coalition, witness testimony, sanctuary, rescue, liberation, direct action, undercover operation, ag-gag, factory farm, slaughterhouse, companion animal, farmed animal
- Bounded contexts: investigation ops vs public campaigns vs coalition coordination vs legal defense
- Entity types: Activist, Organization, Campaign, Investigation, Witness, Evidence, Coalition, Sanctuary

### Testing Principles (→ testing.md, testing-strategy skill)
- Assertion quality over coverage quantity
- Spec-first test generation preferred
- Property-based testing for invariants
- Mutation testing to verify test quality
- AI-generated tests need human review for tautological assertions
- Test error paths, not just happy paths
- Contract tests at service boundaries — AI hallucinates API contracts; verify with consumer-driven contract tests (especially for coalition cross-org APIs)
- Fast test execution is non-negotiable for AI agent loops — if the suite takes 10 minutes, 15 agent iterations burn 2.5 hours
- Flaky tests poison the AI feedback loop — track and eliminate aggressively
- Quality metrics: mutation score over coverage, test-to-code ratio (healthy: 1:1+), test execution time (track P50/P95), flaky test rate

### Five Testing Anti-Patterns to Name Explicitly (→ testing-strategy skill)
1. **Snapshot trap** — AI generates tests that snapshot current output; tests pass today, break on any change including correct changes; tests verify nothing about correctness
2. **Mock everything** — AI loves mocking because it makes tests pass easily; over-mocked tests verify mock behavior, not real code behavior; mock only at system boundaries
3. **Happy path only** — AI-generated tests overwhelmingly test the success path; explicitly request error path, boundary condition, and adversarial input tests
4. **Test-after-commit** — Writing tests after code is committed defeats the feedback loop; tests must be present during development, not after
5. **Coverage theater** — Chasing coverage numbers with meaningless tests; a line "covered" by a test with no assertions is not tested

### Design Principles — Top 10 AI-Violated (→ main instruction files, code-review skill)
Ranked by frequency and impact in AI-generated code (from SOFTWARE_DESIGN.md):
1. **DRY** — AI duplicates existing code without full codebase awareness (4x more cloning in AI repos)
2. **Deep modules over shallow wrappers** — AI generates thin wrappers, pass-through methods, classes that just delegate
3. **Do one thing per function** — AI produces multi-responsibility functions; check function length and responsibility count first
4. **Error handling** — AI suppresses errors, catches too broadly, removes safety checks; review every try/catch block
5. **Information hiding** — AI leaks implementation details across module boundaries; if the interface is as complex as the implementation, the abstraction is shallow
6. **Ubiquitous language** — AI introduces its own terminology instead of using domain language; define terms in instruction files
7. **Design for change** — AI optimizes for "works now," not "works later"; insist on abstraction layers and loose coupling
8. **Legacy code velocity** — AI code churns 2x faster (GitClear); apply Feathers' characterization tests before modifying AI-generated code
9. **Over-patterning** — AI forces design patterns where simpler solutions suffice; Strategy/Factory/Observer for problems that need a function and an if-statement
10. **Test quality** — AI generates tests that look thorough but verify nothing; mutation testing is the countermeasure

### Workflow Principles (→ main instruction files)
- Plan before code — read → plan → code → verify
- Two-failure rule: after two failed fixes, restart with better prompt
- Instruction budget: ~150-200 instructions max, keep main file under 60 lines

### Process Skills Content (→ all 6 skill files)

**git-workflow:** Atomic commits for AI work. Ephemeral branches for experiments — squash-merge or delete within hours (trunk-based development remains the goal; branches exist as safety nets for throwaway, not long-lived workspaces). Commit after each logical subtask, not after entire task. PR curation is a human skill — split agent output into reviewable chunks (target: under 200 lines changed, ideally under 100; AI adoption inflated PR size by 154%). Stacked PRs for large changes (PR1 → PR2 → PR3, each independently reviewable). AI-Assisted tags on all PRs with AI-generated code. Two human approvals for primarily AI-generated PRs. Track Code Survival Rate — how much AI-generated code remains 48 hours after merge — as a quality signal. Healthy suggestion acceptance rate: 25-35%; higher may indicate over-reliance.

**testing-strategy:** Start with spec/acceptance criteria, generate tests from spec before implementation. Review AI-generated assertions against spec, not code. Five generation patterns: implementation-first (dangerous), spec-first (preferred), edge-case generation, characterization tests (legacy), mutation-guided improvement. Ask: would this test fail if the code were wrong? Five anti-patterns to name and avoid: snapshot trap, mock everything, happy path only, test-after-commit, coverage theater (see Testing Anti-Patterns section above). Contract tests at service boundaries for coalition APIs. Fast test execution is critical for AI agent loops.

**requirements-interview:** Ask one question at a time, multiple choice when possible. Understand: purpose, constraints, success criteria, threat model, coalition partners, user safety needs, budget. Focus on who are the users, what are their risks, what happens if this system is compromised/discovered/seized. For advocacy: who are the adversaries, what legal exposure exists, what's the data retention policy, which coalition partners need access.

**plan-first-development:** Never code before planning. Workflow: brainstorm spec → outline step-by-step plan → decompose into subtasks → execute one subtask at a time → test each before moving on. Start each session fresh. Use plan mode (Shift+Tab in Claude Code, Plan Mode in Cline). Break work into chunks that complete within half the context window. Compact at ~50% context usage. **Comprehension check:** After AI generates code, explain what it does in your own words before committing. AI-assisted developers score 17 percentage points lower on comprehension tests (Anthropic study). Use the generation-then-comprehension pattern: generate code, then immediately ask the AI to explain it, then verify your understanding matches. This preserves learning while leveraging AI speed.

**code-review:** Layered review pipeline — do not spend human review time on what automated tools can check: (1) automated formatting/linting (zero human effort), (2) static analysis and type checking (automated gates), (3) AI-assisted first-pass review (automated but probabilistic), (4) human review focused on architecture, security, business logic, and design quality. Ousterhout red flags checklist: shallow module, information leakage, temporal decomposition, pass-through method, repetition, special-general mixture. AI-specific: check for DRY violations (4x more cloning), multi-responsibility functions, suppressed errors, overly broad catch blocks, hallucinated APIs, over-patterning. **Silent failure pattern:** AI may remove safety checks to make code appear to work, create fake output matching desired formats, or edit tests to pass rather than fixing code — verify all safety checks from original code are preserved. Advocacy-specific: data leak vectors, surveillance surface area, emotional safety of displayed content, coalition boundary violations.

**security-audit:** Check: zero-retention compliance (no telemetry to third parties), encrypted storage implementation, plausible deniability of stored data, **slopsquatting defense** (AI hallucinates package names that attackers register — ~20% of AI-recommended packages don't exist; verify every dependency exists in its registry before installing), input validation against adversarial content, ag-gag exposure vectors, coalition data isolation, self-hosted inference for critical paths, device seizure preparation (remote wipe, encrypted volumes), **instruction file integrity** (inspect rule files for hidden Unicode characters or prompt injection payloads — the "Rules File Backdoor" attack uses invisible characters in .cursorrules/.mdc files to direct AI to produce malicious output; treat instruction files as security-critical artifacts requiring review), **MCP server security** (any MCP server handling sensitive advocacy data must be self-hosted; MCP extends agent capabilities but also extends the attack surface).

---

## Phase 1: Claude Code (15 files)

### Task 1: Claude Code — Directory Structure + Main File + Hooks Template

**Files:**
- Create: `claude-code/CLAUDE.md`
- Create: `claude-code/hooks-template.md`

**Step 1: Create directory structure**
```
mkdir -p claude-code/.claude/rules
mkdir -p claude-code/.claude/skills/git-workflow
mkdir -p claude-code/.claude/skills/testing-strategy
mkdir -p claude-code/.claude/skills/requirements-interview
mkdir -p claude-code/.claude/skills/plan-first-development
mkdir -p claude-code/.claude/skills/code-review
mkdir -p claude-code/.claude/skills/security-audit
```

**Step 2: Write CLAUDE.md**

Format: Plain Markdown, under 60 lines. No YAML frontmatter on the main file.

Content structure:
```
# [Project Name] — Animal Advocacy Platform

## Identity
- 1-3 sentences: what this project is, its domain (animal advocacy/liberation)
- Ubiquitous language reference (link to advocacy-domain rule)

## Workflow
- Plan before code — ALWAYS read existing code before making changes
- Never create duplicate functions — check what exists first
- Spec-first: write requirements before implementation
- Test-first: write tests before code
- Two-failure rule: after two failed fixes, clear conversation and restart

## Constraints
- NEVER log, store, or transmit personally identifiable activist data
- NEVER send sensitive content to external APIs without explicit approval
- ALWAYS use zero-retention API configurations
- ALWAYS implement progressive disclosure for traumatic content
- Abstract all model/vendor dependencies — vendor lock-in is a movement risk

## Review
- Check AI output for: shallow modules, DRY violations, suppressed errors
- Every PR must be tagged AI-Assisted if agent-generated
- Security review required for any code touching investigation/evidence data

## Scoped Rules
- See .claude/rules/ for domain-specific guidance on testing, security, privacy, cost, advocacy domain, accessibility, and emotional safety

## Hooks (Deterministic Enforcement)
- Use Claude Code hooks for deterministic checks — strictly superior to instruction-based enforcement
- See hooks-template.md for configuration guide
- Pre-commit: security scanning, PII detection
- Post-edit: formatting
- Pre-push: full test suite

## MCP Servers
- Any MCP server handling sensitive advocacy data MUST be self-hosted
- MCP extends agent capabilities but also extends the attack surface
```

**Step 3: Write hooks-template.md**
Stack-agnostic documentation file describing which hook slots to configure:
```markdown
# Claude Code Hooks Configuration Guide

Hooks execute shell commands before/after agent actions. They are strictly
superior to writing "always format" or "always lint" in CLAUDE.md — deterministic
tools for deterministic checks, zero tokens consumed.

## Recommended Hook Slots

### Pre-Commit Hook
Purpose: Block commits containing sensitive data or security violations
Configure: [Your security scanner command — e.g., detect-secrets, gitleaks, trufflehog]
Why: Investigation data, activist identities, API keys must never reach git history

### Post-Edit Hook
Purpose: Auto-format after every file edit
Configure: [Your formatter command — e.g., prettier, black, gofmt]
Why: Formatting is a deterministic check; never waste instruction budget on it

### Pre-Push Hook
Purpose: Run full test suite before any push to remote
Configure: [Your test runner command]
Why: Ensures no broken code reaches shared branches

### Custom: PII Detection Hook
Purpose: Scan for personally identifiable activist data in code and comments
Configure: [Your PII scanner — custom regex or tool]
Why: Ag-gag legal exposure means ANY activist PII in code is a liability

## How to Configure
Claude Code hooks are configured in .claude/settings.json or via the CLI.
See Claude Code documentation for the exact configuration format for your version.
```

**Step 4: Verify CLAUDE.md line count ≤ 60**

**Step 5: Commit**
```
git add claude-code/CLAUDE.md claude-code/hooks-template.md
git commit -m "feat(claude-code): add main CLAUDE.md instruction file and hooks template"
```

### Task 2: Claude Code — 7 Scoped Rule Files

**Files:**
- Create: `claude-code/.claude/rules/testing.md`
- Create: `claude-code/.claude/rules/security.md`
- Create: `claude-code/.claude/rules/privacy.md`
- Create: `claude-code/.claude/rules/cost-optimization.md`
- Create: `claude-code/.claude/rules/advocacy-domain.md`
- Create: `claude-code/.claude/rules/accessibility.md`
- Create: `claude-code/.claude/rules/emotional-safety.md`

**Format for each:** Markdown with optional YAML `paths:` frontmatter. Example:
```markdown
---
paths:
  - "src/security/**"
  - "**/*auth*"
---
# Security Rules for Animal Advocacy Projects

[Content here]
```

**Content guidance per file:**

**testing.md** — Use `paths:` targeting test directories. Cover: assertion quality (never assert output == output), spec-first generation, property-based testing for invariants, mutation testing to verify test quality, test error paths explicitly, AI-generated tests need review for tautological assertions, test adversarial inputs.

**security.md** — Use `paths:` targeting security/auth/crypto directories. Cover: zero-retention APIs, encrypted local storage with plausible deniability, input validation against industry sabotage, supply chain verification, ag-gag exposure vectors, device seizure preparation, self-hosted inference for critical paths, three adversaries model.

**privacy.md** — Use `paths:` targeting data/user/profile directories. Cover: GDPR/CCPA compliance, data minimization, activist identity protection, coalition data sharing with different risk profiles, whistleblower protection, anonymization requirements, consent as ongoing process not checkbox, right to deletion must be real deletion not soft delete.

**cost-optimization.md** — No paths (applies globally). Cover: model routing (cheap models for simple tasks, capable for complex), token budgets per session, prompt cache optimization (static content first), vendor lock-in as movement risk (abstract model dependencies), self-hosted fallbacks, budget allocation (40% implementation, 30% testing, 20% review, 10% docs).

**advocacy-domain.md** — No paths (applies globally). Cover: ubiquitous language dictionary, bounded contexts (investigation ops / public campaigns / coalition coordination / legal defense), entity definitions (Activist, Organization, Campaign, Investigation, Witness, Evidence, Coalition, Sanctuary), domain events, anti-corruption layers between contexts.

**accessibility.md** — Use `paths:` targeting UI/frontend/i18n directories. Cover: i18n from day one, low-bandwidth optimization, offline-first patterns, low-literacy design, mesh networking compatibility, graceful degradation, device seizure preparation (what happens when connectivity is lost suddenly), multi-language activist networks.

**emotional-safety.md** — Use `paths:` targeting content/media/display directories. Cover: progressive disclosure of traumatic content, configurable detail levels, content warnings, investigation footage handling (never auto-play, always blur by default), witness testimony display (consent verification, anonymization), burnout prevention patterns, secondary trauma mitigation, opt-in escalation of graphic content.

**Step: Write all 7 files**

**Step: Verify each file has correct YAML frontmatter where applicable**

**Step: Commit**
```
git add claude-code/.claude/rules/
git commit -m "feat(claude-code): add 7 scoped rule files for testing, security, privacy, cost, advocacy, accessibility, emotional safety"
```

### Task 3: Claude Code — 6 Skill Files

**Files:**
- Create: `claude-code/.claude/skills/git-workflow/SKILL.md`
- Create: `claude-code/.claude/skills/testing-strategy/SKILL.md`
- Create: `claude-code/.claude/skills/requirements-interview/SKILL.md`
- Create: `claude-code/.claude/skills/plan-first-development/SKILL.md`
- Create: `claude-code/.claude/skills/code-review/SKILL.md`
- Create: `claude-code/.claude/skills/security-audit/SKILL.md`

**Format for each:** YAML frontmatter (name, description) + Markdown body. Example:
```markdown
---
name: git-workflow
description: Git workflow patterns for AI-assisted advocacy development — atomic commits, ephemeral branches, PR curation
---
# Git Workflow

## When to Use
- Before committing, branching, or creating PRs
- When reviewing commit history or merge strategy

## Process
[Step-by-step workflow guidance]
```

**Content:** Draw from the "Process Skills Content" section in the Content Reference above. Each skill should be a complete, actionable workflow — not a list of principles but a sequence of steps the agent follows.

**Step: Write all 6 SKILL.md files**

**Step: Verify YAML frontmatter is valid (name + description fields)**

**Step: Commit**
```
git add claude-code/.claude/skills/
git commit -m "feat(claude-code): add 6 process skill packages"
```

---

## Phase 2: Multi-File Tools (7 tools, parallel)

**All 7 tools in this phase are independent. Dispatch as parallel subagents.**

### Task 4: Cursor (14 files)

**Files:**
- Create: `cursor/.cursorrules`
- Create: `cursor/.cursor/rules/` (13 .mdc files)

**Step 1: Create directory structure**
```
mkdir -p cursor/.cursor/rules
```

**Step 2: Write .cursorrules**
Main instruction file, ~60 lines. Same content principles as CLAUDE.md but adapted for Cursor's ecosystem. Plain Markdown (no frontmatter on the main file).

**Step 3: Write 13 .mdc files**

MDC format requires YAML frontmatter with these fields:
```yaml
---
description: "Short description for agent-requested mode"
globs: ["**/*.test.*", "**/*.spec.*"]  # Only for autoAttached mode
alwaysApply: true  # For always-apply mode
---
```

Activation mode assignments:
| File | Mode | Rationale |
|------|------|-----------|
| testing.mdc | alwaysApply: true | Always relevant |
| security.mdc | alwaysApply: true | Non-negotiable |
| privacy.mdc | description only (agentRequested) | Contextual |
| cost-optimization.mdc | description only (agentRequested) | Contextual |
| advocacy-domain.mdc | alwaysApply: true | Core identity |
| accessibility.mdc | description only (agentRequested) | Contextual |
| emotional-safety.mdc | description only (agentRequested) | Contextual |
| git-workflow.mdc | description only (agentRequested) | Process skill |
| testing-strategy.mdc | globs: ["**/*.test.*", "**/*.spec.*"] (autoAttached) | File-triggered |
| requirements-interview.mdc | No alwaysApply, no globs (manual) | User invokes with @ |
| plan-first.mdc | description only (agentRequested) | Process skill |
| code-review.mdc | No alwaysApply, no globs (manual) | User invokes with @ |
| security-audit.mdc | No alwaysApply, no globs (manual) | User invokes with @ |

**Step 4: Verify all .mdc files have valid YAML frontmatter**

**Step 5: Commit**
```
git add cursor/
git commit -m "feat(cursor): add complete Cursor instruction set with 4 activation modes"
```

### Task 5: GitHub Copilot (22 files)

**Files:**
- Create: `github-copilot/.github/copilot-instructions.md`
- Create: `github-copilot/.github/instructions/` (7 files)
- Create: `github-copilot/.github/prompts/` (6 reusable prompt files)
- Create: `github-copilot/.github/chat-modes/` (2 custom chat mode definitions)
- Create: `github-copilot/.github/skills/` (6 SKILL.md files)

**Note:** Copilot supports the richest instruction hierarchy of any tool — 5 elements: repo-wide instructions, path-specific instructions with applyTo, reusable prompt files, custom chat modes, and skills.

**Step 1: Create directory structure**
```
mkdir -p github-copilot/.github/instructions
mkdir -p github-copilot/.github/prompts
mkdir -p github-copilot/.github/chat-modes
mkdir -p github-copilot/.github/skills/git-workflow
mkdir -p github-copilot/.github/skills/testing-strategy
mkdir -p github-copilot/.github/skills/requirements-interview
mkdir -p github-copilot/.github/skills/plan-first-development
mkdir -p github-copilot/.github/skills/code-review
mkdir -p github-copilot/.github/skills/security-audit
```

**Step 2: Write copilot-instructions.md**
~60 lines. Repository-wide instructions. Same principle-level content.

**Step 3: Write 7 instruction files**
Markdown with `applyTo:` directives where applicable. Example:
```markdown
---
applyTo: "**/*.test.*"
---
# Testing Instructions
```

**Step 4: Write 6 reusable prompt files**
Prompt files are user-invocable workflows. Each maps to a process skill:
- `git-workflow.prompt.md` — Invoked when preparing commits/PRs
- `testing-strategy.prompt.md` — Invoked when writing/reviewing tests
- `requirements-interview.prompt.md` — Invoked to gather requirements from stakeholders
- `plan-first.prompt.md` — Invoked before starting implementation
- `code-review.prompt.md` — Invoked when reviewing code
- `security-audit.prompt.md` — Invoked for security assessment

Each prompt file should contain the workflow steps the agent follows when invoked, written as a structured prompt.

**Step 5: Write 2 custom chat mode definitions**
Custom chat modes define persistent agent personas:

**advocacy-reviewer.yml** — Code reviewer persona focused on: Ousterhout red flags, AI-specific failure patterns, advocacy concerns (data leaks, surveillance surface, emotional safety, coalition boundaries). Uses the layered review pipeline principle.

**requirements-interviewer.yml** — Requirements interviewer persona that: asks one question at a time, probes threat model, identifies coalition partners, assesses legal exposure, maps data retention needs. Follows the requirements-interview skill workflow.

**Step 6: Write 6 SKILL.md files**
Same YAML frontmatter format as Claude Code skills (name + description).

**Step 7: Commit**
```
git add github-copilot/
git commit -m "feat(github-copilot): add complete Copilot instruction set with all 5 hierarchy elements"
```

### Task 6: Windsurf (14 files)

**Files:**
- Create: `windsurf/.windsurf/rules/` (14 .md files including main.md)

**Step 1: Create directory structure**
```
mkdir -p windsurf/.windsurf/rules
```

**Step 2: Write all 14 files**

**CRITICAL CONSTRAINT: 6,000 characters per file. 12,000 characters combined ceiling.**

**12K scope note:** Source docs say "12,000-character combined ceiling" without qualifying which files count. Budget conservatively: Always On files alone should stay well under 12K (~8K total for 4 files at ~2K each) to leave headroom for Model Decision files that may load alongside them.

**Privacy warning for Windsurf content:** Windsurf generates persistent "memories" about your codebase across sessions. The security or privacy rule files should include: "Review and clear Windsurf memories regularly for projects involving sensitive investigation or witness data."

Each file needs a YAML frontmatter comment indicating its trigger mode:
```markdown
<!-- trigger: always_on -->
# Main Rules
```
Or:
```markdown
<!-- trigger: model_decision -->
# Privacy Rules
```

Activation assignments:
| File | Trigger | Chars budget |
|------|---------|-------------|
| main.md | always_on | ~2,000 |
| testing.md | always_on | ~2,000 |
| security.md | always_on | ~2,000 |
| advocacy-domain.md | always_on | ~2,000 |
| privacy.md | model_decision | ≤6,000 |
| cost-optimization.md | model_decision | ≤6,000 |
| accessibility.md | model_decision | ≤6,000 |
| emotional-safety.md | model_decision | ≤6,000 |
| git-workflow.md | model_decision | ≤6,000 |
| testing-strategy.md | glob (test files) | ≤6,000 |
| requirements.md | manual | ≤6,000 |
| plan-first.md | model_decision | ≤6,000 |
| code-review.md | manual | ≤6,000 |
| security-audit.md | manual | ≤6,000 |

**Always On budget: main + testing + security + advocacy-domain ≤ ~8,000 chars total (~2,000 each), leaving 4K headroom for contextually loaded files**

**Step 3: Verify character counts**
```
wc -c windsurf/.windsurf/rules/*.md
```
Ensure no file exceeds 6,000 chars and always_on files total ≤ 12,000.

**Step 4: Commit**
```
git add windsurf/
git commit -m "feat(windsurf): add complete Windsurf instruction set within 6K/12K char limits"
```

### Task 7: Kilo Code (21 files)

**Files:**
- Create: `kilo-code/.kilocode/rules/memory-bank/brief.md`
- Create: `kilo-code/.kilocode/rules/memory-bank/context.md`
- Create: `kilo-code/.kilocode/rules/memory-bank/history.md`
- Create: `kilo-code/.kilocode/rules/` (5 mode files + 7 concern files)
- Create: `kilo-code/.kilocode/skills/` (6 SKILL.md files)

**Step 1: Create directory structure**
```
mkdir -p kilo-code/.kilocode/rules/memory-bank
mkdir -p kilo-code/.kilocode/skills/git-workflow
mkdir -p kilo-code/.kilocode/skills/testing-strategy
mkdir -p kilo-code/.kilocode/skills/requirements-interview
mkdir -p kilo-code/.kilocode/skills/plan-first-development
mkdir -p kilo-code/.kilocode/skills/code-review
mkdir -p kilo-code/.kilocode/skills/security-audit
```

**Step 2: Write Memory Bank files**

**brief.md** — Project identity, advocacy domain, core mission. Always loaded. Short (~20 lines).

**context.md** — Architecture decisions, threat model (three adversaries), technology choices, bounded contexts. Always loaded. Medium (~60 lines).

**history.md** — Template for decision log. Starts with example entries. Students fill in as project evolves.
```markdown
# Decision History

## [Date] — [Decision Title]
**Context:** What situation prompted this decision
**Decision:** What was decided
**Rationale:** Why this approach
**Consequences:** What follows from this decision
```

**Step 3: Write 5 mode-specific rule files**

Each mode file defines behavior constraints for that mode:

**ask-mode.md** — Read-only exploration. No code changes. Focus on explaining existing code, answering architecture questions. Advocacy context: always consider threat model implications when answering questions about data flow.

**architect-mode.md** — Design and planning. Can read files, propose architecture. No code changes. Must consider: bounded contexts, coalition data isolation, vendor lock-in avoidance, offline-first architecture. Use plan-first-development skill.

**code-mode.md** — Implementation. Can read and write files, run commands. Must follow: testing rules, security rules, emotional safety rules. Use git-workflow skill for commits. Use testing-strategy skill for tests.

**debug-mode.md** — Debugging. Can read files, run tests, inspect state. Follow debugging workflow: reproduce → context → hypotheses → binary search → verify fix. Advocacy-specific: check for data leak vectors when debugging network/storage code.

**orchestrator-mode.md** — Coordinates multi-step workflows across other modes. Decomposes tasks, delegates to appropriate modes, aggregates results. Follow plan-first-development skill. Use security-audit skill before any deployment.

**Step 4: Write 7 concern files** (same content principles as Claude Code rules, but no paths: frontmatter — Kilo Code uses mode-specific loading instead)

**Step 5: Write 6 SKILL.md files** (same format as Claude Code skills)

**Step 6: Commit**
```
git add kilo-code/
git commit -m "feat(kilo-code): add complete Kilo Code setup with 5 modes, Memory Bank, and skills"
```

### Task 8: Cline (14 files)

**Files:**
- Create: `cline/.clinerules`
- Create: `cline/.clinerules/` (13 .md files)

**Step 1: Create directory structure**
```
mkdir -p cline/.clinerules
```

**Step 2: Write .clinerules**
Main rules file at root. ~60 lines. Plain Markdown. Emphasizes Plan/Act paradigm:
- Plan Mode first — always explore before changing
- Act Mode — execute the plan
- Reference scoped rules in .clinerules/ directory

**Step 3: Write 13 scoped rule files**
Plain Markdown, no frontmatter. Cline uses global → workspace override hierarchy.

7 concern files + 6 skill-equivalent files (since Cline doesn't have native skill support, these are additional rule files with clear "When to use" headers).

**Step 4: Commit**
```
git add cline/
git commit -m "feat(cline): add complete Cline instruction set with Plan/Act paradigm emphasis"
```

### Task 9: Roo Code (19 files)

**Files:**
- Create: `roo-code/.roomodes`
- Create: `roo-code/.roo/rules/` (18 .md files)

**Step 1: Create directory structure**
```
mkdir -p roo-code/.roo/rules
```

**Step 2: Write .roomodes (JSON)**

Defines custom modes with model assignments and tool restrictions:
```json
{
  "customModes": [
    {
      "slug": "review",
      "name": "Review",
      "roleDefinition": "Code reviewer focused on AI-generated code quality and advocacy-specific concerns",
      "groups": ["read"],
      "source": "project"
    },
    {
      "slug": "interview",
      "name": "Interview",
      "roleDefinition": "Requirements interviewer for advocacy stakeholders — gathers threat model, coalition needs, user safety requirements",
      "groups": ["read"],
      "source": "project"
    }
  ]
}
```

**Step 3: Write 5 mode-specific rule files**
- `rules-architect.md` — Architecture mode, design-focused
- `rules-code.md` — Code mode, implementation-focused
- `rules-debug.md` — Debug mode
- `rules-review.md` — Custom Review mode (code review checklist)
- `rules-interview.md` — Custom Interview mode (requirements gathering)

Each follows Roo Code naming: `rules-{mode-slug}.md`

Mode-specific rule files should include **Boomerang Task** patterns where relevant. Boomerang Tasks delegate subtasks from one mode to another with automatic return of results. Examples:
- Architect mode delegates implementation subtask to Code mode, gets results back
- Code mode delegates review subtask to Review mode, gets findings back
- Orchestrator coordinates multi-mode workflows using Boomerang delegation

**Step 4: Write 7 concern files + 6 skill files** (plain Markdown)

**Step 5: Commit**
```
git add roo-code/
git commit -m "feat(roo-code): add complete Roo Code setup with custom modes and boomerang task patterns"
```

### Task 10: Augment Code (14 files)

**Files:**
- Create: `augment-code/.augment/rules/` (14 .md files including main.md)

**Step 1: Create directory structure**
```
mkdir -p augment-code/.augment/rules
```

**Step 2: Write main.md** (~60 lines, core identity + workflow)

**Step 3: Write 7 concern files + 6 skill files** (plain Markdown)

**Step 4: Commit**
```
git add augment-code/
git commit -m "feat(augment-code): add complete Augment Code instruction set"
```

---

## Phase 3: Single-File Tools (4 tools, parallel)

**All 4 tools are independent. Dispatch as parallel subagents.**

### Task 11: Aider (1 file)

**Files:**
- Create: `aider/CONVENTIONS.md`

**Format:** Single Markdown file loaded as read-only context. Must be self-contained.

**Structure:** All 7 concerns + 6 skills as clearly-headed sections:
```markdown
# Animal Advocacy Development Conventions

## Project Identity
[2-3 sentences]

## Workflow
[Plan-first, test-first, two-failure rule]

## Domain Language
[Ubiquitous language dictionary]

## Testing
[Assertion quality, spec-first, property-based]

## Security
[Zero-retention, ag-gag, three adversaries]

## Privacy
[Activist protection, coalition data, GDPR/CCPA]

## Cost Optimization
[Model routing, token budgets, vendor lock-in]

## Accessibility
[i18n, offline-first, low-bandwidth, mesh]

## Emotional Safety
[Progressive disclosure, content warnings, configurable detail]

## Git Workflow
[Atomic commits, ephemeral branches, PR curation]

## Testing Strategy
[Spec-first, mutation-guided, edge cases]

## Requirements Gathering
[Interview process, threat modeling questions]

## Planning
[Spec → design → tasks, read before write]

## Code Review
[Red flags checklist, advocacy concerns]

## Security Audit
[Threat model assessment checklist]
```

**Challenge:** Fitting all content into one file while remaining useful. Each section should be 5-15 lines of high-signal guidance.

**Commit:**
```
git add aider/
git commit -m "feat(aider): add CONVENTIONS.md with all concerns and skills as sections"
```

### Task 12: Gemini CLI (1 file)

**Files:**
- Create: `gemini-cli/GEMINI.md`

**Format:** Single Markdown file at project root. Same structure as Aider's CONVENTIONS.md but adapted for Gemini CLI's ecosystem.

**Commit:**
```
git add gemini-cli/
git commit -m "feat(gemini-cli): add GEMINI.md instruction file"
```

### Task 13: JetBrains/Junie (1 file)

**Files:**
- Create: `jetbrains-junie/.junie/guidelines.md`

**Step 1: Create directory**
```
mkdir -p jetbrains-junie/.junie
```

**Step 2: Write guidelines.md**
Single always-on file. Same structure as Aider but in `.junie/` directory.

**Commit:**
```
git add jetbrains-junie/
git commit -m "feat(jetbrains-junie): add Junie guidelines file"
```

### Task 14: AGENTS.md Universal (1 file)

**Files:**
- Create: `agents-md/AGENTS.md`

**Format:** The vendor-neutral standard. Supported by 20+ tools. Nearest-file-wins hierarchy.

**Content:** Most comprehensive single file. This is the "works everywhere" fallback. Should cover all 7 concerns and 6 skills in a structured, scannable format. Follows the AGENTS.md spec from the Agentic AI Foundation.

**Commit:**
```
git add agents-md/
git commit -m "feat(agents-md): add universal AGENTS.md vendor-neutral instruction file"
```

---

## Phase 4: README

### Task 15: Repository README

**Files:**
- Create: `README.md`

**Content:**
1. What this library is (1 paragraph)
2. Quick start — pick your tool, copy the directory
3. Tool comparison table (features, complexity, format)
4. What's in each directory (brief descriptions)
5. The 7 concerns explained (what students get)
6. The 6 process skills explained (what students get)
7. Customization — how to adapt for specific tech stacks
8. The advocacy domain — why these instruction files are different from generic ones

**Commit:**
```
git add README.md
git commit -m "docs: add repository README with tool comparison and usage guide"
```

---

## Verification Checklist (run after all phases)

- [ ] Every main instruction file ≤ 60 lines
- [ ] Windsurf always_on files total ≤ 12,000 chars
- [ ] Windsurf individual files ≤ 6,000 chars each
- [ ] All Cursor .mdc files have valid YAML frontmatter
- [ ] All SKILL.md files have name + description frontmatter
- [ ] Claude Code rules with paths: have valid YAML
- [ ] Copilot instructions with applyTo: have valid YAML
- [ ] Roo Code .roomodes is valid JSON
- [ ] Kilo Code Memory Bank has brief.md, context.md, history.md
- [ ] No file references external knowledge base documents
- [ ] No file contains language-specific code or build commands
- [ ] Every file addresses animal advocacy domain concerns
- [ ] All 12 tool directories are self-contained
- [ ] Total file count = 137 + README = 138
- [ ] Claude Code hooks-template.md present
- [ ] Copilot prompt files present (6 in .github/prompts/)
- [ ] Copilot chat mode definitions present (2 in .github/chat-modes/)
- [ ] Slopsquatting named explicitly in security-audit content
- [ ] Prompt injection / Rules File Backdoor named in security-audit content
- [ ] All 5 testing anti-patterns named in testing-strategy content
- [ ] All 10 ranked design principles represented in main instruction files
- [ ] Generation-then-comprehension pattern mentioned in plan-first content
- [ ] Silent failure pattern mentioned in code-review content
- [ ] Windsurf persistent memories privacy warning present

---

## Execution Summary

| Phase | Tools | Files | Parallelizable |
|-------|-------|-------|---------------|
| 1 | Claude Code | 15 | No (first, establishes patterns) |
| 2 | Cursor, Copilot, Windsurf, Kilo Code, Cline, Roo Code, Augment Code | 118 | Yes (7 parallel subagents) |
| 3 | Aider, Gemini CLI, JetBrains/Junie, AGENTS.md | 4 | Yes (4 parallel subagents) |
| 4 | README | 1 | No (needs all tools done first) |
| **Total** | **12 tools** | **137 + 1 README = 138** | |
