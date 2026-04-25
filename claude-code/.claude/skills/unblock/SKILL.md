---
name: unblock
description: Surfaces every pending decision that only the operator can make, with copy-paste-ready next actions. Three sections — credentials needed, decisions needed, sensitivity escalations. Reads the latest /run report (<30min) or derives directly. Every item has a specific actionable next step; if it doesn't, it doesn't belong here. Operator-only.
disable-model-invocation: true
argument-hint: "[--section credentials|decisions|sensitivity] [--repo <name>]"
allowed-tools: Bash(gh:*), Bash(ls:*), Bash(date:*), Bash(stat:*), Read, Grep, Glob
model: sonnet
---

# /unblock — operator decisions queue

Surfaces only items that need the operator. Filters out everything else. If `/unblock` lists something, the operator has a specific action to take — not "wait", not "rerun later".

`/unblock` does NOT apply override labels. Does NOT close PRs. Does NOT merge. It surfaces; the operator executes.

Read these every fire (auto-load via `InstructionsLoaded`; cite by name in any followup):

- `~/.claude/rules/context-repo.md` — **STAGE 13 confidentiality leak rule applies to the sensitivity section. Re-read before formatting any sensitivity item.** No private content goes in the report — repo+number + non-sensitive summary only.
- `~/.claude/rules/pipeline-nevers.md` — override labels are human-only; never apply them
- `~/.claude/rules/git-identity.md` — for credential references (e.g. when an item needs OpenGaryBot to gain a permission)

## Argument parsing

`$ARGUMENTS`:
- `--section <name>` — show only one of: `credentials`, `decisions`, `sensitivity`
- `--repo <name>` — single-repo scope (`Open-Paws/<name>`)

## Algorithm

### 1. Find the input

```bash
LATEST=$(ls -t ~/.claude/orchestrator-log/run-*.md 2>/dev/null | head -1)
```

If `LATEST` exists AND mtime within last 30 minutes:
- Pull `### Stopped at credential gate` rows → credentials section
- Pull `### Stopped at decision conflict` rows → decisions section
- Pull `### Stopped at human gate` rows whose reason matches `sensitivity-escalation:*` or whose label list includes `sensitivity:*` (excluding `sensitivity:public-ok`/`staff-ok`) → sensitivity section
- Also pull any `auto:requires-human` items from `### Stopped at human gate` into the appropriate section based on the `needs:` reason

Otherwise (no recent log, or `--repo` set forcing fresh derivation):
```bash
gh issue list --repo Open-Paws/<repo> --state open --label 'auto:requires-human' --json number,title,labels,url,body --limit 100
gh pr list    --repo Open-Paws/<repo> --state open --label 'auto:requires-human' --json number,title,labels,url,body --limit 100
gh issue list --repo Open-Paws/<repo> --state open --label 'sensitivity-escalation' --json number,title,labels,url,body --limit 100
```

### 2. Per-item action generation

Every item must have a SPECIFIC actionable next step. Generic instructions are not allowed.

**Credentials section:**
- Identify the specific missing credential from the `missing:` field. Look it up:
  - GCP service account / IAM role → fix at `https://console.cloud.google.com/iam-admin/iam?project=<inferable from repo or `gh secret list`>`
  - GitHub Actions secret → fix command: `gh secret set <NAME> --repo Open-Paws/<repo>`
  - Supabase service role key → fix at the project's Supabase dashboard (look up project ref via `mcp__claude_ai_Supabase__list_projects` if available, otherwise label as "operator looks up project ref")
  - npm / PyPI / Cargo publish token → fix at the corresponding registry settings
  - Vercel deploy hook / token → fix at Vercel project settings
  - API key for external service (Stripe, SendGrid, etc.) → fix at the service's dashboard, with specific URL where derivable
- Count downstream items waiting on this credential — items whose `missing:` field references the same credential — and link to a `--fix-mode` filtered run report so the operator can confirm unblocking after rotation:
  ```
  Confirm with: /run --fix-mode --repo <repo>
  ```

**Decisions section:**
- Identify the conflicting decision/proposal from the `conflicts with:` field
- Resolve to one of three concrete operator actions (offer all three; operator picks):
  - **a)** Update the decision/proposal: cite the decision-id (e.g. `decisions.md#sync-labels-pr-mode`) and suggest a one-line revision in the resolution column
  - **b)** Close the PR/issue: provide `gh issue close <repo>/<num> --comment "<one-line reason>"` or `gh pr close <repo>/<num> --comment "<one-line reason>"`
  - **c)** Apply override label: `gh pr edit <repo>/<num> --add-label override:<label>` with a suggested `--body "<reason>"` comment

Per `pipeline-nevers.md`, /unblock NEVER applies the override itself — it only surfaces the command for the operator to run.

**Sensitivity escalations:**

**🔒 STAGE 13 confidentiality leak check applies here.** Re-read `~/.claude/rules/context-repo.md` § "What Must Not Go In" before formatting any sensitivity row. The report must NOT contain:
- The private content itself (no quotes, no excerpts)
- Personal information about anyone named in the original issue
- Active negotiation positions, funder dynamics, HR/performance content
- Anything from a sensitivity:private classification

For each sensitivity item, render ONLY:
- `<repo>#<num>` — issue/PR identifier
- A non-sensitive summary in the operator's words: e.g. "issue body contains personal information about a named contractor" — NOT the content of that information
- Triage's proposed sensitivity tier (e.g. "triage suggested sensitivity:private redirect")
- Three resolution options:
  - **approve** — accept triage's classification; provide command to apply the label
  - **recategorize** — to a different tier; provide command for the alternative
  - **reject** — close as out-of-scope; provide close command

If you find yourself about to write a sensitivity row that quotes from the issue body, **stop**. Use the non-sensitive summary instead. The whole point of this section is that the operator needs to see WHICH items need a call without seeing WHAT they contain.

### 3. "Specific action" filter — drop items without one

Items lacking a specific actionable next step do NOT belong in `/unblock`. Drop them. They belong in `/run`'s report under "Stopped at human gate" with a "needs: more diagnostic info" reason.

If no actionable items remain in a section, the section still renders with `(0)` and one line: `- none`. Don't omit empty sections.

## Output format

```markdown
## /unblock queue — <ISO timestamp>
Source: <log path> (mtime: <H>m ago)  OR  Source: live gh derivation (no recent run log)

### Credentials needed (N)
- <repo>#<num> — <one-line non-sensitive context>
  Missing: <specific credential — IAM role, secret name, API key>
  Fix at: <actual URL or exact command — never generic instructions>
  Unblocks downstream: <count> items
  Confirm: /run --fix-mode --repo <repo>

### Decisions needed (N)
- <repo>#<num> — <what the bot wants to do, one line>
  Blocks on: <decision-id or rule from $OP_CONTEXT_REPO that conflicts>
  Resolutions:
    a) Update decision <decision-id> to permit this case (<one-line suggested revision>)
    b) Close PR/issue: gh <pr|issue> close Open-Paws/<repo>#<num> --comment "<suggested one-line reason>"
    c) Apply override:<label>: gh pr edit Open-Paws/<repo>#<num> --add-label override:<label> --body "<suggested reason>"

### Sensitivity escalations (N)
- <repo>#<num> — <non-sensitive summary of the category, NEVER the content>
  Triage flagged: <proposed tier, e.g. sensitivity:private redirect>
  Options:
    approve     — gh issue edit Open-Paws/<repo>#<num> --add-label sensitivity:private (then close per redirect rule)
    recategorize — gh issue edit Open-Paws/<repo>#<num> --add-label sensitivity:staff-ok
    reject      — gh issue close Open-Paws/<repo>#<num> --comment "out of scope"

### Summary
Credentials: N | Decisions: N | Sensitivity: N | Total: N
```

If `--section <name>` is set, render only that section (still with header + summary). Other sections are suppressed.

## Hard rules

- **Sensitivity section never leaks content.** Repo+number + non-sensitive summary only. Re-read `context-repo.md` § "What Must Not Go In" before formatting. If you can't write the row without quoting the issue body, that's the signal that the operator needs to read the issue directly — write "operator: read issue body, no summary safe in this report" and link to the issue URL.
- **Every row has a specific action.** No "wait", no "rerun later", no "investigate". If there isn't an action, it isn't `/unblock`'s job — it belongs in `/run`'s human-gate section.
- **Never apply override labels itself.** Surface the gh command; operator runs it. Per `pipeline-nevers.md`, override labels are human-only.
- **Never close PRs or issues itself.** Same: surface the close command, operator runs it.
- **Never merge.** That's `/merge`'s read-only suggestion + operator action.
- **Never invoke subagents.** This skill reads existing pipeline state and formats it.

## Followup questions

After surfacing the queue, the operator can ask "what's the actual conflict on context#76?" or "which downstream items will the GCP_DEPLOY_KEY rotation unblock?" — answer from data already gathered. Stay in main session for these followups; that's why this skill has no `agent:` field.

For sensitivity-section followups, the operator may explicitly ask "show me the issue body for context#X." That's allowed because the operator has already chosen to read the private content. The `/unblock` report itself stays clean.
