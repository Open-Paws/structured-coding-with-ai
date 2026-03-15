# Codex Instruction Set

Configuration files for OpenAI Codex. Codex uses `AGENTS.md` as its shared project instruction file across local and GitHub-connected workflows.

## Structure

```text
AGENTS.md                  # Main project instruction file for Codex
```

## How It Works

- `AGENTS.md` lives at the project root and provides the persistent project context Codex should follow.
- The file is written for Codex's execution model: read first, patch carefully, verify changes, and surface approval boundaries clearly.
- Commit `AGENTS.md` to the repository so local Codex sessions and GitHub-connected Codex tasks use the same instructions.

## Setup

Copy into your project root:

```bash
cp AGENTS.md your-project/
```

Then edit the domain language, safety constraints, and verification commands for your own stack.
