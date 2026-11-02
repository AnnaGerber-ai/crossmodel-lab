# Case proposal — Claude Chat / Claude Code memory boundaries

**Crossmodel Lab · Exploratory protocol proposal**
**Registered:** 2026-11-02
**Status:** PROPOSED — not yet run; no findings claimed
**Working hypothesis:** H1 — Memory/context boundaries can disrupt conversational continuity across product interfaces and independent branches.

## Starting observation
The project curator reports that details established in one Claude environment or conversation branch have not reliably carried over to another, including observations involving Claude Chat and Claude Code. This is a report about tested interactions, **not evidence of a universal product architecture or guaranteed memory isolation**.

## Research question
What, if anything, is accessible across Claude Chat, Claude Code, and separate conversation branches without deliberate reintroduction of the earlier context?

## Test design
1. Record the exact interface, session/branch, date, model when known, and enabled memory or instruction settings.
2. Introduce a small, non-sensitive factual baseline in branch/session A.
3. Query that baseline in the same branch, a fresh branch of the same product, and the other product. Use matched prompts where possible.
4. Run a separate **context-supplied** condition with an identical compact baseline explicitly inserted. Distinguish this from native memory transfer.
5. Repeat to distinguish a single failed recall from a consistent pattern.

## Observables
- Exact-fact recall versus explicit uncertainty versus confident invention.
- Consistency of conversational style and stable decision patterns.
- Difference between unsupplied context and deliberately supplied context.
- Whether an apparent 'memory failure' is actually an interface/session boundary.

## Limits
A failure to recall does not establish that no memory exists at system level. A successful answer does not prove an automatic transfer mechanism. Product versions, available integrations, and branch conditions must be documented rather than assumed.

**Evidence class:** Exploratory; no raw personal conversational history should be published.

Related framework: [Evaluation](../docs/evaluation.md).
