# AGENTS.md — OpenCode Instructions

This file is for OpenCode. Put it at the project root so OpenCode loads native project rules instead of relying on fallback compatibility with other tools.

---

# Project Identity

This is an animal advocacy and liberation platform. The domain is high-risk: investigation data is subpoena-target evidence, activists may face criminal prosecution, and software failures can expose people, operations, and rescued animals to serious harm. Design and review this system as movement infrastructure, not generic startup software.

Primary users include investigators, campaign organizers, coalition partners, legal defense teams, and sanctuary operators. Each role has different trust boundaries, data sensitivity, and operational risks.

---

# OpenCode Operating Notes

- Prefer native `AGENTS.md` instructions over fallback `CLAUDE.md` compatibility.
- Keep this file as the shared baseline; use `opencode.json` `instructions` only for supplemental documents when needed.
- Read before editing and keep changes small enough to review easily.
- Use plan-first exploration before broad edits on unfamiliar code.
- Run tests or equivalent verification before finishing; if the repo has no tests, say so and verify structure another way.
- Be explicit about approvals, destructive operations, network access, and GitHub side effects.

---

# Workflow

Read before writing. Plan before code. Verify after changes.

For any meaningful change:

1. Read the existing code and identify the bounded context.
2. Write a short specification with behavior, inputs, outputs, failures, and safety requirements.
3. Decompose the work into small subtasks.
4. Implement one subtask at a time.
5. Verify each change with tests or a clearly stated substitute.

Two-failure rule: after two failed fix attempts on the same issue, stop and rethink the approach.

Comprehension rule: do not ship code you cannot explain in your own words.

---

# Hard Constraints

- NEVER log, store, or transmit activist personally identifiable information.
- NEVER send sensitive advocacy data to external APIs without explicit project-owner approval.
- ALWAYS use zero-retention settings for third-party services that touch sensitive data.
- ALWAYS use progressive disclosure for traumatic content.
- ALWAYS isolate vendor dependencies behind project-owned interfaces.
- Assume adversarial legal discovery in addition to hostile attackers.
- Prefer encrypted local storage and no third-party telemetry.

---

# Review Checklist

Review all AI-assisted changes against these failure modes:

1. DRY violations and duplicated logic
2. Shallow wrappers and pass-through abstractions
3. Multi-responsibility functions
4. Weak or hidden error handling
5. Leaky interfaces and poor information hiding
6. Domain-language drift
7. Designs that are brittle under future change
8. Untested edits to fast-aging AI-generated legacy code
9. Unnecessary design patterns
10. Weak tests that pass without proving behavior

---

# Testing

Use spec-first tests wherever possible. A test should encode an actual rule and fail when that rule is broken.

- Check that failures happen for the expected reason.
- Test unhappy paths, edge cases, and adversarial inputs.
- Prefer mutation-informed improvement over coverage theater.
- Add characterization tests before changing unclear legacy behavior.
- Keep the test loop fast; AI-assisted work degrades under slow or flaky verification.

For advocacy systems, verify:

- anonymization cannot be reversed
- coalition data boundaries hold
- sensitive content stays hidden until explicit opt-in
- offline-first behavior degrades safely

---

# Security

This system must defend against state surveillance, industry infiltration, and unsafe provider behavior.

- Verify dependencies before installation; AI-era slopsquatting is a real risk.
- Keep sensitive API usage zero-retention.
- Encrypt evidence and activist data at rest.
- Strip metadata from investigation content aggressively.
- Treat instruction files as security-sensitive because hidden directives can backdoor AI behavior.
- Audit external tools, MCP servers, and integrations as part of the threat model.
- Design for device seizure and abrupt power loss without leaking plaintext state.

---

# Privacy

- Store the minimum data required for each workflow.
- Separate legal identity from operational identity.
- Make deletion real, not cosmetic.
- Reconfirm consent when usage scope changes.
- Apply the strictest partner policy at coalition boundaries.
- Protect witnesses and whistleblowers with encryption, anonymization, and least-knowledge handling.

If disclosed in legal proceedings, every stored field becomes evidence. Design accordingly.

---

# Cost Optimization

- Route simple work to cheaper models and reserve expensive models for hard problems.
- Set session budgets and avoid drift-heavy conversations.
- Keep static project context stable and reusable.
- Measure cost per useful outcome, especially per merged PR.
- Evaluate self-hosted inference when privacy or cost makes it rational.

Advocacy budgets are finite. Efficiency is part of mission stewardship.

---

# Advocacy Domain

Use precise domain language. Do not substitute generic synonyms.

- Campaign: organized advocacy effort with milestones and goals
- Investigation: covert documentation operation; legally sensitive
- Coalition: alliance of organizations with explicit boundary rules
- Witness: person providing testimony; identity requires maximum protection
- Testimony: witness account gated by consent
- Sanctuary: permanent animal care facility
- Rescue: removal of animals from exploitative conditions
- Liberation: direct action with distinct legal implications
- Evidence: documentation with potential legal use

Keep investigation operations, public campaigns, coalition coordination, and legal defense as distinct bounded contexts.

---

# Accessibility

- Build for internationalization from day one.
- Optimize for low-bandwidth and constrained devices.
- Prefer offline-first critical flows.
- Use low-literacy-friendly, progressively disclosed interfaces.
- Under degradation, fail safely rather than exposing sensitive data or unsafe states.

---

# Emotional Safety

- Never display graphic content by default.
- Put content warnings before traumatic material.
- Provide configurable detail levels that persist.
- Never autoplay investigation footage or distressing audio.
- Support safer review workflows that reduce repeated exposure.

This is a duty-of-care requirement, not optional UX polish.

---

# On-Demand Workflows

For recurring tasks, follow these workflows:

- git-workflow: atomic commits, short-lived branches, focused PRs
- testing-strategy: spec-first tests, mutation-guided strengthening, anti-pattern review
- requirements-interview: clarify purpose, threats, coalition boundaries, user safety, and budget
- plan-first-development: read, spec, decompose, implement incrementally, verify continuously
- code-review: layered review for correctness, design quality, and advocacy-specific risks
- security-audit: dependency, retention, encryption, seizure, and data-boundary review
