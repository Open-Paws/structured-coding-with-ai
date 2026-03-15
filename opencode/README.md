# OpenCode Instruction Set

Configuration files for OpenCode. OpenCode uses `AGENTS.md` as its native project instruction file and can supplement it with `opencode.json` instruction references when needed.

## Structure

```text
AGENTS.md                  # Main project instruction file for OpenCode
```

## How It Works

- `AGENTS.md` at the project root is the primary OpenCode rules file.
- This package uses OpenCode's native rules format instead of relying on fallback `CLAUDE.md` compatibility.
- If a project later needs additional modular docs, they can be layered in through `opencode.json` `instructions`, while keeping `AGENTS.md` as the shared team baseline.

## Setup

Copy into your project root:

```bash
cp AGENTS.md your-project/
```

Then edit the domain language, workflow constraints, and verification commands for your own stack.
