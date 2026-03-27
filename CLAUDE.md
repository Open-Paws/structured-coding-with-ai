# Structured Coding with AI

Ready-to-use AI coding instruction files for 12 tools, tailored for animal advocacy software. Copy a tool directory into any project root and the AI assistant immediately understands advocacy-domain constraints, security threat models, testing standards, and process workflows. Part of the Open Paws developer pipeline.

## Quick Start

No build step. Pick a tool directory, copy its files into your project:

```bash
# Example: Claude Code
cp claude-code/CLAUDE.md your-project/
cp claude-code/hooks-template.md your-project/
cp -r claude-code/.claude your-project/
```

See README.md for copy commands for all 12 tools.

## Architecture

```
claude-code/       15 files — CLAUDE.md + scoped rules + skills + hooks template
cursor/            14 files — .cursorrules + .mdc files (4 activation modes)
github-copilot/    22 files — copilot-instructions + prompts + chat modes + skills
windsurf/          14 files — .windsurf/rules/ (4 trigger types, 6K/12K char limits)
kilo-code/         21 files — mode files + Memory Bank + concerns + skills
cline/             14 files — .clinerules/ (Plan/Act paradigm)
roo-code/          19 files — .roomodes JSON + mode rules + concerns + skills
augment-code/      14 files — .augment/rules/
aider/              1 file  — CONVENTIONS.md (all-in-one)
gemini-cli/         1 file  — GEMINI.md (all-in-one)
jetbrains-junie/    1 file  — .junie/guidelines.md (all-in-one)
agents-md/          1 file  — AGENTS.md (vendor-neutral, 20+ tools)
```

137 files total across 12 tool directories.

## Key Files

| File | Purpose |
|------|---------|
| `README.md` | Full tool comparison, copy commands, content coverage |
| `claude-code/CLAUDE.md` | Claude Code root instruction file |
| `claude-code/hooks-template.md` | Pre-commit/post-edit/pre-push hook setup guide |
| `agents-md/AGENTS.md` | Universal fallback for any unsupported tool |

## Content Coverage

All 12 tools cover the same 7 concerns and 6 process skills:

**Concerns:** Testing, Security, Privacy, Cost optimization, Advocacy domain, Accessibility, Emotional safety

**Skills:** git-workflow, testing-strategy, requirements-interview, plan-first-development, code-review, security-audit

## Development

- **No dependencies** -- pure markdown/JSON instruction files
- **Adding a new tool:** Create `tool-name/` directory, implement the 7 concerns + 6 skills in the tool's native format
- **Editing content:** Each tool was independently authored for its format -- changes to one do not auto-propagate to others
