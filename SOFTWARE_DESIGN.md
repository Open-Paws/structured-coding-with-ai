## How to read this document in the AI age

The principles below are timeless—they predate AI coding tools and will outlast any particular model or vendor. But AI-assisted development shifts which principles demand the most attention. Throughout this document, **[AI-ERA]** annotations flag where AI code generation makes a principle more critical, harder to maintain, or differently relevant. These are not modifications to the original ideas; they are notes on where the pressure points have moved.

> Cross-reference: AI_CODING.md covers the empirical evidence for AI coding tool behavior. TESTING.md covers the testing strategies that make these principles enforceable. GITHUB_RULES.md covers the collaboration practices that operationalize them.

---

## A Philosophy of Software Design (John Ousterhout)

**Core Thesis:**
- Complexity is incremental - comes from accumulated tactical decisions
- Working code isn't enough - must fight complexity continuously
- Strategic programming vs tactical programming (working code vs good design)

**Deep Modules:**
- Best modules have simple interfaces, powerful functionality
- Cost/benefit ratio: interface complexity vs functionality provided
- Information hiding - minimize what users need to know
- Example: Unix I/O (5 methods, infinite capability)
- **[AI-ERA]** AI agents consistently generate shallow modules—thin wrappers, pass-through methods, classes that just delegate. This is the single most common structural flaw in AI-generated code. Review AI output specifically for module depth. If a class or module's interface is as complex as its implementation, the AI has produced a shallow abstraction.

**Complexity Defined:**
- Cognitive load - how much you need to know to change something
- Three symptoms: Change amplification, cognitive load, unknown unknowns
- Two causes: Dependencies and obscurity
- **[AI-ERA]** AI-generated code accelerates complexity accumulation. GitClear found 4x more code cloning in AI-assisted repos and code churn projected to double. Each AI generation session that doesn't actively fight complexity adds to it. The "tactical programming" trap Ousterhout warns about is the default AI behavior—working code shipped fast with no thought to long-term structure.

**Interface Design:**
- Different interface vs deep interface
- Expose as little as possible
- Pass-through methods/variables are red flags
- Getters/setters often indicate shallow design

**Layer Principles:**
- Each layer should provide abstraction
- Pass-through layers add complexity without value
- Dispatcher patterns often wrong - violates information hiding

**Comments:**
- Should describe things code can't
- Not WHAT (code shows that) but WHY and HOW it relates to larger system
- Interface comments vs implementation comments
- Precision matters - vague comments worse than none

**Naming:**
- Names should be precise and unambiguous
- If hard to name, design probably wrong
- Red flag: name longer than entity being named

**Error Handling:**
- Define errors out of existence when possible
- Aggregate exceptions - fewer exception types
- Exception masking vs exception aggregation vs crash

**Design Twice:**
- Always consider multiple approaches
- Easy to get stuck on first idea
- Comparing options reveals what matters

**Pull Complexity Downward:**
- Module developer handles complexity so users don't have to
- Configuration parameters push complexity up to users
- Better to have intelligent defaults

**Better Together/Apart:**
- Bring together if: shared information, used together, overlapping concerns, hard to understand separately
- Separate if: general-purpose vs special-purpose, different concepts
- Length itself doesn't matter - coherence matters

**Consistency:**
- Similar things should be done similarly
- Names, coding style, interfaces, design patterns
- Reduces cognitive load, allows assumptions
- Document conventions early

**Obvious Code:**
- If reader must read other code to understand this code - not obvious
- Event-driven programming inherently obscure (control flow scattered)
- Generic containers trade type safety for flexibility

**Red Flags:**
- Shallow module
- Information leakage
- Temporal decomposition (structure follows execution order)
- Overexposure (interface more complex than implementation)
- Pass-through method/variable
- Repetition
- Special-general mixture
- Conjoined methods (can't understand one without other)
- Comment repeats code
- Implementation documentation contaminates interface
- Vague name
- Hard to pick name (design probably wrong)
- Hard to describe (interface probably wrong)
- Nonobvious code
- **[AI-ERA]** This red flag list doubles as an AI code review checklist. AI-generated code frequently triggers: shallow module, pass-through method, repetition, and temporal decomposition. Print this list. Use it during every AI-generated code review.

**Consistency Mechanisms:**
- Checklist in code review
- Automated enforcement where possible
- Obvious from code structure
- Well-documented

---

## Essentialism: The Disciplined Pursuit of Less (Greg McKeown)

**Core Philosophy:**
- Only do what is essential
- Trade-off: can't have it all, must choose
- Fewer things done better vs many things done poorly

**The Essentialist:**
- Pauses to discern what really matters
- Says no to most things
- Removes obstacles to make essential effortless
- "What are the trade-offs?" not "How can I do it all?"

**Explore:**
- Create space to think
- Permission to play
- Importance of sleep for cognition
- Extreme selectivity in opportunities

**Eliminate:**
- Clarify essential intent (concrete and inspirational)
- Dare to say no gracefully
- Uncommit from non-essentials (sunk cost)
- Edit ruthlessly (making better by removing)
- Set boundaries (protects essential)

**Execute:**
- Buffer (add 50% to time estimates)
- Subtract to progress (what obstacles to remove?)
- Small wins create momentum
- Routine makes essential the default
- Focus on present moment

**Key Mechanics:**
- 90% rule: if not 90% yes, it's a no
- Design intent criteria before seeing options
- Zero-based budgeting mindset
- Regular pruning/editing
- Protect asset that produces value (yourself)

---

## The Pragmatic Programmer (Hunt & Thomas)

**Care About Your Craft:**
- No broken windows (fix bad design/code immediately)
- Be a catalyst for change
- Remember big picture
- Make quality a requirements issue
- Invest regularly in knowledge portfolio
- Critically analyze what you read/hear
- Communicate effectively

**DRY - Don't Repeat Yourself:**
- Every piece of knowledge single, unambiguous, authoritative
- Not just code - documentation, data, APIs
- Duplication of knowledge vs duplication of implementation
- **[AI-ERA]** AI agents are prolific duplicators. They don't know what already exists in your codebase unless it's in context. GitClear's finding of 4x more code cloning traces directly to DRY violations. Mitigation: keep project context files (CLAUDE.md, .cursorrules) that list existing utilities and shared modules so the AI uses them instead of reinventing them.

**Orthogonality:**
- Eliminate effects between unrelated things
- Changes localized
- Promotes reuse
- Two components orthogonal if changes to one don't affect other
- Reduces risk
- Easy to test
- **[AI-ERA]** AI agents working on one module frequently introduce coupling to other modules they've seen in context. When an agent refactors 12 files at once, orthogonality violations multiply because the agent optimizes for "making it work" rather than "keeping things independent." Smaller, focused AI tasks preserve orthogonality better than large multi-file generations.

**Reversibility:**
- No final decisions
- Prepare for contingencies
- Forgo patterns that tie you to specifics

**Tracer Bullets:**
- Quick to target, immediate feedback
- Incremental approach
- Not prototyping (throw-away) - structure you keep building on

**Prototypes:**
- Ignore: correctness, completeness, robustness, style
- Code to be thrown away
- Learn from then discard

**Domain Languages:**
- Program close to problem domain
- Mini-languages for specific problems

**Estimating:**
- Understand what's being asked
- Build model of system
- Break into components
- Give parameters to answer ("in ideal conditions...")
- Track estimates vs actuals

**Debugging:**
- Fix the problem, not the blame
- Don't panic
- Reproduce reliably
- Read the error message
- Binary search to isolate
- Explain it to someone (rubber duck)
- Check obvious first

**Testing:**
- Test against contract
- Design to test
- Test your tests (force errors)
- Test state coverage, not code coverage
- Find bugs once (write test that would catch it)
- **[AI-ERA]** "Test your tests" is the most important Pragmatic Programmer principle for AI workflows. AI generates tests that look comprehensive but often have tautological assertions. Mutation testing ("force errors") is the practical way to verify AI-generated test quality. See TESTING.md for the full assertion quality framework.

**Refactoring:**
- Disciplined technique for restructuring
- Small behavior-preserving transformations
- Do early, do often
- Make it easier to add next feature

**Design by Contract:**
- Preconditions, postconditions, invariants
- Clear responsibilities
- Document assumptions
- Crash early (fail fast)

**Teams:**
- Don't leave broken windows
- Boil the frog (notice incremental decline)
- Know when to stop (good enough vs perfect)
- Build teams, not cathedrals (focus on individuals)

---

## Clean Code (Robert Martin)

**Meaningful Names:**
- Reveal intention
- Avoid disinformation
- Make meaningful distinctions
- Use pronounceable names
- Use searchable names
- Avoid encodings
- Class names: nouns. Method names: verbs
- One word per concept
- Use solution domain names (CS terms)
- Add meaningful context

**Functions:**
- Small (smaller than you think)
- Do one thing
- One level of abstraction per function
- Readable top to bottom
- Few arguments (0-2 ideal, 3 questionable, 4+ rethink)
- No side effects
- Command query separation (do something OR answer something)
- Prefer exceptions to error codes
- Extract error handling
- **[AI-ERA]** AI agents generate long, multi-responsibility functions by default. "Do one thing" and "one level of abstraction" are the principles most commonly violated in AI-generated code. When reviewing AI output, check function length and responsibility count first—these are the fastest signals of quality.

**Comments:**
- Good code mostly doesn't need them
- Explain intent when necessary
- Clarify code that can't be clear
- Warn of consequences
- TODO acceptable
- Bad: mumbling, redundant, mandated, journal, noise, position markers, closing brace, attribution, commented-out code, nonlocal information

**Formatting:**
- Vertical: concepts separated by blank lines, related close together, variables near usage
- Horizontal: short lines, indentation shows scope
- Team agrees on style

**Objects vs Data Structures:**
- Objects hide data, expose behavior
- Data structures expose data, no behavior
- Law of Demeter: module shouldn't know internals of objects it manipulates
- Don't chain method calls (train wrecks)

**Error Handling:**
- Use exceptions
- Write try-catch-finally first
- Provide context with exceptions
- Define exception classes in terms of caller's needs
- Don't return null
- Don't pass null
- **[AI-ERA]** IEEE Spectrum found newer models increasingly generate code that suppresses errors and removes safety checks. AI error handling is frequently too broad (catching Exception instead of specific types) or silently swallows failures. This is one of the most dangerous AI code generation patterns. Review every try/catch block in AI-generated code.

**Boundaries:**
- Third-party code: wrap interfaces you don't control
- Learning tests for external APIs
- Use code that doesn't exist yet (define interface you wish you had)

**Unit Tests:**
- TDD: write test before production code
- Keep tests clean (as important as production code)
- One assert per test (mostly)
- Single concept per test
- F.I.R.S.T: Fast, Independent, Repeatable, Self-validating, Timely

**Classes:**
- Start with variables, then functions
- Small
- Single Responsibility Principle
- High cohesion
- Low coupling
- Organize for change (OCP - open/closed principle)
- DIP - depend on abstractions

**Systems:**
- Separate construction from use
- Dependency injection
- Scale up, not build big upfront
- Use aspect-like mechanisms to separate concerns
- Standards can help, but don't worship them
- DSLs can help

**Emergence (Kent Beck's rules):**
1. Runs all tests
2. No duplication
3. Expresses intent of programmer
4. Minimizes classes and methods

**Concurrency:**
- Separate concurrency code
- Limit scope of data
- Use copies of data
- Threads should be independent
- Know your library
- Know your execution models
- Beware dependencies between synchronized methods

---

## Code Complete (Steve McConnell)

**Construction Prerequisites:**
- Problem definition clear
- Requirements explicit
- Architecture solid
- Major design done upfront

**Metaphors:**
- Software as writing (iterative)
- Software as farming (organic growth)
- Software as building (construction)
- Software as accretion (incremental)
- Pick metaphor that fits project

**Design:**
- Manage complexity (fundamental technical imperative)
- Divide and conquer
- Top-down and bottom-up
- Information hiding
- High cohesion within classes
- Loose coupling between classes
- Design patterns as vocabulary
- Heuristics over algorithms

**Working Classes:**
- Abstract data types
- Good interface
- Good encapsulation
- Inheritance when appropriate
- Composition often better than inheritance
- Single responsibility
- 7±2 elements per interface

**High-Quality Routines:**
- Valid reason for existence
- Strong cohesion
- Loose coupling
- Good name
- Parameters in sensible order
- 7±2 parameters max
- Defensive programming
- One entry, one exit (mostly)

**Defensive Programming:**
- Protect from invalid inputs
- Assertions for impossible conditions
- Error handling for possible conditions
- Barricade your program (validate at boundaries)
- Debugging aids separate from production constraints

**Pseudocode:**
- Write in programming language independent format
- Write at level of intent
- Iterate before coding
- Document assumptions

**Data:**
- Initialize variables
- Scope as small as possible
- Keep together related data
- Use each variable for one purpose
- Beware magic numbers
- Make relationships explicit
- Watch for off-by-one errors

**Control:**
- Organize code for readability
- Write simple conditionals
- Keep nesting shallow
- Follow normal flow
- Watch for boundary conditions in loops
- Make loop control obvious
- Limit loops to 15-20 lines

**Unusual Control:**
- Don't use goto
- Minimize breaks, continues
- Return from multiple points OK if improves readability
- Use exceptions for exceptional conditions only
- Guard clauses acceptable

**Layout:**
- Make logical structure visible
- Show relationships
- Consistent indentation
- Limit line length
- Group related statements
- Blank lines between groups

**Self-Documenting Code:**
- Good variable names
- Good routine names
- Good class names
- Obvious structure
- Minimal comments needed

**Collaboration:**
- Standards for team
- Pair programming for difficult problems
- Code reviews catch 60%+ of errors
- Inspections more thorough than reviews
- Walkthrough focuses on education

**Testing:**
- Basis testing first
- Data-flow testing
- Boundary analysis critical
- Error guessing
- Bad-data tests
- Good-data tests
- Coverage tools

**Debugging:**
- Defects as opportunities to learn
- Stabilize error
- Locate source
- Fix problem not symptom
- Verify fix
- Look for similar defects
- Understand root cause

**Refactoring:**
- Reasons: duplication, long routine, too-large class, long parameter list, divergent change, shotgun surgery, feature envy, data clumps, primitive obsession, switch statements, parallel inheritance, lazy class, speculative generality, temporary fields, message chains, middle man, inappropriate intimacy, incomplete library class, data class, refused bequest, comments
- Safely: tests first, small steps, one at a time, make list, checkpoint frequently, maintain interface

**Strategies:**
- Incremental development
- Design a little, code a little, test a little
- Daily builds
- Automated testing
- Performance budgets
- Manage complexity above all

---

## Working Effectively with Legacy Code (Michael Feathers)

**Definition:**
- Legacy code is code without tests
- Can't refactor safely without tests
- Need tests to change safely
- Need to change to add tests
- The dilemma
- **[AI-ERA]** AI-generated code becomes legacy code faster than human code. GitClear's projected doubling of code churn means AI code gets replaced within weeks. Feathers' techniques—characterization tests, sprout method, wrap method—become relevant not after years of neglect but after months of AI-assisted development. Teams should learn legacy code techniques early, not as a remedial skill.

**Breaking Dependencies:**
- Adapt parameter
- Break out method object
- Definition completion
- Encapsulate global references
- Expose static method
- Extract and override call
- Extract implementer
- Extract interface
- Introduce instance delegator
- Introduce static setter
- Link substitution
- Parameterize constructor/method
- Pull up feature
- Push down dependency
- Replace function with function pointer
- Replace global reference with getter
- Subclass and override method
- Supersede instance variable
- Template redefinition
- Text redefinition

**Seams:**
- Place where behavior can change without editing
- Object seam (polymorphism)
- Preprocessing seam (C/C++)
- Link seam (compile/link)
- Enable testing by using seams

**Sensing vs Separation:**
- Sensing: need to know values
- Separation: need to isolate code
- Different techniques for each goal

**Algorithm:**
1. Identify change points
2. Find test points
3. Break dependencies
4. Write tests
5. Make changes
6. Refactor

**Strategies:**
- Sprout method (new code in new method, tested)
- Sprout class (new responsibility in new class)
- Wrap method (before/after behavior)
- Wrap class (decorator pattern)
- Start working in tested areas, spread outward

**Big Changes:**
- Sketch refactoring (visualize structure)
- Make changes incrementally
- Preserve signatures
- Lean on compiler
- One step at a time

**Testing:**
- Characterization tests (describe actual behavior)
- Use tests to understand code
- Cover before you change
- Break dependencies minimally

**Classes:**
- Extract responsibilities
- SRP violations common in legacy code
- Reduce size incrementally
- Interface segregation

---

## Domain-Driven Design (Eric Evans)

**Ubiquitous Language:**
- Team shares language
- Model-based language
- Used in code, documentation, conversations
- Evolves with understanding
- Resolves ambiguity
- **[AI-ERA]** Ubiquitous language matters more when you're literally having conversations with an AI about your domain model. If your team calls it an "Order" and the AI generates code calling it a "Purchase," you've got a language drift problem. Define domain terms in your context files (CLAUDE.md, .cursorrules) so the AI uses your language, not its own.

**Building Blocks:**
- Entities (identity-based)
- Value Objects (attribute-based, immutable)
- Services (operations that don't belong to objects)
- Modules (organize related concepts)
- Aggregates (consistency boundary)
- Repositories (storage/retrieval abstraction)
- Factories (complex object creation)

**Bounded Contexts:**
- Explicit boundaries for models
- Different models in different contexts
- Context map shows relationships
- Don't try to unify everything
- **[AI-ERA]** AI agents have a natural tendency to blur bounded context boundaries because they optimize for making code work, not for maintaining conceptual boundaries. When an agent needs data from another context, it will import directly rather than going through an anticorruption layer. Explicit boundary documentation in context files is essential.

**Context Mapping:**
- Shared kernel (shared subset)
- Customer-supplier (upstream/downstream)
- Conformist (downstream conforms)
- Anticorruption layer (translate between contexts)
- Separate ways (no relationship)
- Open host service (protocol for access)
- Published language (documented exchange)

**Strategic Design:**
- Core domain (competitive advantage)
- Generic subdomains (necessary but not special)
- Supporting subdomains (specialized but not core)
- Focus resources on core domain
- Buy/outsource generic subdomains

**Distillation:**
- Core domain identified and explicit
- Cohesive mechanisms separated
- Separate core from supporting
- Abstract core
- Declarative style where possible

**Large-Scale Structure:**
- System metaphor
- Responsibility layers
- Knowledge level
- Pluggable component framework
- Choose structure that fits

**Keeping Model Useful:**
- Breakthrough moments (deeper insight restructures model)
- Continuous refinement
- Model expressed in code
- Hands-on modelers
- Cultivate ubiquitous language

---

## Refactoring (Martin Fowler)

**Principles:**
- Improve design without changing behavior
- Small steps
- Tests after each step
- When to refactor: rule of three, when adding feature, when fixing bug, in code review
- When not: rewrite might be better, near deadline

**Code Smells:**
- Duplicated code
- Long method
- Large class
- Long parameter list
- Divergent change (one class many reasons to change)
- Shotgun surgery (one change affects many classes)
- Feature envy
- Data clumps
- Primitive obsession
- Switch statements (consider polymorphism)
- Parallel inheritance hierarchies
- Lazy class
- Speculative generality
- Temporary field
- Message chains
- Middle man
- Inappropriate intimacy
- Alternative classes with different interfaces
- Incomplete library class
- Data class
- Refused bequest
- Comments (sometimes indicate needed refactoring)

**Catalog of Refactorings:**
(Too many to list fully, but categories:)
- Composing methods
- Moving features between objects
- Organizing data
- Simplifying conditional expressions
- Making method calls simpler
- Dealing with generalization

**Key Techniques:**
- Extract method
- Inline method
- Extract variable
- Inline temp
- Replace temp with query
- Introduce explaining variable
- Split temporary variable
- Remove assignments to parameters
- Replace method with method object
- Substitute algorithm
- Move method
- Move field
- Extract class
- Inline class
- Hide delegate
- Remove middle man
- Introduce foreign method
- Introduce local extension

---

## Other Notable Works & Concepts:

**Design Patterns (Gang of Four):**
- 23 classic patterns
- Creational, structural, behavioral
- Common vocabulary
- Proven solutions
- Don't force patterns - recognize when they fit
- **[AI-ERA]** AI agents reach for design patterns aggressively, often applying them where simpler solutions suffice. "Don't force patterns" becomes critical when your AI agent defaults to Strategy/Factory/Observer for problems that need a function and an if-statement. Over-patterned AI code is a common review finding.

**The Mythical Man-Month (Brooks):**
- Adding people to late project makes it later
- No silver bullet
- Plan to throw one away (you will anyway)
- Second-system effect (over-engineering)
- Conceptual integrity crucial
- "How does a project get to be a year late? One day at a time."

**Structure and Interpretation of Computer Programs (Abelson & Sussman):**
- Building abstractions with procedures
- Building abstractions with data
- Modularity, objects, and state
- Metalinguistic abstraction
- Understanding through implementation

**Growing Object-Oriented Software, Guided by Tests (Freeman & Pryce):**
- Test-first development
- Outside-in development
- Listen to tests (bad tests indicate design problems)
- Object-oriented design emerges from TDD
- Integration tests guide architecture
- Unit tests guide design
- Acceptance tests guide features

**Release It! (Nygard):**
- Design for production
- Stability patterns (timeouts, circuit breaker, bulkheads)
- Capacity patterns
- Fail fast vs fail safe
- Operations-aware design
- Monitor everything

**The Art of Unix Programming (Raymond):**
- Rule of Modularity: Write simple parts connected by clean interfaces
- Rule of Clarity: Clarity is better than cleverness
- Rule of Composition: Design programs to be connected with other programs
- Rule of Separation: Separate policy from mechanism, interfaces from engines
- Rule of Simplicity: Design for simplicity; add complexity only where you must
- Rule of Parsimony: Write a big program only when nothing else will do
- Rule of Transparency: Design for visibility to make inspection and debugging easier
- Rule of Robustness: Robustness is the child of transparency and simplicity
- Rule of Representation: Fold knowledge into data so program logic can be stupid and robust
- Rule of Least Surprise: Do the least surprising thing
- Rule of Silence: When a program has nothing interesting to say, say nothing
- Rule of Repair: Repair what you can, but when you must fail, fail noisily and as soon as possible
- Rule of Economy: Programmer time is expensive; conserve it in preference to machine time
- Rule of Generation: Avoid hand-hacking; write programs to write programs when you can
- Rule of Optimization: Prototype before polishing; get it working before you optimize
- Rule of Diversity: Distrust all claims for one true way
- Rule of Extensibility: Design for the future, because it will be here sooner than you think

**Extreme Programming Explained (Beck):**
- Pair programming
- Test-driven development
- Continuous integration
- Simple design
- Refactoring
- Small releases
- Planning game
- Sustainable pace
- Collective code ownership
- Coding standards
- System metaphor

**Peopleware (DeMarco & Lister):**
- People problems, not technical problems
- Quiet, private workspace
- Flow state crucial
- Furniture police (environment matters)
- Team jelling
- Quality obsession
- Overtime is net negative

**The Clean Coder (Martin):**
- Professionalism defined
- Say no when necessary
- Say yes carefully
- Practice (kata, wasa)
- Know your domain
- Continuous learning
- Estimation honesty
- Time management
- Pressure handling
- Collaboration
- Mentoring

---

## AI-era summary: which principles face the most pressure

The principles most frequently violated in AI-generated code, ranked by frequency and impact:

1. **DRY** (Pragmatic Programmer) — AI duplicates existing code because it lacks full codebase awareness
2. **Deep modules** (Ousterhout) — AI generates shallow abstractions and pass-through layers
3. **Do one thing** (Clean Code) — AI produces multi-responsibility functions
4. **Error handling** (Clean Code, Ousterhout) — AI suppresses errors and removes safety checks
5. **Information hiding** (Ousterhout, Code Complete) — AI leaks implementation details across boundaries
6. **Ubiquitous language** (DDD) — AI introduces its own terminology instead of domain language
7. **Design for change** (all sources) — AI optimizes for "works now" over "works later"
8. **Legacy code velocity** (Feathers) — AI code churns faster, making legacy techniques relevant earlier
9. **Over-patterning** (Gang of Four) — AI applies patterns where simpler solutions suffice
10. **Test quality** (Pragmatic Programmer, Clean Code) — AI generates tests that look thorough but verify nothing

These are the areas where human review of AI-generated code provides the most value. See TESTING.md for testing-specific countermeasures and AI_CODING.md for the empirical evidence behind these patterns.