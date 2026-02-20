# Cursor Instruction Set

Configuration files for Cursor (AI-powered code editor). These files control how Cursor's AI agent behaves across an animal advocacy software project.

## Structure

```
.cursorrules               # Always loaded into every conversation
.cursor/
  rules/                   # 13 .mdc files with MDC-format activation modes
```

## How It Works

- **.cursorrules** is always loaded. It defines the project context, workflow constraints, a 10-point review checklist, and references to the scoped rules in `.cursor/rules/`.
- **.cursor/rules/** contains 13 `.mdc` files. Each uses MDC format: YAML frontmatter specifying an activation mode, followed by markdown content. Cursor supports four activation modes:
  - **alwaysApply** (`alwaysApply: true`) -- loaded into every conversation automatically
  - **autoAttached** (`globs: [...]`) -- loaded when the current file matches the glob patterns
  - **agentRequested** (`description: "..."`) -- the agent decides whether to load the rule based on the description text
  - **manual** -- user invokes the rule explicitly with `@` in the chat

## Setup

Copy into your project root:

```bash
cp .cursorrules your-project/
cp -r .cursor your-project/
```

Then edit `.cursorrules` to reflect your project's domain.
