# Kilo Code Configuration

Rule files and skill packages for [Kilo Code](https://kilocode.ai), an AI coding assistant with multiple operational modes.

## Structure

```
.kilocode/
  rules/              # Mode-specific rules, cross-cutting concerns, and memory bank
    ask-mode.md        # Read-only exploration mode
    architect-mode.md  # Design and planning mode
    code-mode.md       # Implementation mode
    debug-mode.md      # Investigation and fix mode
    orchestrator-mode.md # Multi-step workflow coordination
    testing.md         # Testing concern
    security.md        # Security concern
    privacy.md         # Privacy concern
    cost-optimization.md # Cost optimization concern
    advocacy-domain.md # Domain language and bounded contexts
    accessibility.md   # Accessibility concern
    emotional-safety.md # Emotional safety concern
    memory-bank/       # Progressive context disclosure (3 files)
  skills/              # 6 skill packages, each with a SKILL.md
```

## Modes

Kilo Code operates in five modes, each with a dedicated rule file:

- **Ask** -- Read-only exploration and explanation. Cannot modify files or run state-changing commands.
- **Architect** -- Design and planning. Produces specifications and decompositions. No implementation.
- **Code** -- Implementation. Reads, writes, tests. Follows plan-first workflow with a self-review checklist.
- **Debug** -- Structured debugging: reproduce, hypothesize, isolate, fix, verify.
- **Orchestrator** -- Coordinates complex workflows by delegating subtasks to the other four modes.

## Concerns

Seven cross-cutting concern files apply across modes: testing, security, privacy, cost optimization, advocacy domain language, accessibility, and emotional safety.

## Memory Bank

Three template files in `rules/memory-bank/` provide progressive context about the project. Update these as your project evolves.

## Skills

Six skill packages in `skills/`, each with its own `SKILL.md`: git-workflow, testing-strategy, requirements-interview, plan-first-development, code-review, and security-audit.

## Setup

Copy the `.kilocode` directory into your project root:

```bash
cp -r .kilocode your-project/
```

Then update the memory bank files (`brief.md`, `context.md`, `history.md`) to reflect your project.
