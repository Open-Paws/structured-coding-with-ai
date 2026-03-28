# GitHub Copilot Configuration

This directory contains all GitHub Copilot instruction files, prompt files, chat modes,
and skill packages for the animal advocacy platform.

## Contents

- **`copilot-instructions.md`** — Repository-wide instructions loaded into every Copilot
  interaction. Defines workflow, constraints, and the review checklist.

- **`instructions/`** — 7 path-specific instruction files activated by glob patterns.
  Covers testing, security, privacy, cost optimization, advocacy domain, accessibility,
  and emotional safety.

- **`prompts/`** — 6 reusable prompt files (`.prompt.md`) for on-demand workflows:
  code review, git workflow, plan-first development, requirements interview, security
  audit, and testing strategy.

- **`chat-modes/`** — 2 custom agent personas (`advocacy-reviewer.yml` and
  `requirements-interviewer.yml`) that configure Copilot Chat behavior.

- **`skills/`** — 6 process skill packages, each in its own subdirectory with a
  `SKILL.md` workflow file matching the prompt and Claude Code skill sets.
