# Claude Code Hooks Configuration Guide

Hooks are shell commands that Claude Code executes before or after specific agent actions. They are strictly superior to instruction-based enforcement: hooks run deterministically, cost zero tokens, and never hallucinate. Use hooks for any check that must never be skipped — formatting, linting, secret scanning, test gates.

This file is a planning template, not executable configuration. Identify which hooks your project needs, fill in the placeholder commands with your actual tools, then configure them in Claude Code's settings following the official documentation.

## Recommended Hook Slots

### Pre-Commit Hook

**Trigger:** Before any commit is created.

**Purpose:** Prevent sensitive data from entering git history. Once something is committed, it lives in the reflog and potentially in remote mirrors — removal is painful and incomplete.

**What to scan for:**

- Investigation footage paths, facility names, or coordinates
- Activist names, contact information, or organizational affiliations
- API keys, tokens, credentials, or connection strings
- Any data that creates ag-gag legal exposure if discovered through adversarial legal discovery

**Placeholder command:** `[YOUR_SECURITY_SCANNER] --staged-files-only`

Replace with your project's secret-scanning or sensitive-data-detection tool. The command must exit non-zero to block the commit.

### Post-Edit Hook

**Trigger:** After any file is edited by the agent.

**Purpose:** Auto-format the edited file immediately. This is a deterministic check — formatting should never consume instruction budget or rely on the model remembering to do it.

**Placeholder command:** `[YOUR_FORMATTER] --file $EDITED_FILE`

Replace with your project's code formatter. This hook should always exit zero (formatting failures should warn, not block).

### Pre-Push Hook

**Trigger:** Before any push to a remote repository.

**Purpose:** Run the full test suite so broken code never reaches shared branches. This catches issues that per-file checks miss: integration failures, broken imports, and regressions.

**Placeholder command:** `[YOUR_TEST_RUNNER] --full-suite`

Replace with your project's test command. Must exit non-zero to block the push if any test fails.

### Custom: PII Detection Hook

**Trigger:** Before any commit is created (runs alongside the pre-commit security scan).

**Purpose:** Scan code and comments specifically for activist PII. This is separated from general secret scanning because the patterns are domain-specific: names of investigators, shelter contacts, rescue network participants, and organizational roles that could identify individuals if the codebase is subpoenaed or leaked.

Ag-gag laws in many jurisdictions criminalize investigation activities. Code comments like `// TODO: ask [name] about [facility]` become discoverable evidence. This hook catches what generic secret scanners miss.

**Placeholder command:** `[YOUR_PII_SCANNER] --patterns activist-pii.patterns --staged-files-only`

Replace with a grep-based script or dedicated PII scanner configured with your project's custom pattern file. Must exit non-zero if any match is found.

## How to Configure

Claude Code hooks are configured through the tool's settings interface or configuration files. Consult the Claude Code documentation for the exact format and available trigger points. Each hook definition specifies the trigger event, the shell command to run, and whether a non-zero exit code should block the action.
