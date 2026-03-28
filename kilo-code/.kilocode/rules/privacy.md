# Privacy Rules for Animal Advocacy Projects

Privacy in advocacy software is not a compliance checkbox — it is the difference between operational security and activist prosecution. Data that seems harmless in isolation becomes evidence under ag-gag statutes: participation timestamps, IP addresses, device fingerprints, and access patterns can identify investigators, witnesses, and rescue coordinators.

## Data Minimization as Default Architecture

Collect the absolute minimum data required for each function. Do not collect data "in case we need it later." Every stored data point is a subpoena target. Before adding any field to any data model, ask: **if this data appeared in a court filing, who would it endanger?** If the answer is anyone, justify its existence or eliminate it.

## Activist Identity Protection

Activist identities are the highest-sensitivity data category. Use pseudonymous identifiers internally. Never store legal names alongside action records. Separate authentication identity from operational identity — the system that verifies login credentials must not be the system that records investigation participation. Compartmentalization is structural: compromise of one system must not cascade.

## GDPR/CCPA Compliance as Floor, Not Ceiling

Regulatory compliance is the minimum. Advocacy software should exceed it. Right to deletion MUST be real deletion — not soft delete with a `deleted_at` flag. When an activist requests erasure, data must be irrecoverable from all storage layers including backups, replicas, search indices, analytics, and logs. Soft delete in advocacy software is a liability: "deleted" records surfacing in legal discovery destroy trust and endanger people.

## Consent as Ongoing Process

Consent is not a one-time checkbox. Implement re-consent workflows for scope changes — new coalition partner access, new feature collecting additional data, investigation footage shared with a new organization. Withdrawal of consent must be as easy as granting it, with immediate effect. Participation in a public campaign does not imply consent to be recorded as an investigation participant.

## Coalition Data Sharing Across Risk Profiles

Different organizations operate at different risk levels. When sharing data across coalition boundaries: classify each partner's risk level, apply the strictest partner's policies, strip identifying information before sharing across risk tiers, maintain audit trails that themselves do not create identification vectors, and specify what happens to shared data when a partner is compromised or legally compelled.

## Whistleblower and Witness Protection

Whistleblower identities require the strongest protections. Implement: end-to-end encryption for all whistleblower communications, no server-side access to decrypted content, anonymous submission channels without account creation, zero-knowledge architectures where administrators cannot identify whistleblowers. Witness testimony records require consent verification before any display, anonymization by default, and explicit opt-in for identifiable presentation.

## Anonymization Requirements

Anonymization must be irreversible. AI-generated anonymization is often superficial — replacing names while leaving uniquely identifying attribute combinations (location + date + role + demographics). True anonymization requires k-anonymity at minimum: no individual distinguishable from at least k-1 others. Test anonymization by attempting re-identification with publicly available information.
