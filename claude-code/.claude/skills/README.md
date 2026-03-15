# Claude Code Skills

These are process skill packages for Claude Code. Each subdirectory contains a `SKILL.md` file with `name:` and `description:` YAML frontmatter followed by step-by-step process instructions.

## How Skills Work

Skills are invoked on demand -- they are not loaded automatically into every conversation. When a user requests a specific workflow (e.g., "do a code review" or "run the security audit"), Claude Code loads the relevant skill and follows its process steps.

## Skills

| Directory | Skill Name | Purpose |
|-----------|-----------|---------|
| `git-workflow/` | git-workflow | Atomic commits per subtask, ephemeral branches, PR curation into reviewable chunks, AI-Assisted tagging, quality signal tracking |
| `advocacy-testing-strategy/` | advocacy-testing-strategy | Spec-first test generation, assertion quality review against three questions, mutation testing, five generation patterns, five anti-patterns to reject |
| `requirements-interview/` | requirements-interview | Structured stakeholder interview in six phases: purpose/users, threat modeling, coalition/data boundaries, user safety, technical constraints, synthesis |
| `plan-first-development/` | plan-first-development | Read-plan-code-verify workflow with spec writing, subtask decomposition, comprehension checks, and context management |
| `advocacy-code-review/` | advocacy-code-review | Five-layer review pipeline: automated checks, AI-assisted first pass, Ousterhout red flags, AI failure patterns, advocacy-specific concerns |
| `security-audit/` | security-audit | Ten-step audit: dependency verification, API retention, storage encryption, input validation, instruction file integrity, MCP servers, device seizure, ag-gag exposure, coalition boundaries, findings report |
