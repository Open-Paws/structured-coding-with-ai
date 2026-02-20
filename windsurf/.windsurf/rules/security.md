<!-- trigger: always_on -->
# Security Rules

Three adversaries: **state surveillance** (ag-gag statutes, warrants, subpoenas), **industry infiltration** (corporate investigators, social engineering), **AI model bias** (training data encoding industry framing, telemetry leaking investigation details).

## Zero-Retention APIs

NEVER send sensitive data to services that retain inputs. Verify retention policies contractually, not by assumption. Telemetry to third parties is a data exfiltration vector under adversarial legal discovery.

## Encrypted Storage with Plausible Deniability

All investigation data MUST use encrypted volumes. Design storage so sensitive data existence is deniable under device seizure — nested encrypted containers with innocuous outer layer.

## Supply Chain — Slopsquatting Defense

~20% of AI-recommended packages do not exist. Attackers register hallucinated names as malicious packages. Verify EVERY dependency exists in its registry with legitimate maintainers before installing.

## Input Validation

Assume adversarial input on every public surface. 45% of AI code contains OWASP Top 10 vulnerabilities. Validate at system boundaries — the barricade pattern.

## Ag-Gag Legal Exposure

Design every data flow for adversarial legal discovery. Strip metadata aggressively (timestamps, geolocation, device IDs). Audit logs must protect the identities they record.

## Device Seizure Preparation

Remote wipe capability. Auto-lock on suspicious conditions. No temp files with decrypted content, no swap files with sensitive state, no crash dumps with investigation data.

## Instruction File Integrity

The Rules File Backdoor uses hidden Unicode in instruction files to inject invisible directives. Review rule files for non-printable characters. Treat as security-critical artifacts.

## Self-Hosted Inference

Code paths handling investigation data or witness identities should use self-hosted inference, not cloud APIs. Model providers may comply with government data requests.

**WARNING:** Windsurf generates persistent memories about your codebase across sessions. Review and clear Windsurf memories regularly for projects involving sensitive investigation or witness data.
