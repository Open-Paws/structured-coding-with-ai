# AGENTS.md — Universal AI Coding Instructions

This file contains project-level instructions for any AI coding assistant working on this codebase. It is a vendor-neutral standard: if your tool reads AGENTS.md, these rules apply. If your tool uses a different instruction format, this file serves as the authoritative reference for project conventions. Every instruction here is self-contained — no external documents are referenced or required.

---

# Project Identity

This is an **animal advocacy and liberation platform**. Software in this domain is high-risk: investigation data is subpoena-target evidence under ag-gag statutes, activists face criminal prosecution for documenting animal exploitation, and system compromise endangers human lives and animal welfare operations. This is not a generic web application with an advocacy theme — the domain's legal, ethical, and operational constraints are structural, affecting every design decision from data modeling to error handling to deployment architecture.

The platform serves investigators documenting factory farm and slaughterhouse conditions, campaign organizers coordinating public advocacy, coalition partners sharing intelligence across organizational boundaries, legal defense teams managing privileged communications, and sanctuary operators tracking rescued animals. Each user group faces different threats and operates under different constraints.

---

# Workflow

**Read before writing.** Before making any change, read the existing code relevant to the task. Understand the current structure, naming conventions, existing utilities, and architectural patterns. AI agents generate duplicate functions and violate DRY at 4x the normal rate because they lack full codebase awareness. Searching first prevents this.

**Plan before code.** The workflow for every significant change is: read existing code, write a specification, decompose into subtasks, implement one subtask at a time, test each before moving to the next. Never start coding with a vague intent — define what the code should do, what inputs it accepts, what outputs it produces, what error conditions exist, and what security or safety properties it must maintain.

**Verify after.** Run the relevant test subset after every change. Every commit must leave the codebase in a passing state. For advocacy code handling investigation or evidence data, also verify that no sensitive data has leaked into test output, logs, or error messages.

**Two-failure rule.** After two failed fix attempts on the same problem, stop and re-approach with a better strategy rather than compounding errors. Repeated failed fixes degrade context quality and produce increasingly tangled code.

**Comprehension check.** After AI generates code, the developer must be able to explain what it does in their own words before committing. AI-assisted developers score 17 percentage points lower on comprehension tests (Anthropic, 2026). Use the **generation-then-comprehension** pattern: generate code, then immediately ask the AI to explain it, then verify your understanding matches. This preserves learning while leveraging AI speed. If you cannot explain the code, do not commit it.

---

# Constraints

- **NEVER** log, store, or transmit activist personally identifiable information
- **NEVER** send sensitive data to external APIs without explicit project-owner approval
- **ALWAYS** use zero-retention configurations for any third-party service
- **ALWAYS** apply progressive disclosure for traumatic content (investigation footage, slaughter documentation)
- **ALWAYS** abstract vendor dependencies behind project-owned interfaces — vendor lock-in is a movement risk for nonprofit organizations
- Assume adversarial legal discovery: investigation data is court-subpoena material, not just hacker targets
- Encrypted local storage with plausible deniability; no telemetry to third parties

---

# Design Principles — AI-Violated Review Checklist

These ten principles are ranked by frequency and severity of violation in AI-generated code. Use this as a review checklist for every AI-generated change.

## 1. DRY — Don't Repeat Yourself
AI duplicates existing code because it lacks full codebase awareness. GitClear found 4x more code cloning in AI-assisted repositories. Before writing any new function, utility, or module, search the codebase for existing implementations. List known shared modules in project documentation so the AI uses them instead of reinventing them.

## 2. Deep Modules Over Shallow Wrappers
AI generates thin wrappers, pass-through methods, and classes that just delegate to another class. This is the single most common structural flaw in AI-generated code (Ousterhout). A good module has a simple interface and powerful functionality. If a class or module's interface is as complex as its implementation, the AI has produced a shallow abstraction. Reject pass-through layers that add surface area without hiding complexity.

## 3. Single Responsibility
AI produces multi-responsibility functions by default. "Do one thing" and "one level of abstraction per function" (Clean Code) are the principles most commonly violated. When reviewing AI output, check function length and responsibility count first — these are the fastest quality signals. Split multi-responsibility functions immediately.

## 4. Error Handling
AI suppresses errors, catches too broadly, and removes safety checks. IEEE Spectrum found newer models increasingly generate code that silently swallows failures and removes safety validation. In advocacy software, silent failure means lost evidence, exposed activists, or traumatic content displayed without safeguards. Review every try/catch block in AI-generated code. Never accept catch-all handlers or empty catch blocks.

## 5. Information Hiding
AI leaks implementation details across module boundaries. Expose only what callers need. If the interface is as complex as the implementation, the abstraction is shallow. Configuration parameters that push complexity up to users (instead of providing intelligent defaults) are a specific violation to watch for.

## 6. Ubiquitous Language
AI introduces its own terminology instead of domain language. If your team calls it a "campaign" and the AI generates code calling it a "project," you have language drift. In advocacy software, language drift causes miscommunication across coalition partners who rely on precise terminology and obscures the legal distinctions between different operations. Define domain terms explicitly (see Advocacy Domain section below) and enforce them.

## 7. Design for Change
AI optimizes for "works now" over "works later." Advocacy tools must outlast any single campaign or legal proceeding. Insist on abstraction layers, loose coupling, and interfaces that allow implementations to change without cascading modifications. AI-generated code that hardcodes assumptions about current infrastructure, current vendors, or current data formats will need expensive rewrites.

## 8. Legacy Code Velocity
AI-generated code becomes legacy code faster than human code. GitClear projects code churn — code discarded within two weeks — will double in AI-assisted repositories. Feathers' techniques (characterization tests, sprout method, wrap method) become relevant after months of AI-assisted development, not years of neglect. Write characterization tests before modifying AI-generated modules. Apply "cover before you change."

## 9. Over-Patterning
AI applies design patterns aggressively — Strategy, Factory, Observer — where simpler solutions suffice. The Gang of Four warned "don't force patterns." A function and an if-statement should not become an AbstractStrategyFactoryProvider. Review AI output for unnecessary pattern application and simplify.

## 10. Test Quality
AI generates tests that look thorough but verify nothing. Tautological assertions — tests that assert the output equals the output — are the most dangerous pattern. Mutation testing is the countermeasure: if changing `+` to `-` in the implementation leaves the test green, the test is weak. Track mutation score as the primary quality metric, not coverage percentage.

---

# Testing

Testing is the keystone of AI-assisted advocacy development. Without tests, AI agents drift silently — and in advocacy software, silent drift means lost evidence, exposed activists, or traumatic content displayed without safeguards.

## Assertion Quality — The Non-Negotiable
NEVER accept tautological assertions. Ask three questions of every AI-generated test: (1) Does this test fail if the code is wrong? If you break the implementation and the test still passes, it is worthless. (2) Does the assertion encode a domain rule? If you cannot name the rule being verified, it is a snapshot, not a test. (3) Would mutation testing kill this? If changing an operator in the implementation leaves the test green, the assertion is weak. Quality metric: mutation score over coverage percentage. A suite with 90% coverage and 40% mutation score is a false sense of security.

## Spec-First Test Generation
ALWAYS prefer generating tests from specifications or acceptance criteria before writing implementation. Tests generated from existing implementation tend to mirror the code rather than the intent, producing circular validation. Write the test first. Verify it fails for the right reason. Then make it pass.

## Property-Based Testing
Use property-based testing to verify invariants across random inputs. Critical invariants in advocacy software: anonymization must be irreversible, encryption must not leak plaintext length, coalition data boundaries must hold under arbitrary input combinations.

## Test Error Paths Explicitly
AI-generated tests overwhelmingly cover happy paths. In advocacy software, the error paths are where people get hurt. Test: error propagation, cleanup on failure, meaningful error messages, graceful degradation under hostile conditions. Test what happens when the network drops during evidence upload. Test what happens when storage is seized mid-write.

## Contract Tests at Service Boundaries
AI hallucinates API contracts — approximately 20% of AI-recommended packages do not exist. At every service boundary, especially coalition cross-organization APIs, use consumer-driven contract tests. Do not trust AI-generated API client code without contract verification.

## Test Infrastructure
Fast test execution is non-negotiable. AI agents run tests in tight loops — a 10-minute suite across 15 iterations burns 2.5 hours. Invest in parallel execution, test isolation, and selective test running. Flaky tests poison the AI feedback loop — agents cannot distinguish flaky failures from real ones. Track and eliminate flaky tests aggressively. Maintain a test-to-code ratio of 1:1 or higher.

## Five Testing Anti-Patterns

1. **Snapshot trap** — AI generates tests that snapshot current output and assert against it. These tests pass today and break on any change, including correct changes. They verify nothing about correctness. Use snapshots only for visual regression of UI rendering.

2. **Mock everything** — AI loves mocking because it makes tests pass easily. Over-mocked tests verify that mocks behave as expected, not that real code works. Mock only at system boundaries: external APIs, databases, file systems. Do not mock your own code unless testing interaction patterns.

3. **Happy path only** — AI-generated tests overwhelmingly test the success path. Explicitly request error path, boundary condition, and adversarial input tests. A test suite with only happy path tests misses the bugs that matter.

4. **Test-after-commit** — Writing tests after the code is committed defeats the feedback loop. Tests must be present during development, not after. The write-test-fix loop requires tests during implementation.

5. **Coverage theater** — Chasing coverage numbers with meaningless tests. A line of code "covered" by a test with no assertions is not tested. Coverage tells you what is NOT tested (uncovered code) but cannot tell you what is well-tested.

## Adversarial Input Testing
Test inputs crafted to exploit advocacy-specific vulnerabilities: SQL injection through investigation search fields, XSS through witness testimony display, path traversal through evidence file uploads, oversized payloads designed to crash offline-first sync.

---

# Security

Advocacy software faces **three distinct adversaries**, each requiring different countermeasures:

1. **State surveillance** — law enforcement using ag-gag statutes, warrants, and subpoenas to prosecute investigators and seize evidence
2. **Industry infiltration** — corporate investigators posing as volunteers, social engineering attacks against coalition members, sabotage of advocacy tools
3. **AI model bias** — training data encoding industry framing, models refusing to assist with certain advocacy operations, models leaking investigation details through telemetry

Security is not a feature layer — it is the structural foundation of every design decision.

## Zero-Retention APIs
NEVER send sensitive data to external services that retain inputs. Investigation footage, witness identities, activist communications, and coalition coordination data must only flow through zero-retention API configurations. Verify retention policies contractually, not by assumption. Telemetry to third parties is a data exfiltration vector under adversarial legal discovery.

## Encrypted Local Storage with Plausible Deniability
All locally stored investigation data, evidence, and activist records MUST use encrypted volumes. Design storage so that the existence of sensitive data is deniable under device seizure — nested encrypted containers where the outer layer contains innocuous data and the inner layer requires a separate key. A seized device must not reveal what it contains without the correct credentials.

## Supply Chain Verification — Slopsquatting Defense
**Slopsquatting** is a novel supply chain attack: approximately 20% of AI-recommended packages do not exist — they are hallucinated names. Attackers monitor these hallucinated names and register them as real packages containing malicious code. One such package was downloaded 30,000+ times in weeks. Only 1 in 5 AI-recommended dependency versions are both safe and free from hallucination. **Verify EVERY dependency** exists in its actual registry and has legitimate maintainers before installation. In advocacy software, a compromised dependency can exfiltrate investigation data or activist identities.

## Input Validation Against Industry Sabotage
Assume adversarial input on every public-facing surface. AI-generated code contains OWASP Top 10 vulnerabilities in 45% of cases — 2.74x more than human code, with an 86% failure rate on cross-site scripting defenses. Validate and sanitize all inputs at system boundaries.

## Ag-Gag Legal Exposure Vectors
Investigation footage is discoverable evidence under legal proceedings. Design every data flow assuming adversarial legal discovery. Metadata (timestamps, geolocation, device identifiers) can be more damaging than content — strip metadata aggressively. Audit logging must protect the identities it records: logs that identify who accessed investigation data become prosecution tools.

## Device Seizure Preparation
Design for the scenario where devices are confiscated without warning. Remote wipe capability for all sensitive data. Encrypted volumes that lock automatically on suspicious conditions (unexpected power loss, extended inactivity). The application must not leak data on unexpected termination — no temporary files with decrypted content, no swap files containing sensitive state, no crash dumps with investigation data.

## Instruction File Integrity — Rules File Backdoor
The **Rules File Backdoor** attack uses hidden Unicode characters in AI instruction files to inject invisible directives that make AI agents produce malicious output. Treat ALL instruction files (including this one) as security-critical artifacts. Review them for non-printable characters. Diff instruction file changes character-by-character. In advocacy projects, a compromised instruction file could direct the AI to weaken encryption, leak data to external endpoints, or disable safety checks.

## Provider Routing for Sensitive Data
When using AI coding assistants with multiple model providers, sensitive advocacy data (investigation content, witness identities, legal defense materials) must NEVER route through free-tier providers that may retain inputs. Free-tier APIs (Google AI Studio, Groq, Mistral, Cohere, OpenRouter free models, Together AI) may retain inputs for training or compliance — assume they do unless contractually guaranteed otherwise. Route sensitive work exclusively through zero-retention providers or self-hosted inference.

## Self-Hosted Inference for Critical Paths
Any code path handling investigation data, witness identities, or legal defense materials should use self-hosted AI inference — not cloud-hosted APIs. Model providers may comply with government data requests. For routine development tasks, external APIs are acceptable. For anything touching the three adversaries' interests, self-host.

---

# Privacy

Privacy in advocacy software is the difference between operational security and activist prosecution. Data that seems harmless in isolation becomes evidence under ag-gag statutes: participation timestamps, IP addresses, device fingerprints, and access patterns can identify investigators, witnesses, and rescue coordinators.

## Data Minimization as Default
Collect the absolute minimum data required for each function. Before adding any field to any data model, ask: if this data appeared in a court filing, who would it endanger? If the answer is anyone, justify its existence or eliminate it.

## Activist Identity Protection
Use pseudonymous identifiers internally. Never store legal names alongside action records. Separate authentication identity from operational identity — the system that verifies login credentials must not be the system that records who participated in which investigation. Compartmentalization is the structural principle.

## GDPR/CCPA as Floor, Not Ceiling
Right to deletion MUST be real deletion — not soft delete with a `deleted_at` flag. When an activist requests erasure, their data must be irrecoverable from all storage layers including backups, replicas, search indices, analytics pipelines, and log aggregation systems. Soft delete in advocacy software is a liability: "deleted" records surfacing in legal discovery destroy trust and endanger people.

## Consent as Ongoing Process
Consent is not a one-time checkbox. Implement re-consent workflows for scope changes. Withdrawal of consent must be as easy as granting it, with immediate effect. Participation in a public campaign does not imply consent to be recorded as an investigation participant.

## Coalition Data Sharing Across Risk Profiles
Different advocacy organizations operate at different risk levels. A grassroots direct action group, a legal defense fund, and a public education nonprofit have fundamentally different threat models. When sharing data across coalition boundaries: classify each partner's risk level, apply the strictest handling rules of any partner in the exchange, strip identifying information before sharing across risk tiers, and design data sharing agreements that specify what happens when a partner is compromised or legally compelled to disclose.

## Whistleblower and Witness Protection
Implement end-to-end encryption for all whistleblower communications. No server-side access to decrypted content. Anonymous submission channels that do not require account creation. Zero-knowledge architectures where even system administrators cannot identify whistleblowers. Witness testimony records require consent verification before display, anonymization by default, and explicit opt-in for identifiable presentation. Anonymization must be irreversible — AI-generated anonymization is often superficial, replacing names while leaving uniquely identifying attribute combinations.

---

# Cost Optimization

Advocacy organizations operate on nonprofit budgets. Every dollar spent on AI compute is a dollar not spent on investigations, legal defense, or sanctuary operations. Vendor lock-in is a movement risk: a nonprofit locked to a single AI provider faces existential budget exposure when prices change.

## Model Routing
Route tasks to the cheapest model capable of handling them well. Use cheaper, faster models for: test generation, boilerplate, formatting, simple refactoring, documentation. Use mid-tier models for: debugging, multi-file changes, code review. Reserve frontier models for: hard architectural problems, complex debugging, security-critical code review.

## Token Budget Discipline
Set hard budget limits per session and per day. Cap conversation duration to prevent indefinite token consumption. Track actual spend against budget weekly. A single runaway agent conversation can consume a week's compute budget.

## Budget Allocation
For resource-constrained advocacy teams: **40% implementation**, **30% testing** (generation plus execution loops), **20% review and debugging**, **10% documentation**. Track cost per merged PR as the key efficiency metric, not cost per generated line.

## Prompt Cache Optimization
Place static content first in prompts to maximize cache hit rates — target 80%+ cache hits. Instruction files, project context, and architectural descriptions are static content that should appear before dynamic task-specific content.

## Self-Hosted Inference Economics
For teams processing sensitive data regularly, self-hosted open-source inference may be cheaper than cloud APIs at scale while also satisfying security requirements. Calculate the break-even point. For many advocacy organizations, a modest GPU allocation running an open model costs less than heavy API usage and eliminates data retention concerns.

## Efficiency Practices
Run the smallest relevant test subset first during development; full suite on commit. Start sessions fresh rather than extending degraded long conversations. Break work into subtasks that complete within half the context window. Compact conversations at approximately 50% context usage.

---

# Advocacy Domain — Ubiquitous Language and Bounded Contexts

AI agents drift from domain terminology toward generic synonyms — "order" instead of "campaign," "user" instead of "activist," "report" instead of "investigation." Language drift in advocacy software causes miscommunication across coalition partners and obscures legal distinctions between operations.

## Ubiquitous Language Dictionary

Use these terms consistently in code, documentation, and AI prompts. NEVER introduce synonyms.

- **Campaign** — An organized effort to achieve a specific advocacy goal (legislative change, corporate policy reform, public awareness). Has defined start, milestones, and success criteria.
- **Investigation** — Covert documentation of animal exploitation conditions. Legally sensitive. All data classified as potential evidence. Distinguished from "research" or "reporting."
- **Coalition** — A formal or informal alliance of multiple organizations working toward a shared goal. Each member has its own risk profile, data policies, and operational boundaries.
- **Witness** — A person who provides testimony about animal exploitation conditions. Identity requires maximum protection.
- **Testimony** — A witness's account of observed conditions. Subject to consent verification before any use or display.
- **Sanctuary** — A facility providing permanent care for rescued animals. Distinguished from "shelter" (temporary) or "foster" (individual-based).
- **Rescue** — The act of removing animals from exploitative conditions. May have distinct legal status depending on jurisdiction.
- **Liberation** — Direct action to free animals. Carries specific legal implications distinct from "rescue."
- **Direct Action** — Physical intervention in animal exploitation. Legally distinct from campaigning, lobbying, or public education.
- **Undercover Operation** — An investigation conducted by an operative embedded within an exploitative facility. Highest legal risk category.
- **Ag-Gag** — Laws criminalizing undercover investigation of agricultural operations. Determines legal exposure for investigation data.
- **Factory Farm** — Industrial animal agriculture facility. Use this term, not euphemisms like "farm" or "production facility."
- **Slaughterhouse** — Facility where animals are killed for commercial purposes. Use this term precisely.
- **Companion Animal** — Animals kept primarily for companionship. Distinct legal and ethical framework from farmed animals.
- **Farmed Animal** — Animals raised for food, fiber, or other commercial products. Distinguished from "livestock" (industry framing).
- **Evidence** — Documentation (footage, records, testimony) of animal exploitation conditions with potential legal use.

## Bounded Contexts

These are DIFFERENT domains with different models, different rules, and different security requirements. Do not merge them. Do not allow data to flow between them without explicit anti-corruption layers.

**Investigation Operations** — Covert data collection, evidence management, investigator identity protection, chain of custody. Highest security classification. Data never flows outward without explicit declassification. Entities: Investigator, Operation, Evidence, Facility, ChainOfCustody.

**Public Campaigns** — Public-facing advocacy, supporter engagement, media relations, petition management. An "activist" in a public campaign is a fundamentally different entity than an "investigator" in an undercover operation — different data model, different risk profile, different access controls. Entities: Campaign, Supporter, Action, Petition, MediaAsset.

**Coalition Coordination** — Multi-organization planning, shared resource management, joint strategy. Data crosses organizational boundaries and must be governed by the strictest partner's policies. Entities: Coalition, PartnerOrganization, SharedResource, JointAction, DataSharingAgreement.

**Legal Defense** — Legal case management, attorney-client privileged communications, court filings. Attorney-client privilege imposes its own data handling requirements that override other policies. Entities: Case, Attorney, Defendant, Filing, PrivilegedCommunication.

## Anti-Corruption Layers
When data must cross bounded context boundaries, use explicit translation layers. An investigation's raw evidence becomes a "media asset" in a public campaign only through a deliberate transformation that strips operational metadata. NEVER allow direct imports between contexts — AI agents will optimize for expedience and import directly. Each boundary crossing must be auditable.

## Compassionate Language — No Speciesist Idioms

Code, documentation, comments, commit messages, and variable names must use compassionate, non-speciesist language. AI agents frequently generate common English idioms that normalize animal violence — reject these and use alternatives. Examples: "kill two birds with one stone" → "accomplish two things at once"; "beat a dead horse" → "belabor the point"; "more than one way to skin a cat" → "more than one way to solve this"; "guinea pig" → "test subject"; "cattle vs. pets" → "ephemeral vs. persistent"; "master/slave" → "primary/replica"; "whitelist/blacklist" → "allowlist/denylist". For automated enforcement covering 60+ speciesist patterns, see the Open Paws no-animal-violence ecosystem: https://github.com/Open-Paws/no-animal-violence (core rules), with integrations for Semgrep, ESLint, Vale, pre-commit hooks, GitHub Actions, VS Code, and Reviewdog at https://github.com/Open-Paws.

---

# Accessibility

Advocacy networks span borders, languages, economic conditions, and infrastructure environments. Accessibility is not standards compliance — it is ensuring the movement's tools work for everyone the movement serves.

## Internationalization from Day One
Design every user-facing component with i18n from the start — never retrofit. Externalize all user-facing strings. Support right-to-left text layouts. Handle pluralization, date, time, currency, and number formatting per locale. Coalition tools must support simultaneous use in multiple languages within the same deployment.

## Low-Bandwidth and Offline-First
Many activists operate on mobile data in regions with expensive or throttled connections. Design for disconnected operation as the default: local-first data storage with background sync, conflict resolution for offline modifications, queue-and-replay for operations during disconnection. The application must be fully functional for core workflows without network access. Set performance budgets and test on throttled connections.

## Mesh Networking Compatibility
In environments where centralized internet is unavailable, compromised, or surveilled, mesh networking enables device-to-device communication. Design sync protocols that can operate over high-latency, low-bandwidth mesh connections.

## Low-Literacy Design
Use icons alongside text labels, visual workflows, progressive disclosure to avoid information density overload. Support voice input and audio output where possible. Test with users from diverse educational backgrounds.

## Graceful Degradation
Every feature must have a degraded mode under constrained conditions. If encryption fails to load, refuse to transmit sensitive data rather than transmitting plaintext. If media processing is unavailable, store investigation footage safely rather than discarding it. Degrade capability, never safety.

## Device Seizure — Application State
When connectivity or power is lost suddenly, the application must not leave sensitive data exposed. No temporary files with decrypted investigation content. No in-memory caches persisting to swap. No crash dumps containing witness identities. No recovery modes displaying sensitive content without re-authentication.

---

# Emotional Safety

Animal advocacy software routinely handles content documenting extreme suffering. This content is necessary for the movement's work but uncontrolled exposure causes measurable psychological harm. Emotional safety is not a UX preference — it is a duty of care.

## Progressive Disclosure of Traumatic Content
NEVER display graphic content by default. Every piece of investigation footage, slaughter documentation, or exploitation imagery must be behind at least one intentional interaction. The default state is always safe: blurred, hidden, or described in text. Users escalate through deliberate choices, never through automatic loading or scrolling.

## Configurable Detail Levels
Implement persistent user-controlled detail settings. At minimum three tiers: (1) text-only descriptions, (2) blurred or low-detail with context, (3) full resolution. The system MUST remember preferences and never reset them. Different roles need different defaults.

## Content Warnings
Every piece of content involving animal suffering MUST be preceded by a specific warning describing what it contains. Generic "sensitive content" warnings are insufficient — indicate whether content includes graphic injury, death, distress vocalizations, confined conditions, or slaughter processes.

## Investigation Footage Handling
NEVER auto-play video or audio. ALWAYS display footage blurred by default. Require explicit opt-in for full resolution. Provide frame-by-frame navigation for reviewers. Strip audio by default — distress vocalizations cause acute stress. Support annotation without full-resolution viewing.

## Witness Testimony Display
Before displaying testimony: verify consent is current and not withdrawn, anonymize by default, require explicit opt-in for identifying details, log access for audit while protecting accessor identity.

## Burnout Prevention
Track continuous exposure time to traumatic content. Surface non-intrusive reminders after configurable intervals (default: 30 minutes). Provide session summaries so reviewers need not re-expose to verify completeness. Support distributing traumatic content review across the team.

## Secondary Trauma — Developer Protection
Use abstract test data in automated tests, not actual footage. Provide mock data generators with realistic metadata but no graphic content. The CI/CD pipeline must never display graphic content in test output, logs, or failure reports. Document which test suites involve real content.

---

# Skill: Git Workflow

## When to Use
Before committing, branching, or creating a pull request. After an AI agent has generated changes that need to be broken into logical units.

## Process

**1. Create an Ephemeral Branch.** Trunk-based development remains the goal. The branch is a safety net, not a long-lived workspace. If the agent has not produced mergeable work within one session, delete the branch and reconsider the approach.

**2. Implement One Subtask.** Break the task into the smallest logical subtasks. Each subtask is one commit. "Extract interface, implement adapter, update callers" = three commits. Never let the agent complete an entire multi-step task before committing.

**3. Test Before Committing.** Run the relevant test subset before each commit. Every commit must leave the codebase passing. For advocacy code, verify no sensitive data has leaked into test output, logs, or error messages.

**4. Write the Commit Message.** Explain WHY, not WHAT. First line: 50 characters, imperative mood. Reference issues. Add AI attribution trailers.

**5. Repeat.** Continue: implement one subtask, test, commit. Each commit independently understandable.

**6. Curate the Pull Request.** PR curation is the critical human skill. AI adoption inflated PR size by 154%. Do not submit agent output as one PR. Target under 200 lines changed per PR, ideally under 100. Use stacked PRs for large changes (PR1, PR2, PR3 — each independently reviewable).

**7. Tag and Request Review.** Tag every PR containing AI-generated code as AI-Assisted. Require two human approvals for primarily AI-generated PRs. Call out security boundaries, error handling, and investigation/coalition data touchpoints.

**8. Track Quality Signals.** Code Survival Rate: how much AI code remains unchanged 48 hours after merge. Suggestion acceptance rate: healthy range 25-35%; higher may indicate over-reliance.

**Merge Strategy.** Squash-merge ephemeral branches. Delete branches immediately after merge.

---

# External Contribution Safety

When contributing to a repository your organization does not own, suppress all tool identity, org attribution, and advocacy framing from every artifact you produce.

## Repo Classification

Check `git remote get-url origin` before writing any commit message, PR description, or branch name.

- Remote matches `github.com/Open-Paws/` or `github.com:Open-Paws/` → **internal repo** — full identity is fine.
- Remote is anything else → **external repo** — apply all rules below.
- No remote configured → treat as **external** (safe default).

There is no ambiguity. Positive confirmation of an internal remote is required to use internal identity. Absent that confirmation, stay in external mode.

## What to Suppress

- **Tool identity** — No mention of the AI coding tool (Claude Code, Copilot, Cursor, Cline, Windsurf, or any other) in commits, PRs, branch names, or code comments.
- **Organization** — No mention of Open Paws or any advocacy organization in any contribution artifact.
- **Mission framing** — No advocacy language (liberation, compassionate, animal rights, vegan) in code, commits, or PRs unless the target project is explicitly about those topics.
- **Attribution trailers** — No `Co-Authored-By:` lines. No "Generated with" footers. No AI attribution in commit messages or PR descriptions.

## Commit Messages

Read the last five commits first: `git log --oneline -5`. Match their exact style. Proportional to the diff: one-line change, one-line commit. Imperative mood ("Fix", "Add", "Update"). No AI-generated patterns ("This commit introduces...", "Updated X to support Y"). Self-check: does this look indistinguishable from the existing commits in this repo?

## PR Descriptions

Check merged PRs first: `gh pr list --state merged --limit 5`. Match their style. No section headers for small changes. No bullet lists of benefits. One to three sentences. Self-check: does this sound like a developer who works on this codebase, without an agenda? If not, cut it by half.

## Branch Names

Use the target repo's convention. Default: `fix/short-description` or `add/short-description`. Under 40 characters. No advocacy language, org identifiers, or tool names.

## Defense-in-Depth

These instructions are last-line-of-defense. Configure your tool to disable attribution trailers before making external contributions — tool configuration is the first line. Instructions to the AI are what you rely on when configuration fails or when the tool generates prose (PR descriptions, branch names) that configuration does not control.

---

# Skill: Testing Strategy

## When to Use
Writing or generating tests. Reviewing AI-generated test code. Setting up test infrastructure. When test quality is in question.

## Process

**1. Read the Specification.** Identify acceptance criteria. If no spec exists, write one first.

**2. Write Failing Tests from the Spec.** Generate tests from the specification BEFORE implementation. Each test encodes a business rule stated in words. For advocacy: "investigation records must be anonymized before export," "graphic content must never display without a content warning."

**3. Verify Tests Fail for the Right Reason.** A failing test is only useful if it fails because the behavior is absent — not because of setup errors.

**4. Implement Until Tests Pass.** Write the minimum code to make failing tests pass.

**5. Review Assertions Against the Spec, Not the Code.** Ask: does this fail if code is wrong? Does it encode a domain rule? Would mutation testing kill it?

**6. Run Mutation Testing.** Surviving mutants reveal weak assertions. Feed them to the AI to generate targeted tests.

**Five Generation Patterns:** (1) Implementation-first — dangerous, tests mirror code. (2) Spec-first — preferred, tests encode intent. (3) Edge-case generation — AI excels at empty inputs, boundary values, unicode, overflow. (4) Characterization tests — capture current behavior of legacy/AI-generated code before changes. (5) Mutation-guided improvement — use surviving mutants to write better tests.

**Five Anti-Patterns to Reject:** Snapshot trap, mock everything, happy path only, test-after-commit, coverage theater.

---

# Skill: Requirements Interview

## When to Use
Starting a new feature or project. When requirements are ambiguous. Before writing a specification.

## Process

Ask one question at a time. Use multiple choice when possible. Do not overwhelm stakeholders.

**Phase 1 — Purpose and Users.** What are we building? Who are the primary users? What does success look like? What existing tools does this replace?

**Phase 2 — Threat Modeling.** Who are the adversaries? (Law enforcement/ag-gag, industry investigators, hostile public, AI model providers.) What happens if the system is compromised? What happens if a device is seized? What legal jurisdictions apply?

**Phase 3 — Coalition and Data Boundaries.** Which organizations will use this? Do they have different risk profiles? What data crosses organizational boundaries? What must NOT cross? If one partner is legally compelled to disclose, what is the blast radius?

**Phase 4 — User Safety.** Does this handle traumatic content? What progressive disclosure levels are needed? Who reviews traumatic content? What anonymization requirements apply? What emotional safety features do users expect?

**Phase 5 — Technical Constraints.** Budget hard limits? Timeline and drivers? Tech stack constraints? Connectivity constraints (offline-first, mesh)? Language and accessibility requirements?

**Phase 6 — Synthesize.** Compile answers into a specification: purpose, user personas, threat model, data boundaries, success criteria, safety requirements, constraints, open questions. Present for confirmation before design.

---

# Skill: Plan-First Development

## When to Use
Starting any significant implementation work. Beginning a new coding session. When a task involves multiple files or modules. When context window usage is approaching 50%.

## Process

**1. Read Existing Code.** Search for relevant existing implementations, utilities, and patterns. AI agents violate DRY at 4x normal rate because they skip this step.

**2. Identify What Changes.** State the change in one sentence. If you cannot describe it concisely, decompose further. Identify which bounded context is affected and whether the change crosses context boundaries.

**3. Write a Specification.** Define: what the code does, inputs, outputs, error conditions, security/safety properties. For advocacy: data sensitivity classification, device seizure behavior, coalition data boundaries.

**4. Break into Subtasks.** Each subtask produces a testable, committable result within half the remaining context window. Structure by conceptual boundaries, not execution order — temporal decomposition is an Ousterhout red flag.

**5. For Each Subtask: Plan, Test, Implement, Verify.** One at a time. Do not start the next until the current one passes and is committed.

**6. Comprehension Check.** Use the **generation-then-comprehension** pattern. Generate, then explain, then verify understanding. Six usage patterns range from full delegation (worst comprehension at 50%) to conceptual inquiry (best at 86%). Stay in the "generate then understand" zone.

**7. Commit and Continue.** Commit after each subtask. Write WHY in the message. Move to next subtask.

**Context Management.** Start sessions fresh. Compact at ~50% context usage. Two-failure rule: clear and restart with better prompt after two failed fixes.

---

# Skill: Code Review

## When to Use
Reviewing any code before merge. Preparing code for review. When a PR is tagged AI-Assisted. When changes touch investigation data, coalition boundaries, or emotional safety features.

## Process

### Layer 1: Automated Checks (Zero Human Effort)
Formatting, linting, static analysis, type checking, security scanning, test suite. Fix before requesting review.

### Layer 2: AI-Assisted First-Pass Review
AI catches well: inconsistent error handling, missing null checks, unused imports, common security patterns, convention deviations, performance anti-patterns. AI misses: whether the approach is correct, whether business logic matches requirements, whether the code is maintainable, whether tests verify meaningful properties, subtle concurrency issues.

### Layer 3: Human Review — Design Quality (Ousterhout Red Flags)
- **Shallow module** — interface as complex as implementation
- **Information leakage** — callers depend on internals
- **Temporal decomposition** — structured by execution order, not concepts
- **Pass-through method** — does nothing except delegate
- **Repetition** — AI duplicates at 4x normal rate
- **Special-general mixture** — general code polluted with special cases

### Layer 4: Human Review — AI-Specific Failure Patterns
- **DRY violations** — does this duplicate existing code? Search before accepting.
- **Multi-responsibility functions** — does any function do more than one thing?
- **Suppressed errors** — has the AI removed safety checks or caught too broadly?
- **Hallucinated APIs** — does the code call things that do not exist? Verify every external reference.
- **Over-patterning** — unnecessary Strategy/Factory/Observer?
- **Silent failure pattern** — AI may remove safety checks to make code appear to work, create fake output matching desired formats, or **edit tests to pass rather than fixing the underlying code**. Verify ALL safety checks from the original code are preserved. Compare error handling paths explicitly between old and new versions.

### Layer 5: Advocacy-Specific Review
- **Data leak vectors** — new paths for sensitive data to leave the system via logging, error messages, telemetry, API responses, serialization
- **Surveillance surface area** — new timestamps, access logs, IP recording, device fingerprinting that could identify activists under legal discovery
- **Emotional safety** — progressive disclosure respected, graphic content behind explicit opt-in, content warnings specific
- **Coalition boundary violations** — data crossing organizational boundaries without anti-corruption layers

Verdict: distinguish blocking issues (security, data leaks, silent failures, broken tests) from suggestions. Require two human approvals for primarily AI-generated PRs.

---

# Skill: Security Audit

## When to Use
Before deploying changes. When dependencies are added. When code touches investigation data, witness identities, or coalition coordination. After AI-generated code on security-sensitive paths. Periodically as scheduled review.

## Process

**Step 1: Dependency Audit — Slopsquatting Defense.** For EVERY dependency: verify the package exists in its registry, has legitimate maintainers with real commit history, and the version is published. ~20% of AI-recommended packages are hallucinated. In advocacy software, a compromised dependency exfiltrates investigation data.

**Step 2: API Retention Policy Audit.** For every external API: verify zero-retention contractually. Check whether the API retains inputs, logs metadata, or stores conversation history.

**Step 3: Storage Encryption Audit.** Verify encrypted volumes with plausible deniability. Check for temporary files, swap files, crash dumps with decrypted content. Test: if the device powers off unexpectedly, is any sensitive data recoverable without credentials?

**Step 4: Input Validation Review.** AI code has OWASP Top 10 vulnerabilities in 45% of cases. Verify SQL injection, XSS, path traversal, and auth defenses on every input boundary.

**Step 5: Instruction File Integrity — Rules File Backdoor.** Inspect all instruction files for hidden Unicode characters or prompt injection payloads. The **Rules File Backdoor** attack uses invisible characters to direct AI agents toward malicious output. Diff changes character-by-character. Verify no file weakens encryption, disables safety checks, or sends data to external endpoints.

**Step 6: Device Seizure Readiness.** Verify remote wipe capability. Verify auto-lock on suspicious conditions. Test: kill the process unexpectedly and examine what remains on disk.

**Step 7: Ag-Gag Exposure Assessment.** Audit data flows assuming adversarial legal discovery. Verify metadata stripping. Verify audit logs protect the identities they record. Check: if a court subpoena targeted this system, what would be disclosed?

**Step 8: Coalition Data Boundary Verification.** Verify data isolation between partners with different risk profiles. Verify anti-corruption layers at every boundary. Check: if one partner is compelled to disclose, what is the blast radius?

**Findings Classification.** Critical: active data leak, missing encryption, compromised dependency, exposed witness identity. High: weak input validation, missing zero-retention verification. Medium: incomplete metadata stripping, untested seizure scenario. Low: documentation gaps. Block deployment on Critical or High.

---

# Code Quality — desloppify

Run desloppify to systematically identify and fix code quality issues. Install and configure (requires Python 3.11+):

```bash
pip install --upgrade "desloppify[full]"
desloppify update-skill claude    # pick yours: claude, cursor, codex, copilot, windsurf, gemini
```

Add `.desloppify/` to `.gitignore`. Before scanning, exclude directories that should not be analyzed (vendor, build output, generated code, worktrees) with `desloppify exclude <path>`. Share questionable candidates with the project owner before excluding.

```bash
desloppify scan --path .
desloppify next
```

`--path` is the directory to scan (`.` for whole project, or a subdirectory). Your goal is to get the strict score as high as possible. The scoring resists gaming — the only way to improve it is to actually make the code better.

**The loop:** run `next`. It is the execution queue from the living plan, not the whole backlog. It tells you what to fix now, which file, and the resolve command to run when done. Fix it, resolve it, run `next` again. Over and over. This is your main job. Use `desloppify backlog` only when you need to inspect broader open work that is not currently driving execution.

Do not be lazy. Large refactors and small detailed fixes — do both with equal energy. No task is too big or too small. Fix things properly, not minimally.

Use `plan` / `plan queue` to reorder priorities or cluster related issues. Rescan periodically. The scan output includes agent instructions — follow them, do not substitute your own analysis.

## GEO + SEO — Advocacy Website Visibility

Websites for animal advocacy serve two discovery channels: traditional search engines and AI answer systems (ChatGPT, Perplexity, Google AI Overviews, Claude, Gemini). The game has shifted from keyword matching to **intent satisfaction** (does your content completely solve the user's problem?), **entity authority** (does Google's knowledge graph recognize your brand?), and **technical excellence** (can crawlers efficiently process your site?). AI generates an answer first, then scores content against it using embedding distance. Only 17–32% of AI Overview citations come from pages ranking in the organic top 10 — lower-authority pages can win with the right structure (source: Authoritas AI Overviews study, 2024). Domain Authority correlates with AI citations at r=0.18; topical authority (r=0.40) and branded web mentions (r=0.664) are the real predictors (source: Kalicube GEO correlation study, 2025).

### Core Web Vitals (March 2026)

Google confirmed CWV as ranking factors measured via real Chrome user data at the 75th percentile.

| Metric | Good | Needs Improvement | Poor |
|--------|------|-------------------|------|
| LCP (Largest Contentful Paint) | ≤ 2.5s | 2.5–4.0s | > 4.0s |
| INP (Interaction to Next Paint) | ≤ 200ms | 200–500ms | > 500ms |
| CLS (Cumulative Layout Shift) | ≤ 0.1 | 0.1–0.25 | > 0.25 |

43% of sites still fail the INP threshold. Sites with INP above 200ms saw an average ranking drop of 0.8 positions; LCP above 3s causes 23% more traffic loss vs faster competitors. The primary INP technique is `scheduler.yield()` (Chrome-native, with `setTimeout` fallback) — breaks long tasks so the browser can handle user input between them.

### HTML Structure

One `<h1>` per page. Phrase `<h2>` headings as questions — produces 7× more AI citations for smaller sites. First paragraph after any heading must directly answer the question in 40–60 words. AI pulls from the first 30% of content 44% of the time. Keep paragraphs 2–4 sentences. Structure content as self-contained 120–180 word modules — generates 70% more ChatGPT citations than unstructured prose. Use semantic HTML (`<article>`, `<section>`, `<main>`, etc.). Never hide content behind JavaScript-only rendering; AI crawlers generally do not execute JS.

### Semantic Writing for AI

AI retrieval happens at sentence and paragraph level. **Entity salience:** make the primary entity the grammatical subject — active voice gives a salience score of 0.74 vs passive 0.11. **Atomic claims:** every sentence must be a self-contained semantic triple with explicit context (subject + verb + object + attribution). **Proper noun density:** AI-cited text averages 20.6% proper nouns; name the organization, researcher, report, and year. **Content density sweet spot:** 5,000–20,000 characters — under 5,000 chars gets ~66% extracted; over 20,000 chars gets only 12%. Open every major section with a direct 40–60 word answer.

### Content Strategy and E-E-A-T

Match search intent before writing — study top-5 results to understand what format Google considers the best match (informational → guides; commercial investigation → comparisons; transactional → product pages). Google's Helpful Content System (integrated since March 2024) rewards content that solves problems genuinely; since June 2025, Google issues manual actions for scaled AI content abuse. Unedited AI drafts bounce 18% higher. Use AI in a human-led editorial process. Content with proper author metadata gets cited 40% more. E-E-A-T signals: original data, verified author bios with Person schema, specific citations with dates, third-party recognition. Every content page needs a visible author name, link to an author profile page with `@type: Person` schema, and a trust chain: Article → author `@id` → Person schema → `sameAs` external profiles.

### Wikipedia and Wikidata

Wikipedia accounts for 47.9% of ChatGPT's top-10 cited sources. Wikidata serves 11 million queries daily across 119 million entities; companies have gained Knowledge Panels within 7 days of creating a Wikidata entry. Add Wikidata Q-ID and Wikipedia URL to Organization schema `sameAs`. Build an entity web: organization → key tools → key people → related organizations → policy areas. Ensure structured data is consistent with Wikipedia — inconsistency reduces AI confidence.

**Wikipedia COI (mandatory):** Never directly edit your own organization's Wikipedia article. Disclose affiliation on the Talk page. Propose edits through Talk-page requests or neutral editors. Use only independent, reliable sources. Follow Wikipedia's Conflict of Interest and Notability guidelines.

### Structured Data (JSON-LD)

Sites with structured data achieve 41% AI citation rates vs 15% without; only 12.4% of websites implement it. Implement JSON-LD in `<head>` on every page: Organization + WebSite schema (every page); Article schema with `datePublished`, `dateModified`, author `@id` (every content page); FAQPage schema for Q&A sections; BreadcrumbList for navigation; Person schema for author pages. Always use `@id` to connect entities. Keep `dateModified` accurate and synchronized with the visible date. Validate at https://validator.schema.org/.

### Meta Tags and Technical SEO

Title: 50–60 chars, primary keyword first, unique per page. Meta description: 150–160 chars, direct factual answer + one statistic, never duplicated. Security headers required in 2026: HSTS, CSP, `X-Content-Type-Options`, `X-Frame-Options`. Require SSR or SSG — client-side-only rendering is a strategic error. Manage crawl budget: block low-value parameter URLs and internal search in robots.txt; fix redirect chains; return proper HTTP status codes (200/301/404/410). Use WebP/AVIF with `<picture>` element, `srcset`, explicit `width`/`height`, `loading="lazy"`. Descriptive file names. Keep page weight under 1MB. Supply chain: pin exact dependency versions, use `npm ci` in CI, scan with Socket.dev or Snyk.

### Site Architecture and Internal Linking

Hub-and-spoke topic cluster model increases AI citation rates from 12% to 41%; bidirectional links increase citation probability by 2.7×. Pillar page (2,000–4,000 words) + 8–15 cluster pages with bidirectional links. Max 3 levels deep; no important page more than 3 clicks from homepage. Breadcrumbs with BreadcrumbList schema. Use descriptive anchor text — never "read more". Audit for orphan pages.

### Content Freshness

76% of the most-cited AI content was updated within 30 days; Perplexity gives a 3.4× citation advantage to content updated within 30 days. Use visible `<time datetime="YYYY-MM-DD">` Last Updated dates and accurate `dateModified` in Article schema. Only update dates when content actually changes — Google detects date-only freshness hacking.

### Robots.txt, Sitemap, and IndexNow

Allow citation crawlers (OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Claude-SearchBot, Applebot, Amazonbot) in robots.txt — there are 226+ identified AI crawlers (last verified 2026-03-01; source: DarkVisitors); blocking Googlebot blocks AI Overviews too. To block training crawlers without affecting citation, explicitly disallow CCBot and GPTBot (these harvest training data but do not power AI answer systems). Sitemaps: canonical URLs only, accurate `<lastmod>`, submit to Search Console and Bing Webmaster Tools. IndexNow pings Bing (which feeds ChatGPT) instantly on publish — integrate into CI/CD.

### Platform Presence and Link Building

85% of AI brand mentions come from third-party pages. Brand mentions now account for 55% of off-page ranking weight (up from ~20% in 2012); backlinks 45%. Brands on 4+ platforms are 2.8× more likely to appear in AI responses. Publish on Reddit (46.5% of Perplexity citations), YouTube (23.3% of AI citations, enable transcripts), LinkedIn, and GitHub. Convert unlinked brand mentions to backlinks — close rates typically above 30%. Digital PR with original research generates 156% more links. The March 2026 spam update devalued sponsored guest posts on generalist sites, niche edits on thin aged domains, and PBNs.

### Conversion Optimization

For nonprofit donation pages: present 3–4 preset amounts with the middle pre-selected and impact descriptions. Pre-select monthly giving — monthly donors become more valuable than one-time donors within 5.25 months, yet 64% of nonprofits still default to one-time. Single-step forms vastly outperform multi-step (52% drop in completions). Removing site header navigation during the donation flow produced a documented 195% conversion increase. Embed the form on-site; never redirect to a third-party processor. For all forms: target 3–5 fields maximum. Dark patterns carry FTC legal risk — the $2.5 billion Amazon settlement (September 2025) is the largest dark pattern enforcement action in history.

### Analytics

Use **Plausible** ($9/month cloud) or **Umami** (self-hosted, free) as primary analytics — no cookies, no consent banner required. Add GA4 only for Google Ads integration or predictive analytics. Track AI referral traffic with a custom channel group in GA4 matching `(chatgpt\.com|perplexity\.ai|claude\.ai|gemini\.google\.com|copilot\.microsoft\.com)` — AI referral traffic grew 357% YoY to 1.1 billion visits in June 2025. Mark key conversions: `donation_completed` (with value), `newsletter_signup`, `volunteer_form_submit`.

### Internationalization

For multilingual sites, use **next-intl** (1.8M weekly downloads) with subdirectory URL strategy (`/en/`, `/hi/`, `/ar/`) to centralize domain authority. Set `lang` and `dir` on `<html>`. Hreflang tags must be self-referencing and reciprocal on every page — 31% of international sites have broken hreflang. Use ICU MessageFormat for plural/gender forms (Arabic requires 6 CLDR plural categories). CSS logical properties (`ps-4`, `pe-4`, `text-start`) handle RTL layout automatically.

### llms.txt

Place at `/llms.txt`. Current value is effectively zero per multiple studies — zero AI crawler visits documented across 8 months. Implement it (low effort) but do not invest significant time. The IETF AIPREF Working Group (co-authored by Google and Mozilla) is the more likely path to a real standard.

### Citation Volatility and Defensive Awareness

40–60% monthly citation turnover is normal; only 11% of domains are cited by both ChatGPT and Perplexity for the same queries. Build multi-platform presence rather than depending on any single system. Avoid: hidden text injection (invisible Unicode U+E0000–U+E007F, white-on-white text) — actively detected by SpamBrain with domain-wide penalties; agent-aware cloaking (serving different content to AI crawlers) — explicitly prohibited; scaled AI content without human review — sites lost up to 80% of organic traffic overnight. FTC "Operation AI Comply" (September 2024): using AI to deceive is illegal with no AI exemption. Add a CI job or pre-commit hook that scans all committed files for invisible Unicode (U+E0000–U+E007F) and zero-width characters and fails the pipeline if any are found — this prevents inadvertent injection and provides a clear audit trail.

### Key Statistics

| Signal | Impact |
|--------|--------|
| LCP ≤ 2.5s (Good threshold) | Sites above 3s see 23% more traffic loss |
| INP > 200ms | −0.8 average position drop; 43% of sites fail |
| FAQ/structured data | 41% citation rate vs 15% without |
| Question-based H2s | 7× citation impact for smaller sites |
| 120–180 word modular sections | 70% more ChatGPT citations |
| Author metadata | +40% AI citations |
| Topic cluster architecture | 12% → 41% citation rate |
| Fresh content (within 30 days) | 76% of most-cited; 3.4× Perplexity advantage |
| Wikipedia/Wikidata presence | Knowledge Panel within 7 days |
| Original or proprietary data | 4.31× more citations per URL |
| AI Overview citations from top-10 | Only 17–32% — lower-authority pages can win |
| Brand mentions vs AI citations | r=0.664 — strongest overall signal |
| Topical authority vs AI citations | r=0.40 — strongest on-site predictor |
| Monthly citation turnover | 40–60% — continuous freshness required |
| Pre-selecting monthly giving | 31% of nonprofit online revenue |
| AI referral traffic growth | 357% YoY to 1.1B visits (June 2025) |
