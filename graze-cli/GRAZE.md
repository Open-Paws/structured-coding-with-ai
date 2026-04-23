# GRAZE.md — Open Paws Graze-CLI Instructions

Graze-CLI is the agentic coding CLI for Open Paws developers. Forked from opencode, it includes advocacy-aware system prompts that enforce speciesist language detection, economic impact testing, and Guild quest submission workflows. Install from the Open Paws fork only.

## Installation

```bash
npm install -g @open-paws/graze
```

**Do NOT** use `npm install -g opencode` — that's upstream without advocacy rules.

## Provider Setup (India Bootcamp)

Free-tier providers:
- **Gemini**: Get API key from Google AI Studio
- **Groq**: Free tier API key
- **SambaNova**: Free research access API
- **Colab**: Store secrets in Colab Secrets (for no-local-install participants)

```bash
# Example env vars
export GEMINI_API_KEY=your_key_here
export GROQ_API_KEY=your_key_here
```

## Advocacy Workflow Rules

Graze enforces these automatically:

1. **desloppify gate**: Run `desloppify scan` before every commit (quality ≥85 required)
2. **Speciesist language**: All output scanned: `semgrep --config semgrep-no-animal-violence.yaml`
3. **Economic test**: Before implementing, confirm: \"Does this make exploitation less profitable or alternatives more competitive?\"
4. **Guild quests**: When done, run `platform_submit_quest_completion` to submit to the Guild

## Common Failure Modes

- **Model refusal**: Factory farming content blocked? Use advocacy knowledge base context.
- **Euphemisms**: Industry terms slip in? NAV pre-commit catches them.
- **Token budget**: Large strategy/policy context → trim aggressively, focus on immediate task.

## Usage

```bash
# Interactive mode with rotation
graze run

# Guide topics
graze guide security-audit
graze guide git-workflow
graze guide requirements-interview

# Export session
graze export ses_xxxxxxxx
```

See [graze-cli README](https://github.com/Open-Paws/graze-cli) for technical details."
</xai:function_call<parameter name="extension">.md