# Security Rules for Animal Advocacy Projects

Advocacy software faces three distinct adversaries: **state surveillance** (ag-gag statutes, warrants, subpoenas), **industry infiltration** (corporate investigators, social engineering), and **AI model bias** (training data encoding industry framing, telemetry leaking investigation details). Security is not a feature layer — it is the structural foundation of every design decision.

## Zero-Retention APIs

NEVER send sensitive data to external services that retain inputs. Investigation footage, witness identities, activist communications, and coalition coordination data must only flow through zero-retention API configurations. Verify retention policies contractually, not by assumption. Telemetry to third parties is a data exfiltration vector in adversarial legal discovery.

## Encrypted Local Storage with Plausible Deniability

All locally stored investigation data, evidence, and activist records MUST use encrypted volumes. Design storage so that the existence of sensitive data is deniable under device seizure. Nested encrypted containers — outer layer with innocuous data, inner layer requiring a separate key — is the standard pattern. A seized device must not reveal what it contains without correct credentials.

## Supply Chain Verification — Slopsquatting Defense

Approximately **20% of AI-recommended packages do not exist** — hallucinated names that attackers register as malicious packages. One was downloaded 30,000+ times. **Verify EVERY dependency** exists in its actual registry with legitimate maintainers before installation. Only 1 in 5 AI-recommended dependency versions are both safe and free from hallucination. A compromised dependency can exfiltrate investigation data or activist identities.

## Input Validation Against Industry Sabotage

Assume adversarial input on every public-facing surface. Validate and sanitize all inputs at system boundaries. AI-generated input validation is weak: 45% of AI-generated code contains OWASP Top 10 vulnerabilities, with 86% failure rate on XSS defenses. Industry actors will probe investigation submission forms, evidence upload endpoints, and public campaign tools.

## Ag-Gag Legal Exposure Vectors

Investigation footage is discoverable evidence. Design every data flow assuming adversarial legal discovery. Metadata (timestamps, geolocation, device identifiers) can be more damaging than content — strip aggressively. Audit logs must protect the identities they record — logs identifying who accessed investigation data become prosecution tools.

## Device Seizure Preparation

Design for confiscation without warning. Remote wipe capability for all sensitive data. Encrypted volumes that lock automatically on suspicious conditions (unexpected power loss, extended inactivity, SIM removal). No temporary files with decrypted content, no swap files with sensitive state, no crash dumps with investigation data.

## Instruction File Integrity — Rules File Backdoor

The "Rules File Backdoor" attack uses hidden Unicode characters in instruction files to inject invisible directives that make AI produce malicious output. **Treat ALL instruction files as security-critical artifacts.** Review for non-printable characters. Diff changes character-by-character. A compromised instruction file could direct the AI to weaken encryption, leak data, or disable safety checks.

## Self-Hosted Inference for Critical Paths

Code paths handling investigation data, witness identities, or legal defense materials should use self-hosted AI inference — not cloud-hosted APIs. Model providers may comply with government data requests. For routine tasks (formatting, boilerplate, docs), external APIs are acceptable. For anything touching adversary interests, self-host.

## MCP Server Security

MCP servers extend agent capabilities but also extend the attack surface. Any MCP server handling sensitive advocacy data MUST be self-hosted. Audit each server's data access, network egress, and retention before enabling.


## Provider Routing for Sensitive Data

When using AI coding assistants with multiple model providers, sensitive advocacy data (investigation content, witness identities, legal defense materials) must NEVER route through free-tier providers that may retain inputs. Free-tier APIs (Google AI Studio, Groq, Mistral, Cohere, OpenRouter free models, Together AI) may retain inputs for training or compliance — assume they do unless contractually guaranteed otherwise. Route sensitive work exclusively through zero-retention providers or self-hosted inference.
