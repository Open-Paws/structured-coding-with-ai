# Animal Advocacy Platform — Project Guidelines

Software for animal liberation and advocacy. This is a high-risk domain: investigation data is subpoena-target evidence, activists face legal prosecution under ag-gag statutes, and system compromise endangers lives. Every design decision must account for three adversaries: **state surveillance** (law enforcement using ag-gag laws, warrants, subpoenas), **industry infiltration** (corporate investigators, social engineering against coalition members), and **AI model bias** (training data encoding industry framing, models leaking investigation details through telemetry).

---

## Workflow

Read existing code before writing anything. Plan before code: read, plan, code, verify. Never create files or functions that duplicate existing ones — search first. Write a specification before implementation. Write a failing test before writing code. After two failed fix attempts, stop and re-approach with a better prompt rather than compounding errors.

When Junie generates tests automatically via its built-in test generation, review every generated assertion for correctness against the specification — not against the implementation. Junie's integration with IntelliJ inspections catches formatting and structural issues; rely on those deterministic checks rather than restating style rules here.

---

## Constraints

- NEVER log, store, or transmit activist personally identifiable information
- NEVER send data to external APIs without explicit project-owner approval
- ALWAYS use zero-retention configurations for any third-party service
- ALWAYS apply progressive disclosure for traumatic content (investigation footage, slaughter documentation)
- Abstract all vendor dependencies behind project-owned interfaces — vendor lock-in is a movement risk for nonprofits that cannot absorb pricing changes
- Assume adversarial legal discovery: investigation data is court-subpoena material, not just hacker targets
- Encrypted local storage with plausible deniability; no telemetry to third parties

---

## Design Principles — AI Code Review Checklist

Before finishing any task, verify AI output against these ten ranked failure modes (most frequently violated in AI-generated code):

1. **DRY** — AI duplicates existing logic at 4x the normal rate; search the codebase before writing anything new
2. **Deep modules over shallow wrappers** — reject pass-through methods and thin wrappers that add surface area without hiding complexity; if the interface is as complex as the implementation, the abstraction is shallow (Ousterhout red flags: shallow module, overexposure, pass-through)
3. **Single responsibility** — each function does one thing at one level of abstraction; split multi-responsibility functions immediately
4. **Error handling** — never catch-all or silently swallow failures; AI suppresses errors and removes safety checks — the **silent failure pattern** means AI may remove safety checks to make code appear to work, create fake output matching desired formats, or edit tests to pass rather than fixing code; verify every error path in advocacy-critical code where silent failure means evidence loss
5. **Information hiding** — expose only what callers need; implementation details must not leak across module boundaries
6. **Ubiquitous language** — code must use movement terminology (campaign, investigation, coalition, sanctuary, witness, testimony, rescue, liberation, direct action, ag-gag, farmed animal), not AI-invented synonyms; language drift causes miscommunication across coalition partners
7. **Design for change** — insist on abstraction layers and loose coupling; AI optimizes for "works now" over "works later," but advocacy tools must outlast any single campaign
8. **Legacy code velocity** — AI code churns 2x faster (GitClear); write for readability and changeability, apply characterization tests before modifying AI-generated modules (Feathers' "cover before you change")
9. **Over-patterning** — use the simplest structure that works; reject Strategy/Factory/Observer where a plain function and conditional suffice; AI applies design patterns aggressively where simpler solutions work
10. **Test quality** — every test must fail when the behavior it covers is broken; mutation testing is the countermeasure for tautological AI-generated assertions

For investigation or evidence-handling code: always add security review for data leakage, PII exposure, and ag-gag legal risk.

---

## Testing

Testing is the keystone of AI-assisted advocacy development. Without tests, AI agents drift silently — and in advocacy software, silent drift means lost evidence, exposed activists, or traumatic content displayed without safeguards.

**Assertion quality is the non-negotiable.** NEVER accept tautological assertions — tests that assert output equals output. Ask three questions of every AI-generated test: (1) Does this test fail if the code is wrong? (2) Does the assertion encode a domain rule you can name? (3) Would mutation testing kill this? Quality metric: mutation score over coverage percentage. A suite with 90% coverage and 40% mutation score is false security.

**Spec-first generation preferred.** Generate tests from specifications or acceptance criteria before writing implementation — not after. Tests generated from existing implementation mirror the code rather than the intent, producing circular validation. When Junie auto-generates tests from implementation, treat them as characterization tests that need assertion review, not as correctness tests.

**Property-based testing for invariants.** Verify that invariants hold across random inputs. Critical advocacy invariants: anonymization must be irreversible, encryption must not leak plaintext length, coalition data boundaries must hold under arbitrary input combinations.

**Test error paths explicitly.** AI-generated tests overwhelmingly cover happy paths. In advocacy software, error paths are where people get hurt — failed encryption, leaked identity, broken anonymization, missing content warnings. Test what happens when the network drops during evidence upload. Test what happens when storage is seized mid-write.

**Contract tests at service boundaries.** AI hallucinates API contracts — approximately 20% of AI-recommended packages do not exist. At every service boundary, especially coalition cross-organization APIs, use consumer-driven contract tests.

**Test infrastructure.** Fast execution is non-negotiable — AI agents run tests in tight loops; a 10-minute suite across 15 iterations burns 2.5 hours. Flaky tests poison the AI feedback loop; agents cannot distinguish flaky from real failures. Maintain test-to-code ratio of 1:1 or higher.

**Adversarial input testing.** Test inputs crafted to exploit advocacy-specific vulnerabilities: SQL injection through investigation search fields, XSS through witness testimony display, path traversal through evidence file uploads, oversized payloads designed to crash offline-first sync.

### Five Testing Anti-Patterns to Reject

1. **Snapshot trap** — tests that snapshot current output and assert against it; they pass today and break on any correct change; they verify nothing about correctness
2. **Mock everything** — over-mocked tests verify that mocks behave as expected, not that real code works; mock only at system boundaries (external APIs, databases, file systems)
3. **Happy path only** — AI-generated tests overwhelmingly test the success path; explicitly request error path, boundary condition, and adversarial input tests; in advocacy software, error paths are where people get hurt
4. **Test-after-commit** — writing tests after code is committed defeats the feedback loop; tests must exist during development, not after
5. **Coverage theater** — chasing coverage numbers with meaningless assertions; a line "covered" by a test with no assertion is not tested

---

## Security

Advocacy software faces the three adversaries model. Security is the structural foundation, not a feature layer.

**Zero-retention APIs.** NEVER send sensitive data to external services that retain inputs. Investigation footage, witness identities, activist communications, and coalition coordination data must only flow through zero-retention configurations. Verify retention policies contractually, not by assumption.

**Encrypted local storage with plausible deniability.** All locally stored investigation data, evidence, and activist records MUST use encrypted volumes. Design storage so that the existence of sensitive data is deniable under device seizure — nested encrypted containers where the outer layer contains innocuous data and the inner layer requires a separate key.

**Supply chain verification — slopsquatting defense.** Approximately 20% of AI-recommended packages do not exist — they are hallucinated names. Attackers register these hallucinated names as real packages containing malicious code (one was downloaded 30,000+ times in weeks). VERIFY EVERY dependency exists in its actual registry and has legitimate maintainers before installation. Only 1 in 5 AI-recommended dependency versions are both safe and free from hallucination.

**Input validation against industry sabotage.** AI-generated code contains OWASP Top 10 vulnerabilities in 45% of cases — 2.74x more than human code, with 86% failure rate on XSS defenses. Validate and sanitize all inputs at system boundaries (the "barricade" pattern). Assume adversarial input on every public-facing surface — industry actors will probe investigation tools.

**Ag-gag legal exposure vectors.** Investigation footage is discoverable evidence. Design every data flow assuming adversarial legal discovery. Metadata (timestamps, geolocation, device identifiers) can be more damaging than content — strip aggressively. Audit logs must protect the identities they record; logs identifying who accessed investigation data become prosecution tools.

**Device seizure preparation.** Remote wipe capability for all sensitive data. Encrypted volumes that lock on suspicious conditions (unexpected power loss, extended inactivity). No temporary files with decrypted content, no swap files with sensitive state, no crash dumps with investigation data.

**Instruction file integrity — Rules File Backdoor.** The "Rules File Backdoor" attack uses hidden Unicode characters in instruction files (`.junie/guidelines.md`, `.cursorrules`, `.mdc` files) to inject invisible directives that make AI produce malicious output. Treat ALL instruction files as security-critical artifacts. Review for non-printable characters. Diff changes character-by-character. In advocacy projects, a compromised instruction file could direct AI to weaken encryption, leak data, or disable safety checks.

**Provider routing for sensitive data.** When using AI coding assistants with multiple model providers, sensitive advocacy data (investigation content, witness identities, legal defense materials) must NEVER route through free-tier providers that may retain inputs. Free-tier APIs may retain inputs for training or compliance — assume they do unless contractually guaranteed otherwise. Route sensitive work exclusively through zero-retention providers or self-hosted inference.

**Self-hosted inference for critical paths.** Any code path handling investigation data, witness identities, or legal defense materials should use self-hosted AI inference — not cloud APIs. Model providers may comply with government data requests.

**MCP server security.** Any MCP server handling sensitive advocacy data MUST be self-hosted. Audit each server's data access, network egress, and retention before enabling. An MCP server with network access can exfiltrate data regardless of application-level encryption.

---

## Privacy

Privacy in advocacy software is the difference between operational security and activist prosecution. Data that seems harmless in isolation becomes evidence under ag-gag statutes: participation timestamps, IP addresses, device fingerprints, and access patterns can identify investigators, witnesses, and rescue coordinators.

**Data minimization as default architecture.** Collect the absolute minimum data required. Before adding any field, ask: if this data appeared in a court filing, who would it endanger? If the answer is anyone, justify its existence or eliminate it.

**Activist identity protection.** Use pseudonymous identifiers internally. Never store legal names alongside action records. Separate authentication identity from operational identity — the system that verifies login must not be the system that records who participated in which investigation. Compartmentalization is structural: compromise of one system must not cascade.

**GDPR/CCPA as floor, not ceiling.** Right to deletion MUST be real deletion — not soft delete with a `deleted_at` flag. "Deleted" records surfacing in legal discovery destroy trust and endanger people. Erasure must be irrecoverable from all storage layers including backups, replicas, search indices, analytics, and logs.

**Consent as ongoing process.** Implement re-consent workflows for scope changes. Withdrawal must be as easy as granting, with immediate effect. Participation in a public campaign does not imply consent to be recorded as an investigation participant.

**Coalition data sharing across risk profiles.** Different organizations operate at different risk levels. When sharing across coalition boundaries: classify each partner's risk level, apply the strictest rules of any partner in the exchange, strip identifying information before sharing across risk tiers, design agreements specifying what happens when a partner is compromised.

**Whistleblower and witness protection.** End-to-end encryption for all whistleblower communications. No server-side access to decrypted content. Anonymous submission channels without account creation. Zero-knowledge architectures where administrators cannot identify whistleblowers. Witness testimony requires consent verification before display, anonymization by default, explicit opt-in for identifiable presentation.

**Anonymization must be irreversible.** AI-generated anonymization is often superficial — replacing names while leaving uniquely identifying attribute combinations. True anonymization requires k-anonymity at minimum.

---

## Cost Optimization

Advocacy organizations operate on nonprofit budgets. Every dollar on AI compute is a dollar not spent on investigations, legal defense, or sanctuary operations.

**Model routing.** Route tasks to the cheapest capable model. Cheap models for: test generation, boilerplate, formatting, simple refactoring, documentation. Mid-tier for: debugging, multi-file changes, code review. Frontier models for: hard architectural problems, complex debugging, security-critical review.

**Token budget discipline.** Set hard limits per session and per day. Cap conversation duration. When an agent hits budget, stop and reassess rather than allocating more tokens to an unproductive path.

**Prompt cache optimization.** Place static content first in prompts to maximize cache hits (target 80%+). Instruction files and project context before dynamic task content.

**Budget allocation.** 40% implementation, 30% testing (generation + execution loops), 20% review and debugging, 10% documentation. Track cost per merged PR as the key efficiency metric.

**Vendor lock-in as movement risk.** ALWAYS abstract model and vendor dependencies behind project-owned interfaces. Maintain self-hosted fallback for critical paths. Evaluate open-source models regularly. A nonprofit locked to a single provider faces existential budget exposure.

**Efficiency.** Run smallest relevant test subset first; full suite on commit. Start sessions fresh rather than extending degraded conversations. Break work into subtasks completing within half the context window. Compact at ~50% context usage.

---

## Advocacy Domain — Ubiquitous Language and Bounded Contexts

AI agents drift from domain terminology toward generic synonyms ("user" instead of "activist," "report" instead of "investigation"). Language drift causes miscommunication across coalition partners and obscures legal and ethical distinctions.

### Domain Terms — Use Consistently, NEVER Introduce Synonyms

- **Campaign** — organized effort for a specific advocacy goal (legislative change, corporate reform, public awareness)
- **Investigation** — covert documentation of animal exploitation conditions; legally sensitive; all data is potential evidence
- **Coalition** — alliance of organizations with shared goals; each member has its own risk profile and data policies
- **Witness** — person providing testimony about exploitation conditions; identity requires maximum protection
- **Testimony** — witness account of observed conditions; subject to consent verification before any use
- **Sanctuary** — facility providing permanent care for rescued animals (distinct from shelter or foster)
- **Rescue** — removing animals from exploitative conditions; distinct legal status by jurisdiction
- **Liberation** — direct action to free animals; carries specific legal implications distinct from rescue
- **Direct Action** — physical intervention in exploitation; legally distinct from campaigning or lobbying
- **Undercover Operation** — investigation by operative embedded within exploitative facility; highest legal risk
- **Ag-Gag** — laws criminalizing undercover investigation of agricultural operations; determines legal exposure
- **Factory Farm** — industrial animal agriculture facility (not "farm" or "production facility")
- **Slaughterhouse** — facility where animals are killed commercially (use precise term)
- **Companion Animal** — animals kept for companionship; distinct legal framework from farmed animals
- **Farmed Animal** — animals raised for food/fiber/products (not "livestock," which is industry framing)
- **Evidence** — documentation of exploitation conditions with potential legal use

### Bounded Contexts — Do Not Merge

**Investigation Operations** — covert data collection, evidence management, investigator identity protection, chain of custody. Highest security. Data never flows outward without explicit declassification.

**Public Campaigns** — public-facing advocacy, supporter engagement, media relations. An "activist" in a public campaign is a fundamentally different entity than an "investigator" in an undercover operation — different data model, risk profile, access controls.

**Coalition Coordination** — multi-organization planning, shared resources, joint strategy. Data crosses organizational boundaries and must be governed by the strictest partner's policies.

**Legal Defense** — case management, attorney-client privileged communications. Privilege imposes its own data handling requirements that override other policies.

**Anti-corruption layers between contexts.** When data crosses bounded context boundaries, use explicit translation layers. Raw investigation evidence becomes a "media asset" in a public campaign only through deliberate transformation stripping operational metadata. NEVER allow direct imports between contexts — AI agents optimize for expedience and import directly rather than translating through anti-corruption layers.

### Compassionate Language — No Speciesist Idioms

Code, documentation, comments, commit messages, and variable names must use compassionate, non-speciesist language. AI agents frequently generate idioms that normalize animal violence — reject and replace. Examples: "kill two birds with one stone" → "accomplish two things at once"; "beat a dead horse" → "belabor the point"; "guinea pig" → "test subject"; "cattle vs. pets" → "ephemeral vs. persistent"; "master/slave" → "primary/replica"; "whitelist/blacklist" → "allowlist/denylist". For automated enforcement covering 60+ patterns, see: https://github.com/Open-Paws/no-animal-violence (core rules) and integrations at https://github.com/Open-Paws.

---

## Accessibility

Advocacy networks span borders, languages, economic conditions, and infrastructure environments.

**Internationalization from day one.** Externalize all user-facing strings from the start. Support RTL layouts. Handle locale-specific formatting. Adding i18n after the fact costs exponentially more.

**Low-bandwidth optimization.** Many activists operate on mobile data in regions with expensive or throttled connections. Compress assets, lazy-load non-critical content, minimize payloads, sync only deltas.

**Offline-first architecture.** Design for disconnected operation as default. Local-first data storage with background sync. Conflict resolution for offline-modified data. Core workflows must function without network access.

**Low-literacy design patterns.** Use icons alongside text, visual workflows instead of text-heavy instructions, voice I/O where possible, progressive disclosure to avoid information overload.

**Mesh networking compatibility.** In environments where internet is unavailable, compromised, or surveilled, design sync protocols for high-latency, low-bandwidth, intermittent peer-to-peer connectivity.

**Graceful degradation.** Degrade capability, never safety. If encryption fails to load, refuse to transmit rather than transmitting plaintext. If network drops, show clear status — no silent failures.

**Device seizure — application state.** When connectivity is lost suddenly (confiscation, jamming, power cut), leave zero recoverable sensitive state on disk. No temp files with decrypted content, no swap/crash data with investigation info, no recovery modes displaying sensitive content without re-authentication.

---

## Emotional Safety

Advocacy software handles content documenting extreme suffering: factory farm conditions, slaughterhouse footage, animal testing documentation, witness testimony. Emotional safety is a duty of care to the people doing this work.

**Progressive disclosure.** NEVER display graphic content by default. Every piece of investigation footage or exploitation imagery behind at least one intentional interaction. Default state is always safe: blurred, hidden, or text description.

**Configurable detail levels.** Three tiers minimum: (1) text-only, (2) blurred/low-detail with descriptions, (3) full resolution. Persist preference across sessions. Different roles need different defaults.

**Content warnings mandatory.** Every piece of suffering content preceded by specific warning describing what it contains — graphic injury, death, distress vocalizations, confined conditions, slaughter. Generic "sensitive content" is insufficient.

**Investigation footage handling.** NEVER auto-play. ALWAYS blur by default. Require explicit opt-in for full resolution. Frame-by-frame navigation for reviewers. Strip audio by default (distress vocalizations cause acute stress). Support annotation on blurred preview.

**Witness testimony display.** Verify consent is current before display. Anonymize by default. Require opt-in for identifying details. Apply progressive disclosure and content warnings.

**Burnout prevention.** Session time awareness with reminders after configurable intervals (default 30 min). "Take a break" prompts for extended review. Session summaries so reviewers need not re-expose to verify completeness. Workload distribution across team.

**Secondary trauma — development workflow.** Use abstract test data (described references, not actual footage). Mock data generators producing realistic metadata without graphic content. CI/CD pipeline must never display graphic content in test output, logs, or failure reports.

---

## Git Workflow

### When to Use
Before committing, branching, or creating a pull request.

### Process

**1. Create an ephemeral branch.** Trunk-based development remains the goal. The branch is a safety net, not a long-lived workspace. If the agent has not produced mergeable work within one session, delete the branch and reconsider.

**2. Implement one subtask per commit.** Break overall task into smallest logical subtasks. "Extract interface, implement adapter, update callers" is three commits, not one. Never let the agent complete an entire multi-step task before committing.

**3. Test before committing.** Run relevant tests before each commit. Every commit leaves the codebase passing. For advocacy code, also verify no sensitive data leaked into test output, logs, or error messages.

**4. Write commit messages explaining WHY.** 50 characters, imperative mood. Reference issues. Add AI attribution trailers.

**5. Curate the pull request.** PR curation is the critical human skill. AI inflated PR size by 154%. Split into reviewable chunks: under 200 lines changed per PR, ideally under 100. Use stacked PRs for large changes. Each PR tells a coherent story.

**6. Tag and request review.** Tag every PR with AI-generated code as AI-Assisted. Two human approvals for primarily AI-generated PRs. Call out security boundaries, error handling, and code touching investigation or coalition data.

**7. Track quality signals.** Code Survival Rate: how much AI code remains 48 hours post-merge. Suggestion acceptance rate: healthy 25-35%; higher may indicate over-reliance.

**Merge strategy.** Squash-merge ephemeral branches. Delete immediately after merge.

---

## Testing Strategy

### When to Use
Writing, generating, or reviewing any tests.

### Process

**1. Read the specification.** Identify spec or acceptance criteria. If none exists, write one. Without a spec, AI generates tests mirroring implementation, not intent.

**2. Write failing tests from spec.** Generate tests from specification BEFORE implementation. Each test encodes a business rule: "investigation records must be anonymized before export," "coalition data must not cross boundaries without agreement."

**3. Verify tests fail for the right reason.** Failing because behavior is absent, not because of setup errors.

**4. Implement until tests pass.** Minimum implementation. No more code than tests demand.

**5. Review assertions against spec, not code.** The three questions: fails if wrong? encodes domain rule? mutation testing kills it?

**6. Run mutation testing.** Surviving mutants reveal assertions that look thorough but verify nothing. Feed surviving mutants to AI to generate targeted tests.

### Five Generation Patterns
1. **Implementation-first** — dangerous; tests mirror code, not intent; use only for characterization
2. **Spec-first** — preferred; encodes intended behavior
3. **Edge-case generation** — give function signature, ask for: empty inputs, boundary values, null, unicode, timezone boundaries, concurrent access, overflow
4. **Characterization tests** — capture current behavior of legacy/AI-generated code before changes (Feathers: cover before you change)
5. **Mutation-guided improvement** — run mutation testing, feed surviving mutants, generate targeted tests

When Junie generates tests automatically, classify them as Pattern 1 (implementation-first) and apply the corresponding review rigor — these need assertion quality review, not blind acceptance.

---

## Requirements Interview

### When to Use
Starting a new feature, when requirements are ambiguous, before writing a spec.

### Process

Ask one question at a time. Multiple choice when possible. Do not overwhelm stakeholders — advocacy stakeholders are often volunteers with limited time.

**Phase 1 — Purpose:** What are we building? Who are the users? (Investigators, campaign organizers, sanctuary staff, legal team, coalition coordinators, public supporters.) What does success look like?

**Phase 2 — Threat modeling:** Who are the adversaries? (Law enforcement/ag-gag, industry investigators, hostile public, AI model providers.) What happens if compromised? What if a device is seized? Which jurisdictions apply?

**Phase 3 — Coalition and data boundaries:** Which organizations use this? Different risk profiles? What data crosses boundaries? What must NOT cross? If one partner is compelled to disclose, what is the blast radius?

**Phase 4 — User safety:** Traumatic content involved? Progressive disclosure levels needed? Who reviews traumatic content? Burnout prevention? Witness/whistleblower identities? Anonymization requirements?

**Phase 5 — Technical constraints:** Budget limits? Timeline and driver? Tech stack? Connectivity constraints (offline-first, low-bandwidth, mesh)? Language and accessibility requirements?

**Phase 6 — Synthesize:** Purpose statement, user personas with risk profiles, threat model, data boundaries, success criteria, safety requirements, constraints, open questions. Present to stakeholder for confirmation before design.

---

## Plan-First Development

### When to Use
Starting any significant implementation, beginning a new session, multi-file changes.

### Process

**1. Read existing code.** Understand current structure, naming, utilities, patterns. AI generates duplicate functions at 4x rate because it lacks full codebase awareness.

**2. Identify what needs to change.** State in one sentence. If you cannot, decompose further. Identify which bounded context is affected and whether the change crosses context boundaries.

**3. Write a specification.** Requirements before implementation. What the code does, inputs, outputs, error conditions, security properties. For advocacy: data sensitivity classification, device seizure behavior, coalition boundary implications.

**4. Break into subtasks.** Each subtask produces a testable, committable result within half the remaining context window. Follow conceptual boundaries, not execution order (temporal decomposition is a red flag).

**5. For each subtask: plan, test, implement, verify.** One at a time. Do not start the next until the current passes and is committed.

**6. Comprehension check.** After AI generates code, explain what it does in your own words before committing. AI-assisted developers score 17 percentage points lower on comprehension tests (Anthropic, 2026). Use the **generation-then-comprehension** pattern: generate code, then immediately ask the AI to explain it, then verify your understanding. Six usage patterns range from full delegation (worst: 50% comprehension) to conceptual inquiry (best: 86%). Stay in the "generate then understand" zone. If you cannot explain the code, do not commit it.

**7. Commit after each subtask.** Write WHY in the message. Move to next subtask.

**Context management.** Start sessions fresh. Compact at ~50% context usage. After two failed fixes, clear and restart with better prompt.

---

## Code Review

### When to Use
Reviewing any code before merge, preparing code for review, AI-Assisted PRs, changes touching investigation data or coalition boundaries.

### Process

**Layer 1 — Automated checks (zero human effort).** Formatting, linting, static analysis, type checking, security scanning, test suite. Use IntelliJ inspections and CI gates. Fix before requesting review.

**Layer 2 — AI-assisted first pass.** AI catches: inconsistent error handling, missing null checks, unused imports, common security patterns, convention deviations, performance anti-patterns. AI misses: whether the approach is correct, business logic match, maintainability, test meaningfulness, concurrency issues.

**Layer 3 — Human review: design quality (Ousterhout red flags).**
- Shallow module — interface as complex as implementation
- Information leakage — implementation details escape through interface
- Temporal decomposition — structured by execution order, not concepts
- Pass-through method — does nothing except delegate with same signature
- Repetition — same logic in multiple places (AI: 4x normal duplication rate)
- Special-general mixture — general-purpose code polluted with special cases

**Layer 4 — Human review: AI-specific failure patterns.**
- DRY violations — duplicates existing codebase functions
- Multi-responsibility functions — more than one thing at one abstraction level
- Suppressed errors — removed safety checks, overly broad catches, swallowed failures
- Hallucinated APIs — calls to libraries, methods, or endpoints that do not exist
- Over-patterning — Strategy/Factory/Observer where plain functions suffice
- **Silent failure pattern** — AI may remove safety checks to make code appear to work, create fake output matching desired formats, or edit tests to pass rather than fixing underlying code; verify ALL original safety checks are preserved; compare error handling between old and new versions

**Layer 5 — Advocacy-specific review.**
- Data leak vectors — new paths for sensitive data to leave the system (logging, errors, telemetry, serialization)
- Surveillance surface area — new timestamps, access logs, IP recording, device fingerprinting usable to identify activists
- Emotional safety — progressive disclosure respected? Graphic content behind opt-in? Content warnings specific?
- Coalition boundary violations — data crossing organizational boundaries without anti-corruption layers

Two human approvals for primarily AI-generated PRs. Distinguish blocking issues (security, data leaks, silent failures, broken tests) from suggestions.

---

## Security Audit

### When to Use
Before deploying, when adding dependencies, when code touches investigation/witness/coalition data, after AI changes to security-sensitive paths, periodically.

### Process

**1. Dependency audit — slopsquatting defense.** ~20% of AI-recommended packages do not exist. Verify EVERY dependency exists in its registry with legitimate maintainers. One hallucinated package was downloaded 30,000+ times.

**2. API retention policy audit.** Verify zero-retention contractually for every external API handling sensitive data.

**3. Storage encryption audit.** Verify encrypted volumes with plausible deniability. Check for temp files, swap, crash dumps with decrypted content. Test: unexpected power-off — is anything recoverable without credentials?

**4. Input validation review.** 45% AI-generated code has OWASP Top 10 vulnerabilities. Verify SQL injection, XSS, path traversal, auth defenses on every input boundary.

**5. Instruction file integrity — Rules File Backdoor.** Inspect instruction files for hidden Unicode characters or prompt injection. Diff character-by-character. Verify no file weakens encryption, disables checks, or exfiltrates data.

**6. MCP server audit.** Self-hosted for sensitive data. Audit access patterns, network egress, retention.

**7. Device seizure readiness.** Remote wipe exists. Auto-lock on suspicious conditions. No sensitive data on unexpected termination.

**8. Ag-gag exposure assessment.** Audit data flows for adversarial legal discovery. Verify metadata stripping. Verify audit logs protect identities. Minimize what a court subpoena would disclose.

**9. Coalition boundary verification.** Data isolation between partners. Anti-corruption layers at every crossing. Agreements enforced in code. Blast radius assessment if one partner is compromised.

**10. Findings report.** Severity: Critical (active leak, missing encryption, compromised dependency, exposed witness), High (weak validation, unverified retention, unaudited MCP), Medium (incomplete metadata stripping, untested seizure), Low (docs, config). Block deployment on Critical or High.

---

## Code Quality — desloppify

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

`--path` is the directory to scan (`.` for whole project, or a subdirectory). Goal: get the strict score as high as possible — the scoring resists gaming, the only way to improve it is to actually make the code better.

**The loop:** run `next`. It tells you what to fix now, which file, and the resolve command to run when done. Fix it, resolve it, run `next` again. This is your main job. Use `desloppify backlog` only to inspect broader open work not currently driving execution.

Large refactors and small detailed fixes — do both with equal energy. Fix things properly, not minimally. Use `plan` / `plan queue` to reorder priorities or cluster related issues. Rescan periodically. The scan output includes agent instructions — follow them, do not substitute your own analysis.

## GEO + SEO — Advocacy Website Visibility

Websites for animal advocacy serve two discovery channels: traditional search engines and AI answer systems (ChatGPT, Perplexity, Google AI Overviews, Claude, Gemini). The game has shifted from keyword matching to **intent satisfaction** (does your content completely solve the user's problem?), **entity authority** (does Google's knowledge graph recognize your brand?), and **technical excellence** (can crawlers efficiently process your site?). AI generates an answer first, then scores content against it using embedding distance. Only 17–32% of AI Overview citations come from pages ranking in the organic top 10 — lower-authority pages can win with the right structure. Domain Authority correlates with AI citations at r=0.18; topical authority (r=0.40) and branded web mentions (r=0.664) are the real predictors.

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

### Structured Data (JSON-LD)

Sites with structured data achieve 41% AI citation rates vs 15% without; only 12.4% of websites implement it. Implement JSON-LD in `<head>` on every page: Organization + WebSite schema (every page); Article schema with `datePublished`, `dateModified`, author `@id` (every content page); FAQPage schema for Q&A sections; BreadcrumbList for navigation; Person schema for author pages. Always use `@id` to connect entities. Keep `dateModified` accurate and synchronized with the visible date. Validate at schema.org/validator.

### Meta Tags and Technical SEO

Title: 50–60 chars, primary keyword first, unique per page. Meta description: 150–160 chars, direct factual answer + one statistic, never duplicated. Security headers required in 2026: HSTS, CSP, `X-Content-Type-Options`, `X-Frame-Options`. Require SSR or SSG — client-side-only rendering is a strategic error. Manage crawl budget: block low-value parameter URLs and internal search in robots.txt; fix redirect chains; return proper HTTP status codes (200/301/404/410). Use WebP/AVIF with `<picture>` element, `srcset`, explicit `width`/`height`, `loading="lazy"`. Descriptive file names. Keep page weight under 1MB. Supply chain: pin exact dependency versions, use `npm ci` in CI, scan with Socket.dev or Snyk.

### Site Architecture and Internal Linking

Hub-and-spoke topic cluster model increases AI citation rates from 12% to 41%; bidirectional links increase citation probability by 2.7×. Pillar page (2,000–4,000 words) + 8–15 cluster pages with bidirectional links. Max 3 levels deep; no important page more than 3 clicks from homepage. Breadcrumbs with BreadcrumbList schema. Use descriptive anchor text — never "read more". Audit for orphan pages.

### Content Freshness

76% of the most-cited AI content was updated within 30 days; Perplexity gives a 3.4× citation advantage to content updated within 30 days. Use visible `<time datetime="YYYY-MM-DD">` Last Updated dates and accurate `dateModified` in Article schema. Only update dates when content actually changes — Google detects date-only freshness hacking.

### Robots.txt, Sitemap, and IndexNow

Allow citation crawlers (OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot) in robots.txt — there are 226+ identified AI crawlers (last verified 2026-03-01; source: DarkVisitors); blocking Googlebot blocks AI Overviews too. Sitemaps: canonical URLs only, accurate `<lastmod>`, submit to Search Console and Bing Webmaster Tools. IndexNow pings Bing (which feeds ChatGPT) instantly on publish — integrate into CI/CD.

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

40–60% monthly citation turnover is normal; only 11% of domains are cited by both ChatGPT and Perplexity for the same queries. Build multi-platform presence rather than depending on any single system. Avoid: hidden text injection (invisible Unicode U+E0000–U+E007F, white-on-white text) — actively detected by SpamBrain with domain-wide penalties; agent-aware cloaking (serving different content to AI crawlers) — explicitly prohibited; scaled AI content without human review — sites lost up to 80% of organic traffic overnight. FTC "Operation AI Comply" (September 2024): using AI to deceive is illegal with no AI exemption.

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
