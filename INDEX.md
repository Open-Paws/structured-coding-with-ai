## Structured Coding Knowledge Base

This knowledge base supports C4C Campus curriculum development, distributed team standards, and autonomous agent governance. It consists of four documents organized in a deliberate progression from timeless principles to contemporary practice.

---

## Reading order

Read bottom-up to build a coherent mental model:

```
Layer 4: TESTING.md .............. Testing strategy for AI-assisted development
                                   The keystone — every other practice depends on this

Layer 3: AI_CODING.md ........... The practitioner's guide to coding with AI agents
                                   Contemporary reality — what's different now

Layer 2: GITHUB_RULES.md ........ Git/GitHub workflow patterns from canonical sources
                                   Collaboration mechanics — how teams work together

Layer 1: SOFTWARE_DESIGN.md ..... Software design principles from 15+ books
                                   Foundation — why good code matters
```

**For curriculum designers:** Start at Layer 1 and work up. Each layer assumes familiarity with the layers below it.

**For practitioners:** Start at Layer 3 (AI_CODING.md) for the immediately actionable material, then reference Layers 1-2 for the principles that inform the practices.

**For team leads setting standards:** Start at Layer 2 (GITHUB_RULES.md) and Layer 3 (AI_CODING.md) in parallel, using Layer 4 (TESTING.md) as the enforcement mechanism.

---

## Document summaries

### SOFTWARE_DESIGN.md — Foundational principles

Distilled notes from: A Philosophy of Software Design (Ousterhout), The Pragmatic Programmer (Hunt & Thomas), Clean Code (Martin), Code Complete (McConnell), Working Effectively with Legacy Code (Feathers), Domain-Driven Design (Evans), Refactoring (Fowler), Design Patterns (GoF), The Mythical Man-Month (Brooks), SICP (Abelson & Sussman), Growing Object-Oriented Software (Freeman & Pryce), Release It! (Nygard), The Art of Unix Programming (Raymond), Extreme Programming Explained (Beck), Peopleware (DeMarco & Lister), The Clean Coder (Martin), and Essentialism (McKeown).

**AI-era annotations** throughout the document flag which principles face the most pressure from AI code generation. A ranked summary at the end identifies the ten most frequently violated principles in AI-generated code.

### GITHUB_RULES.md — Collaboration mechanics

Synthesized from: Pro Git, Git for Teams, Continuous Delivery, Accelerate, The DevOps Handbook, and industry engineering practices.

Covers: branching strategies, commit practices, merge strategies, PR size guidelines, code review processes, team coordination patterns by size, and workflow anti-patterns.

**[TENSION] markers** flag four key conflicts between established best practices and AI-assisted development realities, with resolutions for each:
- Trunk-based development vs. AI experiment branches
- PR size limits vs. AI-inflated PR sizes
- Atomic commits vs. multi-file AI refactoring
- Review capacity vs. AI-driven review load increases

### AI_CODING.md — Contemporary practice

Evidence-based guide covering: the three modes of AI coding tools, the productivity paradox (individual speed vs. organizational reality), workflow patterns that work, documented failure modes, skill atrophy research, multi-agent orchestration, educational framework for C4C Campus, team standards, autonomous agent rules, AI-assisted code review, debugging with AI, and cost economics.

Grounded in specific research: METR RCT, Faros AI telemetry (10,000+ developers), Veracode security analysis, GitClear code quality study, Anthropic's comprehension study, Columbia DAPLab failure taxonomy, and others.

### TESTING.md — The keystone

Testing strategy specifically for AI-assisted development. Covers: why testing matters more now, the testing pyramid shifts, the assertion quality problem, five patterns for using AI to generate tests, what to test when AI generates code, test infrastructure requirements, AI-specific testing anti-patterns, cost considerations, and recommended tools.

This document is the enforcement mechanism for the principles in the other three. Without testing, the design principles in SOFTWARE_DESIGN.md are aspirational, the workflow practices in GITHUB_RULES.md are unverifiable, and the AI coding patterns in AI_CODING.md are untrustworthy.

---

## How concepts connect across documents

### The quality chain
SOFTWARE_DESIGN.md defines what good code looks like → GITHUB_RULES.md defines the process for reviewing and merging code → AI_CODING.md documents how AI tools affect both quality and process → TESTING.md provides the verification layer that holds it all together.

### The curriculum thread
SOFTWARE_DESIGN.md provides the principles taught in Foundation (Weeks 1-4) → GITHUB_RULES.md provides the collaboration skills for Intermediate (Weeks 5-10) → AI_CODING.md provides the AI-specific skills for all four stages → TESTING.md should be integrated from day one, not introduced as a separate module.

### The review thread
SOFTWARE_DESIGN.md red flags (Ousterhout) → GITHUB_RULES.md review process and PR standards → AI_CODING.md AI-assisted code review layer → TESTING.md assertion quality review. Review happens at every layer.

### The tension thread
Four cross-document tensions are explicitly flagged and resolved:

| Tension | Documents | Resolution |
|---------|-----------|------------|
| Trunk-based vs. AI branches | GITHUB_RULES.md ↔ AI_CODING.md | Ephemeral AI branches, squash-merged or deleted within hours |
| PR size limits vs. AI output volume | GITHUB_RULES.md ↔ AI_CODING.md | PR curation becomes a core human skill; stacked PRs for large changes |
| Atomic commits vs. multi-file AI changes | GITHUB_RULES.md ↔ AI_CODING.md | Task decomposition produces subtasks; each subtask = one commit |
| Review capacity vs. AI-driven load | GITHUB_RULES.md ↔ AI_CODING.md | Layered review: automated gates → AI review → human review |

---

## For C4C Campus curriculum development

The four-stage curriculum progression in AI_CODING.md maps to these documents:

| Stage | Weeks | Primary documents | Focus |
|-------|-------|-------------------|-------|
| Foundation | 1-4 | SOFTWARE_DESIGN.md, TESTING.md | Principles + testing from day one |
| Intermediate | 5-10 | GITHUB_RULES.md, TESTING.md, AI_CODING.md | Collaboration + AI tool basics |
| Advanced | 11-16 | AI_CODING.md, TESTING.md | Multi-agent, CI/CD, security, cost |
| Specialist | 16+ | All documents | Red-teaming, custom workflows, team standards |

---

## Maintenance

This knowledge base reflects the state of AI coding tools and research as of early 2026. AI_CODING.md requires the most frequent updates as the landscape evolves. SOFTWARE_DESIGN.md and GITHUB_RULES.md contain mostly timeless principles that change slowly. TESTING.md should be updated as new testing tools and techniques emerge.

Key sources to monitor for updates: DORA State of DevOps Report (annual), SWE-bench leaderboard (continuous), OWASP Top 10 (periodic), and major model releases from Anthropic, OpenAI, and Google.