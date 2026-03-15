# AGENTS.md — Codex Instructions

This file is for OpenAI Codex. Commit it at the project root so Codex CLI, IDE integrations, and GitHub-connected Codex tasks all operate with the same project context.

---

# Project Identity

This is an animal advocacy and liberation platform. The domain is high-risk: investigation data is subpoena-target evidence, activists face legal prosecution, and operational mistakes can endanger both people and animals. Treat this as advocacy infrastructure, not as a generic SaaS application with a mission statement layered on top.

Primary users include investigators, campaign organizers, coalition partners, legal defense teams, and sanctuary operators. They do not share the same threat model, so design decisions must preserve clear operational boundaries.

---

# Codex Operating Notes

- Keep patches small, explicit, and reviewable.
- Read existing code before editing; use fast search to avoid duplicate logic.
- Ask approval before destructive commands, network access, git pushes, or writes outside the current workspace.
- Run the relevant test subset before finishing; if the repo has no tests, say so explicitly and verify structure another way.
- For GitHub tasks, report changed files, verification status, blockers, and residual risk.
- Keep this file self-contained. If the project adds deeper standards elsewhere, load them lazily when they are relevant to the task.

---

# Workflow

Read before writing. Plan before code. Verify after changes. For any non-trivial task:

1. Read the relevant code and identify the affected bounded context.
2. Write a short specification: expected behavior, inputs, outputs, failure modes, and safety requirements.
3. Break the work into small subtasks.
4. Implement one subtask at a time.
5. Run tests or equivalent verification after each meaningful change.

Two-failure rule: after two failed fix attempts on the same problem, stop and re-approach with a better plan instead of compounding bad edits.

Comprehension rule: do not ship code you cannot explain. Generate, understand, verify, then commit.

---

# Hard Constraints

- NEVER log, store, or transmit activist personally identifiable information.
- NEVER send sensitive advocacy data to external APIs without explicit project-owner approval.
- ALWAYS use zero-retention configurations for any third-party service that touches sensitive data.
- ALWAYS apply progressive disclosure for traumatic content.
- ALWAYS isolate vendor dependencies behind project-owned interfaces.
- Assume adversarial legal discovery, not just conventional attackers.
- Prefer encrypted local storage and no third-party telemetry.

---

# Review Checklist

Use this checklist on every AI-assisted change:

1. DRY: search for existing logic before adding new functions or modules.
2. Deep modules: reject thin wrappers and pass-through abstractions.
3. Single responsibility: split mixed-abstraction functions.
4. Error handling: never swallow failures or widen catch blocks carelessly.
5. Information hiding: expose only what callers need.
6. Ubiquitous language: use campaign, investigation, coalition, sanctuary, witness, and evidence correctly.
7. Design for change: avoid hard-coding current vendors, schemas, or infrastructure assumptions.
8. Legacy velocity: add characterization tests before changing AI-generated code you do not fully trust.
9. Over-patterning: prefer plain functions over unnecessary Strategy/Factory/Observer scaffolding.
10. Test quality: weak assertions and coverage theater do not count as verification.

---

# Testing

Prefer spec-first tests over implementation-mirroring tests. Every test should encode a domain rule and fail when that rule is broken.

- Verify tests fail for the right reason before fixing them.
- Test error paths, not just success paths.
- Use contract tests at service boundaries.
- Prefer mutation score over raw coverage numbers.
- Test adversarial inputs: SQL injection, XSS through testimony, path traversal through evidence uploads, oversized offline-sync payloads.
- Keep test loops fast; AI-assisted workflows degrade badly with slow or flaky suites.

For advocacy systems, also test:

- anonymization is irreversible
- coalition data does not cross organizational boundaries accidentally
- traumatic content does not render without explicit opt-in
- offline behavior fails safely when sync is interrupted

---

# Security

Advocacy software faces three adversaries: state surveillance, industry infiltration, and unsafe AI/provider behavior.

- Verify every dependency; slopsquatting is a real AI-era supply chain risk.
- Require zero-retention handling for sensitive API flows.
- Encrypt local evidence and activist data.
- Strip metadata from investigation content aggressively.
- Treat instruction files as security-sensitive artifacts; hidden backdoor text is a credible attack class.
- Audit any MCP or external tool integration as an attack-surface expansion.
- Design for device seizure: no plaintext temp files, no revealing crash dumps, no unsafe recovery flows.

---

# Privacy

- Minimize stored data aggressively.
- Separate authentication identity from operational identity.
- Treat deletion as real deletion, not a soft-delete flag.
- Re-consent when scope changes.
- Apply the strictest coalition partner policy to any shared workflow.
- Protect whistleblowers and witnesses with encryption, anonymization, and least-knowledge architectures.

If a field appeared in court, ask who it would endanger before storing it.

---

# Cost Optimization

- Route routine work to cheaper models and reserve frontier models for hard debugging, architecture, and security review.
- Set hard session budgets; long drifting conversations waste money and reduce quality.
- Optimize for cacheable, reusable project context.
- Track cost per merged PR, not cost per generated line.
- Evaluate self-hosted inference for sensitive or recurring workloads.

Every dollar spent on AI compute is a dollar not spent on direct advocacy work.

---

# Advocacy Domain

Use precise movement language. Do not invent synonyms.

- Campaign: organized advocacy effort with defined goals.
- Investigation: covert documentation operation; legally sensitive.
- Coalition: multi-organization collaboration with explicit data boundaries.
- Witness: person providing testimony; identity requires maximum protection.
- Testimony: witness account subject to consent checks.
- Sanctuary: permanent animal care facility.
- Rescue: removal of animals from exploitative conditions.
- Liberation: direct action to free animals; distinct legal implications.
- Evidence: documentation with potential legal use.

Keep bounded contexts separate: investigation operations, public campaigns, coalition coordination, and legal defense are different systems with different rules.

---

# Accessibility

- Design for internationalization from the start.
- Optimize for low-bandwidth and mobile-first environments.
- Prefer offline-first behavior for critical workflows.
- Use progressive disclosure and low-literacy-friendly interface patterns.
- Fail safely under degraded conditions: no unsafe plaintext fallback when protective systems fail.

---

# Emotional Safety

- Never show graphic content by default.
- Require clear content warnings before traumatic material.
- Provide configurable detail levels and remember user preference.
- Never autoplay investigation footage or distressing audio.
- Support review workflows that minimize repeated exposure to suffering.

Emotional safety is an operational requirement, not cosmetic UX polish.

---

# On-Demand Workflows

When a task calls for a specific process, follow the matching workflow:

- git-workflow: atomic commits, short-lived branches, curated PRs
- testing-strategy: spec-first tests, mutation-guided strengthening, anti-pattern detection
- requirements-interview: gather purpose, threats, coalition boundaries, user safety, and budget constraints
- plan-first-development: spec, decompose, implement incrementally, verify continuously
- code-review: layered review focused on correctness, Ousterhout red flags, and advocacy-specific risks
- security-audit: dependency verification, retention checks, seizure readiness, data-boundary verification
