# Aider — Structured Coding Instructions

This directory contains a single file, `CONVENTIONS.md`, which provides project-level coding conventions for [Aider](https://aider.chat).

## What It Contains

`CONVENTIONS.md` is a comprehensive instruction file covering:

- **7 concerns**: design principles, testing, security, privacy, cost optimization, accessibility, emotional safety
- **6 process skills**: git workflow, testing strategy, requirements interview, plan-first development, code review, security audit

The file references Aider-specific features:

- `/architect` mode for planning, design, and codebase exploration
- `/code` mode for implementation
- Aider's automatic commit behavior

## How Aider Uses It

Aider loads `CONVENTIONS.md` as read-only context into every prompt when the file is present in the project root. Its position at the start of the context is inherently cache-friendly for prompt cache optimization.

## Setup

```bash
cp CONVENTIONS.md your-project/
```

Then start Aider in your project directory. The file is picked up automatically.
