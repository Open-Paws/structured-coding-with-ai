# Claude Code Hooks Configuration Guide

Hooks are shell commands that Claude Code executes before or after specific agent actions. They are strictly superior to instruction-based enforcement: hooks run deterministically, cost zero tokens, and never hallucinate. Use hooks for any check that must never be skipped — formatting, linting, secret scanning, test gates.

This file is a planning template, not executable configuration. Identify which hooks your project needs, fill in the placeholder commands with your actual tools, then configure them in Claude Code's settings following the official documentation. For `PreToolUse` and `PostToolUse`, Claude Code sends hook input as JSON on `stdin`, so hook commands should read fields like `.tool_input.command` or `.tool_input.file_path` from that payload.

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

**Placeholder command:** `[YOUR_FORMATTER] --file <path-from-stdin-json>`

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

Claude Code hooks are configured through `.claude/settings.json` in your project root. Install `jq` first for JSON parsing, then add a structure like this:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "jq -er '.tool_input.command | startswith(\"git commit\")' >/dev/null || exit 0; [YOUR_SECURITY_SCANNER] --staged-files-only",
            "timeout": 30
          }
        ]
      },
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "jq -er '.tool_input.command | startswith(\"git push\")' >/dev/null || exit 0; [YOUR_TEST_RUNNER] --full-suite",
            "timeout": 120
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Edit|MultiEdit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "FILE_PATH=$(jq -r '.tool_input.file_path // empty'); test -n \"$FILE_PATH\" || exit 0; [YOUR_FORMATTER] --file \"$FILE_PATH\"",
            "timeout": 10
          }
        ]
      }
    ],
    "SessionStart": [],
    "SessionEnd": [],
    "Notification": []
  }
}
```

**Key details:**
- `PreToolUse` and `PostToolUse` receive JSON on `stdin`; read `.tool_input.command` and `.tool_input.file_path` from that payload
- Common matchers: `"Bash"` (shell commands), `"Edit|MultiEdit|Write"` (file edits), `"*"` (all tools)
- `type`: only `"command"` is currently supported
- Additional lifecycle events include `UserPromptSubmit`, `Stop`, `SubagentStop`, and `PreCompact` alongside `Notification`, `SessionStart`, and `SessionEnd`
- Timeout is in seconds (optional, defaults to 120)
- Hooks can also be configured via the `/hooks` slash command in Claude Code
