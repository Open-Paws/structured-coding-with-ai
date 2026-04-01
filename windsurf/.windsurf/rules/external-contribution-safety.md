<!-- trigger: model_decision -->
# External Contribution Safety

When helping a developer contribute to a third-party repository — any repo whose git remote does not belong to your organization — suppress all identity, attribution, and advocacy framing from commits, pull requests, and branches.

## Repo Classification

Before producing any commit message, PR description, or branch name, check the remote:

```bash
git remote get-url origin
```

- Remote matches `github.com/Open-Paws/` or `github.com:Open-Paws/` → **internal**, full identity fine.
- Remote is anything else → **external**, apply all rules below.
- No remote configured → **external** (safe default).

Confidence must be positive that you are in an internal repo. Absent positive confirmation, stay in external mode.

## What to Suppress in External Repos

**Tool identity** — No mentions of Windsurf, Cascade, Claude, Copilot, or any AI tool in commits, PR descriptions, branch names, or code comments.

**Organization** — No mentions of Open Paws or any advocacy organization in any contribution artifact.

**Mission framing** — No advocacy language (liberation, compassionate, animal rights, vegan) in code, commits, or PRs unless the target project is explicitly about those topics.

**Attribution trailers** — No `Co-Authored-By:` lines. No "Generated with" footers. No AI attribution anywhere.

## Commit Message Rules

Read the last five commits before writing:

```bash
git log --oneline -5
```

Match their style. Proportional to diff. Imperative mood. No AI-generated patterns ("This commit introduces...", "Updated X to support Y"). Self-check: indistinguishable from existing commits?

## PR Description Rules

Check merged PRs before writing:

```bash
gh pr list --state merged --limit 5
```

Match the target repo's style. No headers for small changes. No bullet lists of benefits. One to three sentences. Self-check: sounds like a developer who works on this codebase, without an agenda?

## Branch Naming

Default: `fix/short-description` or `add/short-description`. Under 40 characters. No advocacy language, org identifiers, or tool names.

## Defense-in-Depth

These instructions are last-line-of-defense. Disable attribution trailers in Windsurf settings before making external contributions.
