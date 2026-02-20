<!-- trigger: model_decision -->
# Privacy Rules

Privacy in advocacy software is not compliance — it is the difference between operational security and activist prosecution. Data that seems harmless in isolation becomes evidence under ag-gag statutes: participation timestamps, IP addresses, device fingerprints, and access patterns can identify investigators and witnesses.

## Data Minimization as Default

Collect the absolute minimum for each function. Every stored data point can be subpoenaed, seized, or leaked. Before adding any field: **if this data appeared in a court filing, who would it endanger?** If the answer is anyone, justify or eliminate it.

## Activist Identity Protection

Use pseudonymous identifiers internally. Never store legal names alongside action records. Separate authentication identity from operational identity — the login system must not be the system recording investigation participation. Compartmentalization prevents cascade: compromise of one system must not enable identification across systems.

## GDPR/CCPA as Floor, Not Ceiling

Right to deletion MUST be real deletion — not soft delete with a `deleted_at` flag. Irrecoverable from all layers: backups, replicas, search indices, analytics, logs. "Deleted" records surfacing in legal discovery destroy trust and endanger people.

Consent is ongoing, not a one-time checkbox. Re-consent on scope changes (new coalition partner, new feature, new data sharing). Withdrawal must be as easy as granting, with immediate effect.

## Coalition Data Sharing

Different organizations operate at different risk levels. When sharing across coalition boundaries:
1. Classify each partner's risk level
2. Apply the strictest handling rules of any partner
3. Strip identifying information before sharing across risk tiers
4. Design agreements specifying what happens when a partner is compromised or legally compelled
5. Audit trails must not themselves create identification vectors

## Whistleblower and Witness Protection

End-to-end encryption for all whistleblower communications. No server-side access to decrypted content. Anonymous submission without account creation. Zero-knowledge architectures where admins cannot identify whistleblowers. Witness testimony: consent verification before display, anonymization by default, explicit opt-in for identifiable presentation.

## Investigation Participant Records

Records of investigation participants are the most legally dangerous data. Maximize encryption, compartmentalization, and access restriction. Consider whether records need to exist at all. Design with plausible deniability: storage must not reveal whether it contains investigation records without correct credentials.

## Anonymization

Must be irreversible. AI anonymization is often superficial — replacing names while leaving identifying attribute combinations. Require k-anonymity at minimum. Test by attempting re-identification with publicly available information.
