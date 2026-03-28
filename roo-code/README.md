# Roo Code Configuration

Rule files and custom mode definitions for [Roo Code](https://roocode.com), an AI coding assistant that supports mode-specific rules and Boomerang Task delegation between modes.

## Structure

```
.roomodes               # JSON file defining 2 custom modes (Review, Interview)
.roo/
  rules/                # 5 mode rules, 7 concerns, 6 skills (18 files total)
    rules-architect.md   # Architect mode rules
    rules-code.md        # Code mode rules
    rules-debug.md       # Debug mode rules
    rules-review.md      # Review mode rules (custom)
    rules-interview.md   # Interview mode rules (custom)
    testing.md           # Testing concern
    security.md          # Security concern
    privacy.md           # Privacy concern
    cost-optimization.md # Cost optimization concern
    advocacy-domain.md   # Domain language concern
    accessibility.md     # Accessibility concern
    emotional-safety.md  # Emotional safety concern
    git-workflow.md      # Git workflow skill
    testing-strategy.md  # Testing strategy skill
    requirements-interview.md # Requirements interview skill
    plan-first.md        # Plan-first development skill
    code-review.md       # Code review skill
    security-audit.md    # Security audit skill
```

## Custom Modes

The `.roomodes` file defines two custom modes with read-only tool restrictions:

- **Advocacy Code Reviewer** (`review`) -- Layered review pipeline: automated checks, AI failure pattern detection (DRY violations, shallow modules, suppressed errors, hallucinated APIs), advocacy-specific review (data leak vectors, surveillance surface, emotional safety, coalition boundaries). Uses Ousterhout red flags as structural checklist.
- **Requirements Interviewer** (`interview`) -- One-question-at-a-time stakeholder interview covering threat model, legal exposure, coalition needs, user safety, and technical constraints. Produces a structured specification document.

## Boomerang Task Delegation

Roo Code supports delegating subtasks between modes. The intended chain is:

**Interview** (gather requirements) --> **Architect** (design) --> **Code** (implement) --> **Review** (audit) --> **Code** (address findings)

## Setup

Copy both the `.roomodes` file and the `.roo` directory into your project root:

```bash
cp .roomodes your-project/
cp -r .roo your-project/
```
