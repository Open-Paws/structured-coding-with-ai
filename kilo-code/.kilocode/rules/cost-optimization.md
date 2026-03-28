# Cost Optimization for Animal Advocacy Projects

Advocacy organizations operate on nonprofit budgets. Every dollar spent on AI compute is a dollar not spent on investigations, legal defense, or sanctuary operations. Cost optimization is a movement resource allocation decision. Vendor lock-in is a movement risk: a nonprofit locked to a single AI provider faces existential budget exposure when prices change.

## Model Routing — Right Model for Each Task

Route tasks to the cheapest model capable of handling them well. Use cheaper, faster models for: test generation, boilerplate, formatting, simple refactoring, documentation. Use mid-tier models for: debugging, multi-file changes, code review, integration work. Reserve frontier models for: hard architectural problems, complex debugging, novel design, security-critical review. Consider token-efficient tools for routine workflows — some achieve comparable quality at 3x fewer tokens.

## Token Budget Discipline

Set hard budget limits per session and per day. A single runaway conversation can consume a week's compute budget. Cap conversation duration. When hitting the budget ceiling, stop and reassess rather than allocating more tokens to a potentially unproductive path. Track actual spend weekly.

## Prompt Cache Optimization

Place static content first in prompts to maximize cache hit rates — target 80%+ cache hits. Instruction files, project context, and architectural descriptions are static content that should appear before dynamic task-specific content. Every cache miss on repeated static content is wasted money.

## Budget Allocation Framework

For resource-constrained advocacy teams: **40% implementation**, **30% testing** (generation plus execution loops), **20% review and debugging**, **10% documentation**. If testing allocation drops below 30%, test quality degrades and downstream bug costs multiply. Track **cost per merged PR** as the key efficiency metric — not cost per generated line of code.

## Vendor Lock-In as Movement Risk

ALWAYS abstract model and vendor dependencies behind project-owned interfaces. A nonprofit on a single vendor's proprietary API faces: price increases exceeding budget (advocacy budgets cannot scale with enterprise pricing), and policy changes restricting advocacy use cases (model providers have content policies that may conflict with investigation documentation). Maintain self-hosted fallback capability. Evaluate open-source models regularly for non-frontier tasks.

## Self-Hosted Inference Economics

For teams processing sensitive data regularly, self-hosted open-source inference may be cheaper than cloud APIs at scale while satisfying security requirements. Calculate the break-even point: cloud API costs versus infrastructure for self-hosted deployment. For many organizations, a modest GPU running an open model costs less per month than heavy API usage and eliminates data retention concerns.

## Efficiency Practices

Run smallest relevant test subset first; full suite on commit only. Use watch mode for continuous feedback. Parallelize test execution. Start sessions fresh rather than extending degraded conversations. Break work into subtasks completing within half the context window. Compact at approximately 50% context usage.
