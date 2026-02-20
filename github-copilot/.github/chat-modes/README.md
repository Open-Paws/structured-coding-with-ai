# GitHub Copilot Custom Chat Modes

2 custom chat mode YAML files that create persistent agent personas. Each file defines a `name`, `description`, `instructions` block, and `tools` list.

Unlike prompts (which are one-shot workflow guides), chat modes create a persistent persona that stays active for the duration of the chat session. The agent behaves according to its instructions across multiple messages.

## Chat Modes

| File | Persona | Purpose |
|------|---------|---------|
| `advocacy-reviewer.yml` | Advocacy Code Reviewer | Reviews code using a four-layer pipeline: verify automated checks, Ousterhout design quality red flags, AI-specific failure patterns (DRY violations, suppressed errors, hallucinated APIs, silent failures), and advocacy-specific concerns (data leaks, surveillance surface, emotional safety, coalition boundaries). Classifies findings as blocking or suggestions. |
| `requirements-interviewer.yml` | Requirements Interviewer | Gathers requirements through structured one-question-at-a-time interviews across six phases: purpose/users, threat modeling, coalition/data boundaries, user safety, technical constraints, and synthesis into a specification document. |

Both chat modes have `file_search` tool access enabled.
