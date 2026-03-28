<!-- trigger: model_decision -->
# Cost Optimization

Advocacy organizations run on nonprofit budgets. Every dollar on AI compute is a dollar not spent on investigations, legal defense, or sanctuary operations. Vendor lock-in is a movement risk: a nonprofit locked to one AI provider faces existential budget exposure when prices change.

## Model Routing

Route tasks to the cheapest capable model:
- **Cheap/fast models:** test generation, boilerplate, formatting, simple refactoring, documentation
- **Mid-tier models:** debugging, multi-file changes, code review, integration work
- **Frontier models:** hard architecture problems, complex debugging, security-critical review

## Token Budget Discipline

Set hard limits per session and per day. A single runaway conversation can consume a week's budget. Cap conversation duration. When hitting the ceiling, stop and reassess rather than throwing more tokens at an unproductive path. Track actual spend weekly.

## Prompt Cache Optimization

Place static content first in prompts — target 80%+ cache hit rates. Instruction files, project context, and architectural descriptions are static and should appear before dynamic task content. Every cache miss on repeated static content is wasted money.

## Budget Allocation

For resource-constrained teams: **40% implementation, 30% testing, 20% review/debugging, 10% documentation.** If testing drops below 30%, downstream bug costs multiply. Track **cost per merged PR** as the efficiency metric — not cost per generated line.

## Vendor Lock-In Mitigation

ALWAYS abstract model dependencies behind project-owned interfaces. Risks: price increases exceeding nonprofit budgets, policy changes restricting advocacy use cases. Maintain self-hosted fallback for critical paths. Evaluate open-source models regularly for non-frontier tasks.

## Self-Hosted Economics

For teams processing sensitive data regularly, self-hosted open-source inference may be cheaper than cloud APIs at scale while satisfying security requirements. Calculate the break-even: cloud costs versus infrastructure for self-hosted deployment.

## Efficiency

Run smallest relevant test subset first; full suite on commit. Use watch mode. Parallelize execution. Start sessions fresh rather than extending degraded conversations. Break work into chunks completing within half the context window. Compact at ~50% context usage.
