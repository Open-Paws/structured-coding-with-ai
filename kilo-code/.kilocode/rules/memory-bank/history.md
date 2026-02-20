# Decision History

Record significant architectural, security, and design decisions here as the project evolves. This log helps future contributors understand WHY the codebase looks the way it does — the code shows WHAT, this log shows WHY.

---

## 2026-XX-XX — [Template: Decision Title]

**Context:** What situation prompted this decision. What problem were you solving? What constraints existed?

**Decision:** What was decided. Be specific — name the approach chosen.

**Rationale:** Why this approach over the alternatives. What tradeoffs were accepted? What was explicitly rejected and why?

**Consequences:** What follows from this decision. What becomes easier? What becomes harder? What new constraints does this create?

---

## Example Entries

### 2026-XX-XX — Chose Offline-First Architecture

**Context:** Investigation teams operate in rural areas with intermittent connectivity. Two field investigations lost data when sync failed silently during poor network conditions.

**Decision:** Adopted offline-first architecture — local-first data storage with background sync when connectivity is available, queue-and-replay for operations during disconnection.

**Rationale:** Designing for connectivity-as-default excluded the activists who need the tools most. Offline-first adds complexity to conflict resolution but eliminates data loss from network failures. Rejected "online-with-cache" approach because it degrades silently when offline.

**Consequences:** All features must work without network access for core workflows. Conflict resolution strategy needed for concurrent offline edits. Sync protocol must handle high latency and intermittent peers. Testing must cover disconnected scenarios explicitly.

---

### 2026-XX-XX — Separated Investigation Ops from Public Campaigns as Bounded Contexts

**Context:** Early prototype had a shared "user" model for both investigators and campaign supporters. A bug in the campaign email feature exposed the full user list, which included investigator aliases.

**Decision:** Split into separate bounded contexts with an anti-corruption layer between them. Investigation Operations and Public Campaigns share no data models directly.

**Rationale:** An investigator and a campaign supporter have fundamentally different risk profiles. Sharing a data model means a bug in the low-security context (campaigns) can expose the high-security context (investigations). Anti-corruption layers add development overhead but prevent category-crossing data leaks.

**Consequences:** Data cannot flow between contexts without explicit transformation. Coalition coordination that touches both contexts must go through defined interfaces. Duplication of some common structures (e.g., both contexts have "organization" but with different attributes). Increased development time offset by elimination of cross-context data leak risk.
