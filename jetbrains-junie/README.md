# JetBrains Junie — Structured Coding Instructions

This directory contains a `.junie/` folder with `guidelines.md`, which provides project-level coding conventions for [Junie](https://www.jetbrains.com/junie/) (JetBrains' AI coding agent).

## What It Contains

`.junie/guidelines.md` is a comprehensive instruction file covering:

- **7 concerns**: design principles, testing, security, privacy, cost optimization, accessibility, emotional safety
- **6 process skills**: git workflow, testing strategy, requirements interview, plan-first development, code review, security audit

The file references Junie-specific features:

- Junie's automatic test generation and how to review those tests (treat as implementation-first / characterization tests)
- IntelliJ inspections for automated formatting and structural checks (Layer 1 of code review)
- MCP server security considerations

## How Junie Uses It

Junie reads `.junie/guidelines.md` automatically. It is loaded into every prompt. No additional configuration is needed.

## Setup

```bash
cp -r .junie your-project/
```

Then open your project in a JetBrains IDE with Junie enabled. The guidelines file is picked up automatically.
