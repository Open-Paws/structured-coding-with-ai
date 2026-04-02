# Kilo Code — Animal Advocacy Instructions

Kilo Code instruction files for animal advocacy development. Uses mode-based architecture with Memory Bank for persistent context. Copy this directory into any Open Paws project root.

## Usage

```bash
cp -r .kilocode your-project/
```

Kilo Code loads rules from `.kilocode/rules/` based on active mode. Skills are loaded on demand from `.kilocode/skills/`.

## .kilocode/rules/ Contents

| File | What it covers | When to read |
|------|---------------|--------------|
| `architect-mode.md` | System design and architecture review rules | Architect mode |
| `ask-mode.md` | Question-answering and explanation rules | Ask mode |
| `code-mode.md` | Implementation rules: advocacy constraints, 10-point checklist | Code mode (default) |
| `debug-mode.md` | Debugging and error investigation rules | Debug mode |
| `orchestrator-mode.md` | Multi-agent orchestration rules | Orchestrator mode |
| `accessibility.md` | Internationalization, low-bandwidth, offline-first, low-literacy design | Accessibility work |
| `advocacy-domain.md` | Ubiquitous language dictionary, bounded contexts, anti-corruption layers | Any advocacy feature work |
| `cost-optimization.md` | Model routing, token budget discipline, vendor lock-in as movement risk | LLM integration work |
| `emotional-safety.md` | Progressive disclosure, content warnings, burnout prevention | Content-displaying features |
| `external-contribution-safety.md` | Two-state identity: advocacy mode vs neutral mode for external repos | Any external repo work |
| `geo-seo.md` | SEO and GEO optimization rules | Public-facing pages |
| `privacy.md` | Activist identity protection, real deletion, zero-knowledge architecture | Any data handling |
| `security.md` | Three-adversary threat model, zero-retention APIs, device seizure preparation | Any security-sensitive work |
| `testing.md` | Testing concerns and quality gates | Test setup |

## .kilocode/rules/memory-bank/ Contents

| File | What it covers | When to read |
|------|---------------|--------------|
| `brief.md` | Project brief template for Memory Bank | Initialize new project context |
| `context.md` | Running context template | Ongoing session context |
| `history.md` | Decision history template | Track architectural decisions |

## .kilocode/skills/ Contents

Skill subdirectories: code-review, geo-seo-audit, git-workflow, plan-first-development, requirements-interview, security-audit, testing-strategy.

## Cross-References

- For Claude Code format, see `../claude-code/`
- For Cursor MDC format, see `../cursor/`
- For universal vendor-neutral instructions, see `../agents-md/AGENTS.md`
