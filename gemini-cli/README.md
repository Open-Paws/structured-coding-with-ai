# Gemini CLI — Structured Coding Instructions

This directory contains a single file, `GEMINI.md`, which provides project-level coding conventions for [Gemini CLI](https://github.com/google-gemini/gemini-cli).

## What It Contains

`GEMINI.md` is a comprehensive instruction file covering:

- **7 concerns**: design principles, testing, security, privacy, cost optimization, accessibility, emotional safety
- **6 process skills**: git workflow, testing strategy, requirements interview, plan-first development, code review, security audit

The file references Gemini CLI-specific features:

- Sandbox mode and its implications for data leakage outside the sandbox boundary
- Tool confirmation prompts and why auto-approval should be avoided for sensitive projects
- `GEMINI.md` as the only instruction file Gemini CLI reads

## How Gemini CLI Uses It

`GEMINI.md` sits at the project root and is loaded into every Gemini CLI prompt automatically. It is the sole instruction file for Gemini CLI -- there is no other mechanism for persistent project-level rules.

## Setup

```bash
cp GEMINI.md your-project/
```

Then run Gemini CLI from your project directory. The file is picked up automatically.
