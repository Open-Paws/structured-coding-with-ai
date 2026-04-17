# Cline — Animal Advocacy Instructions

Cline instruction files for animal advocacy development using the Plan/Act paradigm. Copy this directory into any Open Paws project root.

## Usage

```bash
cp -r .clinerules your-project/
```

The `.clinerules/` directory contains flat files. Cline loads all of them and applies them contextually.

## .clinerules/ Contents

| File | What it covers | When to read |
|------|---------------|--------------|
| `main.md` | Always-active baseline: advocacy domain, security constraints, 10-point checklist | Cline loads this automatically |
| `accessibility.md` | Internationalization, low-bandwidth, offline-first, low-literacy design | Accessibility work |
| `advocacy-domain.md` | Ubiquitous language dictionary, bounded contexts, anti-corruption layers | Any advocacy feature work |
| `code-review.md` | Five-layer review pipeline (automated → AI → Ousterhout → AI failures → advocacy) | PR review |
| `cost-optimization.md` | Model routing, token budget discipline, vendor lock-in as movement risk | LLM integration work |
| `emotional-safety.md` | Progressive disclosure, content warnings, burnout prevention | Content-displaying features |
| `external-contribution-safety.md` | Two-state identity: advocacy mode vs neutral mode for external repos | Any external repo work |
| `geo-seo.md` | SEO and GEO optimization rules | Public-facing pages |
| `git-workflow.md` | Issue-first GitHub workflow: worktree-per-task, plan→review→implement loops, desloppify gate, PR monitoring | Git operations |
| `plan-first.md` | Read → plan → code → verify workflow | Before any implementation |
| `privacy.md` | Activist identity protection, real deletion, zero-knowledge architecture | Any data handling |
| `requirements-interview.md` | Six-phase stakeholder interview | Requirements gathering |
| `security-audit.md` | 10-step advocacy security audit | Security reviews |
| `security.md` | Three-adversary threat model, zero-retention APIs, device seizure preparation | Any security-sensitive work |
| `testing-strategy.md` | Spec-first, mutation testing, five anti-patterns | Test writing |
| `testing.md` | Testing concerns and quality gates | Test setup |

## Cross-References

- For Claude Code format, see `../claude-code/`
- For Cursor MDC format, see `../cursor/`
- For universal vendor-neutral instructions, see `../agents-md/AGENTS.md`
