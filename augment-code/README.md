# Augment Code Configuration

Rule files for [Augment Code](https://www.augmentcode.com), an AI coding assistant with directory-based rules.

## Structure

```
.augment/
  rules/
    main.md                  # Core rules
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

## How It Works

Augment Code uses a simple directory-based rule system. All files in `.augment/rules/` are loaded together and applied to every interaction. There are no separate modes or conditional loading -- the full rule set is always active.

`main.md` contains the core workflow (read-plan-code-verify), security constraints, and project identity. The remaining 13 files provide detailed rules for specific concerns and skills.

## Setup

Copy the `.augment` directory into your project root:

```bash
cp -r .augment your-project/
```
