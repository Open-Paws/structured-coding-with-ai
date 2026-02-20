# Emotional Safety Rules for Animal Advocacy Projects

Animal advocacy software routinely handles content documenting extreme suffering: factory farm conditions, slaughterhouse footage, animal testing documentation, and witness testimony of abuse. This content is necessary for investigations, legal cases, campaigns, and policy change. But uncontrolled exposure causes measurable psychological harm. Every display decision must balance operational need against the human cost of exposure.

## Progressive Disclosure of Traumatic Content

NEVER display graphic content by default. Every piece of investigation footage, slaughter documentation, or exploitation imagery must be behind at least one intentional interaction. Default state is always safe: blurred, hidden, or represented by text description. Users escalate through deliberate choices, never through automatic loading, scrolling, or navigation.

## Configurable Detail Levels

Implement user-controlled detail settings that persist across sessions. At minimum, three tiers: (1) text-only descriptions with no imagery, (2) blurred or low-detail representations with contextual descriptions, (3) full-resolution content. Each user chooses their default. The system MUST remember this preference and never reset it. Different roles need different defaults: legal reviewers need full-resolution evidence; campaign coordinators may need only text summaries.

## Content Warnings — Mandatory Before Display

Every piece of content involving animal suffering MUST be preceded by a specific content warning describing what it contains. Generic "sensitive content" warnings are insufficient — the warning must indicate whether content includes: graphic injury, death, distress vocalizations, confined living conditions, or slaughter processes. Users must make informed decisions about viewing specific content.

## Investigation Footage Handling

Investigation footage is the most operationally important and psychologically dangerous content:
- NEVER auto-play video or audio from investigations
- ALWAYS display in blurred state by default
- Require explicit opt-in for full resolution — deliberate click, not hover or scroll
- Provide frame-by-frame navigation for examining specific moments without watching continuous footage
- Strip audio by default — distress vocalizations cause acute stress; audio is a separate opt-in from video
- Support annotation without full-resolution viewing (mark timestamps on blurred preview)

## Witness Testimony Display

Before displaying testimony: (1) verify display consent is current, (2) anonymize by default — pseudonyms, not legal names, (3) require explicit opt-in for identifying details, (4) log access for audit while protecting accessor identity. Apply progressive disclosure and content warnings to testimony describing suffering.

## Burnout Prevention Patterns

Actively support user wellbeing during extended content review:
- **Session time awareness** — track continuous exposure to traumatic content, surface reminders after configurable intervals (default: 30 minutes)
- **Break prompts** — non-intrusive suggestions for reviewers processing footage or testimony for extended periods
- **Session summaries** — summary of reviewed content so reviewers do not re-expose themselves to verify completeness
- **Workload distribution** — support distributing traumatic content review across the team

## Secondary Trauma Mitigation

Secondary trauma affects developers building and testing this software. Design the development workflow to minimize unnecessary exposure: abstract test data (described references, not actual footage) in automated tests, mock data generators producing realistic metadata without graphic content, documentation of which test suites involve real content. The CI/CD pipeline must NEVER display graphic content in test output, logs, or failure reports.

## Opt-In Escalation of Graphic Content

For full-resolution graphic content, require multiple confirmation steps proportional to severity. A single click is insufficient for the most graphic content. Confirmation dialog must name what the user is about to see, require explicit acknowledgment, and provide alternatives (text description, blurred summary). This is informed consent applied to content exposure.
