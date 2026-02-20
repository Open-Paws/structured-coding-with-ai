# Memory Bank

Three files for progressive context disclosure. These give the AI agent project-specific knowledge that persists across sessions. They are templates -- update them as your project evolves.

## Files

- `brief.md` -- Project identity. What the software is, the domain it operates in, the core mission, what makes it different, and the ubiquitous language convention. This is the first thing an agent reads to orient itself.
- `context.md` -- Architecture and decisions. Threat model (three adversaries), technology approach, bounded context definitions (Investigation Operations, Public Campaigns, Coalition Coordination, Legal Defense), key design decisions, and AI-assisted development rules.
- `history.md` -- Decision log. Records significant architectural, security, and design decisions with context, rationale, and consequences. Includes a template entry and two example entries. Add new entries as decisions are made.

## Usage

The memory bank is loaded by Kilo Code to provide project context. Start by editing `brief.md` with your project's identity, then fill in `context.md` with your architecture and threat model. Use `history.md` as an ongoing decision log -- each entry should explain not just what was decided but why, so future contributors understand the reasoning.
