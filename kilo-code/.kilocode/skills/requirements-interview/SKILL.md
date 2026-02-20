---
name: requirements-interview
description: Structured stakeholder interview for advocacy projects — gathers purpose, threat model, coalition needs, legal exposure, user safety requirements, and budget constraints one question at a time
---
# Requirements Interview

## When to Use
- Starting a new feature or project
- When requirements are ambiguous or incomplete
- Before writing a specification or design document
- When a new coalition partner or user group is introduced

## Process

Ask one question at a time. Use multiple choice when possible. Wait for the answer before proceeding. Do not overwhelm stakeholders with a wall of questions — advocacy stakeholders are often volunteers with limited time.

### Phase 1: Purpose and Users
1. What are we building? (One sentence describing the core function)
2. Who are the primary users? (Investigators, campaign organizers, sanctuary staff, legal team, coalition coordinators, public supporters)
3. What does success look like? (Specific, measurable criteria — not "make it better")
4. What existing tools or workflows does this replace or augment?

### Phase 2: Threat Modeling
5. Who are the adversaries for this system?
   - [ ] Law enforcement (ag-gag statutes, warrants, subpoenas)
   - [ ] Industry investigators (corporate surveillance, infiltration)
   - [ ] Hostile public (doxxing, harassment campaigns)
   - [ ] AI model providers (data retention, content policy restrictions)
   - [ ] Other: ___
6. What happens if this system is compromised? (Who is endangered, what evidence is exposed, what legal liability)
7. What happens if a device running this software is seized? (What data is recoverable, what operations exposed)
8. What legal jurisdictions apply? (Which ag-gag laws, data protection regulations, countries)

### Phase 3: Coalition and Data Boundaries
9. Which organizations will use this system?
10. Do organizations have different risk profiles? (Direct action group vs. legal defense fund = different threat models)
11. What data crosses organizational boundaries? What must NOT cross?
12. If one partner is legally compelled to disclose, what is the blast radius to other partners?
13. What existing data sharing agreements constrain the design?

### Phase 4: User Safety
14. Does this system handle traumatic content? (Investigation footage, slaughter documentation, witness testimony)
15. What progressive disclosure levels are needed? (Text-only, blurred preview, full resolution)
16. Who reviews traumatic content, and what burnout prevention measures exist?
17. Does this system handle witness or whistleblower identities? What anonymization requirements?
18. What emotional safety features do users expect? (Content warnings, session time reminders, configurable detail)

### Phase 5: Technical Constraints
19. Budget — hard limits on infrastructure and AI compute costs? (Every dollar has an alternative use in direct advocacy)
20. Timeline — deadline and what drives it? (Legislative session, planned investigation, campaign launch)
21. Tech stack preferences or constraints? (Existing infrastructure, team skills, self-hosted requirements)
22. Connectivity constraints? (Offline-first, low-bandwidth, mesh networking)
23. Language and accessibility requirements? (Which languages, low-literacy users, assistive technology)

### Phase 6: Synthesize
After gathering answers, produce a specification document:
- **Purpose statement** — one paragraph
- **User personas** — who uses this, risk profiles
- **Threat model** — adversaries, attack surfaces, legal exposure
- **Data boundaries** — what is stored, where, who accesses, what crosses org boundaries
- **Success criteria** — measurable outcomes
- **Safety requirements** — emotional safety, anonymization, progressive disclosure
- **Constraints** — budget, timeline, technology, connectivity, language
- **Open questions** — what needs clarification before design

Present the synthesized spec for stakeholder confirmation before proceeding to design.
