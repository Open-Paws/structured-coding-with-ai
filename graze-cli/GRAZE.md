# GRAZE.md — Open Paws Graze-CLI Guide

## What is graze and why use it?

Graze-CLI is Open Paws' fork of [opencode](https://github.com/anomalyco/opencode), an agentic coding CLI for advocacy developers. It supports automatic failover across 9 LLM providers (7 with free tiers: Gemini, Groq, Cerebras, SambaNova, DeepInfra, Ollama, Mistral/CodeStral). Key differences from upstream:
- Advocacy-aware system prompts (neutral mode for external repos, full kernel for Open Paws)
- Pre-configured NAV/desloppify hooks
- India bootcamp / global south optimized (free-tier providers, Colab secrets)

Copy this `graze-cli/` directory to your project root. Graze auto-detects it.

## Installation (Open Paws fork)

**NOT** `npm i -g opencode` (upstream, lacks advocacy rules).

### Global install (recommended for Guild devs)
```bash
git clone https://github.com/Open-Paws/graze-cli.git
cd graze-cli
npm install
npm run build
npm link  # or `bun link`
```
Test: `graze --version`

### Colab / no-install (India bootcamp)
```bash
git clone https://github.com/Open-Paws/graze-cli.git
cd graze-cli
npm install
npx graze --version  # or add to $PATH
```
Use Colab secrets for API keys: `GOOGLE_GENERATIVE_AI_API_KEY`, `GROQ_API_KEY`, etc.

**npm package pending** (@open-paws/graze publishing tracked [#74](https://github.com/Open-Paws/graze-cli/issues/74)).

## Free-tier Provider Setup (India Bootcamp)

| Provider | Env Var | Get Key |
|----------|---------|---------|
| Gemini 1.5 Flash | `GOOGLE_GENERATIVE_AI_API_KEY` | [Google AI Studio](https://aistudio.google.com/app/apikey) (free) |
| Groq Llama 3.3 70B | `GROQ_API_KEY` | [Groq Console](https://console.groq.com/keys) (12K TPM free) |
| Cerebras Sonnet 7B | `CEREBRAS_API_KEY` | [Sonnet Playground](https://cerebras.ai/sonnet-playground) (free research) |
| SambaNova | `SAMBANOVA_API_KEY` | [SambaNova Cloud](https://cloud.sambanova.ai) (free tier) |

`graze herd status` shows ready providers. `graze herd list` for all.

## Advocacy Workflow Rules

1. **Pre-commit**: Always `desloppify scan .` + `semgrep --config=p/open-paws/semgrep-rules-no-animal-violence`
2. **Economic test**: Before implementing, ask: \"Does this make exploitation less profitable or alternatives more competitive?\"
3. **Quest submission** (Guild): `platform_submit_quest_completion` when done
4. **Two-state prompts**: Advocacy kernel auto-injects in Open Paws repos; neutral elsewhere
5. **Token discipline**: Large context (strategy docs) — `graze run --max-tokens 32k`

## Common Failure Modes

- **Free-tier TPM exceeded** (Groq): System prompt ~55K tokens. Use `graze run --provider gemini` first.
- **Speciesist output**: NAV hook catches; retry with `graze run --context advocacy`.
- **Repo context wrong**: Advocacy rules injected everywhere? Check `isAdvocacyMode()` logs.
- **India networks**: Gemini blocked? Fallback: `graze herd list | grep free`.

## Links
- [Graze-CLI Repo](https://github.com/Open-Paws/graze-cli)
- [India Bootcamp Module 1](https://github.com/Open-Paws/c4c-bootcamp/issues/10)
- [Desloppify OP Fork](https://github.com/Open-Paws/desloppify)

**Last updated**: 2026-04-26