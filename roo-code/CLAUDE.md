# Roo Code — Animal Advocacy Instructions

Roo Code instruction files for animal advocacy development. Uses JSON-based mode definitions with per-mode rule files. Copy this directory into any Open Paws project root.

## Usage

```bash
cp .roomodes your-project/
cp -r .roo your-project/
```

`.roomodes` defines the available modes (code, architect, ask, debug, review, interview). `.roo/rules/` contains rule files loaded per mode.

## Files

| File | What it covers | When to read |
|------|---------------|--------------|
| `.roomodes` | Mode definitions (JSON): code, architect, ask, debug, review, interview | Configure available modes |

## .roo/rules/ Contents

Mode-specific rule files:

| File | What it covers | When to read |
|------|---------------|--------------|
| `rules-architect.md` | Architecture mode: system design, bounded contexts, advocacy constraints | Architect mode |
| `rules-code.md` | Code mode: implementation rules, 10-point checklist, advocacy domain | Code mode (default) |
| `rules-debug.md` | Debug mode: error investigation without compromising security | Debug mode |
| `rules-interview.md` | Interview mode: structured requirements gathering | Interview mode |
| `rules-review.md` | Review mode: five-layer code review pipeline | Review mode |
| `accessibility.md` | Internationalization, low-bandwidth, offline-first, low-literacy design | Accessibility work |
| `advocacy-domain.md` | Ubiquitous language dictionary, bounded contexts, anti-corruption layers | Any advocacy feature work |
| `code-review.md` | Five-layer review pipeline (automated → AI → Ousterhout → AI failures → advocacy) | PR review |
| `cost-optimization.md` | Model routing, token budget discipline, vendor lock-in as movement risk | LLM integration work |
| `emotional-safety.md` | Progressive disclosure, content warnings, burnout prevention | Content-displaying features |
| `external-contribution-safety.md` | Two-state identity: advocacy mode vs neutral mode for external repos | Any external repo work |
| `geo-seo.md` | SEO and GEO optimization rules | Public-facing pages |
| `git-workflow.md` | Atomic commits, ephemeral branches, PR curation | Git operations |
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
