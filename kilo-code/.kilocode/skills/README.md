# Skills Directory

Seven skill packages for Kilo Code. Each skill lives in its own subdirectory and contains a `SKILL.md` file that defines the skill's name, description, and detailed instructions.

## Skills

| Directory | Skill | Description |
|-----------|-------|-------------|
| `git-workflow/` | git-workflow | Atomic commits per subtask, ephemeral branches, PR curation, AI-Assisted tagging |
| `testing-strategy/` | testing-strategy | Spec-first test generation, assertion quality review, mutation testing, AI test anti-patterns |
| `requirements-interview/` | requirements-interview | Structured stakeholder interview covering threat model, legal exposure, coalition needs, user safety, and constraints |
| `plan-first-development/` | plan-first-development | Read-plan-code-verify workflow with spec writing and subtask decomposition |
| `code-review/` | code-review | Layered review pipeline: automated checks, AI-assisted review, human review with Ousterhout red flags |
| `security-audit/` | security-audit | Dependency verification, zero-retention compliance, slopsquatting defense, device seizure readiness |
| `geo-seo-audit/` | geo-seo-audit | SEO + GEO audit workflow — Core Web Vitals, HTML structure, semantic writing, E-E-A-T, structured data, crawl budget, topic clusters, link building, conversion optimization, AI citation-risk checks |

## How Skills Work

Modes reference skills by name. For example, Code mode uses `git-workflow` and `testing-strategy`; Orchestrator mode uses `plan-first-development` and `security-audit`. Each `SKILL.md` contains the full instructions the agent follows when that skill is invoked.
