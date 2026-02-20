# Project Context — Architecture and Threat Model

## Threat Model

Three distinct adversaries, each requiring different countermeasures:

**State Surveillance** — Law enforcement using ag-gag statutes, warrants, and subpoenas to prosecute investigators and seize evidence. Countermeasures: zero-retention APIs, encrypted storage with plausible deniability, metadata stripping, device seizure preparation, remote wipe capability.

**Industry Infiltration** — Corporate investigators posing as volunteers, social engineering attacks against coalition members, probing of investigation submission tools. Countermeasures: input validation on every public surface, compartmentalized access, monitoring for anomalous behavior patterns, coalition data isolation.

**AI Model Bias** — Training data encoding industry framing ("livestock" instead of "farmed animals"), models refusing to assist with certain advocacy operations, telemetry leaking investigation details to model providers. Countermeasures: self-hosted inference for critical paths, explicit domain language enforcement, zero-retention API configurations, instruction file integrity checks.

## Technology Approach

Stack-agnostic principles. Students choose their own technology. These rules apply regardless of language or framework:

- **Offline-first architecture** — design for disconnected operation as default, not exception
- **Vendor lock-in avoidance** — abstract all model and vendor dependencies behind project-owned interfaces; lock-in is a movement risk, not just a technical preference
- **Self-hosted fallbacks** — critical code paths handling investigation data or witness identities must have self-hosted inference capability
- **Zero-retention by default** — no sensitive data to external services that retain inputs
- **Encrypted local storage** — with plausible deniability under device seizure
- **Progressive disclosure** — traumatic content behind intentional user interactions, never auto-displayed

## Bounded Contexts

Four distinct domains. Different models, different rules, different security requirements. Do NOT merge them. Data crossing boundaries MUST go through anti-corruption layers.

**Investigation Operations** — Covert data collection, evidence management, investigator identity protection, chain of custody. Highest security classification. Data never flows outward without explicit declassification. Entities: Investigator, Operation, Evidence, Facility, ChainOfCustody.

**Public Campaigns** — Public-facing advocacy, supporter engagement, media relations, petition management. Lower security but high visibility. An "activist" in a campaign is fundamentally different from an "investigator" in an undercover operation — different data model, different risk profile, different access controls. Entities: Campaign, Supporter, Action, Petition, MediaAsset.

**Coalition Coordination** — Multi-organization planning, shared resources, joint strategy. Data crosses organizational boundaries and must be governed by the strictest partner's policies. Entities: Coalition, PartnerOrganization, SharedResource, JointAction, DataSharingAgreement.

**Legal Defense** — Case management, attorney-client privileged communications, court filings. Attorney-client privilege imposes its own data handling requirements that override other policies. Entities: Case, Attorney, Defendant, Filing, PrivilegedCommunication.

## Key Design Decisions

- Compartmentalization over convenience — compromise of one subsystem must not cascade
- Data minimization as default — every stored data point is a subpoena target
- Real deletion, not soft delete — "deleted" records in legal discovery endanger people
- Coalition data governed by strictest partner's policies
- Consent as ongoing process, not one-time checkbox
- Security is structural foundation, not feature layer

## AI-Assisted Development Rules

- Plan before code — read, plan, code, verify
- Two-failure rule: after two failed fixes, restart with better prompt
- Never duplicate existing code — search first (AI clones at 4x normal rate)
- Every PR with AI-generated code tagged AI-Assisted
- Comprehension check: explain AI-generated code before committing
