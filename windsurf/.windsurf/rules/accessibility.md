<!-- trigger: model_decision -->
# Accessibility Rules

Advocacy networks span borders, languages, economic conditions, and infrastructure environments. An activist coordinating rescue in rural areas with intermittent connectivity has fundamentally different needs than a campaign organizer at a well-resourced urban nonprofit.

## Internationalization from Day One

Design every user-facing component with i18n from the start — never retrofit. Externalize all strings. Support right-to-left layouts. Handle pluralization rules across languages. Locale-aware date, time, currency, and number formatting. Adding i18n after the fact requires touching every component — cost grows exponentially.

## Low-Bandwidth Optimization

Many activists operate on expensive or throttled mobile data. Compress all assets, lazy-load non-critical content, minimize payloads, transfer only deltas. Set performance budgets and test on throttled connections. Tools requiring broadband exclude the activists who need them most.

## Offline-First Architecture

Design for disconnected operation as the default. Local-first data storage with background sync. Conflict resolution for data modified offline by multiple users. Queue operations during disconnection and replay on reconnect. Core workflows must be fully functional without network access.

## Low-Literacy Design

Not all participants are fluent readers. Use icons alongside text labels, visual workflows instead of text-heavy instructions, support voice input/output where possible, progressive disclosure to avoid information overload. Test with users who have limited formal literacy.

## Mesh Networking Compatibility

In environments where internet is unavailable, compromised, or surveilled, mesh networking enables device-to-device communication. Design sync protocols for high latency, low bandwidth, and intermittent peer availability. Activists in regions with government internet shutdowns depend on mesh-capable tools.

## Graceful Degradation

Every feature must have a degraded mode under constrained conditions. If encryption fails to load, refuse to transmit rather than sending plaintext. If media processing is unavailable, store safely for later rather than discarding. Degrade capability, never safety.

## Device Seizure — Application State

When connectivity is lost suddenly (device seized, signal jammed, power cut), the application must not leave sensitive data exposed. No temp files with decrypted content, no swap-to-disk caches, no crash dumps with witness identities, no recovery modes displaying sensitive content without re-authentication.

## Multi-Language Networks

Support simultaneous use in multiple languages within the same deployment. Each user sees their interface language; shared content available in translated or original form. Machine translation for real-time use, human-reviewed translation for legally sensitive content.
