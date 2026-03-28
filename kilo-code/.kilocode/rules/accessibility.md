# Accessibility Rules for Animal Advocacy Projects

Advocacy networks span borders, languages, economic conditions, and infrastructure environments. An activist coordinating a rescue in a rural area with intermittent connectivity has fundamentally different needs than a campaign organizer at a well-resourced urban nonprofit. Accessibility ensures the movement's tools work for everyone the movement serves.

## Internationalization from Day One

Design every user-facing component with internationalization from the start — never retrofit. Advocacy networks operate across linguistic boundaries. Externalize all user-facing strings from the beginning. Support right-to-left text layouts. Handle pluralization rules across languages. Date, time, currency, and number formatting must respect locale. Adding i18n after the fact touches every component — the cost grows exponentially with codebase size.

## Low-Bandwidth Optimization

Many activists operate on mobile data in regions with expensive or throttled connections. Optimize aggressively: compress all assets, lazy-load non-critical content, minimize payload sizes, implement efficient synchronization transferring only deltas. Set performance budgets and test on throttled connections. A tool requiring broadband excludes the activists who need it most.

## Offline-First Architecture

Design for disconnected operation as the default. Activists in areas with unreliable connectivity — rural investigation sites, countries with internet shutdowns, disaster response — need tools that work without a network. Local-first data storage with background sync. Conflict resolution for concurrent offline edits. Queue operations during disconnection, replay on reconnect. Core workflows must be fully functional without network access.

## Low-Literacy Design Patterns

Not all advocacy participants are fluent readers. Rescue coordinators, sanctuary workers, and community organizers come from diverse educational backgrounds. Use icons alongside text labels, provide visual workflows, support voice input and audio output where possible, use progressive disclosure to reduce information density. Test interfaces with users who have limited formal literacy.

## Mesh Networking Compatibility

In environments where centralized internet is unavailable, compromised, or surveilled, mesh networking enables device-to-device communication. Design synchronization protocols that operate over high-latency, low-bandwidth, intermittent mesh networks. Activists in regions with government internet shutdowns depend on mesh-capable tools.

## Graceful Degradation

Every feature must have a degraded mode under constrained conditions. If encryption fails to load, refuse to transmit sensitive data — never fall back to plaintext. If media processing is unavailable, store investigation footage safely for later processing. If the network drops, show clear status indicators. Degrade capability, never safety.

## Device Seizure Preparation — Application State

When connectivity is lost suddenly — device confiscated, signal jammed, power cut — the application must not leave sensitive data exposed. No temporary files with decrypted content. No in-memory caches persisting to swap. No crash dumps with witness identities. No recovery modes displaying sensitive content without re-authentication. Power loss at any moment must leave zero recoverable sensitive state on disk.

## Multi-Language Activist Networks

Coalition tools must support simultaneous use in multiple languages within the same deployment. Each user sees the interface in their language; shared content can be viewed in translated or original form. Support machine translation for real-time use and human-reviewed translation for legally sensitive content.
