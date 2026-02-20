# Requirements Interview Workflow

This is the full requirements interview workflow for advocacy projects — a step-by-step process for gathering requirements from stakeholders. Distinct from the Interview custom mode (which defines the agent's persona), this file documents the complete structured interview methodology.

## When to Use
- Starting a new feature or project
- When requirements are ambiguous or incomplete
- Before writing a specification or design document
- When a new coalition partner or user group is introduced

## Process

Ask one question at a time. Use multiple choice when possible. Wait for each answer before proceeding. Advocacy stakeholders are often volunteers with limited time.

### Phase 1: Purpose and Users
1. What are we building? (One sentence describing the core function)
2. Who are the primary users? (Investigators, campaign organizers, sanctuary staff, legal team, coalition coordinators, public supporters)
3. What does success look like? (Specific, measurable criteria)
4. What existing tools or workflows does this replace or augment?

### Phase 2: Threat Modeling
5. Who are the adversaries? (Law enforcement/ag-gag, industry investigators, hostile public, AI model providers)
6. What happens if this system is compromised? (Who is endangered, what evidence exposed, what legal liability)
7. What happens if a device is seized? (What data recoverable, what operations exposed)
8. What legal jurisdictions apply? (Ag-gag laws, data protection regulations, countries)

### Phase 3: Coalition and Data Boundaries
9. Which organizations will use this system?
10. Do organizations have different risk profiles?
11. What data crosses organizational boundaries? What must NOT cross?
12. If one partner is legally compelled to disclose, what is the blast radius?
13. What existing data sharing agreements constrain the design?

### Phase 4: User Safety
14. Does this system handle traumatic content? (Investigation footage, slaughter documentation, witness testimony)
15. What progressive disclosure levels are needed? (Text-only, blurred, full-resolution, configurable)
16. Who reviews traumatic content? What burnout prevention measures exist?
17. Does this system handle witness or whistleblower identities? What anonymization requirements?
18. What emotional safety features do users expect?

### Phase 5: Technical Constraints
19. Budget — hard limits on infrastructure and AI compute costs?
20. Timeline — deadline and what drives it?
21. Tech stack preferences or constraints?
22. Connectivity constraints? (Full, low-bandwidth, offline-first, mesh networking)
23. Language and accessibility requirements?

### Phase 6: Synthesize
Compile answers into a specification document:
- **Purpose statement** — one paragraph
- **User personas** — who uses this, their risk profiles
- **Threat model** — adversaries, attack surfaces, legal exposure
- **Data boundaries** — what is stored, where, who accesses, what crosses org boundaries
- **Success criteria** — measurable outcomes
- **Safety requirements** — emotional safety, anonymization, progressive disclosure
- **Constraints** — budget, timeline, technology, connectivity, language
- **Open questions** — what needs clarification before design

Present the synthesized spec to the stakeholder for confirmation before proceeding to architecture.
