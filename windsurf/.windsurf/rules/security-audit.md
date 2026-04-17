<!-- trigger: manual -->
# Security Audit

## When to Use
Before deploying to production, when dependencies are added, when code touches investigation/witness/coalition data, after AI-generated code enters security paths, periodically for full codebase review.

## Step 1: Dependency Audit — Slopsquatting Defense
~20% of AI-recommended packages do not exist. Attackers register hallucinated names as malicious packages. For EVERY dependency: verify it exists in its registry, has legitimate maintainers with real history, and the version is published. In advocacy software, a compromised dependency exfiltrates investigation data or activist identities.

## Step 2: API Retention Policy Audit
For every external API: verify retention policy contractually. Confirm zero-retention for all sensitive flows. Check input retention, request metadata logging, conversation history storage. Any API handling investigation, witness, or activist data must be zero-retention.

## Step 3: Storage Encryption Audit
Verify encrypted volumes with plausible deniability for all investigation data. Check for temp files, swap files, crash dumps with decrypted content. Verify keys not stored alongside encrypted data. Test: if device powers off, is sensitive data recoverable without credentials?

## Step 4: Input Validation
AI code has OWASP vulnerabilities at 2.74x human rate. For every input boundary:
- SQL injection on all database inputs
- XSS on all display paths (especially testimony, investigation notes)
- Path traversal on evidence uploads
- Auth checks on every endpoint
- Assume adversarial input on all public surfaces

## Step 5: Instruction File Integrity
Rules File Backdoor: hidden Unicode in instruction files injects invisible directives. Inspect all rule files for non-printable characters. Diff character-by-character. Verify no file weakens encryption, disables safety, or exfiltrates data.

## Step 6: MCP Server Audit
Verify servers handling sensitive data are self-hosted. Audit data access, network egress, retention. MCP extends capabilities but also the attack surface.

## Step 7: Device Seizure Readiness
Remote wipe capability. Auto-lock on suspicious conditions. No temp files, swap files, or crash dumps with sensitive data. Test: terminate the process unexpectedly, examine what remains on disk.

## Step 8: Ag-Gag Exposure Assessment
Audit data flows for adversarial legal discovery. Verify metadata stripping (timestamps, geolocation, device IDs). Verify audit logs protect recorded identities. If subpoenaed, what gets disclosed? Minimize that surface.

## Step 9: Coalition Data Boundaries
Verify isolation between partners with different risk profiles. Anti-corruption layers at every boundary. Data sharing agreements enforced in code. If one partner is compelled, what is blast radius? Shared data transformed appropriately across tiers.

## Step 10: Findings Report
- **Critical** — active data leak, missing encryption, compromised dependency, exposed witness identity
- **High** — weak validation, missing zero-retention verification, unaudited MCP server
- **Medium** — incomplete metadata stripping, untested seizure scenario, missing contract tests
- **Low** — documentation gaps, minor config improvements

Block deployment on Critical or High. Track all findings to resolution.
