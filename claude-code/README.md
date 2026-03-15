# Claude Code Instruction Set

Configuration files for Claude Code (Anthropic's CLI agent). These files control how the agent behaves across an animal advocacy software project.

## Structure

```
CLAUDE.md                  # Main instruction file — loaded every prompt
hooks-template.md          # Guide for setting up deterministic shell hooks
.claude/
  rules/                   # 8 scoped rule files, activated by file path or task context
  skills/                  # 6 process skill packages, invoked on demand
```

## How It Works

- **CLAUDE.md** is the main file. Claude Code reads it at the start of every conversation. It defines the project context, workflow constraints, a 10-point review checklist, and references to scoped rules and hooks.
- **hooks-template.md** is a planning guide for configuring shell hooks (pre-commit, post-edit, pre-push, PII detection). Hooks run deterministically and cost zero tokens. Fill in the placeholder commands with your actual tools.
- **.claude/rules/** contains 8 markdown files with optional `paths:` YAML frontmatter. Claude Code activates a rule file when the current file matches its path patterns or the task context.
- **.claude/skills/** contains 6 subdirectories, each with a `SKILL.md` file. Skills have `name:` and `description:` frontmatter and are invoked on demand, not loaded automatically.

## Setup

Copy into your project root:

```bash
cp CLAUDE.md hooks-template.md your-project/
cp -r .claude your-project/
```

Then edit `CLAUDE.md` to reflect your project's domain, and fill in the hook placeholders in `hooks-template.md` with your actual tool commands.
