# Windsurf — Animal Advocacy Instructions

Windsurf instruction files for animal advocacy development. Copy this directory into any Open Paws project root.

## Usage

```bash
cp -r .windsurf your-project/
```

Windsurf loads rules from `.windsurf/rules/` based on trigger type. Rule files respect 6K character (always-active) and 12K character (agent-requested) limits.

## .windsurf/rules/ Contents

| File | What it covers | When to read |
|------|---------------|--------------|
| `main.md` | Always-active baseline: advocacy domain, security constraints, 10-point checklist | Windsurf loads this always |
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
| `requirements.md` | Six-phase stakeholder interview for requirements gathering | Requirements sessions |
| `security-audit.md` | 10-step advocacy security audit | Security reviews |
| `security.md` | Three-adversary threat model, zero-retention APIs, device seizure preparation | Any security-sensitive work |
| `testing-strategy.md` | Spec-first, mutation testing, five anti-patterns | Test writing |
| `testing.md` | Testing concerns and quality gates | Test setup |

## Cross-References

- For Claude Code format, see `../claude-code/`
- For Cursor MDC format, see `../cursor/`
- For universal vendor-neutral instructions, see `../agents-md/AGENTS.md`
