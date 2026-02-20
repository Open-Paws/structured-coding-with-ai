# GitHub Copilot Instruction Set

Configuration files for GitHub Copilot (VS Code, JetBrains, CLI). This is the richest instruction hierarchy of the four tools, with five distinct configuration elements.

## Structure

```
.github/
  copilot-instructions.md       # Repo-wide instructions, always loaded
  instructions/                 # 7 path-specific instruction files
  prompts/                      # 6 reusable prompt files (.prompt.md)
  chat-modes/                   # 2 custom chat mode YAML files
  skills/                       # 6 skill packages (subdirectories with SKILL.md)
```

## How It Works

- **copilot-instructions.md** is always loaded. It defines the project context, workflow constraints, a 10-point review checklist, and references to the other directories.
- **instructions/** contains 7 markdown files with `applyTo:` YAML frontmatter. Copilot loads a file when the active file matches its glob pattern.
- **prompts/** contains 6 `.prompt.md` files. Users invoke these manually to start a specific workflow (git workflow, testing strategy, etc.).
- **chat-modes/** contains 2 `.yml` files that define persistent agent personas. These create specialized chat agents with their own system instructions and tool access.
- **skills/** contains 6 subdirectories, each with a `SKILL.md` file. Skills provide detailed step-by-step process guidance invoked on demand.

## Setup

Copy into your project root:

```bash
cp -r .github your-project/
```

Then edit `copilot-instructions.md` to reflect your project's domain. The instructions, prompts, chat modes, and skills reference each other and work as a coordinated set.
