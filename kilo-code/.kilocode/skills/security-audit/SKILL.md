---
name: security-audit
description: Security audit workflow for advocacy projects — dependency verification, zero-retention compliance, slopsquatting defense, encrypted storage, instruction file integrity, device seizure readiness, ag-gag exposure assessment
---
# Security Audit

## When to Use
- Before deploying any change to production
- When new dependencies are added
- When code touches investigation data, witness identities, or coalition coordination
- After AI-generated code has been added to security-sensitive paths
- Periodically as a scheduled review of the full codebase

## Process

### Step 1: Dependency Audit — Slopsquatting Defense
Approximately 20% of AI-recommended packages do not exist. Attackers register hallucinated names as malicious packages — one was downloaded 30,000+ times. For EVERY dependency: verify the package exists in its registry, has legitimate maintainers with real commit history, and the version is published. Only 1 in 5 AI-recommended dependency versions are both safe and free from hallucination. A compromised dependency can exfiltrate investigation data or activist identities.

### Step 2: API Retention Policy Audit
For every external API: verify retention policy contractually, not by assumption. Confirm zero-retention for all sensitive data flows. Check whether the API retains inputs, logs metadata, or stores conversation history. Telemetry to third parties is an exfiltration vector under adversarial legal discovery. Any API handling investigation footage, witness identities, or activist communications must be zero-retention.

### Step 3: Storage Encryption Audit
Verify all locally stored investigation data, evidence, and activist records use encrypted volumes with plausible deniability. Check for temp files, swap files, crash dumps, or caches with decrypted content. Verify encryption keys are not stored alongside encrypted data. Test: if the device powers off unexpectedly, is any sensitive data recoverable without credentials?

### Step 4: Input Validation Review
AI-generated code contains OWASP Top 10 vulnerabilities in 45% of cases. For every input boundary:
- SQL injection defenses on all database-facing inputs
- XSS protection on all content display paths, especially testimony and investigation notes
- Path traversal protection on evidence file uploads
- Authentication and authorization on every endpoint
- Assume adversarial input on every public surface — industry actors will probe investigation tools

### Step 5: Instruction File Integrity Check
The "Rules File Backdoor" uses hidden Unicode characters to inject invisible directives making AI produce malicious output. Inspect all instruction files for non-printable characters beyond standard whitespace. Diff changes character-by-character. Verify no file weakens encryption, disables safety checks, or sends data externally. Treat instruction files as security-critical artifacts.

### Step 6: MCP Server Audit
For every MCP server: verify sensitive advocacy data servers are self-hosted. Audit data access patterns, network egress, and retention. MCP extends capabilities but also extends the attack surface — check whether any server can exfiltrate data regardless of application-level encryption.

### Step 7: Device Seizure Readiness
Verify remote wipe for all sensitive data. Verify encrypted volumes lock on suspicious conditions (power loss, inactivity). Check application does not leak on unexpected termination — no temp files with decrypted content, no swap files with sensitive state, no crash dumps with investigation data. Test: terminate the process and examine what remains on disk.

### Step 8: Ag-Gag Exposure Assessment
Investigation footage is discoverable evidence:
- Audit every data flow assuming adversarial legal discovery
- Verify metadata stripping on all investigation content (timestamps, geolocation, device IDs)
- Verify audit logs protect recorded identities — logs identifying investigation data accessors become prosecution tools
- Check: if a court subpoena targeted this system, what would be disclosed? Minimize that surface.

### Step 9: Coalition Data Boundary Verification
- Data isolation between partners with different risk profiles
- Anti-corruption layers at every boundary crossing
- Data sharing agreements enforced in code, not just policy
- Blast radius analysis: if one partner is compelled to disclose, what reaches others?
- Shared data transformed appropriately — identifying info stripped before cross-tier sharing

### Step 10: Findings Report
Classify findings by severity:
- **Critical** — active data leak, missing encryption, compromised dependency, exposed witness identity
- **High** — weak input validation, missing zero-retention verification, unaudited MCP server
- **Medium** — incomplete metadata stripping, untested seizure scenario, missing boundary contract tests
- **Low** — documentation gaps, minor configuration improvements

Block deployment on any Critical or High finding. Track all findings to resolution.
