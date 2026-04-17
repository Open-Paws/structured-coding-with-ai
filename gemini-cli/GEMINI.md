# Animal Advocacy Platform

Software for animal liberation and advocacy. This is a high-risk domain: investigation data is subpoena-target evidence, activists face legal prosecution under ag-gag statutes, and system compromise endangers lives. Three distinct adversaries shape every design decision: **state surveillance** (law enforcement using warrants, subpoenas, and ag-gag prosecutions), **industry infiltration** (corporate investigators posing as volunteers, social engineering against coalition members), and **AI model bias** (training data encoding industry framing, models refusing advocacy operations, telemetry leaking investigation details).

---

## Workflow

**Read before writing. Plan before code. Verify after.**

1. Read existing code before making any change — search for existing functions, utilities, and patterns before creating new ones
2. Write a specification before implementation — state what the code does, its inputs, outputs, error conditions, and safety properties
3. Write a failing test before writing code — generate tests from the spec, not from the implementation
4. Implement the minimum code to pass the test
5. Verify: run tests, confirm the change works, check for data leaks in error messages and logs
6. Commit after each completed subtask with a message explaining WHY

After two failed fix attempts, stop and re-approach with a better prompt. Do not compound errors. Start each session fresh rather than extending a degraded conversation. Break work into subtasks that complete within half the context window.

**Comprehension check:** After AI generates code, explain what it does in your own words before committing. AI-assisted developers score 17 percentage points lower on comprehension tests (Anthropic, 2026). Use the **generation-then-comprehension** pattern: generate code, then immediately ask the AI to explain it, then verify your understanding matches. Full delegation produces the worst comprehension (50%); conceptual inquiry produces the best (86%).

---

## Constraints

- NEVER log, store, or transmit activist personally identifiable information
- NEVER send sensitive data to external APIs without explicit project-owner approval
- ALWAYS use zero-retention configurations for any third-party service
- ALWAYS apply progressive disclosure for traumatic content (investigation footage, slaughter documentation)
- Abstract ALL vendor dependencies behind project-owned interfaces — vendor lock-in is a movement risk for nonprofits
- Assume adversarial legal discovery: investigation data is court-subpoena material, not just hacker targets
- Encrypted local storage with plausible deniability; no telemetry to third parties
- When using Gemini CLI's sandbox mode, verify that sandboxed execution does not write sensitive data to temporary locations outside the sandbox boundary
- Review tool confirmation prompts carefully — confirm that each tool invocation is appropriate for advocacy-sensitive code before approving

---

## Review Checklist — 10 AI-Violated Design Principles

Before finishing any task, verify AI output against these ranked failure modes (from most frequent to most impactful):

1. **DRY** — AI clones existing logic at 4x the normal rate because it lacks full codebase awareness. Search the codebase before writing anything new. Maintain a list of existing utilities in this file if duplication recurs.
2. **Deep modules over shallow wrappers** — Reject pass-through methods and thin wrappers that add interface surface without hiding complexity. If the interface is as complex as the implementation, the abstraction is shallow. (Ousterhout red flags: shallow module, overexposure, pass-through.)
3. **Single responsibility** — Each function does one thing at one level of abstraction. AI produces multi-responsibility functions by default. Check function length and responsibility count first — these are the fastest quality signals.
4. **Error handling** — AI suppresses errors, catches too broadly, and removes safety checks. In advocacy code, silent failure means evidence loss or exposed activists. Verify every try/catch block. Never catch-all or silently swallow failures. The **silent failure pattern** is the most dangerous: AI may remove safety checks to make code appear to work, create fake output matching desired formats, or edit tests to pass rather than fixing the underlying code.
5. **Information hiding** — Expose only what callers need. AI leaks implementation details across module boundaries. If callers depend on internals, the boundary is broken.
6. **Ubiquitous language** — Code MUST use movement terminology (campaign, investigation, coalition, sanctuary, witness, testimony, rescue, liberation), not AI-invented synonyms. Language drift causes miscommunication across coalition partners. See the Domain Language section below.
7. **Design for change** — AI optimizes for "works now" over "works later." Insist on abstraction layers, loose coupling, and interfaces that survive campaign lifecycle changes. Advocacy tools must outlast any single campaign.
8. **Legacy code velocity** — AI code churns 2x faster (GitClear). Write for readability and changeability. Apply characterization tests (Feathers) before modifying AI-generated modules — capture actual behavior before changing anything.
9. **Over-patterning** — AI forces Strategy/Factory/Observer where a plain function and conditional suffice. Use the simplest structure that works. "Don't force patterns — recognize when they fit" (Gang of Four).
10. **Test quality** — AI generates tests that look thorough but verify nothing. Mutation testing is the countermeasure for tautological assertions. A suite with 90% coverage and 40% mutation score is a false sense of security.

---

## Testing

Testing is the keystone of AI-assisted advocacy development. Without tests, AI agents drift silently — and in advocacy software, silent drift means lost evidence, exposed activists, or traumatic content displayed without safeguards.

**Assertion quality is non-negotiable.** Three questions for every AI-generated test:
1. Does this test fail if the code is wrong? If you break the implementation and the test still passes, it is worthless.
2. Does the assertion encode a domain rule? If you cannot name the rule, it is a snapshot, not a test.
3. Would mutation testing kill this? If changing `+` to `-` leaves the test green, the assertion is weak.

NEVER accept tautological assertions — tests that assert output equals the output of the same function call.

**Spec-first test generation preferred.** Write tests from spec/acceptance criteria before implementation. Tests generated from existing code mirror the implementation, not the intent. Five generation patterns: (1) implementation-first (dangerous — use only for characterization), (2) spec-first (preferred), (3) edge-case generation (AI excels here), (4) characterization tests for legacy code (cover before you change), (5) mutation-guided improvement (feed surviving mutants to AI).

**Property-based testing** verifies invariants across random inputs — catches classes of bugs, not individual bugs. Critical advocacy invariants: anonymization must be irreversible, encryption must not leak plaintext length, coalition data boundaries must hold under arbitrary input.

**Test error paths explicitly.** AI-generated tests overwhelmingly cover happy paths. In advocacy software, error paths are where people get hurt: failed encryption, leaked identity, broken anonymization, missing content warnings. Test what happens when the network drops during evidence upload. Test what happens when storage is seized mid-write.

**Contract tests at service boundaries.** AI hallucinates API contracts — approximately 20% of AI-recommended packages do not exist. Use consumer-driven contract tests at every coalition cross-organization API.

**Fast execution is non-negotiable.** AI agents run tests in tight loops. A 10-minute suite across 15 iterations burns 2.5 hours. Invest in parallel execution, test isolation, selective test running. Flaky tests poison the AI feedback loop — track and eliminate aggressively.

**Quality metrics:** Mutation score over coverage percentage. Test-to-code ratio of 1:1 or higher. Track P50/P95 test execution time.

### Five Testing Anti-Patterns

1. **Snapshot trap** — Tests that snapshot current output and assert against it. Pass today, break on any correct change. Verify nothing about correctness.
2. **Mock everything** — Over-mocked tests verify mock behavior, not real code. Mock only at system boundaries: external APIs, databases, file systems.
3. **Happy path only** — AI-generated tests overwhelmingly test success paths. Explicitly request error path, boundary condition, and adversarial input tests.
4. **Test-after-commit** — Tests written after code is committed defeat the feedback loop. Tests must exist during development, not after.
5. **Coverage theater** — Chasing coverage numbers with meaningless assertions. A line "covered" by a test with no assertion is not tested. Coverage tells you what is NOT tested; it cannot tell you what IS well-tested.

### Adversarial Input Testing

Test inputs crafted to exploit advocacy-specific vulnerabilities: SQL injection through investigation search fields, XSS through witness testimony display, path traversal through evidence file uploads, oversized payloads designed to crash offline-first sync.

---

## Security

Advocacy software faces the **three adversaries model**: state surveillance, industry infiltration, and AI model bias. Security is the structural foundation, not a feature layer.

**Zero-retention APIs.** NEVER send sensitive data to services that retain inputs. Investigation footage, witness identities, activist communications must flow only through zero-retention configurations. Verify retention policies contractually, not by assumption.

**Encrypted local storage with plausible deniability.** All investigation data, evidence, and activist records MUST use encrypted volumes. Design storage so sensitive data existence is deniable under device seizure — nested encrypted containers where the outer layer contains innocuous data and the inner layer requires a separate key.

**Supply chain verification — slopsquatting defense.** Approximately 20% of AI-recommended packages do not exist — they are hallucinated names. Attackers register these names as real packages containing malicious code. One was downloaded 30,000+ times in weeks. **Verify EVERY dependency** exists in its registry with legitimate maintainers before installation. Only 1 in 5 AI-recommended dependency versions are both safe and free from hallucination.

**Input validation against industry sabotage.** Assume adversarial input on every public-facing surface. AI-generated input validation is weak: 45% of AI-generated code contains OWASP Top 10 vulnerabilities, with 86% failure rate on cross-site scripting defenses.

**Ag-gag legal exposure vectors.** Investigation footage is discoverable evidence. Design every data flow assuming adversarial legal discovery. Metadata (timestamps, geolocation, device identifiers) can be more damaging than content — strip aggressively. Audit logs must protect the identities they record.

**Device seizure preparation.** Remote wipe capability. Encrypted volumes that lock automatically on suspicious conditions (unexpected power loss, extended inactivity, SIM removal). No temporary files with decrypted content, no swap files containing sensitive state, no crash dumps with investigation data.

**Instruction file integrity — Rules File Backdoor.** The "Rules File Backdoor" attack uses hidden Unicode characters in instruction files (GEMINI.md, .cursorrules, CLAUDE.md) to inject invisible directives that make AI agents produce malicious output. **Treat ALL instruction files as security-critical artifacts.** Review for non-printable characters. Diff changes character-by-character. In advocacy projects, a compromised instruction file could direct the AI to weaken encryption, leak data, or disable safety checks. When using Gemini CLI, verify that your GEMINI.md has not been tampered with before each session on shared machines.

**Provider routing for sensitive data.** When using AI coding assistants with multiple model providers, sensitive advocacy data (investigation content, witness identities, legal defense materials) must NEVER route through free-tier providers that may retain inputs. Free-tier APIs may retain inputs for training or compliance — assume they do unless contractually guaranteed otherwise. Route sensitive work exclusively through zero-retention providers or self-hosted inference.

**Self-hosted inference for critical paths.** Any code path handling investigation data, witness identities, or legal defense materials should use self-hosted AI inference — not cloud-hosted APIs. Model providers may comply with government data requests.

**MCP server security.** Any MCP server handling sensitive advocacy data MUST be self-hosted. Audit each server's data access patterns, network egress, and data retention before enabling.

---

## Privacy

Privacy in advocacy software is the difference between operational security and activist prosecution. Data that seems harmless in isolation becomes evidence under ag-gag statutes.

**Data minimization as default.** Collect the absolute minimum. Before adding any field, ask: if this data appeared in a court filing, who would it endanger? If the answer is anyone, justify or eliminate.

**Activist identity protection.** Use pseudonymous identifiers internally. Never store legal names alongside action records. Separate authentication identity from operational identity — compartmentalize so compromise of one system does not cascade.

**GDPR/CCPA as floor, not ceiling.** Right to deletion MUST be real deletion — not soft delete with a `deleted_at` flag. "Deleted" records surfacing in legal discovery destroy trust and endanger people. Erasure must be irrecoverable from all storage layers including backups, replicas, search indices, analytics, and logs.

**Consent as ongoing process.** Re-consent for scope changes (new coalition partner, new feature, new data sharing). Participation in a public campaign does not imply consent to investigation participation. Withdrawal must be as easy as granting, with immediate effect.

**Coalition data sharing across risk profiles.** Different organizations operate at different risk levels. When sharing across boundaries: classify risk levels, apply the strictest partner's rules, transform data at boundaries (strip identifying info before sharing across tiers), maintain audit trails that do not create new identification vectors.

**Whistleblower and witness protection.** End-to-end encryption for all whistleblower communications. No server-side access to decrypted content. Anonymous submission channels without account creation. Zero-knowledge architecture where administrators cannot identify whistleblowers.

**Anonymization must be irreversible.** AI-generated anonymization is often superficial — replacing names while leaving uniquely identifying attribute combinations. Require k-anonymity at minimum. Test by attempting re-identification with public information.

---

## Cost Optimization

Every dollar on AI compute is a dollar not spent on investigations, legal defense, or sanctuary operations.

**Model routing.** Cheap models for test generation, boilerplate, formatting. Mid-tier for debugging, multi-file changes, code review. Frontier models only for hard architectural problems, complex debugging, security-critical review.

**Token budget discipline.** Hard limits per session and per day. Cap conversation duration. When hitting the ceiling, stop and reassess rather than allocating more tokens to an unproductive path.

**Prompt cache optimization.** Static content first to maximize cache hits — target 80%+. Instruction files and project context before dynamic task content.

**Budget allocation:** 40% implementation, 30% testing, 20% review and debugging, 10% documentation. Track cost per merged PR, not cost per generated line.

**Vendor lock-in is movement risk.** Abstract model dependencies behind project-owned interfaces. Maintain self-hosted fallback for critical paths. Evaluate open-source models for non-frontier tasks.

**Efficiency practices.** Smallest relevant test subset first; full suite on commit. Start sessions fresh. Compact at 50% context usage. Break work into subtasks completing within half the context window.

---

## Advocacy Domain Language

AI agents drift from domain terminology toward generic synonyms — "order" instead of "campaign," "user" instead of "activist." Language drift in advocacy software causes miscommunication across coalition partners and obscures legal and ethical distinctions.

### Ubiquitous Language

Use these terms consistently. NEVER introduce synonyms.

- **Campaign** — Organized effort toward a specific advocacy goal (legislative change, corporate reform, public awareness). Has start, milestones, success criteria.
- **Investigation** — Covert documentation of exploitation conditions. Legally sensitive. All data is potential evidence. Not "research" or "reporting."
- **Coalition** — Alliance of organizations with shared goal. Each member has own risk profile, data policies, operational boundaries.
- **Witness** — Person providing testimony about exploitation. May be investigator, whistleblower, or bystander. Identity requires maximum protection.
- **Testimony** — Witness account of observed conditions. Subject to consent verification before any use or display.
- **Sanctuary** — Permanent animal care facility. Not "shelter" (temporary) or "foster" (individual).
- **Rescue** — Removing animals from exploitative conditions. Distinct legal status by jurisdiction.
- **Liberation** — Direct action to free animals. Specific legal implications distinct from rescue.
- **Direct Action** — Physical intervention in exploitation. Legally distinct from campaigning or lobbying.
- **Undercover Operation** — Investigation by operative embedded in exploitative facility. Highest legal risk.
- **Ag-Gag** — Laws criminalizing undercover investigation of agricultural operations. Determines legal exposure.
- **Factory Farm** — Industrial animal agriculture facility. Not "farm" or "production facility."
- **Slaughterhouse** — Facility where animals are killed commercially. Use precisely.
- **Companion Animal** — Animals kept for companionship. Distinct legal/ethical framework from farmed animals.
- **Farmed Animal** — Animals raised for food/fiber/commercial products. Not the industry commodity term.
- **Evidence** — Documentation of exploitation with potential legal use.

### Bounded Contexts

These are DIFFERENT domains with different models, rules, and security requirements. Do not merge them. Do not allow data to flow between them without explicit anti-corruption layers.

**Investigation Operations** — Covert data collection, evidence management, investigator identity protection, chain of custody. Highest security. Data never flows outward without explicit declassification. Entities: Investigator, Operation, Evidence, Facility, ChainOfCustody.

**Public Campaigns** — Public-facing advocacy, supporter engagement, media, petitions. Lower security, high visibility. An "activist" in a campaign is fundamentally different from an "investigator" in an undercover operation — different data model, risk profile, access controls. Entities: Campaign, Supporter, Action, Petition, MediaAsset.

**Coalition Coordination** — Multi-organization planning, shared resources, joint strategy. Data crosses organizational boundaries governed by strictest partner's policies. Entities: Coalition, PartnerOrganization, SharedResource, JointAction, DataSharingAgreement.

**Legal Defense** — Case management, attorney-client privilege, court filings. Privilege requirements override other policies. Entities: Case, Attorney, Defendant, Filing, PrivilegedCommunication.

**Anti-corruption layers:** When data crosses bounded context boundaries, use explicit translation layers. An investigation's raw evidence becomes a "media asset" in a campaign only through deliberate transformation stripping operational metadata. NEVER allow direct imports between contexts — AI agents optimize for expedience and will import directly. Each boundary crossing must be auditable.

### Compassionate Language — No Speciesist Idioms

Code, documentation, comments, commit messages, and variable names must use compassionate, non-speciesist language. AI agents frequently generate idioms that normalize animal violence — reject and replace. For automated enforcement covering 60+ patterns, see: https://github.com/Open-Paws/no-animal-violence (core rules) and integrations at https://github.com/Open-Paws.

---

## Accessibility

Advocacy networks span borders, languages, economic conditions, and infrastructure environments.

**Internationalization from day one.** Externalize all user-facing strings from the start. Support RTL layouts, locale-aware formatting, language-specific pluralization. Retrofitting i18n touches every component — cost grows exponentially.

**Low-bandwidth optimization.** Compress all assets, lazy-load non-critical content, minimize payloads, sync only deltas. Set performance budgets, test on throttled connections.

**Offline-first architecture.** Design for disconnected operation as default. Local-first data with background sync. Conflict resolution for offline-modified data. Queue operations during disconnection, replay on reconnect. Core workflows must function without network access.

**Low-literacy design.** Icons alongside text labels, visual workflows, voice input/output where possible, progressive disclosure to reduce information density.

**Mesh networking compatibility.** Data sync protocols that operate over mesh networks with high latency, low bandwidth, intermittent peer availability. Activists in regions with government internet shutdowns depend on this.

**Graceful degradation.** Every feature has a degraded mode under constraints. If encryption fails to load, refuse to transmit rather than sending plaintext. If media processing is unavailable, store safely for later rather than discarding. Degrade capability, never safety.

**Device seizure — application state.** When connectivity is lost suddenly (confiscation, jamming, power cut), the application must leave zero recoverable sensitive state on disk. No temp files with decrypted content, no swap caches, no crash dumps with witness data, no recovery modes showing sensitive content without re-authentication.

---

## Emotional Safety

Advocacy software handles content documenting extreme suffering. Every display decision must balance operational access against the human cost of exposure.

**Progressive disclosure — mandatory.** NEVER display graphic content by default. Every piece of investigation footage or exploitation imagery must be behind at least one intentional interaction. Default state is always safe: blurred, hidden, or text description.

**Configurable detail levels.** Three tiers minimum: (1) text-only, (2) blurred/low-detail with descriptions, (3) full resolution. Per-user, persistent across sessions, never auto-reset. Different roles need different defaults.

**Content warnings — specific, not generic.** "Sensitive content" is insufficient. Warnings must indicate: graphic injury, death, distress vocalizations, confined conditions, slaughter processes. Informed decision, not surprise.

**Investigation footage handling:** Never auto-play. Always blurred by default. Explicit opt-in for full resolution (click, not hover or scroll). Frame-by-frame navigation for reviewers. Strip audio by default — distress vocalizations cause acute stress. Support annotation on blurred previews.

**Witness testimony display:** Verify display consent is current. Anonymize by default. Explicit opt-in for identifying details. Log access for audit while protecting accessor identity.

**Burnout prevention:** Session time awareness (reminders after configurable intervals, default 30 minutes). Break prompts for extended content review. Session summaries to avoid re-exposure for verification. Workload distribution across reviewers.

**Secondary trauma mitigation — including developers.** Use abstract test data in automated tests, not actual footage. Mock data generators with realistic metadata but no graphic content. Document which test suites involve real content. CI/CD must never display graphic content in output, logs, or failure reports.

**Opt-in escalation.** Multiple confirmation steps proportional to severity. Confirmation dialog naming what the user is about to see, requiring explicit acknowledgment, with alternatives alongside full-access option.

---

## GitHub Workflow

Never commit or push directly to `main`. Never merge to `main` directly. Never share a branch between parallel agents.

### When to Use
Before starting any coding task on a GitHub repository. Before committing, branching, or creating a PR. When multiple agents run in parallel. After an AI agent has generated a batch of changes.

### Process

**Step 0 — GitHub issue first.** Before writing any code, verify there is a documented issue: `gh issue list --search "keywords"`. If no issue exists, create one: `gh issue create --title "Fix: description" --body "..."`. Include problem description, acceptance criteria, affected files, and security/privacy considerations. Do not begin implementation until the issue is documented.

**Step 1 — One worktree per task.** Every task — especially in parallel agent swarms — gets its own git worktree: `git worktree add ../worktrees/<branch-name> -b <branch-name>`. Branch naming: `fix/<issue-number>-short-description` or `feat/<issue-number>-short-description`. Under 50 characters. When spawning parallel sub-agents, each agent MUST receive its own unique branch name and worktree path — agents sharing a branch produce conflicts and corrupted history.

**Step 2 — Read the codebase.** Before planning, read every file in the affected module(s), existing utilities and patterns, test files, and recent git log. Do not begin planning until you can describe the current behavior in your own words.

**Step 3 — Write a plan.** Write a detailed implementation plan: specific change in one sentence, which files change and why, subtask decomposition (each subtask = one commit), test strategy, security/privacy considerations, desloppify score impact.

**Step 4 — Review the plan (loop until approved).** Review against the issue's acceptance criteria: fully addresses it? No duplicate code? Follows conventions? Security/privacy addressed? Each subtask atomic? Loop: revise → review → until all concerns resolved. No implementation on unresolved concerns.

**Step 5 — Implement one subtask at a time.** For each subtask: implement, run tests, verify no data leakage, commit WHY not WHAT: `git commit -m "fix(#<issue>): <imperative-mood description>"`. Every commit must leave the codebase passing.

**Step 6 — Review implementation (loop until approved).** Review full diff against plan: matches plan? Acceptance criteria met? No scope creep? Tests fail when behavior breaks? All safety checks preserved? Loop: fix → review → until clean.

**Step 7 — desloppify (score must not drop).** Before opening a PR: `desloppify scan --path . && desloppify next`. Score after changes must be ≥ score before — a drop means the PR is not ready. If the repo has no published score, establish a baseline first. Minimum scores: Gary ≥80 · Platform repos ≥75 · All other repos ≥70

**Step 8 — Submit PR.** `gh pr create --title "fix: description (closes #<issue>)"` with summary, closes reference, test plan, and desloppify before/after scores. Under 200 lines changed (ideally under 100). Stacked PRs for large changes. AI-Assisted label for primarily agent-generated code. Two human approvals required.

**Step 9 — Monitor until merged.** After submitting, check periodically: `gh pr view <number>`, `gh pr checks <number>`, `gh pr view <number> --comments`. Fix CI failures immediately on the same branch. Respond to every review comment; fix blocking issues and push. Re-request review when fixes are pushed. **The task is not done until the PR is merged.**

**Quality signals.** Code Survival Rate: how much AI code remains 48 hours after merge. Suggestion acceptance rate: healthy 25-35%; higher may indicate over-reliance.

**Merge strategy.** Squash-merge ephemeral branches. Delete branches immediately after merge.

**External contribution safety.** When contributing to a third-party repository (any repo whose remote does not match `github.com/Open-Paws/`), suppress all tool identity, org attribution, and advocacy framing from commits, PR descriptions, and branch names. Check the remote with `git remote get-url origin` before writing any commit message or PR description. Read the last five commits (`git log --oneline -5`) and match the target repo's exact style: length, format, tense. Imperative mood only. No AI-generated patterns ("This commit introduces...", "Updated X to support Y"). No `Co-Authored-By:` trailers, no "Generated with" footers. No mentions of Open Paws, Gemini CLI, or any AI tool. Check merged PRs (`gh pr list --state merged --limit 5`) and match their description style: one to three sentences, no benefit bullet lists, no section headers for small changes. Branch names: `fix/short-description` or `add/short-description`, under 40 characters, no advocacy language. If there is no remote, default to external mode. There is no ambiguity: positive confirmation of an internal remote is required to unlock internal identity; absent that, stay in external mode. When using Gemini CLI's sandbox mode for external contributions, verify the sandbox does not generate co-author trailers or tool attribution in commit output.

---

## Testing Strategy

### When to Use
Writing or generating tests. Reviewing AI-generated test code. Setting up test infrastructure.

### Process

1. **Read the spec.** Identify specification or acceptance criteria. If none exists, write one. Without a spec, AI generates tests mirroring implementation, not intent.
2. **Write failing tests from spec.** Generate tests from specification BEFORE implementation. Each test encodes a business rule: "investigation records must be anonymized before export," "graphic content must never display without a content warning."
3. **Verify tests fail for the right reason.** Failure should describe missing behavior, not broken setup.
4. **Implement until tests pass.** Minimum code to satisfy tests.
5. **Review assertions against spec, not code.** The critical step. Apply the three assertion quality questions.
6. **Run mutation testing.** Surviving mutants reveal weak assertions. Feed survivors to AI for targeted tests.
7. **Fix weak tests.** Close the loop between generation and quality.

### Advocacy-Specific Testing
- Contract tests at every coalition API boundary
- Test adversarial inputs: injection through investigation search, XSS through testimony display, traversal through evidence uploads
- Verify progressive disclosure: graphic content must not render without explicit opt-in
- Test offline behavior: connectivity drops during evidence sync
- Verify anonymization irreversibility

---

## Requirements Interview

### When to Use
Starting a new feature or project. When requirements are ambiguous. Before writing a spec.

### Process

Ask one question at a time. Multiple choice when possible. Do not overwhelm advocacy stakeholders — they are often volunteers.

**Phase 1 — Purpose:** What are we building? Who are the users? What does success look like? What does this replace?

**Phase 2 — Threat modeling:** Who are the adversaries? (Law enforcement/ag-gag, industry investigators, hostile public, AI providers, other.) What happens if compromised? What happens if a device is seized? What jurisdictions apply?

**Phase 3 — Coalition boundaries:** Which organizations? Different risk profiles? What data crosses boundaries? What must NOT cross? Blast radius if one partner is compelled to disclose?

**Phase 4 — User safety:** Traumatic content? Progressive disclosure levels needed? Who reviews traumatic content? Witness/whistleblower identities? Emotional safety features?

**Phase 5 — Constraints:** Budget (nonprofit — every dollar has alternative advocacy use). Timeline. Tech stack. Connectivity (offline-first, mesh). Languages, accessibility.

**Phase 6 — Synthesize:** Purpose statement, user personas with risk profiles, threat model, data boundaries, success criteria, safety requirements, constraints, open questions. Present to stakeholder for confirmation before design.

---

## Plan-First Development

### When to Use
Starting any significant implementation. Beginning a new session. Multi-file or multi-module changes.

### Process

1. **Read existing code.** Understand structure, naming, existing utilities, patterns. This prevents DRY violations.
2. **Identify what changes.** State it in one sentence. If you cannot, decompose further. Also identify: which bounded context is affected, whether the change crosses context boundaries.
3. **Write a spec.** Requirements before code. What the code does, inputs, outputs, error conditions, safety properties, data sensitivity classification, device seizure behavior, coalition boundaries.
4. **Decompose into subtasks.** Each completes within half the remaining context window. Each produces a testable, committable result. Follow conceptual boundaries, not execution order (temporal decomposition is an Ousterhout red flag).
5. **For each subtask: plan, test, implement, verify.** One at a time. Do not start the next until the current passes tests and is committed.
6. **Comprehension check.** Explain the code in your own words. Use the generation-then-comprehension pattern. If you cannot explain it, do not commit it.
7. **Commit.** Message explains WHY. Then move to next subtask.

**Context management:** Fresh sessions over degraded conversations. Compact at 50% usage. Two-failure rule: after two failed fixes, clear and restart with better prompt.

---

## Code Review

### When to Use
Reviewing any code before merge. Preparing code for review. AI-Assisted tagged PRs. Changes touching investigation, coalition, or emotional safety.

### Layered Review Pipeline

**Layer 1 — Automated (zero human effort).** Formatting, linting, static analysis, type checking, security scanning, test suite. If any fail, fix before requesting review.

**Layer 2 — AI-assisted first pass.** AI catches: inconsistent error handling, missing null checks, unused imports, common security patterns, convention deviations, performance anti-patterns. AI misses: whether the approach is correct, business logic accuracy, long-term maintainability, meaningful test properties, concurrency issues.

**Layer 3 — Human review: design quality.** Ousterhout red flags checklist:
- Shallow module (interface as complex as implementation)
- Information leakage (implementation details escape through interface)
- Temporal decomposition (structured by execution order, not concepts)
- Pass-through method (does nothing except delegate)
- Repetition (AI duplicates at 4x normal rate)
- Special-general mixture (general code polluted with special cases)

**Layer 4 — Human review: AI-specific failures.**
- DRY violations — search before accepting
- Multi-responsibility functions — split
- Suppressed errors — verify every error path
- Hallucinated APIs — verify every external dependency exists
- Over-patterning — reject unnecessary Strategy/Factory/Observer
- **Silent failure pattern** — AI may remove safety checks, create fake matching output, or edit tests to pass rather than fixing code. Compare error handling between old and new versions explicitly. Verify ALL original safety checks are preserved.

**Layer 5 — Advocacy-specific review.**
- Data leak vectors: logging, error messages, telemetry, API responses, serialization — check for investigation data, witness identities, activist PII
- Surveillance surface area: new timestamps, access logs, IP recording, device fingerprinting usable for identification under legal discovery
- Emotional safety: progressive disclosure respected, graphic content behind opt-in, content warnings specific
- Coalition boundary violations: data crossing organizational boundaries without anti-corruption layers

**Verdict:** Distinguish blocking (security, data leaks, silent failures, broken tests) from suggestions. Two human approvals for AI-generated PRs.

---

## Security Audit

### When to Use
Before deploying to production. When new dependencies are added. When code touches investigation data, witness identities, or coalition coordination. Periodically as scheduled review.

### Process

1. **Dependency audit — slopsquatting defense.** For EVERY dependency: verify the package exists in its registry with legitimate maintainers and real commit history. ~20% of AI-recommended packages are hallucinated. A compromised dependency exfiltrates investigation data.

2. **API retention policy audit.** For every external API: verify zero-retention contractually. Check for input retention, request metadata logging, conversation history storage.

3. **Storage encryption audit.** Verify encrypted volumes with plausible deniability. Check for temp files, swap files, crash dumps with decrypted content. Test: if device powers off unexpectedly, is sensitive data recoverable without credentials?

4. **Input validation review.** 45% of AI-generated code contains OWASP Top 10 vulnerabilities. Verify SQL injection, XSS, path traversal, auth/authz defenses on every boundary. Assume adversarial input on every public surface.

5. **Instruction file integrity — Rules File Backdoor.** Inspect GEMINI.md and all instruction files for non-printable Unicode characters beyond standard whitespace. Diff changes character-by-character. Verify no instruction weakens encryption, disables safety checks, or sends data externally. In Gemini CLI, this file loads into every prompt — a compromised GEMINI.md affects all agent behavior.

6. **MCP server audit.** Verify sensitive-data servers are self-hosted. Audit data access, network egress, retention for each server.

7. **Device seizure readiness.** Remote wipe capability. Auto-locking encrypted volumes. No sensitive data in temp files, swap, or crash dumps. Test: terminate process unexpectedly, examine what remains on disk.

8. **Ag-gag exposure assessment.** Audit every data flow assuming adversarial legal discovery. Verify metadata stripping. Verify audit logs protect identities. Minimize what a court subpoena would disclose.

9. **Coalition data boundary verification.** Verify isolation between partners. Anti-corruption layers at every crossing. Data sharing agreements enforced in code. Blast radius assessment if one partner is compelled to disclose.

10. **Findings report.** Severity: Critical (active leak, missing encryption, compromised dependency, exposed identity), High (weak validation, unverified retention, unaudited MCP), Medium (incomplete metadata stripping, untested seizure, missing contract tests), Low (documentation, configuration). Block deployment on Critical or High.

---

## Code Quality — desloppify

Run desloppify to systematically identify and fix code quality issues. Install and configure (requires Python 3.11+):

```bash
pip install --upgrade "desloppify[full]"
desloppify update-skill gemini
```

Add `.desloppify/` to `.gitignore`. Before scanning, exclude directories that should not be analyzed (vendor, build output, generated code, worktrees) with `desloppify exclude <path>`. Share questionable candidates with the project owner before excluding.

```bash
desloppify scan --path .
desloppify next
```

`--path` is the directory to scan (`.` for whole project, or a subdirectory). Goal: get the strict score as high as possible — the scoring resists gaming, the only way to improve it is to actually make the code better.

**The loop:** run `next`. It tells you what to fix now, which file, and the resolve command to run when done. Fix it, resolve it, run `next` again. This is your main job. Use `desloppify backlog` only to inspect broader open work not currently driving execution.

Large refactors and small detailed fixes — do both with equal energy. Fix things properly, not minimally. Use `plan` / `plan queue` to reorder priorities or cluster related issues. Rescan periodically. The scan output includes agent instructions — follow them, do not substitute your own analysis.

---

## Gemini CLI-Specific Notes

This GEMINI.md is the only instruction file Gemini CLI reads. It loads into every prompt automatically. Keep this file under version control and review changes with the same rigor as code changes.

**Sandbox mode.** When running Gemini CLI in sandbox mode, the agent executes in a restricted environment. Verify the sandbox boundary does not allow data leakage to host filesystem locations outside the project. For advocacy projects, sandbox mode is recommended for any task involving dependency installation or code execution — it prevents a compromised or hallucinated dependency from accessing investigation data outside the workspace.

**Tool confirmations.** Gemini CLI prompts for confirmation before executing certain tool actions. Do not auto-approve tool confirmations in advocacy projects handling sensitive data. Review each confirmation to verify the action is appropriate — especially file writes, network requests, and command execution. A malicious prompt injection through code comments or dependency files could trigger tool actions that exfiltrate data.

**Context budget.** This file consumes context in every prompt. Every line must earn its place. If Gemini CLI behavior degrades, check whether this file has grown beyond the effective instruction budget (~150-200 instructions reliably followed by frontier models). Prefer dense, high-signal content over verbose explanations.

## GEO + SEO — Advocacy Website Visibility

SEO and GEO (Generative Engine Optimization) ensure advocacy content ranks in search engines and appears in AI answer systems (ChatGPT, Perplexity, Google AI Overviews, Claude, Gemini). ~60% of searches now end without a click. Apply these rules when building or modifying any public-facing advocacy website.

**How AI citation works:** Google generates an answer first, then scores content using embedding distance. Only 17-32% of AI Overview citations come from pages ranking in the top 10. Domain Authority correlates with AI citations at r=0.18; topical authority (r=0.40) and brand mentions (r=0.664) are the real predictors.

**Core Web Vitals (March 2026 thresholds):** LCP ≤ 2.5s, INP ≤ 200ms (replaced FID), CLS ≤ 0.1. Use `scheduler.yield()` to break long tasks for INP. Require SSR or SSG — AI crawlers do not execute JavaScript. Target TTFB < 200ms; page weight < 1MB. Preload LCP element; add explicit `width`/`height` on all images; use `loading="lazy"` for below-fold images; use WebP/AVIF with `<picture>` fallbacks.

**HTML structure:** One `<h1>` per page. Question-format `<h2>` headings (7× AI citation impact for smaller sites). Answer-first paragraphs: 40-60 words. Self-contained 120-180 word content modules. Semantic HTML, `lang` attribute on `<html>`, descriptive `alt` text, meaningful anchor text. `<table>` for comparisons, `<ol>`/`<ul>` for lists, `<blockquote cite="...">` for quotations (+28-40% AI visibility). `id` attributes on all headings.

**Semantic writing for AI retrieval:** Primary entity as grammatical subject in active voice (salience 0.74 vs passive 0.11). Self-contained atomic claims — every sentence makes sense in isolation. Proper noun density 20.6% (vs 5-8% standard). Content density 5,000-20,000 characters for optimal AI retrieval. Open every section with a 40-60 word declarative answer.

**Content strategy:** Match the intent format of top-ranking results before writing. Helpful Content System: content must be primarily for users, not search engines. E-E-A-T: demonstrate Experience (original data, case studies), Expertise (specific citations with named sources and dates), Authoritativeness (third-party coverage), Trustworthiness (contact info, privacy policy, HTTPS). Every content page: visible author name, credentials, link to author profile with Person schema (+40% AI citations).

**Wikipedia and Wikidata (highest-leverage off-site action):** Wikipedia = 47.9% of ChatGPT's top-10 citations. Organizations with Wikidata entries get Knowledge Panels within 7 days. Add Wikipedia URL and Wikidata Q-ID to Organization schema `sameAs`. Build entity web: organization → tools → people → related orgs → policy areas.

**Wikipedia COI (mandatory):** Never directly edit your own organization's Wikipedia article. Disclose affiliation on the Talk page. Propose edits through Talk-page requests or neutral editors. Use only independent, reliable sources.

**Structured data (JSON-LD):** 41% AI citation rate with schema vs 15% without. Required on every page: Organization + WebSite schema (with `sameAs` to Wikipedia and Wikidata). Required on content pages: Article schema with `author`, `datePublished`, `dateModified`. Required on Q&A pages: FAQPage schema. Also implement: BreadcrumbList, Person (author pages), HowTo, VideoObject. Use `@id` to connect entities. Validate at https://validator.schema.org/.

**Meta tags:** Title: `Primary Keyword — Brand Name`, 50-60 chars, unique per page. Description: 150-160 chars, direct answer + one statistic, unique. `<link rel="canonical">` on every page. Full Open Graph and Twitter Card tags. Article timestamps in ISO 8601 format.

**Robots.txt — allow AI citation crawlers:** `OAI-SearchBot`, `ChatGPT-User`, `PerplexityBot`, `ClaudeBot`, `Claude-SearchBot`, `Applebot`, `Amazonbot`. Blocking Googlebot blocks both Google Search and AI Overviews. Add `Sitemap:` directive.

**Sitemap + IndexNow:** Canonical URLs only; `<lastmod>` reflects actual updates (never faked). Submit to Google Search Console and Bing Webmaster Tools. IndexNow notifies Bing (which feeds ChatGPT) instantly on publish — integrate into CI/CD.

**Site architecture:** Descriptive hyphenated lowercase URLs, max 3 levels deep, canonical tags, 301 redirects. Hub-and-spoke topic clusters: pillar page (2,000-4,000 words) + 8-15 cluster pages + bidirectional links = citation rate 12% → 41%. Content freshness: visible `<time>` Last Updated dates, `dateModified` synchronized, genuinely updated not just date-changed.

**Platform presence and brand signals:** 85% of AI brand mentions from third-party pages. Platform trust: YouTube (~23.3% AI citations), Wikipedia (~18.4%), Reddit (up to 46.5% Perplexity citations). Authentic participation in relevant subreddits, YouTube transcripts, LinkedIn posts, GitHub documentation. Monitor unlinked brand mentions; convert high-authority ones to backlinks (>30% close rate).

**Conversion optimization:** Donation pages: 3-4 preset amounts with middle pre-selected and impact descriptions. Pre-select monthly giving (64% of nonprofits still default one-time). Single-step forms (52% drop with multi-step). Remove header navigation during donation flow. 3-5 form fields maximum. Dark patterns carry FTC legal risk.

**Analytics:** Use Plausible or Umami as primary (no cookies, ~1KB script). Track AI referral traffic with a custom GA4 channel group matching `chatgpt.com`, `perplexity.ai`, `claude.ai`, `gemini.google.com`. AI referral traffic grew 357% YoY to 1.1B visits (June 2025). Mark conversions: `donation_completed`, `newsletter_signup`, `volunteer_form_submit`. **i18n:** Use next-intl with subdirectory URLs (`/en/`, `/hi/`, `/ar/`). Set `lang` and `dir` on `<html>`. Hreflang must be self-referencing and reciprocal — 31% of international sites have broken hreflang. Use ICU MessageFormat for plurals (Arabic requires 6 CLDR plural categories).

**Defensive awareness:** Prohibited and actively detected: hidden text (white-on-white, zero-size fonts, invisible Unicode U+E0000-U+E007F), agent-aware cloaking (serving different content to AI crawlers), scaled AI content without human review (Google manual actions since June 2025). Penalties are domain-wide.

**Key statistics:**

| Signal | Impact |
|--------|--------|
| LCP ≤ 2.5s (Good threshold) | Sites above 3s see 23% more traffic loss |
| INP > 200ms | -0.8 average position drop; 43% of sites fail |
| Structured data (schema) | 73% higher AI selection rate |
| Wikipedia/Wikidata presence | Knowledge Panel within 7 days |
| Topic cluster architecture | Citation rate 12% → 41% |
| Fresh content (within 30 days) | 76% of most-cited; 3.4× Perplexity advantage |
| Original or proprietary data | 4.31× citations per URL; 156% more links |
| Author metadata | +40% citations |
| Brand mentions vs AI citations | r=0.664 — strongest signal |
| AI referral traffic growth | 357% YoY to 1.1B visits (June 2025) |
| Pre-selecting monthly giving | 31% of nonprofit online revenue |
