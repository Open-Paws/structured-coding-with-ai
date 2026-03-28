# AGENTS.md — Universal AI Coding Instructions

This directory contains `AGENTS.md`, a vendor-neutral instruction file following the [AGENTS.md standard](https://agents-md.org) supported by 20+ AI coding tools.

## What It Contains

`AGENTS.md` is a comprehensive, tool-agnostic instruction file covering:

- **7 concerns**: design principles, testing, security, privacy, cost optimization, accessibility, emotional safety
- **6 process skills**: git workflow, testing strategy, requirements interview, plan-first development, code review, security audit

The file makes no references to any specific AI coding tool. It is completely tool-agnostic.

## When to Use

- As a **fallback** for AI coding tools that are not otherwise listed in this repository (e.g., Cursor, Windsurf, Copilot, Cline, etc.)
- As a **supplementary file** alongside tool-specific instructions, providing a shared baseline that any tool can read

## How Tools Use It

Tools that support the AGENTS.md standard automatically discover and load the file when it is present in the project root or in parent directories. The file is self-contained -- no external documents are referenced or required.

## Setup

```bash
cp AGENTS.md your-project/
```

The file is picked up automatically by any AGENTS.md-compatible tool.
