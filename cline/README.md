# Cline Configuration

Rule files for [Cline](https://cline.bot), an AI coding assistant that operates in Plan and Act modes.

## Structure

```
.clinerules/
  main.md                  # Global rules (always loaded)
  testing.md               # Testing concern
  security.md              # Security concern
  privacy.md               # Privacy concern
  cost-optimization.md     # Cost optimization concern
  advocacy-domain.md       # Domain language concern
  accessibility.md         # Accessibility concern
  emotional-safety.md      # Emotional safety concern
  git-workflow.md          # Git workflow skill
  testing-strategy.md      # Testing strategy skill
  requirements-interview.md # Requirements interview skill
  plan-first.md            # Plan-first development skill
  code-review.md           # Code review skill
  security-audit.md        # Security audit skill
```

## Plan/Act Paradigm

Cline operates in two modes:

- **Plan Mode** -- Read-only exploration. Read existing code, understand structure, identify what already exists. No file changes, no commands. Build an attack plan first.
- **Act Mode** -- Execution. Implement the plan from Plan Mode.

The `main.md` file enforces using Plan Mode before Act Mode on every task. This prevents the most common AI failure: duplicating existing code because the agent skipped exploration.

## Setup

Copy the `.clinerules` directory into your project root:

```bash
cp -r .clinerules your-project/
```
