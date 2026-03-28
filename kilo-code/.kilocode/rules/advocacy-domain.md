# Advocacy Domain Language and Bounded Contexts

This is the domain language reference for animal advocacy software. AI agents drift from domain terminology toward generic synonyms — "order" instead of "campaign," "user" instead of "activist," "report" instead of "investigation." Language drift causes miscommunication across coalition partners and obscures legal and ethical distinctions between operations.

## Ubiquitous Language Dictionary

Use these terms consistently in code, documentation, and conversations. NEVER introduce synonyms.

- **Campaign** — Organized effort for a specific advocacy goal (legislative change, corporate reform, public awareness). Defined start, milestones, success criteria.
- **Investigation** — Covert documentation of animal exploitation conditions. Legally sensitive. All data classified as potential evidence. Distinguished from "research" or "reporting."
- **Coalition** — Alliance of multiple organizations toward a shared goal. Each member has its own risk profile, data policies, and operational boundaries.
- **Witness** — Person providing testimony about exploitation conditions. May be investigator, whistleblower, or bystander. Identity requires maximum protection.
- **Testimony** — A witness's account of observed conditions. Subject to consent verification before any use or display.
- **Sanctuary** — Facility providing permanent care for rescued animals. Distinguished from "shelter" (temporary) or "foster" (individual-based).
- **Rescue** — Removing animals from exploitative conditions. May have distinct legal status by jurisdiction.
- **Liberation** — Direct action to free animals. Specific legal implications distinct from "rescue."
- **Direct Action** — Physical intervention in animal exploitation. Legally distinct from campaigning, lobbying, education.
- **Undercover Operation** — Investigation by operative embedded in exploitative facility. Highest legal risk category.
- **Ag-Gag** — Laws criminalizing undercover investigation of agricultural operations. Determines legal exposure for investigation data.
- **Factory Farm** — Industrial animal agriculture facility. Use this term, not euphemisms like "farm" or "production facility."
- **Slaughterhouse** — Facility where animals are killed for commercial purposes. Use precisely.
- **Companion Animal** — Animals kept for companionship. Distinct legal/ethical framework from farmed animals.
- **Farmed Animal** — Animals raised for food, fiber, or commercial products. Distinguished from "livestock" (industry framing).
- **Evidence** — Documentation of exploitation conditions with potential legal use.

## Bounded Contexts

DIFFERENT domains with different models, rules, and security requirements. Do not merge. Do not allow data to flow between them without explicit anti-corruption layers.

**Investigation Operations** — Covert data collection, evidence management, investigator identity protection, chain of custody. Highest security. Data never flows outward without declassification. Entities: Investigator, Operation, Evidence, Facility, ChainOfCustody.

**Public Campaigns** — Public-facing advocacy, supporter engagement, media, petitions. Lower security, high visibility. Entities: Campaign, Supporter, Action, Petition, MediaAsset.

**Coalition Coordination** — Multi-org planning, shared resources, joint strategy. Data crosses org boundaries; governed by strictest partner's policies. Entities: Coalition, PartnerOrganization, SharedResource, JointAction, DataSharingAgreement.

**Legal Defense** — Case management, attorney-client privileged communications, court filings. Privilege overrides other policies. Entities: Case, Attorney, Defendant, Filing, PrivilegedCommunication.

## Anti-Corruption Layers

When data crosses bounded context boundaries, use explicit translation layers. Raw evidence becomes a "media asset" only through deliberate transformation stripping operational metadata. Coalition intelligence becomes an investigation lead only through documented intake. NEVER allow direct imports between contexts — AI agents will optimize for expedience. Each boundary crossing must be auditable.


## Compassionate Language — No Speciesist Idioms

Code, documentation, comments, commit messages, and variable names must use compassionate, non-speciesist language. AI agents frequently generate common English idioms that normalize animal violence — reject these and use alternatives.

**Prohibited patterns** (with alternatives):
- "kill two birds with one stone" → "accomplish two things at once"
- "beat a dead horse" → "belabor the point"
- "more than one way to skin a cat" → "more than one way to solve this"
- "let the cat out of the bag" → "reveal the secret"
- "like shooting fish in a barrel" → "effortless task"
- "guinea pig" (as test subject) → "test subject" or "early adopter"
- "open a can of worms" → "open a difficult topic"
- "wild goose chase" → "futile search"
- "cattle vs. pets" → "ephemeral vs. persistent"
- "pet project" → "side project"
- "master/slave" → "primary/replica"
- "whitelist/blacklist" → "allowlist/denylist"
- "grandfathered" → "legacy"

This is not exhaustive — 60+ patterns are enforced by the Open Paws no-animal-violence tooling ecosystem:
- Semgrep rules: https://github.com/Open-Paws/semgrep-rules-no-animal-violence
- ESLint plugin: https://github.com/Open-Paws/eslint-plugin-no-animal-violence
- Vale style rules: https://github.com/Open-Paws/vale-no-animal-violence
- Pre-commit hook: https://github.com/Open-Paws/no-animal-violence-pre-commit
- GitHub Action: https://github.com/Open-Paws/no-animal-violence-action
- VS Code extension: https://github.com/Open-Paws/vscode-no-animal-violence
- Reviewdog runner: https://github.com/Open-Paws/reviewdog-no-animal-violence

Core rule definitions: https://github.com/Open-Paws/no-animal-violence
