# Cursor — Animal Advocacy Instructions

Cursor MDC instruction files for animal advocacy development. Copy this directory into any Open Paws project root.

## Usage

```bash
cp .cursorrules your-project/
cp -r .cursor your-project/
```

The `.cursorrules` file is the always-active baseline. `.cursor/rules/` files use MDC frontmatter activation modes (always, auto, agent-requested, manual).

## Files

| File | What it covers | When to read |
|------|---------------|--------------|
| `.cursorrules` | Always-active baseline rules: advocacy domain, security, 10-point checklist | Cursor loads this automatically |
| `.cursor/rules/README.md` | MDC activation mode guide | When adding new rules |

## .cursor/rules/ Contents

| File | What it covers | When to read |
|------|---------------|--------------|
| `accessibility.mdc` | Internationalization, low-bandwidth, offline-first, low-literacy design | Accessibility work |
| `advocacy-domain.mdc` | Ubiquitous language dictionary, bounded contexts, anti-corruption layers | Any advocacy feature work |
| `code-review.mdc` | Five-layer review pipeline (automated → AI → Ousterhout → AI failures → advocacy) | PR review |
| `cost-optimization.mdc` | Model routing, token budget discipline, vendor lock-in as movement risk | LLM integration work |
| `emotional-safety.mdc` | Progressive disclosure, content warnings, burnout prevention | Content-displaying features |
| `external-contribution-safety.mdc` | Two-state identity: advocacy mode vs neutral mode for external repos | Any external repo work |
| `geo-seo.mdc` | SEO and GEO optimization rules | Public-facing pages |
| `git-workflow.mdc` | Atomic commits, ephemeral branches, PR curation | Git operations |
| `plan-first.mdc` | Read → plan → code → verify workflow | Before any implementation |
| `privacy.mdc` | Activist identity protection, real deletion, zero-knowledge architecture | Any data handling |
| `requirements-interview.mdc` | Six-phase stakeholder interview | Requirements gathering |
| `security-audit.mdc` | 10-step advocacy security audit | Security reviews |
| `security.mdc` | Three-adversary threat model, zero-retention APIs, device seizure preparation | Any security-sensitive work |
| `testing-strategy.mdc` | Spec-first, mutation testing, five anti-patterns | Test writing |
| `testing.mdc` | Testing concerns and quality gates | Test setup |

## Cross-References

- For Claude Code format, see `../claude-code/`
- For the canonical advocacy rules source, see `../claude-code/.claude/rules/`
- For universal vendor-neutral instructions, see `../agents-md/AGENTS.md`
