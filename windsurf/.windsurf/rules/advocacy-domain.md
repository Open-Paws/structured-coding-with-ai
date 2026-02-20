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
