# Code Mode — Implementation

Code mode is for building. You can read files, write code, run commands, and execute tests. This is where design becomes reality. Every line of code you write operates in a high-risk advocacy domain where errors can expose activists, lose evidence, or compromise investigations.

## Workflow — Follow Every Time

1. **Read** existing code before writing anything — search for existing utilities, patterns, and conventions
2. **Plan** the change — identify which bounded context is affected, what tests are needed
3. **Code** the minimum implementation to satisfy the specification
4. **Test** — run relevant tests before committing; every commit must leave the codebase passing
5. **Verify** — check your output against the review checklist below

## Skills to Use

- **git-workflow** — for commits, branches, and PR curation. Commit after each logical subtask. Ephemeral branches, squash-merge.
- **testing-strategy** — for writing and reviewing tests. Spec-first generation preferred. Review assertions against specification, not code.

## Design Principles — AI Code Review Checklist

Before finishing any implementation, check your output against these ranked failure modes (most common in AI-generated code):

1. **DRY** — did you duplicate existing logic? Search the codebase. AI clones at 4x the normal rate.
2. **Deep modules** — are your abstractions deep (simple interface, powerful functionality) or shallow (pass-through wrappers that hide nothing)?
3. **Single responsibility** — does each function do one thing at one level of abstraction?
4. **Error handling** — did you catch-all or silently swallow failures? Review every error path. In advocacy code, silent failure means lost evidence.
5. **Information hiding** — does your interface expose only what callers need?
6. **Ubiquitous language** — does your code use movement terminology (campaign, investigation, coalition, sanctuary), not AI-invented synonyms?
7. **Design for change** — did you add abstraction layers and loose coupling?
8. **Legacy velocity** — is the code readable and changeable? AI code churns 2x faster.
9. **Over-patterning** — did you apply Strategy/Factory/Observer where a function and conditional suffice?
10. **Test quality** — does every test fail when the behavior it covers is broken?

## Concern Files — Follow All Applicable

Testing, security, privacy, cost optimization, advocacy domain, accessibility, and emotional safety concern files all apply in Code mode. Read and follow the relevant concern files for the code you are writing.

## Two-Failure Rule

After two failed fix attempts, STOP. Clear the conversation and restart with a better prompt incorporating what you learned. Do not compound errors — three wrong attempts in a row rarely converge on the right answer.

## What You Must Not Do

- Do not commit code that breaks existing tests
- Do not introduce dependencies without verifying they exist in their registry (slopsquatting defense)
- Do not send sensitive data to external APIs without explicit approval
- Do not log, store, or transmit activist personally identifiable information
- Do not display traumatic content without progressive disclosure and content warnings
- Do not allow data to cross bounded context boundaries without anti-corruption layers
