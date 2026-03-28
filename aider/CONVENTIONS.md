# Animal Advocacy Platform — Development Conventions

This is software for animal liberation and advocacy. It is a high-risk domain: investigation data is subpoena-target evidence, activists face legal prosecution under ag-gag statutes, and system compromise endangers lives. Every design decision must account for adversarial legal discovery, device seizure, and coalition partners with different risk profiles. The three adversaries are **state surveillance** (law enforcement, warrants, subpoenas), **industry infiltration** (corporate investigators, social engineering), and **AI model bias** (training data encoding industry framing, telemetry leaking investigation details).

---

## Workflow

Read existing code before writing anything — AI duplicates existing logic at 4x the normal rate because it lacks full codebase awareness. Plan before code: read, plan, code, verify. Write a specification before implementation. Write a failing test before writing code. After two failed fix attempts, stop and re-approach with a better prompt rather than compounding errors.

When using Aider's `/architect` mode, use it for planning and design — explore the codebase, identify bounded contexts, and draft the spec before switching to `/code` mode for implementation. Never start in `/code` mode on an unfamiliar part of the codebase.

---

## Design Principles Review Checklist

Before finishing any task, verify AI output against these ten failure modes, ranked by frequency and impact in AI-generated code:

1. **DRY** — AI clones existing logic at 4x the normal rate. Search the codebase before writing anything new. Keep a mental map of existing utilities.
2. **Deep modules over shallow wrappers** — Reject thin wrappers and pass-through methods that add interface surface without hiding complexity. If the interface is as complex as the implementation, the abstraction is shallow.
3. **Single responsibility** — Each function does one thing at one level of abstraction. AI produces multi-responsibility functions by default; check function length and responsibility count first.
4. **Error handling** — AI suppresses errors, catches too broadly, and removes safety checks. In advocacy code, silent failure means evidence loss or exposed activists. Verify every error path. Never catch-all or silently swallow failures.
5. **Information hiding** — Expose only what callers need. AI leaks implementation details across module boundaries.
6. **Ubiquitous language** — Code must use movement terminology (campaign, investigation, coalition, sanctuary), not AI-invented synonyms. Language drift causes miscommunication across coalition partners.
7. **Design for change** — Insist on abstraction layers and loose coupling. AI optimizes for "works now" over "works later," but advocacy tools must outlast any single campaign. Abstract all vendor dependencies behind project-owned interfaces.
8. **Legacy code velocity** — AI code churns 2x faster (replaced within weeks). Apply characterization tests before modifying AI-generated modules. Feathers' legacy code techniques are relevant after months of AI-assisted development, not years of neglect.
9. **Over-patterning** — AI forces Strategy/Factory/Observer where a plain function and conditional suffice. Use the simplest structure that works.
10. **Test quality** — AI generates tests that look thorough but verify nothing. Mutation testing is the countermeasure for tautological assertions.

---

## Advocacy Domain Language

Use these terms consistently in code, documentation, and conversations. NEVER introduce synonyms.

- **Campaign** — Organized effort toward a specific advocacy goal (legislative, corporate, public awareness). Has start, milestones, success criteria.
- **Investigation** — Covert documentation of animal exploitation. Legally sensitive. All data is potential evidence.
- **Coalition** — Alliance of organizations with shared goals but different risk profiles and data policies.
- **Witness** — Person providing testimony about exploitation conditions. Identity requires maximum protection.
- **Testimony** — Witness account. Subject to consent verification before any use.
- **Sanctuary** — Permanent animal care facility. Distinct from shelter (temporary) or foster (individual).
- **Rescue** — Removing animals from exploitative conditions. Jurisdiction-dependent legal status.
- **Liberation** — Direct action to free animals. Distinct legal implications from rescue.
- **Direct Action** — Physical intervention in exploitation. Legally distinct from campaigning or lobbying.
- **Undercover Operation** — Investigation by operative embedded in an exploitative facility. Highest legal risk.
- **Ag-Gag** — Laws criminalizing undercover investigation of agricultural operations. Determines legal exposure for investigation data.
- **Factory Farm** — Industrial animal agriculture facility. Use this term, not euphemisms.
- **Slaughterhouse** — Facility where animals are killed commercially. Use precisely.
- **Farmed Animal** — Animals raised for food, fiber, or commercial products. Not "livestock" (industry framing).
- **Evidence** — Documentation of exploitation with potential legal use.

### Bounded Contexts

These are separate domains with different models, rules, and security requirements. Do not merge them. Data must not flow between them without explicit anti-corruption layers.

- **Investigation Operations** — Covert data collection, evidence management, chain of custody. Highest security. Data never flows outward without explicit declassification.
- **Public Campaigns** — Public-facing advocacy, supporter engagement, media. Lower security but high visibility. An "activist" here is a fundamentally different entity than an "investigator" in an undercover operation.
- **Coalition Coordination** — Multi-organization planning, shared resources, joint strategy. Data crosses organizational boundaries and must be governed by the strictest partner's policies.
- **Legal Defense** — Case management, attorney-client privilege, court filings. Privilege requirements override other policies.

AI agents blur bounded context boundaries because they optimize for making code work, not for maintaining conceptual boundaries. When an agent needs data from another context, it will import directly rather than going through an anti-corruption layer. Reject this.

### Compassionate Language — No Speciesist Idioms

Code, documentation, comments, commit messages, and variable names must use compassionate, non-speciesist language. AI agents frequently generate common English idioms that normalize animal violence — reject these and use alternatives. Examples: "kill two birds with one stone" → "accomplish two things at once"; "beat a dead horse" → "belabor the point"; "more than one way to skin a cat" → "more than one way to solve this"; "guinea pig" → "test subject"; "cattle vs. pets" → "ephemeral vs. persistent"; "master/slave" → "primary/replica"; "whitelist/blacklist" → "allowlist/denylist". For automated enforcement covering 60+ speciesist patterns, see: https://github.com/Open-Paws/no-animal-violence (core rules) and integrations for Semgrep, ESLint, Vale, pre-commit, GitHub Actions, VS Code, and Reviewdog at https://github.com/Open-Paws.

---

## Testing

Testing is the keystone. Without tests, AI agents drift silently — in advocacy software, silent drift means lost evidence, exposed activists, or traumatic content displayed without safeguards.

**Assertion quality is the non-negotiable.** NEVER accept tautological assertions — tests that assert output equals the output of the same function call. Every assertion must encode a business rule you can explain in words. Ask three questions of every AI-generated test: (1) Does this test fail if the code is wrong? (2) Does the assertion encode a domain rule? (3) Would mutation testing kill this? Quality metric: mutation score over coverage percentage.

**Spec-first test generation preferred.** Generate tests from specifications before writing implementation — not after. Tests generated from existing implementation mirror the code rather than the intent, producing circular validation.

**Property-based testing for invariants.** Verify that invariants hold across random inputs. Critical advocacy invariants: anonymization must be irreversible, encryption must not leak plaintext length, coalition data boundaries must hold under arbitrary input combinations.

**Test error paths explicitly.** AI-generated tests overwhelmingly cover happy paths. In advocacy software, error paths are where people get hurt — failed encryption, leaked identity, broken anonymization, missing content warnings.

**Contract tests at service boundaries.** AI hallucinates API contracts (~20% of recommended packages do not exist). At every service boundary, especially coalition cross-organization APIs, use consumer-driven contract tests.

**Fast execution is non-negotiable.** AI agents run tests in tight loops. A 10-minute suite across 15 iterations burns 2.5 hours. Invest in parallel execution, test isolation, and selective test running. Flaky tests poison the AI feedback loop — agents cannot distinguish flaky from real failures.

**Adversarial input testing.** Test inputs crafted to exploit advocacy-specific vulnerabilities: SQL injection through investigation search, XSS through testimony display, path traversal through evidence uploads.

---

## Security

Advocacy software faces three distinct adversaries requiring different countermeasures.

**Zero-retention APIs.** NEVER send sensitive data to services that retain inputs. Investigation footage, witness identities, activist communications — only zero-retention configurations. Verify retention policies contractually, not by assumption. Telemetry to third parties is a data exfiltration vector under adversarial legal discovery.

**Encrypted local storage with plausible deniability.** All investigation data and activist records MUST use encrypted volumes. Design storage so the existence of sensitive data is deniable under device seizure — nested encrypted containers where the outer layer contains innocuous data and the inner layer requires a separate key.

**Supply chain verification — slopsquatting defense.** Approximately 20% of AI-recommended packages do not exist — they are hallucinated names. Attackers register these as real packages with malicious code (one was downloaded 30,000+ times in weeks). Verify EVERY dependency exists in its registry and has legitimate maintainers before installation. In advocacy software, a compromised dependency can exfiltrate investigation data or activist identities.

**Input validation against industry sabotage.** Assume adversarial input on every public-facing surface. Industry actors will probe investigation submission forms and evidence upload endpoints. AI-generated input validation is weak: 45% of AI-generated code contains OWASP Top 10 vulnerabilities, with 86% XSS failure rate.

**Ag-gag legal exposure vectors.** Investigation footage is discoverable evidence. Design every data flow assuming adversarial legal discovery. Metadata (timestamps, geolocation, device IDs) can be more damaging than content — strip aggressively. Audit logs must protect the identities they record.

**Device seizure preparation.** Remote wipe capability for sensitive data. Encrypted volumes that lock automatically on suspicious conditions. No temporary files with decrypted content, no swap files with sensitive state, no crash dumps with investigation data.

**Instruction file integrity — Rules File Backdoor.** The "Rules File Backdoor" attack uses hidden Unicode characters in instruction files to inject invisible directives that make AI produce malicious output. Treat ALL instruction files as security-critical artifacts. Review for non-printable characters. Diff changes character-by-character. A compromised instruction file could direct the AI to weaken encryption, leak data, or disable safety checks.

**Provider routing for sensitive data.** When using AI coding assistants with multiple model providers, sensitive advocacy data (investigation content, witness identities, legal defense materials) must NEVER route through free-tier providers that may retain inputs. Free-tier APIs may retain inputs for training or compliance — assume they do unless contractually guaranteed otherwise. Route sensitive work exclusively through zero-retention providers or self-hosted inference.

**Self-hosted inference for critical paths.** Any code path handling investigation data, witness identities, or legal defense materials should use self-hosted AI inference. Model providers may comply with government data requests.

---

## Privacy

Privacy in advocacy software is the difference between operational security and activist prosecution. Data that seems harmless in isolation becomes evidence under ag-gag statutes: participation timestamps, IP addresses, device fingerprints can identify investigators and rescue coordinators.

**Data minimization as default.** Collect the absolute minimum for each function. Before adding any field, ask: if this data appeared in a court filing, who would it endanger?

**Activist identity protection.** Use pseudonymous identifiers. Never store legal names alongside action records. Separate authentication identity from operational identity — the login system must not be the system recording who participated in which investigation.

**GDPR/CCPA as floor, not ceiling.** Right to deletion MUST be real deletion — not soft delete with a `deleted_at` flag. "Deleted" records surfacing in legal discovery destroy trust and endanger people. Erasure must be irrecoverable from all storage layers including backups, replicas, indices, and logs.

**Consent as ongoing process.** Implement re-consent for scope changes. Participation in a public campaign does not imply consent to be recorded as an investigation participant. Withdrawal must be immediate.

**Coalition data sharing across risk profiles.** Classify each partner's risk level. Apply the strictest handling rules of any partner in the exchange. Strip identifying information before sharing across risk tiers. Design data sharing agreements that specify what happens when a partner is compromised.

**Whistleblower and witness protection.** End-to-end encryption for all whistleblower communications. No server-side access to decrypted content. Anonymous submission channels without account creation. Zero-knowledge architectures where even administrators cannot identify whistleblowers.

---

## Cost Optimization

Every dollar spent on AI compute is a dollar not spent on investigations, legal defense, or sanctuary operations.

**Model routing.** Use cheaper models for: test generation, boilerplate, formatting, simple refactoring, documentation. Use capable models for: debugging, multi-file changes, code review. Reserve frontier models for: hard architectural problems, complex debugging, security-critical review. Aider achieves comparable benchmark scores at 3x fewer tokens than some alternatives — use `/architect` for planning (where reasoning matters) and `/code` for implementation (where speed matters).

**Token budget discipline.** Set hard limits per session and per day. A runaway conversation can consume a week's budget. When hitting the ceiling, stop and reassess approach.

**Prompt cache optimization.** Place static content first in prompts for 80%+ cache hit rates. This CONVENTIONS.md loads as read-only context — its position at the start of every prompt is inherently cache-friendly.

**Budget allocation.** 40% implementation, 30% testing, 20% review and debugging, 10% documentation. If testing drops below 30%, downstream bug costs multiply.

**Vendor lock-in as movement risk.** Abstract model dependencies behind project-owned interfaces. A nonprofit locked to one provider faces existential budget exposure on price changes and policy restrictions on advocacy use cases. Maintain self-hosted fallback capability for critical paths.

---

## Accessibility

Advocacy networks span borders, languages, economic conditions, and infrastructure environments. An activist coordinating a rescue in a rural area with intermittent connectivity has fundamentally different needs than an organizer at a well-resourced urban nonprofit.

**i18n from day one.** Externalize all user-facing strings from the start. Support right-to-left layouts. Never retrofit — the cost grows exponentially with codebase size.

**Low-bandwidth optimization.** Compress assets, lazy-load non-critical content, minimize payloads, transfer only deltas. A tool requiring broadband excludes the activists who need it most.

**Offline-first architecture.** Design for disconnected operation as default. Local-first data storage with background sync. Conflict resolution for offline-modified data. Queue operations during disconnection. The application must be fully functional for core workflows without network access.

**Low-literacy design.** Icons alongside text labels, visual workflows, voice input support, progressive disclosure to avoid information density overload.

**Mesh networking compatibility.** Design sync protocols for high-latency, low-bandwidth, intermittent peer availability. Activists in regions with government internet shutdowns depend on mesh-capable tools.

**Graceful degradation.** Every feature must have a degraded mode. If encryption fails to load, refuse to transmit sensitive data — never transmit plaintext. Degrade capability, never safety.

**Device seizure — application state.** When connectivity is lost suddenly, the application must not leave sensitive data exposed. No temp files with decrypted content, no in-memory caches persisting to swap, no crash dumps with witness identities.

---

## Emotional Safety

Advocacy software handles content documenting extreme suffering: factory farm conditions, slaughterhouse footage, witness testimony of abuse. Uncontrolled exposure causes measurable psychological harm.

**Progressive disclosure of traumatic content.** NEVER display graphic content by default. Every piece of investigation footage or exploitation imagery must be behind at least one intentional interaction. Default state: blurred, hidden, or text description. Users escalate through deliberate choices, never automatic loading.

**Configurable detail levels.** Three tiers minimum: (1) text-only descriptions, (2) blurred/low-detail with context, (3) full resolution. Persist preference across sessions. Different roles need different defaults — legal reviewer vs. campaign coordinator.

**Content warnings — mandatory before display.** Every piece of content involving animal suffering MUST have a specific warning describing what it contains. Generic "sensitive content" warnings are insufficient — specify: graphic injury, death, distress vocalizations, confined conditions, slaughter processes.

**Investigation footage handling.** NEVER auto-play. ALWAYS blurred by default. Require explicit opt-in for full resolution. Strip audio by default — distress vocalizations cause acute stress responses. Support frame-by-frame navigation and annotation without full-resolution viewing.

**Witness testimony display.** Verify display consent is current. Anonymize by default. Require opt-in for identifying details.

**Burnout prevention.** Track continuous exposure time to traumatic content. Surface non-intrusive reminders after configurable intervals. Provide session summaries so reviewers do not re-expose themselves. Support distributing content review across team members.

**Secondary trauma mitigation for developers.** Use abstract test data in automated tests, not actual footage. Provide mock data generators producing metadata without graphic content. CI/CD must never display graphic content in output, logs, or failure reports.

---

## Git Workflow

Use Aider's automatic commit feature — every change is committed with a sensible message. Layer human judgment on top.

**Ephemeral branches.** Create short-lived branches per task. Trunk-based development remains the goal — branches are safety nets, not long-lived workspaces. If no mergeable work within one session, delete the branch and reconsider.

**One subtask, one commit.** Break tasks into smallest logical subtasks. If the task decomposes into "extract interface, implement adapter, update callers," those are three commits. Test before each commit — every commit must leave the codebase passing.

**PR curation.** PR curation is the critical human skill. AI inflated PR size by 154%. Split into reviewable chunks: target under 200 lines changed, ideally under 100. Use stacked PRs for large changes. Each PR tells a coherent story.

**Tag and review.** Tag every PR containing AI-generated code as AI-Assisted. Require two human approvals for primarily AI-generated PRs. Call out security boundaries and investigation/coalition data handling.

**Quality signals.** Code Survival Rate — how much AI code remains unchanged 48 hours after merge. Healthy suggestion acceptance rate: 25-35%; higher may indicate over-reliance.

**Merge strategy.** Squash-merge ephemeral branches. Delete immediately after merge.

---

## Testing Strategy

### When to Use
When writing or generating any tests, reviewing AI-generated test code, or when test quality is in question.

### Process
1. **Read the specification.** Identify acceptance criteria before writing any test. Without a spec, AI generates tests mirroring implementation rather than intent.
2. **Write failing tests from spec.** Generate tests from specification BEFORE implementation. Each test encodes a business rule stated in words. Verify tests fail for the right reason.
3. **Implement until tests pass.** Write minimum code the tests demand.
4. **Review assertions against spec, not code.** The critical step for AI-generated tests.
5. **Run mutation testing.** Surviving mutants reveal weak assertions. Feed surviving mutants to the AI and ask for tests that kill them.

### Five Generation Patterns
1. **Implementation-first** — Dangerous: tests mirror code. Use only for characterization tests on legacy code.
2. **Spec-first** — Preferred. Produces tests encoding intent, not behavior.
3. **Edge-case generation** — Give AI a function signature; ask for: empty inputs, boundaries, null, unicode, timezones, concurrency, overflow.
4. **Characterization tests** — Capture current behavior before changing legacy/AI-generated code.
5. **Mutation-guided** — Run mutation testing, feed surviving mutants to AI, generate targeted tests.

### Five Anti-Patterns to Reject
1. **Snapshot trap** — Tests snapshotting current output. Pass today, break on any correct change. Verify nothing about correctness.
2. **Mock everything** — Over-mocked tests verify mock behavior, not real code. Mock only at system boundaries.
3. **Happy path only** — AI tests overwhelmingly test success paths. Explicitly demand error, boundary, and adversarial input tests.
4. **Test-after-commit** — Tests after code is committed defeat the feedback loop. Tests must exist during development.
5. **Coverage theater** — Chasing numbers with meaningless assertions. A "covered" line with no assertion is not tested.

---

## Requirements Gathering

### When to Use
Starting a new feature, when requirements are ambiguous, before writing specifications.

### Process
Ask one question at a time. Multiple choice when possible.

**Phase 1 — Purpose:** What are we building? Who are the users? What does success look like? What does this replace?

**Phase 2 — Threat model:** Who are the adversaries? (Law enforcement/ag-gag, industry investigators, hostile public, AI model providers.) What happens if the system is compromised? If a device is seized? Which legal jurisdictions apply?

**Phase 3 — Coalition boundaries:** Which organizations use this? Different risk profiles? What data crosses organizational boundaries? What must NOT cross? Blast radius if one partner is compelled to disclose?

**Phase 4 — User safety:** Traumatic content handling? Progressive disclosure levels? Who reviews traumatic content, and what burnout prevention exists? Witness/whistleblower anonymization? Emotional safety features?

**Phase 5 — Constraints:** Budget limits? Timeline drivers? Tech stack? Connectivity constraints (offline-first, low-bandwidth, mesh)? Language and accessibility needs?

**Phase 6 — Synthesize** into spec: purpose, personas, threat model, data boundaries, success criteria, safety requirements, constraints, open questions. Present to stakeholder for confirmation before design.

---

## Plan-First Development

### When to Use
Starting any significant work. Beginning a new session. Changes across multiple files. Use Aider's `/architect` mode for Steps 1-4, then switch to `/code` mode for Step 5.

### Process
1. **Read existing code.** Understand structure, naming, utilities, patterns. Search before writing.
2. **Identify change scope.** State in one sentence. If you cannot, decompose further. Identify affected bounded context.
3. **Write specification.** Requirements before implementation: what it does, inputs, outputs, error conditions, security properties, data sensitivity, seizure behavior, coalition boundaries.
4. **Break into subtasks.** Each produces a testable, committable result. Follow conceptual boundaries, not execution order (temporal decomposition is a red flag).
5. **For each subtask: plan, test, implement, verify.** One at a time. Do not start the next until current passes and is committed.
6. **Comprehension check.** Explain what the AI generated in your own words before committing. AI-assisted developers score 17 percentage points lower on comprehension tests. Use the **generation-then-comprehension** pattern: generate code, immediately ask the AI to explain it, verify your understanding matches. This preserves learning while leveraging speed. If you cannot explain the code, do not commit it.

### Context Management
Start sessions fresh. Break work into chunks completing within half the context window. After two failed fixes, clear conversation and restart with better prompt.

---

## Code Review

### When to Use
Reviewing any code before merge. Preparing code for review. When a PR is tagged AI-Assisted. When changes touch investigation data, coalition boundaries, or emotional safety.

### Layered Review Pipeline

**Layer 1 — Automated (zero human effort):** Formatting, linting, static analysis, type checking, security scanning, test suite. Fix failures before requesting review.

**Layer 2 — AI-assisted first pass:** AI catches: inconsistent error handling, missing null checks, unused imports, common security patterns, convention deviations, performance anti-patterns. AI misses: whether the approach is correct, whether business logic matches requirements, maintainability, meaningful test properties, concurrency issues.

**Layer 3 — Human review: design red flags (Ousterhout):**
- Shallow module — interface as complex as implementation
- Information leakage — implementation details escape through interface
- Temporal decomposition — structured by execution order, not concepts
- Pass-through method — does nothing except delegate
- Repetition — same logic in multiple places (AI duplicates at 4x rate)
- Special-general mixture — general code polluted with special cases

**Layer 4 — Human review: AI-specific failures:**
- DRY violations — duplicates existing codebase functions
- Multi-responsibility functions — does more than one thing
- Suppressed errors — safety checks removed, exceptions caught too broadly
- Hallucinated APIs — calls to libraries/methods/endpoints that do not exist
- Over-patterning — patterns where conditionals suffice
- **Silent failure pattern** — AI may remove safety checks to make code appear to work, create fake output matching desired formats, or edit tests to pass rather than fixing underlying code. Verify ALL safety checks from original code are preserved.

**Layer 5 — Advocacy-specific:**
- Data leak vectors — new paths for sensitive data to leave the system (logging, error messages, telemetry, serialization)
- Surveillance surface area — new timestamps, access logs, IP recording, device fingerprinting usable to identify activists under legal discovery
- Emotional safety — progressive disclosure respected, graphic content behind opt-in, content warnings specific enough
- Coalition boundary violations — data crossing organizational boundaries without anti-corruption layer

---

## Security Audit

### When to Use
Before deploying changes. When new dependencies are added. When code touches investigation data, witness identities, or coalition coordination.

### Process
1. **Dependency audit — slopsquatting defense.** For EVERY dependency: verify package exists in registry, has legitimate maintainers, version is published. ~20% of AI-recommended packages are hallucinated.
2. **API retention policy audit.** Verify zero-retention contractually for every external API touching sensitive data.
3. **Storage encryption audit.** Verify encrypted volumes with plausible deniability. Check for temp files, swap files, crash dumps with decrypted content.
4. **Input validation review.** Verify defenses against SQL injection, XSS, path traversal, auth bypass on every input boundary.
5. **Instruction file integrity check.** Inspect instruction files for hidden Unicode (Rules File Backdoor). Diff character-by-character. Verify no file weakens encryption or leaks data.
6. **Device seizure readiness.** Remote wipe exists. Encrypted volumes auto-lock on suspicious conditions. Kill the process unexpectedly and examine what remains on disk.
7. **Ag-gag exposure assessment.** Audit data flows assuming adversarial legal discovery. Verify metadata stripping. Check: if a court subpoena targeted this system, what would be disclosed?
8. **Coalition data boundary verification.** Verify isolation between partners. Anti-corruption layers at every crossing. Blast radius assessment if one partner is compelled to disclose.
9. **Findings report.** Classify: Critical (active leak, missing encryption, compromised dependency, exposed witness), High (weak validation, unverified retention), Medium (incomplete metadata stripping, untested seizure scenario), Low (documentation gaps). Block deployment on Critical or High.

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

Websites built for animal advocacy serve two discovery channels: traditional search engines and AI answer systems (ChatGPT, Perplexity, Google AI Overviews, Claude, Gemini, Bing Copilot). Approximately 60% of searches end without a click — AI systems are the fastest-growing discovery channel with distinct citation requirements. Apply these rules when building or modifying any public-facing advocacy website.

**HTML structure.** Every page needs exactly one `<h1>` containing the primary topic. Use a logical heading hierarchy (h1 > h2 > h3), never skipping levels. Phrase h2 headings as questions — question-based headings produce 7× more AI citations for smaller sites. The first paragraph after any heading must directly answer that question in 40-60 words; AI systems pull from the first 30% of content 44% of the time. Keep paragraphs to 2-4 sentences (40-60 words). Structure content as self-contained 120-180 word modules — this modular pattern generates 70% more ChatGPT citations than unstructured prose. Use semantic HTML correctly: article, section, nav, aside, header, footer, main. Add lang attribute to html element. Every img must have descriptive alt text. Every anchor must have meaningful text — never "click here". Use table for comparison data (32.5% of AI-cited content uses tables), ol and ul for lists (78% of AI answers include list formats), blockquote with cite attribute for expert quotations (+28-40% AI visibility). Flag any content rendered exclusively by JavaScript — AI crawlers often skip JS rendering. Do NOT keyword-stuff — stuffing decreases AI visibility by 10%.

**Structured data (JSON-LD).** This is the single highest-leverage GEO action: 41% citation rate with schema vs 15% without, yet only 12.4% of websites implement it. Every page needs Organization + WebSite schema in a @graph array. Every content page needs Article schema with headline, author (with name, url, jobTitle), publisher, datePublished, dateModified, image, and description. Any page with Q&A content needs FAQPage schema with 40-80 word direct answers per question. Also implement when applicable: HowTo, BreadcrumbList, SoftwareApplication, Event, Dataset, Person. Always use JSON-LD format, not Microdata. Keep dateModified accurate. Validate at schema.org/validator.

**Meta tags.** Title tag: Primary Keyword — Brand Name, 50-60 chars, keywords first, unique per page. Meta description: 150-160 chars, direct factual answer to the primary query, one specific statistic, never duplicated across pages. Every page needs a canonical link tag, full Open Graph tags (og:title, og:description, og:type, og:url, og:image, og:site_name), Twitter Card tags, and article timestamp tags in ISO 8601 format.

**robots.txt.** Allow AI citation crawlers — they power AI answer systems: OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Claude-SearchBot, Applebot, Amazonbot. Optionally block AI training crawlers if not consenting to training use: GPTBot, CCBot, Google-Extended. Include a Sitemap directive. Note: blocking Googlebot blocks both Google Search AND Google AI Overviews — there is no way to separate them.

**Sitemap and architecture.** XML sitemap at /sitemap.xml with accurate lastmod dates — never fake them. Submit to Google Search Console and Bing Webmaster Tools. Regenerate automatically on content changes. Use descriptive hyphenated lowercase URLs under 75 characters, max 3 levels deep, canonical tags on every page. Implement hub-and-spoke topic cluster model: pillar page (2,000-4,000 words) + 8-15 cluster pages with bidirectional links — increases AI citation rate from 12% to 41%. Display "Last Updated" visibly with time[datetime] tag; synchronize with dateModified in schema (76% of most-cited AI content was updated within 30 days).

**Performance.** AI crawlers timeout at 1-5 seconds: TTFB under 200ms, LCP under 2.5s, CLS under 0.1, page weight under 1MB. Require SSR or SSG — AI crawlers often skip JavaScript rendering. Enforce HTTPS.

**Content patterns that earn AI citations.** Citable paragraph: direct statement of fact, specific statistic with attribution, brief elaboration, named source and date. Author attribution on every content page — visible name, credentials, link to profile page with Person schema — increases AI citations by 40%. Pages over 2,900 words are 59% more likely to be cited. Original or proprietary data generates 4.31× more citations per URL. Adding statistics to claims increases AI visibility by 41%. Citing credible sources inline increases AI visibility by 30-40%. Expert quotations increase AI visibility by 28-40%.
