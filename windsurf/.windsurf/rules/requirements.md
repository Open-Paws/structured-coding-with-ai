<!-- trigger: manual -->
# Requirements Interview

## When to Use
Starting a new feature or project, ambiguous requirements, before writing a spec, when a new coalition partner or user group is introduced.

## Process
Ask one question at a time. Multiple choice when possible. Wait for answers. Do not overwhelm stakeholders — advocacy stakeholders are often volunteers with limited time.

### Phase 1: Purpose and Users
1. What are we building? (One sentence, core function)
2. Who are the primary users? (Investigators / campaign organizers / sanctuary staff / legal team / coalition coordinators / public supporters)
3. What does success look like? (Specific, measurable)
4. What existing tools or workflows does this replace?

### Phase 2: Threat Modeling
5. Who are the adversaries?
   - Law enforcement (ag-gag, warrants, subpoenas)
   - Industry investigators (surveillance, infiltration)
   - Hostile public (doxxing, harassment)
   - AI model providers (data retention, content restrictions)
6. What happens if the system is compromised? (Who endangered, what exposed, what liability)
7. What happens if a device is seized? (What data recoverable, what operations exposed)
8. What legal jurisdictions apply? (Ag-gag laws, data protection, countries)

### Phase 3: Coalition and Data Boundaries
9. Which organizations will use this?
10. Do they have different risk profiles?
11. What data crosses org boundaries? What must NOT cross?
12. If one partner is compelled to disclose, what is the blast radius?
13. Existing data sharing agreements or policies?

### Phase 4: User Safety
14. Does this handle traumatic content? (Footage, documentation, testimony)
15. What progressive disclosure levels needed?
16. Who reviews traumatic content? Burnout prevention measures?
17. Witness/whistleblower identities? Anonymization requirements?
18. Emotional safety features expected? (Warnings, session reminders, configurable detail)

### Phase 5: Technical Constraints
19. Budget hard limits? (Every dollar has alternative use in advocacy)
20. Timeline and driver? (Legislative session, investigation, campaign launch)
21. Tech stack constraints? (Existing infra, team skills, self-hosted needs)
22. Connectivity constraints? (Offline-first, low-bandwidth, mesh)
23. Language and accessibility requirements?

### Phase 6: Synthesize
Compile answers into a spec containing: purpose statement, user personas with risk profiles, threat model, data boundaries, success criteria, safety requirements, constraints, and open questions. Present to stakeholder for confirmation before design.
