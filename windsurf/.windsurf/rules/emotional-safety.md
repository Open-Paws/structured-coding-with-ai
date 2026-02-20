<!-- trigger: model_decision -->
# Emotional Safety Rules

Advocacy software handles content documenting extreme suffering: factory farm conditions, slaughterhouse footage, animal testing documentation, witness testimony. This content drives investigations, legal cases, and policy change — but uncontrolled exposure causes measurable psychological harm. Emotional safety is a duty of care to the people doing this work.

## Progressive Disclosure — Mandatory

NEVER display graphic content by default. Every piece of investigation footage or exploitation imagery must be behind at least one intentional interaction. Default state is always safe: blurred, hidden, or text description only. Users escalate through deliberate choices, never automatic loading or scrolling.

## Configurable Detail Levels

Three tiers minimum, persisting across sessions:
1. Text-only descriptions, no imagery
2. Blurred/low-detail with contextual descriptions
3. Full-resolution content

Different roles need different defaults. Legal reviewers may need full access; campaign coordinators may need text only. The system MUST remember preferences and never reset them.

## Content Warnings — Specific, Not Generic

Every piece of suffering content MUST have a specific warning: graphic injury, death, distress vocalizations, confined conditions, or slaughter processes. "Sensitive content" is insufficient — users need informed decisions about specific content.

## Investigation Footage

- NEVER auto-play video or audio
- ALWAYS display blurred by default
- Require explicit opt-in for full resolution (deliberate click, not hover)
- Frame-by-frame navigation for reviewers examining specific moments
- Strip audio by default — distress vocalizations cause acute stress; separate opt-in from video
- Support annotation on blurred preview without full-resolution viewing

## Witness Testimony

Before display: verify consent is current, anonymize by default (pseudonyms not legal names), require opt-in for identifying details, log access for audit while protecting accessor identity. Apply progressive disclosure and content warnings to written descriptions of suffering.

## Burnout Prevention

- Session time awareness: reminders after configurable intervals (default 30 min of content review)
- Non-intrusive "take a break" prompts for extended review sessions
- Session summaries so reviewers avoid re-exposure to verify completeness
- Workload distribution across team for traumatic content review

## Secondary Trauma — Developer Protection

Use abstract test data in automated tests, not actual footage. Provide mock data generators producing realistic metadata without graphic content. CI/CD must never display graphic content in test output or logs. Document which test suites involve real content so developers can prepare.

## Opt-In Escalation

For the most graphic content, require multi-step confirmation: dialog naming what the user will see, explicit acknowledgment, alternative offered alongside full access. This is informed consent applied to content exposure.
