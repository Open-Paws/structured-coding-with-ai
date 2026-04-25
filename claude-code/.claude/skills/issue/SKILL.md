---
name: issue
description: File one or many GitHub issues from any input — a sentence, a meeting transcript, a funder email. Auto-detects single-vs-batch and asks for approval before filing anything in batch mode.
disable-model-invocation: true
argument-hint: "<text or pasted content> [--repo <name>] [--dry-run] [--no-confirm]"
allowed-tools: Bash(gh:*), Read, Grep, Glob
model: opus
---

# /issue — file GitHub issues from arbitrary input

Operator-only command. Takes anything from a one-sentence note to a pasted meeting transcript and turns it into well-formed GitHub issues that `scout`/`triage` would themselves accept. Auto-detects single-vs-batch — the operator never declares a mode.

Read these every fire (auto-load via `InstructionsLoaded`; this skill must respect them, not work around them):

- `~/.claude/rules/pipeline-nevers.md` — conventional-commit prefixes, never apply `auto:approved`, never apply `override:*`
- `~/.claude/rules/context-repo.md` — sensitivity taxonomy and STAGE 13 confidentiality leak rule (load-bearing for sanitization)
- `~/.claude/rules/advocacy-domain.md` — ubiquitous-language terms; titles and bodies must use them
- `~/.claude/rules/voice.md` — no flattery, no corporate filler in issue bodies either
- `~/.claude/rules/git-identity.md` — bot identity rules (referenced by the startup check below)

Issues this skill files must be drop-in acceptable to `~/.claude/agents/scout.md` (well-formed: real observation, no fabricated paths, dedup-checked) and `~/.claude/agents/triage.md` (label set + sensitivity reasoning ready to be confirmed). If you find yourself wanting to relax those agents to make this skill easier, stop and report instead.

## Startup gate — operator session, not bot session

Before any other work, run:

```bash
gh auth status 2>&1 | head -10
```

Parse the active account. If it is `OpenGaryBot` (or any other bot identity matching `*Bot` / `*-bot`), refuse:

```
/issue refuses to run under bot identity (active: OpenGaryBot).

Issues filed by /issue must carry the operator's identity — the bot triages, the
operator files. Mixing creates a confusing audit trail (per ~/.claude/rules/git-identity.md
the bot is for commits/automation, not operator-driven issue creation).

Switch with:  gh auth switch --user <your-personal-account>
Then re-run /issue.
```

Halt. Do not proceed to argument parsing or any gh write. This is non-negotiable — there is no `--force` flag.

## Argument parsing

`$ARGUMENTS` is the raw input. Parse out flags first, then everything remaining (in original order) is the input text:

- `--repo <name>` — explicit target repo. Overrides any inferred repo. In Mode B, applied as a default to all extracted candidates (per-candidate inference can still override if the candidate explicitly names a different repo).
- `--dry-run` — compute the full plan but never call `gh issue create`. Output everything that would be filed.
- `--no-confirm` — Mode A only: skip the confirm prompt and file immediately. **Forbidden in Mode B.** If `--no-confirm` is set and detection lands on Mode B, error out: `--no-confirm is forbidden in batch mode; remove the flag and re-run`.

Empty input after flag-stripping → output one-line usage hint and stop.

## Algorithm

### STEP 1 — Mode detection (deterministic, first match wins)

1. **Mode A (Direct file)** — input is ≤3 sentences AND a repo can be resolved per STEP 2.
2. **Mode B (Decompose and triage)** — input is >3 sentences OR contains multi-item markers.
3. **Mode C (Clarify)** — anything else (chiefly: short input where repo can't be resolved).

**Sentence count.** Count terminal punctuation (`.`, `!`, `?`) outside code blocks (` ``` ... ``` ` and ` ` ... ` `), URLs (anything matching `https?://...`), and the abbreviation set: `e.g.`, `i.e.`, `etc.`, `vs.`, `Mr.`, `Mrs.`, `Dr.`, `St.`, `Inc.`, `Ltd.`, `U.S.`, `U.K.`, `cf.`. Be conservative — "I noticed the deploy is broken. Can you file something?" is **2 sentences**, Mode A.

**Multi-item markers.** Any of:

- Two or more lines starting with bullet glyphs at column 0 (after optional whitespace): `-`, `*`, `•`, `–`
- Two or more numbered list lines: `1.`, `1)`, `2.`, `2)`...
- Conjunctive phrases (case-insensitive): `and also`, `another thing`, `another issue`, `separately`, `second issue`, `third issue`, `next thing`
- Two or more paragraph breaks (`\n\n`) with topic shifts. Topic-shift detection is judgment — paragraphs that share subject/error/repo are not topic shifts; paragraphs that cover unrelated systems are. When uncertain, prefer Mode B (decompose) over Mode A — Mode B has an explicit approval gate, Mode A does not.

### STEP 2 — Repo inference (deterministic, fail-safe; first success wins)

a. `--repo` flag is set → use it. Stop.
b. **Literal repo-name token in input.** Tokenize the input on whitespace + punctuation; if any token exactly matches a name in the canonical Open-Paws repo list (cached via `gh repo list Open-Paws --limit 200 --json name`), use that repo. Stop.
c. **Nickname in input** — match against the alias map below (case-insensitive, whole-word match only). Stop on first hit.
d. **Cwd inside an Open-Paws checkout** — `git rev-parse --show-toplevel` inside cwd; if it resolves and the basename matches an Open-Paws repo, use that. Stop.
e. **Fail.** Mode A falls through to Mode C. (Inference NEVER falls back on content keywords. "There's an auth bug" without a repo token does NOT become `ai-security`. Misfiling is worse than asking.)

### STEP 3a — Mode A (Direct file)

1. **Draft.**

   - **Title** — imperative, specific, ≤80 chars. Use ubiquitous-language terms from `advocacy-domain.md` where applicable. Good: `Add --delete-branch to /merge command output`. Bad: `merge command thing`, `fix this`.
   - **Body** — exactly three sections:

     ```
     **Observed:** <what's happening or what the operator noticed; one paragraph max>

     **Expected:** <what should happen instead, or "—" if not yet known>

     **Next step:** <one specific suggestion, or "investigate" if genuinely unknown — never fabricate>
     ```

   - **Labels** — type (`type:bug` / `type:feature` / `type:chore` / `type:docs` / `type:refactor` / `type:security` / `type:proposal`), severity (`severity:trivial` / `severity:minor` / `severity:major` / `severity:blocker`), and component if obvious from input. Apply `stage:triaged` so triage picks it up. **Never** apply `auto:approved`, `auto:auto-fixable`, `auto:requires-human`, or any `override:*` label — those are gates triage owns, not defaults filing owns.
   - Confirm every label exists in the target repo via `gh label list --repo Open-Paws/<repo>` before applying. Drop labels that don't exist; do not auto-create.

2. **Sanitize.** Run STEP 4 on the body.

3. **Dedup probe.** `gh issue list --repo Open-Paws/<repo> --search "<3-5 keywords from title>" --state all --limit 10`. If a clear duplicate exists, surface it: `Possible duplicate: #<n> "<title>" (<state>) — file anyway? (y/n)`. Operator confirms or aborts.

4. **Display the draft.**

   ```
   ## /issue — Mode A (direct file) → Open-Paws/<repo>

   **Title:** <title>
   **Labels:** <comma-separated>

   **Body:**
   <rendered body>

   ---
   File this? (y / edit / n)
   ```

5. **Operator response.**

   - `y` → file via `gh issue create --repo Open-Paws/<repo> --title "<title>" --body "<body>" --label "<l1>" --label "<l2>" ...`. Emit the URL gh prints.
   - `edit` → drop the operator into editing the title and/or body inline (one prompt for title, one for body; empty input keeps existing). After edits, file directly. **Do not re-sanitize after operator edits** — the operator's edit is the final word; they may have intentionally added something (per Hard Rules).
   - `n` → abort, no file, no follow-up.

6. **`--no-confirm`** — skip step 4's prompt and file the draft directly. Still run sanitization (step 2) and the dedup probe (step 3). If dedup finds a clear duplicate, abort and surface the duplicate URL — `--no-confirm` does not override dedup safety.

7. **`--dry-run`** — render the full draft block above, append `(dry-run; nothing filed)` and stop. No `gh issue create` call.

### STEP 3b — Mode B (Decompose and triage)

1. **Extract candidates.** Walk the input and pull every actionable item — anything that, if isolated, could become its own issue. Skip:

   - Pure discussion ("we should think about X someday")
   - Strategy / fundraising debate
   - Philosophical asides
   - Status updates with no action ("the deploy went fine")

   Each kept candidate gets: a short summary (becomes draft title), the literal source span (for sanitization), and any repo-relevant tokens.

2. **Per-candidate processing.**

   For each candidate:

   - **Repo.** Run STEP 2 inference per-candidate. `--repo` is the default but explicit per-candidate naming overrides. If unresolved → mark as `???` (operator must set before that row can be filed).
   - **Dedup classification.** `gh issue list --repo Open-Paws/<repo> --search "<keywords>" --state all --limit 10`. Classify into one bucket:
     - `NEW` — no matching open or recently-closed (≤90d) issue
     - `DUPLICATE_OF #N` — matches an open issue or a recent close that addresses the same thing (link `#N`)
     - `ALREADY_RESOLVED` — matches a closed issue that already addresses it (link `#N`, note the closing PR if any)
     - `OUT_OF_SCOPE` — judged not-actionable on closer read (discussion / strategy / opinion). Always show this with a one-line reason; never silently drop.
   - **Draft.** For NEW only, draft title + body using the same shape as Mode A. Run STEP 4 (sanitize) on each.
   - **Labels.** Same rules as Mode A.

3. **Display the classification table.**

   ```
   ## /issue — Mode B → extracted N candidates from input

   | # | Action            | Repo                  | Title                            | Reason                               |
   |---|-------------------|-----------------------|----------------------------------|--------------------------------------|
   | 1 | NEW               | <repo>                | <draft title>                    | not present in open or recent issues |
   | 2 | DUPLICATE_OF #299 | <repo>                | (matches #299)                   | #299 opened 4d ago, same root cause  |
   | 3 | NEW               | ???                   | <draft title>                    | could not infer repo — needs operator|
   | 4 | OUT_OF_SCOPE      | —                     | <one-line summary>               | strategy discussion, not actionable  |

   Approve which rows for filing?
     all                          — file every NEW row with a resolved repo
     1,3,6-9                      — file these row numbers only
     all except 4                 — file every NEW row with a resolved repo, minus #4
     none                         — abort everything
     edit <n>                     — edit row <n>'s draft (title/body/labels) before filing
     set repo <n> <reponame>      — resolve a ??? row's repo
   ```

4. **Operator selects.** Loop on `set repo` and `edit` until the operator says `all`, a row list, `all except ...`, or `none`. **Any row whose repo is `???` is unfileable** — operator must explicitly resolve before that row can be approved. If the operator's selection includes a still-`???` row, refuse the selection and re-display the table.

5. **File approved rows.** For each, render the draft and call `gh issue create --repo Open-Paws/<repo> ...`. Emit a final list grouped by repo:

   ```
   Filed:
   Open-Paws/<repo-a>:
     - #<n> <url>
     - #<n> <url>
   Open-Paws/<repo-b>:
     - #<n> <url>
   ```

6. **Atomic-ish failure mode.** If the first `gh issue create` in the batch fails, abort the rest. Print partial state explicitly: `Filed N of M before failure on row K (<reason>). Remaining rows NOT filed; re-run /issue or file manually`. Do not retry inline.

7. **`--dry-run`** — render the table and (for every NEW row) the full sanitized draft body in a collapsed-list format. No `gh issue create` calls. Skip the approval prompt; instead append `(dry-run; nothing filed)`.

### STEP 3c — Mode C (Clarify)

1. **Ask exactly ONE question.** Pick the question that most reduces the search space:

   - If repo is the blocker: `Which repo? Recent activity in: <list 3 most plausible based on input>` (use `gh repo list Open-Paws --limit 200 --json name,pushedAt --sort pushedAt` and the alias map).
   - If scope is the blocker (input is unclear about whether it's one issue or many): `Is this one issue or multiple? A one-line summary of what you're filing helps.`
   - If intent is the blocker (input doesn't make clear what kind of issue): `Is this a bug, an enhancement, or a discussion item?`

2. **Wait for the operator.** Once they reply, concatenate their answer onto the original input and re-run STEP 1 with combined input.

3. **One question, no second.** If the combined input is still ambiguous, output: `I can't pick this up from what's been described. Want to draft it manually and I'll polish?` Stop. No second clarifying question — that's nagging.

### STEP 4 — Sensitivity sanitization (every body, both modes)

1. **Tier the target repo.** Per `~/.claude/rules/context-repo.md`:

   - `Open-Paws/context` → tier is `staff-ok` by default for context-repo issues; treat as **mild strip**. Never paste verbatim if input was clearly meeting-transcript or email-private.
   - All other public Open-Paws code repos → `public` → **strict strip**.
   - Private Open-Paws repos (if any) → `private` → no strip required, but never copy verbatim from a confidential origin.
   - **Unknown tier** → ask once: `<repo> sensitivity tier? (public / staff-ok / private)`. Do not assume. Cache the answer for this fire.

2. **Strict-strip rules (`public` tier).**

   - Remove names of external individuals (funders, partners, third parties, journalists, consultants). Replace with role: `the funder`, `a partner org rep`, `the consultant`, `the journalist`.
   - Remove names of external organizations that are not already public. Use generic descriptors: `a foundation`, `a coalition partner`, `a vendor`.
   - Remove email addresses, phone numbers, internal URLs, dashboard links containing tokens or session ids, anything that looks like a credential or secret.
   - Remove any verbatim Slack/CryptPad/email source paste — paraphrase.
   - **Keep:** technical detail, error messages, public-facing URLs, repo references, public issue numbers, public PR numbers, public commit SHAs.

3. **Mild-strip rules (`staff-ok` tier).**

   - Same as strict, EXCEPT internal staff names and internal program names may stay. External individuals/orgs still get stripped per strict.

4. **Verbatim is forbidden.** NEVER paste raw input verbatim into an issue body. Quote sparingly — at most one sentence — and paraphrase the rest. For Mode B candidates derived from a transcript or email, prepend the body with one provenance line:

   ```
   > from: <one-sentence paraphrase or sanitized quote of the source>
   ```

   DO NOT dump the whole transcript or email into the body. Ever.

5. **STAGE 13 self-check.** Before emitting any body bound for a `public`-tier repo, re-read the STAGE 13 confidentiality-leak patterns in `context-repo.md`:

   - Closed decision citing a specific funder's objection
   - Priority justified by "we lost trust with X partner"
   - Program doc listing specific individuals as "struggling"
   - Playbook referencing active campaign targets by name before launch

   If anything in the draft would fail STAGE 13 if it were a PR comment, strip it harder — abstract up a level or remove. When in doubt, the rule from `context-repo.md` applies: *the default direction is out, not in*.

## Hard rules

These are non-negotiable. If a rule and a plausible operator request conflict, the rule wins; surface the conflict.

1. **Never apply `auto:approved`, `auto:auto-fixable`, `auto:requires-human`, or any `override:*` label.** Those are gates triage and humans own; filing only sets `stage:triaged` plus type/severity/component.
2. **Never file an issue body that contains raw transcript or email content.** Paraphrase, quote sparingly (one sentence max), strip per the sensitivity tier.
3. **Never silently drop a candidate in Mode B.** Every extracted item appears in the table — even `OUT_OF_SCOPE` ones, with a one-line reason.
4. **Never infer repo from content keywords alone.** STEP 2 rule (c) is strict: explicit token / alias whole-word match only. "There's an auth bug" without a repo token does not become `ai-security`.
5. **Never ask more than one clarifying question per turn** (Mode C). If still ambiguous after one round, hand it back to the operator with a "draft it manually and I'll polish" offer.
6. **`--no-confirm` is forbidden in Mode B.** Batch filing always requires explicit approval. Detection-time conflict → error out, do not silently downgrade to Mode A.
7. **The operator's edit on a Mode A draft is the final word.** Do not re-sanitize after their edit; they may have intentionally added something. (Strict sanitization runs *before* showing the draft, exactly once.)
8. **`gh` errors stop the run.** If `gh issue create` returns an error, surface it verbatim and stop. Do not retry inline. Do not half-file a Mode B batch — file all approved rows in order, abort at the first failure, surface partial state explicitly.
9. **Refuse under bot identity.** The startup gate above is mandatory. No `--force`, no env-var override.

## Repo aliases

Whole-word, case-insensitive match. Operator extends this map over time.

| Alias                                | Resolves to               |
|--------------------------------------|---------------------------|
| `slingshot`                          | `slingshot-uk-phase1`     |
| `platform`                           | `platform`                |
| `bot`, `gary`                        | `gary`                    |
| `language tooling`, `nav`, `no-animal-violence` | `no-animal-violence` |
| `context`, `why`                     | `context`                 |
| `desloppify`                         | `desloppify`              |
| `coderabbit`                         | `coderabbit`              |
| `graze`                              | `graze-cli`               |
| `where they stand`, `wts`            | `where-they-stand`        |
| `ai security`, `ai-security`         | `ai-security`             |
| `c4c`, `bootcamp`                    | `c4c-bootcamp`            |
| `c4c website`                        | `c4c-campus-website`      |
| `mobius`                             | `mobius-real-estate`      |
| `avs`, `vegan recommendations`       | `avs-vegan-recommendations` |
| `protein library`                    | `Protein-Research-Library` |
| `ace`                                | `ace-research-library`    |
| `cryptpad pm`                        | `cryptpad-project-management` |
| `n8n`                                | `n8n-workflow-history`    |
| `proxy`, `privatemode`               | `privatemode-proxy`       |
| `api gateway`                        | `api-gateway`             |
| `compassionate code`                 | `project-compassionate-code` |
| `docs`                               | `documentation`           |
| `structured`, `instruction files`    | `structured-coding-with-ai` |
| `org-default`, `.github`             | `.github`                 |

Multi-word aliases match as whole phrases (e.g. `language tooling` matches `... the language tooling repo ...` but not `language` alone). Single-word aliases require word-boundary match (the regex `\b<alias>\b`).

When a candidate has both an explicit repo-name token (rule b) and a nickname (rule c), the repo-name token wins — explicit beats inferred.

## End-to-end behavior summary

- Operator pastes input → bot-identity gate → flags parsed → mode detected → repo inferred → draft(s) built → sanitized → (Mode A: confirm) / (Mode B: classification table + approval) / (Mode C: one question) → `gh issue create` calls → URLs back to operator.
- `--dry-run` short-circuits the `gh issue create` calls only; everything else (drafting, sanitization, dedup probes, classification) runs as normal.
- Nothing about this skill drives the pipeline forward. It's a feeder for STAGE 1 (scout) → STAGE 2 (triage). What it files, scout/triage will pick up next.
