# Cost Optimization for Animal Advocacy Projects

Advocacy organizations operate on nonprofit budgets. Every dollar spent on AI compute is a dollar not spent on investigations, legal defense, or sanctuary operations. Cost optimization is not an engineering preference — it is a movement resource allocation decision. Vendor lock-in is a movement risk: a nonprofit locked to a single AI provider faces existential budget exposure when prices change.

## Model Routing — Right Model for Each Task

Route tasks to the cheapest model capable of handling them well.

- **Cheap tier — Claude Haiku 4.5 (`claude-haiku-4-5-20251001`)**: test generation, boilerplate code, formatting assistance, simple refactoring, mechanical edits, documentation, glue code, log parsing, summarization of structured output. Default for desloppify-driven mechanical work. Default for first-pass scout / triage when the observation is well-structured.
- **Mid tier — Claude Sonnet 4.6 (`claude-sonnet-4-6`)**: debugging, multi-file changes, code review, integration work, plan authoring against a clear spec, test review, persona-QA narrative writing.
- **Frontier — Claude Opus 4.7 (`claude-opus-4-7`, default on this stack)**: hard architectural problems, complex debugging, novel design challenges, security-critical code review, adversarial audit, the strategic / Chat-Gary surface.

Aider achieves comparable benchmark scores at 3× fewer tokens than some alternatives — consider token-efficient tools for routine workflows. The single biggest cost win in this stack is **routing cheap things to Haiku rather than reaching for Opus by default**.

## Token Budget Discipline

Set hard budget limits per session and per day. A single runaway agent conversation can consume a week's compute budget. Cap conversation duration to prevent indefinite token consumption. When an agent hits the budget ceiling, stop and reassess approach rather than allocating more tokens to a potentially unproductive path. Track actual spend against budget weekly.

## Prompt Cache Optimization

Place static content first in prompts to maximize cache hit rates — target 80%+ cache hits. Instruction files, project context, and architectural descriptions are static content that should appear before dynamic task-specific content. Every cache miss on repeated static content is wasted money. Structure your instruction file hierarchy so the most commonly loaded content is also the most cacheable.

## Budget Allocation Framework

For resource-constrained advocacy teams, allocate AI compute budget approximately: **40% implementation**, **30% testing** (generation plus execution loops), **20% review and debugging**, **10% documentation**. If testing allocation drops below 30%, test quality degrades and downstream bug costs multiply. Track **cost per merged PR** as the key efficiency metric — not cost per generated line of code. A cheap PR that introduces bugs costs more than an expensive PR that ships clean.

## Vendor Lock-In as Movement Risk

ALWAYS abstract model and vendor dependencies behind project-owned interfaces. A nonprofit that builds critical advocacy infrastructure on a single vendor's proprietary API faces two risks: price increases that exceed budget (advocacy budgets cannot scale with enterprise pricing), and policy changes that restrict advocacy use cases (model providers have content policies that may conflict with investigation documentation). Maintain self-hosted fallback capability for critical code paths. Evaluate open-source models regularly as cost-effective alternatives for non-frontier tasks.

## Self-Hosted Inference Economics

For teams processing sensitive data regularly, self-hosted open-source inference may be cheaper than cloud APIs at scale while also satisfying security requirements for investigation and witness data. Calculate the break-even point: cloud API costs versus infrastructure costs for self-hosted deployment. For many advocacy organizations, a modest GPU allocation running an open model costs less per month than heavy API usage and eliminates data retention concerns entirely.

## Efficiency Practices

Run the smallest relevant test subset first during development; full suite on commit only. Use watch mode for continuous feedback during implementation. Parallelize test execution to reduce wall-clock time. Start sessions fresh rather than extending degraded long conversations. Break work into subtasks that complete within half the context window — long contexts degrade quality and waste tokens on repeated content. Compact conversations at approximately 50% context usage.
