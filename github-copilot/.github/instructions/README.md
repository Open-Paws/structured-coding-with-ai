# GitHub Copilot Path-Specific Instructions

8 instruction files with `applyTo:` YAML frontmatter. Copilot loads a file automatically when the active file matches its glob pattern.

## Files

| File | Glob Pattern | Concern |
|------|-------------|---------|
| `testing.md` | `**/*.test.*,**/*.spec.*,**/test/**,**/tests/**,**/__tests__/**` | Test assertion quality, spec-first generation, mutation testing, adversarial input testing |
| `security.md` | `**/*auth*,**/*crypto*,**/security/**,**/*encrypt*` | Zero-retention APIs, encrypted storage, supply chain verification, ag-gag exposure, device seizure, MCP security |
| `privacy.md` | `**/*pii*,**/data/**,**/user/**,**/profile/**` | Data minimization, activist identity protection, GDPR/CCPA, consent workflows, coalition data sharing, anonymization |
| `cost-optimization.md` | (no `applyTo:`) | Model routing, token budgets, prompt caching, vendor lock-in, self-hosted inference economics |
| `advocacy-domain.md` | (no `applyTo:`) | Ubiquitous language dictionary, bounded contexts, anti-corruption layers, entity definitions |
| `accessibility.md` | `**/ui/**,**/frontend/**,**/i18n/**,**/l10n/**` | Internationalization, low-bandwidth optimization, offline-first, mesh networking, graceful degradation |
| `emotional-safety.md` | `**/content/**,**/media/**,**/display/**,**/upload/**` | Progressive disclosure, content warnings, investigation footage handling, burnout prevention |
| `geo-seo.md` | `**/*.html,**/robots.txt,**/sitemap.xml,**/[Ll]ayout.*,**/[Hh]ead/**,**/[Bb]ase[Hh]ead.*,**/[Ss]eo/**,**/[Mm]eta/**,**/[Ss]chema/**,**/[Ss]tructured-[Dd]ata/**,**/llms.txt` | SEO + GEO optimization for AI citation, structured data, Core Web Vitals, Wikipedia/Wikidata presence |

Files without `applyTo:` frontmatter (`cost-optimization.md`, `advocacy-domain.md`) are available as general reference and may be loaded based on context or referenced from the repo-wide `copilot-instructions.md`.
