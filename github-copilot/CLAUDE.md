# GitHub Copilot — Animal Advocacy Instructions

GitHub Copilot instruction files for animal advocacy development. Copy this directory into any Open Paws project root.

## Usage

```bash
cp -r .github your-project/
```

The `.github/` directory contains Copilot's instruction format: persistent instructions, context instructions, prompt files, skills, and chat modes.

## .github/ Contents

| File | What it covers | When to read |
|------|---------------|--------------|
| `copilot-instructions.md` | Always-active baseline instructions for Copilot | Copilot loads this automatically |

## .github/instructions/ Contents

Context-specific instruction files loaded when Copilot detects relevant file patterns:

| File | What it covers | When to read |
|------|---------------|--------------|
| `accessibility.md` | Internationalization, low-bandwidth, offline-first, low-literacy design | Accessibility work |
| `advocacy-domain.md` | Ubiquitous language dictionary, bounded contexts, anti-corruption layers | Any advocacy feature work |
| `cost-optimization.md` | Model routing, token budget discipline, vendor lock-in as movement risk | LLM integration work |
| `emotional-safety.md` | Progressive disclosure, content warnings, burnout prevention | Content-displaying features |
| `external-contribution-safety.md` | Two-state identity: advocacy mode vs neutral mode for external repos | Any external repo work |
| `geo-seo.md` | SEO and GEO optimization rules | Public-facing pages |
| `privacy.md` | Activist identity protection, real deletion, zero-knowledge architecture | Any data handling |
| `security.md` | Three-adversary threat model, zero-retention APIs, device seizure preparation | Any security-sensitive work |
| `testing.md` | Testing concerns and quality gates | Test setup |

## .github/prompts/ Contents

Reusable prompt files invoked from Copilot chat:

| File | What it covers | When to read |
|------|---------------|--------------|
| `code-review.prompt.md` | Five-layer code review pipeline | PR review |
| `geo-seo-audit.prompt.md` | SEO and GEO audit workflow | Public pages audit |
| `git-workflow.prompt.md` | Issue-first GitHub workflow: worktree-per-task, plan→review→implement loops, desloppify gate, PR monitoring | Git operations |
| `plan-first.prompt.md` | Read → plan → code → verify workflow | Before implementation |
| `requirements-interview.prompt.md` | Six-phase stakeholder interview | Requirements gathering |
| `security-audit.prompt.md` | 10-step advocacy security audit | Security reviews |
| `testing-strategy.prompt.md` | Spec-first, mutation testing, five anti-patterns | Test writing |

## .github/chat-modes/ Contents

| File | What it covers | When to read |
|------|---------------|--------------|
| `advocacy-reviewer.yml` | Chat mode for code review with advocacy focus | PR review mode |
| `requirements-interviewer.yml` | Chat mode for structured requirements gathering | Requirements sessions |

## .github/skills/ Contents

Each subdirectory is a Copilot skill (code-review, geo-seo-audit, git-workflow, plan-first-development, requirements-interview, security-audit, testing-strategy).

## Cross-References

- For Claude Code format, see `../claude-code/`
- For Cursor MDC format, see `../cursor/`
- For universal vendor-neutral instructions, see `../agents-md/AGENTS.md`
