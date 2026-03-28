# Windsurf Rules

14 rule files for Windsurf, each with an HTML comment trigger declaration on the first line.

## Trigger Types

- **Always On** -- loaded every conversation. Combined ceiling: 12K characters.
- **Model Decision** -- Windsurf decides whether to load based on current task context.
- **Glob** -- loaded when the active file matches the pattern.
- **Manual** -- user invokes explicitly.

## Files

| File | Trigger | Size |
|------|---------|------|
| `main.md` | Always On | ~2.0K |
| `testing.md` | Always On | ~2.1K |
| `security.md` | Always On | ~2.2K |
| `advocacy-domain.md` | Always On | ~2.5K |
| `privacy.md` | Model Decision | ~3.0K |
| `cost-optimization.md` | Model Decision | ~2.4K |
| `accessibility.md` | Model Decision | ~2.9K |
| `emotional-safety.md` | Model Decision | ~3.1K |
| `git-workflow.md` | Model Decision | ~2.2K |
| `plan-first.md` | Model Decision | ~2.2K |
| `testing-strategy.md` | Glob: `**/*.test.*,**/*.spec.*` | ~3.0K |
| `requirements.md` | Manual | ~2.6K |
| `code-review.md` | Manual | ~3.0K |
| `security-audit.md` | Manual | ~3.3K |

## Character Budget

The four Always On files total approximately **8,500 characters** against the 12K combined ceiling. This leaves roughly 3,500 characters of headroom for additional Always On rules if needed. All files are well under the 6K per-file limit.
