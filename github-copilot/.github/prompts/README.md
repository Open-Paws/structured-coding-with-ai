# GitHub Copilot Reusable Prompts

6 reusable prompt files (`.prompt.md`). Users invoke these manually to start a specific workflow. Each file contains step-by-step instructions that Copilot follows as a guided process.

## Prompts

| File | Purpose |
|------|---------|
| `git-workflow.prompt.md` | Guides the developer through atomic commits, ephemeral branches, PR curation, and AI-Assisted tagging |
| `testing-strategy.prompt.md` | Spec-first test generation, assertion quality review, mutation testing, five generation patterns and five anti-patterns |
| `requirements-interview.prompt.md` | Structured stakeholder interview: purpose, threat modeling, coalition boundaries, user safety, technical constraints, synthesis |
| `plan-first.prompt.md` | Plan-before-code workflow: read existing code, write spec, decompose into subtasks, implement one at a time, comprehension check |
| `code-review.prompt.md` | Layered code review: automated checks, AI-assisted first pass, Ousterhout red flags, AI failure patterns, advocacy-specific concerns |
| `security-audit.prompt.md` | Security audit: dependency verification, API retention, encrypted storage, input validation, instruction file integrity, device seizure, ag-gag exposure |

## Usage

In GitHub Copilot Chat, reference a prompt file to start the corresponding workflow. The prompt provides the agent with the full process to follow.
