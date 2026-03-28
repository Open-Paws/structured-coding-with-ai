<!-- trigger: always_on -->
# Advocacy Domain Language and Bounded Contexts

AI agents drift from domain terminology toward generic synonyms. Language drift causes miscommunication across coalition partners and obscures legal distinctions.

## Ubiquitous Language — Use Consistently, NEVER Introduce Synonyms

- **Campaign** — organized effort for a specific advocacy goal
- **Investigation** — covert documentation of exploitation. Legally sensitive. All data = potential evidence
- **Coalition** — alliance of organizations with different risk profiles and data policies
- **Witness** — person providing testimony. Identity requires maximum protection
- **Testimony** — witness account, subject to consent verification before any use
- **Sanctuary** — permanent animal care facility (not "shelter" or "foster")
- **Rescue** — removing animals from exploitative conditions
- **Liberation** — direct action to free animals, distinct legal implications
- **Direct Action** — physical intervention, legally distinct from campaigning
- **Undercover Operation** — investigation by embedded operative. Highest legal risk
- **Ag-Gag** — laws criminalizing undercover investigation of agriculture
- **Factory Farm** — industrial animal agriculture (not "farm" or "production facility")
- **Slaughterhouse** — facility where animals are killed commercially
- **Farmed Animal** — animals raised for commercial products (not "livestock")
- **Evidence** — documentation of exploitation with potential legal use

## Bounded Contexts — Do NOT Merge

**Investigation Operations** — covert data, evidence management, investigator identity. Highest security. Data never flows outward without declassification. Entities: Investigator, Operation, Evidence, Facility, ChainOfCustody.

**Public Campaigns** — public advocacy, supporter engagement, media. Lower security, high visibility. Entities: Campaign, Supporter, Action, Petition, MediaAsset.

**Coalition Coordination** — multi-org planning, shared resources. Governed by strictest partner's policies. Entities: Coalition, PartnerOrganization, SharedResource, DataSharingAgreement.

**Legal Defense** — case management, attorney-client privilege. Entities: Case, Attorney, Filing, PrivilegedCommunication.

## Anti-Corruption Layers

NEVER allow direct imports between contexts. AI will import directly for expedience. Every boundary crossing must go through explicit translation layers and be auditable.


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
