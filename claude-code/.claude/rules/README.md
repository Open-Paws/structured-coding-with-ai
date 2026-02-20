# Claude Code Scoped Rules

These are scoped rule files for Claude Code. Each file contains markdown guidance that the agent loads conditionally based on file path patterns.

## Activation

Each rule file can include optional `paths:` YAML frontmatter. When the file you are editing matches a rule's glob pattern, Claude Code includes that rule in context. Files without `paths:` frontmatter (like `cost-optimization.md` and `advocacy-domain.md`) are loaded based on task context rather than file path.

## Files

| File | Concern | Path Patterns |
|------|---------|---------------|
| `testing.md` | Test assertion quality, spec-first generation, mutation testing, adversarial input testing | `**/*.test.*`, `**/*.spec.*`, `**/test/**`, `**/tests/**`, `**/__tests__/**` |
| `security.md` | Zero-retention APIs, encrypted storage, supply chain verification, ag-gag legal exposure, device seizure, MCP server security | `**/security/**`, `**/*auth*`, `**/*crypto*`, `**/*encrypt*` |
| `privacy.md` | Data minimization, activist identity protection, GDPR/CCPA, consent workflows, coalition data sharing, anonymization | `**/data/**`, `**/user/**`, `**/profile/**`, `**/*pii*` |
| `cost-optimization.md` | Model routing, token budgets, prompt caching, vendor lock-in, self-hosted inference economics | (no path filter) |
| `advocacy-domain.md` | Ubiquitous language dictionary, bounded contexts, anti-corruption layers, entity definitions | (no path filter) |
| `accessibility.md` | Internationalization, low-bandwidth optimization, offline-first architecture, mesh networking, graceful degradation | `**/ui/**`, `**/frontend/**`, `**/i18n/**`, `**/l10n/**` |
| `emotional-safety.md` | Progressive disclosure of traumatic content, content warnings, investigation footage handling, burnout prevention | `**/content/**`, `**/media/**`, `**/display/**`, `**/upload/**` |
