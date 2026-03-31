# GitHub Copilot Skills

7 skill packages, each in its own subdirectory with a `SKILL.md` file. Each `SKILL.md` has `name:` and `description:` YAML frontmatter followed by step-by-step process instructions.

Skills are invoked on demand, not loaded automatically. They provide detailed process guidance for specific workflows.

## Skills

| Directory | Skill Name | Purpose |
|-----------|-----------|---------|
| `git-workflow/` | git-workflow | Atomic commits per subtask, ephemeral branches, PR curation into reviewable chunks, AI-Assisted tagging, quality signal tracking |
| `testing-strategy/` | testing-strategy | Spec-first test generation, assertion quality review, mutation testing, five generation patterns, five anti-patterns to reject |
| `requirements-interview/` | requirements-interview | Structured stakeholder interview: purpose/users, threat modeling, coalition/data boundaries, user safety, technical constraints, synthesis |
| `plan-first-development/` | plan-first-development | Read-plan-code-verify workflow with spec writing, subtask decomposition, comprehension checks, context management |
| `code-review/` | code-review | Five-layer review pipeline: automated checks, AI-assisted first pass, Ousterhout red flags, AI failure patterns, advocacy-specific concerns |
| `security-audit/` | security-audit | Ten-step audit: dependency verification, API retention, storage encryption, input validation, instruction file integrity, MCP servers, device seizure, ag-gag exposure, coalition boundaries, findings report |
| `geo-seo-audit/` | geo-seo-audit | SEO + GEO audit and implementation workflow — Core Web Vitals, HTML structure, semantic writing, E-E-A-T, content intent, Wikipedia/Wikidata, JSON-LD schema, meta tags, crawl budget, robots.txt, sitemap, IndexNow, topic cluster architecture, link building, brand signals, conversion optimization, analytics, internationalization, platform presence, defensive review |
