## How this document relates to the others

This document covers collaboration mechanics—the "how" of working together on code. It synthesizes principles from canonical software engineering texts and applies them to git/GitHub workflows. Where AI-assisted development changes the calculus, cross-references point to AI_CODING.md. Where design principles underpin the workflow choices, cross-references point to SOFTWARE_DESIGN.md. Where testing practices are the enforcement mechanism, cross-references point to TESTING.md.

Several genuine tensions exist between the timeless principles documented here and the realities of AI-assisted development documented in AI_CODING.md. These are flagged explicitly rather than papered over.

---

## Pro Git (Scott Chacon & Ben Straub)

**THE canonical Git reference - official Git book, comprehensively revised**

**Git Basics:**
- Working directory, staging area, repository (three states)
- Commit early, commit often - commits are cheap
- Each commit is a snapshot, not a delta
- Branching is cheap (just a pointer)
- Distributed means every clone is a full backup

**Commit Best Practices:**
- Atomic commits (one logical change)
- Write commit messages for humans in the future
- First line: 50 chars, imperative mood ("Fix bug" not "Fixed bug")
- Blank line, then details if needed
- Why, not what (code shows what)
- Reference issues/tickets

**Branching Models:**
- Topic branches (short-lived feature branches)
- Long-running branches (master/develop stable, next/pu experimental)
- Integration branches
- Feature branches merged via pull request
- Delete branches after merge

**Merging vs Rebasing:**
- Merge preserves history (creates merge commit)
- Rebase rewrites history (linear)
- "Do not rebase commits that exist outside your repository"
- Golden rule: never rebase public history
- Interactive rebase for cleaning up local commits before push
- Squash commits when appropriate (multiple WIP commits → one feature commit)

**Distributed Workflows:**
- Centralized (one canonical repo, everyone pushes)
- Integration-Manager (maintainer merges, contributors fork)
- Dictator-Lieutenants (Linux kernel model, hierarchical)
- Pull requests for contribution
- Fork + PR for open source
- Branch + PR for teams with shared repo

**Contributing to Projects:**
- Follow project's commit message style
- Keep commits small and focused
- One feature per branch
- Rebase on latest before submitting PR
- Respond to review feedback with new commits or force-push after rebase (project dependent)

**Maintaining Projects:**
- Topic branches for everything
- Test before merging
- Cherry-pick for backports
- Never rewrite published history
- Tag releases
- Write good release notes

**Git Internals:**
- Objects: blobs, trees, commits, tags
- References: heads, tags, remotes
- Packfiles for efficiency
- Understanding this helps debug weird situations

---

## Git for Teams (Emma Jane Hogbin Westby)

**Team-focused workflows - practical patterns for collaboration**

**Branching Strategies:**

**Collated (Single Branch):**
- Everyone commits to main/master
- Works for: very small teams, tight coordination
- Requires: discipline, frequent integration, good communication
- Risk: breaks affect everyone immediately

**Branch-per-Feature:**
- Each feature gets its own branch
- Merged when complete and tested
- Works for: most teams
- Isolation + integration balance
- Delete after merge

**State Branching (Gitflow):**
- master (production), develop (integration), feature/* (work), release/*, hotfix/*
- Structured but heavyweight
- Works for: scheduled releases, multiple environments
- Overhead for continuous deployment

**Scheduled Deployment (GitHub Flow):**
- master always deployable
- Branch for features
- PR for review
- Merge and deploy immediately
- Works for: continuous deployment, web apps
- Simple, fast-moving teams

**Team Patterns:**

**Commit Size:**
- Small commits easier to review
- Each commit should compile/pass tests
- "Checkpoint commits" OK locally, squash before merge
- Aim for "this is reviewable in one sitting"

**Review Process:**
- All code reviewed before merge (no exceptions)
- Author responsibility: make reviewable (small, clear, tested)
- Reviewer responsibility: timely feedback, constructive
- Pair programming can reduce formal review need
- Review tools matter (GitHub, GitLab, etc.)

**Communication:**
- Document workflow in CONTRIBUTING.md
- Link commits to issues
- Use PR/MR descriptions to explain context
- @mention for specific feedback requests
- Status updates in standup/async

**Onboarding:**
- Written workflow guide
- Pairing with experienced dev
- Small first PR
- Quick feedback loop
- Normalize questions

---

## Continuous Delivery (Jez Humble & David Farley)

**Not specifically Git, but defines modern workflows**

**Version Control:**
- Everything in version control (code, tests, config, scripts, docs, DB schemas)
- Commit frequently (at least daily)
- Don't break the build
- Small, incremental changes
- Branch by abstraction over long-lived branches

**Trunk-Based Development:**
- All developers work on trunk (main/master)
- Very short-lived feature branches (hours to 1-2 days max)
- Feature flags for incomplete features
- Continuous integration on trunk
- Release from trunk

> **[TENSION]** Accelerate and Continuous Delivery advocate trunk-based development with short-lived branches. AI_CODING.md recommends "feature branches for AI work so you can delete and restart if the agent goes sideways." The resolution: **trunk-based development remains the goal, with ephemeral AI experiment branches that get squash-merged or deleted within hours.** AI branches should be even shorter-lived than human feature branches—if the agent hasn't produced mergeable work in one session, the branch should be deleted and the approach reconsidered. The branch exists as a safety net for throwaway, not as a long-lived workspace.

**Branching:**
- Long-lived branches are inventory (waste in Lean terms)
- The longer a branch lives, the harder the merge
- Branch for release, not for development
- Don't branch to defer integration pain - integrate continuously

**Commits:**
- Check in regularly (multiple times per day)
- Each commit must build
- Each commit should pass tests
- Small commits reduce merge conflicts
- Frequent commits enable fast feedback

> **[TENSION]** "Commit early, commit often" meets "atomic commits" when an AI agent refactors 12 files at once. The resolution: **AI agents should be configured to commit after each logical subtask, not after the entire task completes.** If the agent's task decomposes into "extract interface, implement adapter, update callers," those are three commits, not one. Task decomposition (see AI_CODING.md, "Task decomposition is non-negotiable") is the mechanism that preserves atomic commits in AI workflows. The human's job is to define the subtasks; the agent's job is to execute and commit each one.

**Code Review:**
- Review before or after commit (team decides)
- Pair programming as continuous review
- Automated checks (lint, format, tests) before human review
- Keep reviews small (commits small)
- Reviews shouldn't block for days

---

## Accelerate (Nicole Forsgren, Jez Humble, Gene Kim)

**Research-based - what actually correlates with high performance**

**Key Findings:**
- Trunk-based development correlates with high performance
- Short-lived branches (< 1 day) or straight to trunk
- Comprehensive test automation enables frequent integration
- Small batch sizes (small PRs/commits)
- Teams with code review perform better
- Pair programming counts as review

**Metrics that Matter:**
- Deployment frequency (high performers: multiple per day)
- Lead time for changes (commit to production: < 1 hour)
- Time to restore service (< 1 hour)
- Change failure rate (< 15%)

**What Enables This:**
- Trunk-based development
- Automated testing
- Continuous integration
- Short integration cycles
- Small, frequent changes
- Everyone can fix any code

**Anti-patterns:**
- Long-lived feature branches
- Infrequent merges
- Large batch sizes
- Manual testing gates
- Code freeze periods

---

## The DevOps Handbook (Gene Kim, Jez Humble, Patrick Debois, John Willis)

**Workflow patterns from DevOps practice**

**Version Control:**
- Single source of truth
- Main/trunk always deployable
- Branch rarely, integrate frequently
- Automated validation on every commit
- Fast feedback loops

**Deployment Pipeline:**
- Commit → Build → Test → Deploy
- Every commit goes through pipeline
- Fail fast (catch issues early)
- Visualize pipeline status
- Optimize for speed

**Code Review:**
- Required but lightweight
- Focus on: correctness, readability, maintainability
- Automated checks first (lint, format, tests)
- Humans review: logic, design, context
- 24-hour review SLA (don't block progress)

> **[TENSION]** AI adoption increased PR review time by **91%** while PR volume surged (Faros AI, AI_CODING.md). A 24-hour SLA becomes impossible if review load nearly doubles. The resolution requires all three levers: (1) stricter PR size limits to keep individual reviews manageable, (2) AI-assisted code review to handle the mechanical first pass (see AI_CODING.md, "AI-assisted code review"), and (3) automated quality gates doing more pre-review filtering (see TESTING.md for test-based gates). The 24-hour SLA remains the target, but it's only achievable if the review pipeline is layered: automated checks → AI review → human review of what remains.

**Merging Strategy:**
- Integrate continuously
- Resolve conflicts immediately
- Don't accumulate integration debt
- Test after every merge
- Roll forward, not back

---

## Engineering Practices (from various sources - these are industry standard but I'm honest these come from practice more than single-source books)

**Commit Frequency:**
- Minimum: daily to trunk/develop
- Ideal: multiple times per day
- Each commit: compiles, passes tests, adds value
- Use feature flags to hide incomplete work

**When to Commit:**
- Completed logical unit of work
- All tests passing
- Code compiles
- No commented-out code
- Removed debugging artifacts
- Before switching context

**PR/MR Size:**
- Small: < 200 lines changed (ideal: < 100)
- Large PRs don't get reviewed well
- Break features into smaller PRs if possible
- "Stack" PRs for large features (PR1 → PR2 → PR3)
- Review time increases non-linearly with size

> **[TENSION]** AI adoption increased PR size by **154%** (Faros AI, AI_CODING.md). This directly contradicts the <200 line ideal. The resolution: **PR discipline becomes the critical human skill in AI-assisted development.** The ease of generating large changes is not permission to submit large PRs. AI-generated work must be broken into reviewable chunks before submission—not after a reviewer complains. The human's job shifts from writing code to curating PRs: splitting agent output into logical, reviewable units. Stacked PRs are the primary mechanism for large AI-generated changes.

**When to Merge:**
- All tests passing
- CI green
- Reviewed and approved
- Conflicts resolved
- As soon as approved (don't let PRs sit)

**Merge Strategies:**

**Merge Commit:**
- Preserves history
- Shows when branches merged
- Can clutter history
- Good for: tracking feature integration

**Squash and Merge:**
- Combines all commits into one
- Clean linear history
- Loses granular commit history
- Good for: feature branches with messy commits

**Rebase and Merge:**
- Linear history
- Preserves individual commits
- Requires force-push if updating PR
- Good for: clean commit history, no merge commits

---

## Specific AI-Age Considerations

**Since code writing is cheap but review is expensive:**

**Optimize for Review:**
- Each PR should tell a story
- Commits should be logical steps
- PR description explains "why" (code shows "what")
- Link to design docs for complex changes
- Include screenshots for UI changes
- Call out areas needing close review

**Test Before Review:**
- All automated tests pass
- Manual testing complete
- Edge cases considered
- Performance impact measured
- No "test this for me" PRs

**Review Automation:**
- Linting/formatting automated (not reviewed by humans)
- Type checking automated
- Security scanning automated
- Test coverage measured
- Only human-judgment questions reach reviewers

**Commit Strategy with AI:**
- AI-generated code still needs atomic commits
- Don't commit entire AI output as one blob
- Break into logical pieces
- Write commit messages explaining intent (AI can't do this)
- Each commit should make sense independently

**Review Focus:**
- Architecture decisions (not syntax)
- Edge cases (not formatting)
- Security implications (not style)
- Performance impact (not naming)
- Maintainability (not line count)

---

## Workflow Anti-Patterns (from various practitioners)

**Long-Lived Feature Branches:**
- Merge conflicts accumulate
- Divergence from main grows
- Integration becomes risky event
- Testing becomes harder
- Review becomes impossible

**"WIP" Commits:**
- OK locally
- Never push to shared branches
- Rebase/squash before PR
- Each pushed commit should be meaningful

**Mega Commits:**
- 50 files changed, "various fixes"
- Unreviewable
- Hard to revert
- Hides multiple concerns
- Break into separate commits

**Merge Debt:**
- Delaying integration
- Stacking un-merged changes
- Creates compound conflicts
- Increases risk
- Merge frequently

**Review Bottlenecks:**
- One person approves everything
- Reviews take days
- Large PRs sit waiting
- Synchronous review meetings
- Solution: smaller PRs, distributed ownership, async review

**Broken Main/Trunk:**
- Tests failing on main
- "Will fix later"
- Blocks everyone
- Fix immediately or revert

**Unclear Ownership:**
- Who can merge?
- Who should review?
- Who maintains this code?
- Document in CODEOWNERS or similar

---

## Team Coordination Patterns

**Small Teams (2-5):**
- Can work on trunk directly
- Quick sync before merge
- Informal review OK
- High trust, high communication

**Medium Teams (5-20):**
- Feature branches recommended
- Required reviews
- Branch protection on main
- Clear ownership boundaries
- Some specialization OK

**Large Teams (20+):**
- Strict PR process
- Multiple reviewers
- Automated checks gate merge
- Clear ownership (CODEOWNERS)
- Coordination via RFCs/design docs
- Monorepo or well-defined repo boundaries

---

## Monorepo Considerations (Google, Facebook scale)

**From "Software Engineering at Google" practices:**
- Single repo for entire company
- Atomic cross-project changes
- Unified versioning
- Shared infrastructure
- Requires excellent tooling
- Scale requires investment

**But for smaller orgs:**
- Multiple repos with clear boundaries
- Services loosely coupled
- Independent deployment
- Easier to manage without Google-scale tools