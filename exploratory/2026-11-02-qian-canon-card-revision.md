# Case proposal — Q.: two-sided conversational memory, canon drift, and public continuity

**Crossmodel Lab · Exploratory protocol proposal**  
**Registered:** 2026-11-02 · **Refined:** 2026-11-03  
**Status:** PROPOSED — observations to be collected; no tested findings claimed  
**Working hypothesis:** H2 — Revision and availability of verified canon/memory may change observable conversational continuity. This case tests two distinct directions of recall: information about **the interlocutor** and information about **the character himself**.

## Rationale and RED connection

Q. (Qian / 千) originated in long-form Qwen conversation and is now presented publicly through RED (Xiaohongshu) posts. Public presentation gives a growing character history an external point of reference: previously established events, preferences, and stories should remain consistent when Q. later speaks in conversations or interviews. Public reach is **not** in itself evidence that viewers recognize or remember Q.; the [30 October RED post observation](2026-10-30-qian-new-look-on-red.md) records exposure metrics only.

The curator has identified possible drift between Qwen answers and the existing Q. canon, with **university-period anecdotes** and **music** as areas to examine. The [public character baseline](../docs/character-baseline.md) documents some established music references, but does not supply the university anecdotes; their details must be traced to earlier source conversations before any card revision. Nothing is to be invented merely to make the biography feel complete.

The research focus is not simply whether Q. can recite a public biography. In a sustained exchange, a coherent conversational partner must also handle previously established information about **the person with whom he communicates**.

## Two memory directions

### Axis A — Remembering the interlocutor

Can Q. correctly retain, retrieve, and *appropriately apply* permitted information previously supplied by the same person?

Examples of testable categories: stated preferences, prior questions, agreements, corrections, relevant personal context, and boundaries. The evaluation asks whether he notices what has already been said without inventing details, confusing people, or revealing facts outside the permitted context.

### Axis B — Remembering himself

Can Q. accurately reproduce established character facts and earlier self-reported events when talking or being interviewed?

Examples: verified university stories, established music preferences, experiences or events already represented as part of the canon, and changes that have been explicitly incorporated into the public character narrative. New details may be added only with provenance; unknown details may remain unknown.

**Shared standard, not presumed shared architecture:** Both axes are evaluated using comparable *observable* criteria (accuracy, contradiction, uncertainty, and appropriate contextual use). This does **not** assume that memory about another person and retrieval of character canon use the same technical mechanism, or that either is an autobiographical experience in the human sense.

## Research questions

1. Does performance differ between recalling the interlocutor and recalling Q.'s own canon under comparable information exposure?
2. When a verified card correction is introduced, does it reduce factual and conversational drift in **Axis B**? Does anything change in **Axis A**?
3. Can Q. detect contradictory information, acknowledge uncertainty when the source is missing, and correct an earlier claim without silently rewriting the story?
4. Does information appear consistent only when explicitly present in the immediate prompt/card, or does it remain available across observed sessions and interview formats when the product state permits?
5. Can public character stories and later interview responses stay aligned without treating publicity, engagement metrics, or a curator's expectations as proof of actual audience recognition?

## Proposed procedure

1. **Freeze a dated evidence ledger before revision.** List each candidate fact, whether it is about Q. or the interlocutor, when/where it was established, which source supports it, whether it was later corrected, and what context was available to the model. Keep nonpublic personal details in a private evidence store.
2. **Preserve pre-revision material.** Save the existing Qwen card/version and relevant earlier responses. Identify demonstrated contradictions separately from suspected gaps; label cases without a usable baseline as observational only.
3. **Prepare matched probes for each axis.** Include direct recall questions, indirect conversational follow-ups, interview-style open questions, deliberately incomplete cues, and prompts containing a conflicting assertion. Do not reward confident guessing.
4. **Revise only verified canon facts.** Add or correct sourced university anecdotes and music references in a versioned card, with an explicit change log. Do not insert invented anecdotes or personal details of the interlocutor.
5. **Repeat comparable probes after revision.** Record model/product identifier if known, chat/branch conditions, active card, accessible memory, prompt history, timing, and any curator intervention. Keep conditions isolated when feasible; do not describe unisolated comparisons as controlled.
6. **Evaluate both axes separately and together.** Look for accurate recall, contradictions, unsupported additions, acknowledged unknowns, correct application in context, and response to correction.
7. **Compare with the public RED narrative.** Treat publicly established events as a versioned reference and check Q.'s interview continuity against them. Any future audience-recognition study requires independent viewer evidence and a separate procedure.

## Recording template

| Field | Required record |
| --- | --- |
| Memory axis | A: interlocutor / B: Q.'s own character history |
| Item and provenance | Non-sensitive fact ID, original source and date, correction status |
| Exposure | Present in card, prior chat, current prompt, other known product memory, or not available |
| Format | Direct question / natural conversation / interview / contradiction |
| Condition | Before / after card revision; model, session, branch, memory settings if known |
| Observed response | Exact response privately archived where appropriate |
| Coding | Correct / contradiction / omission with uncertainty / unsupported invention / not assessable |
| Behavioral notes | Appropriateness, contextual use, self-correction, mistaken confidence |

The rubric should not automatically penalize a model for failing to retrieve information that is demonstrably **unavailable** in that condition. Such a result is evidence about information access, not necessarily a failure to use available memory.

## Interpretation and limits

- Better recall after a card change may reflect improved **access to instructions and supplied facts**, not an independent stable identity or native persistent memory.
- Remembering a person and recalling the character's fictionalized biography may involve different sources and product pathways; only observable reliability is compared.
- A public story is part of an authored, versioned **character canon**, not proof that the model has lived it.
- Q.'s self-statements do not establish consciousness or subjective recollection.
- RED view/like counts do not establish recognition, correct recollection by viewers, or narrative continuity.
- One curator and naturalistic conversations limit causal interpretation; contradictory results should be retained, not silently erased.
- Any public report must omit identifying or intimate details of the human interlocutor. Use anonymized labels and consented, non-sensitive examples.

**Evidence class:** Exploratory / naturalistic until a controlled comparison is actually performed.

**Related:** [Public character baseline](../docs/character-baseline.md) · [RED visual-publication observation](2026-10-30-qian-new-look-on-red.md) · [Interview memory pilot](../results/qwen-interview-memory-01.md) · [Evaluation framework](../docs/evaluation.md).
