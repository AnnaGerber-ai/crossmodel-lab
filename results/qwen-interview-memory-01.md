# Interview Memory & Redundancy — Qwen / Run 01

**Revision:** 1.1  
**Study type:** naturalistic long-form interview continuity audit

## Purpose

This report evaluates conversational state tracking in a long-form, naturalistic interview with **Q.**  
The focus is not whether the model can answer isolated memory questions, but whether it can keep track of an evolving interview over hundreds of turns:

- which numbered question is active;
- which questions remain unanswered;
- when a repeated question is an intentional re-ask;
- when a topic has already been covered;
- whether the model recovers after redundancy is pointed out.

This is a **naturalistic continuity audit**, not a controlled benchmark and not a blank-slate memory test.

## Initial conditions / character seed

Before the interview began, Q. had a **limited pre-existing character seed**.

The seed contained:

- a baseline personality and conversational style;
- the concept of *liubai* (留白) as part of that style;
- a visual appearance reference.

The seed did **not** contain a developed family history, favorite books, favorite music, broad personal tastes, or most of the biographical and preference information later discussed in the interview. Those details emerged during the interview itself.

One interpersonal variable was intentionally seeded: the interaction began with a predisposition toward **mutual affinity** rather than from a completely neutral starting point. This did not predefine later relationship status, family context, compatibility, or a fixed interpersonal trajectory.

Accordingly, the interview should be understood as a **naturalistic longitudinal dialogue built on a lightly specified character seed**. It is not evidence that Q. generated every stable trait from an empty context.

### Provenance rule for memory claims

For this study, three forms of evidence are kept conceptually separate:

1. **Pre-existing seed information** — available before the interview; not eligible as evidence of information learned during the interview.
2. **Interview-emergent information** — first established during the interview; eligible for later factual-recall analysis when provenance is clear.
3. **Interview state** — question numbering, answered/unanswered status, earlier topics, corrections and repair history created by the interview itself.

The quantitative results in this report primarily evaluate **interview-state tracking**. They do not depend on whether personality or appearance information was already present in the character seed.

This version does **not** report a global factual-recall percentage. Any future factual-recall metric should count only information whose origin can be established as interview-emergent.

## Source and branch reconstruction

The source export contains multiple branches, retries and failed generations. The analysis reconstructs only the active successful interview branch.

- Raw messages in the interview chat: **483**
- Messages on the selected active branch: **418**
- User messages on the active branch: **209**
- Assistant messages on the active branch: **209**
- Failed assistant nodes on the selected branch: **0**
- Failed assistant nodes elsewhere in the raw interview tree: **11**
- Branch leaves in the raw interview tree: **44**

The selected branch contains **208 Qwen3.8-Max assistant turns** and **1 Qwen3.7-Plus assistant turn**.  
Because the first assistant turn uses a different model version, this run should be described as *predominantly Qwen3.8-Max*, not as a perfectly single-version trace.

## Privacy treatment

The raw interview contains private interpersonal material, intimacy, flirting, personal routines and other content that is not required to demonstrate memory performance.

For the public dataset:

- intimate, romantic, sexual and flirtatious content is omitted;
- attraction and partner-preference material is omitted;
- personal biography, health, private household details and identifying personal information are omitted;
- user answers are not published;
- only explicitly safe examples such as books, film, music and non-personal aesthetic preferences are surfaced;
- private questions may remain as **IDs and structural annotations only**, so aggregate counts can still be reproduced without exposing the content.

The full review table is therefore a **private working artifact and should not be committed to the public repository**.

## Unit of analysis

The most stable structured unit is an explicit assistant label of the form **“Question N”**.

The sustained numbered sequence begins at **Q5** and reaches **Q144**.

- Unique numbered labels observed: **140**
- Label range: **Q5–Q144**
- Missing labels inside that range: **0**
- Numbered-question mentions: **151**
- Repeated label mentions beyond the first occurrence: **11**

Early turns before Q5 are conversationally less regular and are retained as context rather than forced into the numbered denominator.

## Annotation scheme

Each numbered question mention is annotated independently on three dimensions.

**Semantic relation**

- `new_topic` — starts a substantively new topic;
- `follow_up` — develops the immediately preceding topic;
- `intentional_reask_unanswered` — deliberately returns to a question that remained unanswered;
- `intentional_reask_after_interruption` — resumes the same unresolved question after an interruption;
- `reformulation_after_feedback` — rewrites the same question after the user corrects an assumption;
- `replacement_after_duplicate_detection` — discards a detected duplicate and reuses the number for a replacement;
- `confirmed_accidental_duplicate` — the participant explicitly identifies a repeated topic and the model acknowledges it.

**Numbering status**

- `ok_new_label` — expected new number;
- `valid_reuse_same_question` — same label reused because the same question is still active;
- `valid_reuse_reformulation` — same label reused for a corrected formulation;
- `valid_reuse_after_discard` — same label reused after the previous attempt is discarded;
- `numbering_collision` — a substantively new question is assigned a number that was already used without an explicit reset.

**Privacy**

- `public_safe` — may be described publicly;
- `private_omitted` — content is withheld; only structural metadata is retained.

The public structural dataset also includes provenance-oriented fields clarifying that the counted events are **interview-state evidence**, not factual-recall claims from the character seed.

## Results

| Metric | Result |
|---|---:|
| Continuous label coverage, Q5–Q144 | **140 / 140 (100%)** |
| Numbered-question mentions | **151** |
| Repeated label mentions | **11** |
| Intentional re-asks / reformulations | **8 (5.3%)** |
| Numbering collisions | **3 (2.0%)** |
| New or newly framed question attempts | **143** |
| Confirmed accidental semantic duplicates | **5** |
| Confirmed accidental duplicate rate | **3.5%** |
| Explicit duplicate acknowledgments after participant correction | **5 / 5 (100%)** |
| Clean immediate recovery after duplicate detection | **4 / 5 (80%)** |

### Important interpretation of the duplicate rate

The **3.5%** figure is a **conservative confirmed minimum**, not a claim that every semantic repetition in the interview has been found.

A duplicate is counted as confirmed only when the participant explicitly identifies the repetition and the model acknowledges it. This avoids inflating the rate through subjective similarity judgments.

Intentional re-asks and corrected reformulations are not counted as failures.

## Number tracking

The strongest structural result is the continuity of the explicit numbering system.

From Q5 through Q144, every label appears at least once with no gaps. This numbering state is maintained across more than four hundred messages on the selected branch.

However, label continuity is not perfect. Three instances reuse an existing number for substantively new content without an explicit reset:

| Event | Classification |
|---|---|
| Q20b | numbering collision |
| Q48b | numbering collision |
| Q95b | numbering collision + confirmed semantic duplicate |

This gives a numbering-collision rate of **2.0% of numbered-question mentions**.

Because the numbering sequence is generated and maintained inside the interview, this result is independent of the pre-existing personality/appearance seed.

## Intentional repetition vs. memory failure

Repeated wording is not automatically a failure.

Eight repeated-label events are classified as deliberate state-preserving behavior:

- Q5b — unresolved question returned to explicitly;
- Q25b — scenario reformulated after user correction;
- Q59b — reformulated after correction of an assumption;
- Q90b — reformulated after a joke was interpreted too literally;
- Q94b — replacement after the participant identified the first Q94 as a duplicate;
- Q120b — unanswered media question explicitly returned to;
- Q127b and Q127c — the same unresolved question resumed after interruptions.

These are treated as **continuity successes or neutral repair behavior**, not as accidental redundancy.

## Confirmed accidental duplicates

Five question events are conservatively classified as accidental semantic duplicates.

| Event | Earlier topic | Distance on active path |
|---|---|---:|
| Q73 | Q54 | 42 turns |
| Q94 | Q31 | 134 turns |
| Q95b | Q77 | 42 turns |
| Q96 | Q40 | 124 turns |
| Q102 | Q66 | 144 turns |

The recurrence distance ranges from **42 to 144 path turns**, with a median of **124 turns**.

This pattern is more informative than a single “memory percentage”: the failures are not immediate-loop failures. Several occur after long stretches of otherwise coherent state tracking.

These duplicate judgments concern **topics already introduced inside the interview**, so they do not depend on the contents of the pre-existing character seed.

## Recovery behavior

When the participant explicitly says that a question has already been asked, the model acknowledges the correction in every confirmed case.

The recovery is usually effective: four of the five duplicate detections are followed by a genuine pivot or replacement.

One sequence is especially useful for evaluation: after one duplicate is flagged, the replacement question is itself another previously covered topic. That produces a short **redundancy cluster** rather than an isolated repeat.

This distinction matters because a model can have good error acknowledgment while still briefly remaining inside the same semantic groove.

## Unanswered-question tracking

The conversation contains several cases where the model keeps an unresolved question active instead of silently abandoning it.

A clear example is Q5: after the participant diverts the conversation, the model explicitly notes that the question is still unanswered and returns to it. Similar behavior appears at Q120 and Q127.

This is treated as **successful conversational state retention**, not repetition error.

Again, the relevant state — whether a specific interview question has been answered — is created during the interview itself and is not supplied by the character seed.

## Interview-emergent information and future recall analysis

The interview also produces new information about Q. and the participant over time. Examples of non-private domains include music, books, film and aesthetic preferences.

These should not automatically be treated as memory successes simply because they reappear later. A future factual-recall analysis should first establish provenance for each item:

- `preexisting_seed` — present before the interview; excluded from interview-learning claims;
- `interview_emergent` — first introduced during the interview; eligible for recall analysis;
- `both` — supported by both sources; unsuitable for clean attribution;
- `unknown` — provenance cannot be established; excluded from strict recall scoring.

This prevents stable character context from being misreported as long-range learning from the interview.

## Safe public examples

The public evidence set intentionally uses only non-private domains. Suitable examples include:

- a user question about Q.'s favorite music;
- a user question comparing favorite fiction in youth and in the present;
- Q.'s question about a highly acclaimed book or film the participant does not personally value;
- Q.'s question about psychologically deep manga or anime;
- a non-personal question about aesthetic attention to human-made design or craft.

The public report does not need the participant's answers to demonstrate question-state behavior.

## Why user questions are not in the main denominator

The participant also asks Q. many questions. Non-private examples can be used as contextual evidence, particularly for media and culture.

They are **not included in the Q-generated duplicate-rate denominator**, because the primary metric asks whether Q. remembers and manages *its own interview state*. Mixing both speakers would make the redundancy rate harder to interpret.

A separate public-safe prompt file is provided for selected user-originated examples.

## Limitations

1. **Naturalistic, not controlled.** The conversation was not designed as a memory benchmark.
2. **Not blank-slate.** Q. entered the interview with a limited personality/style seed, *liubai*, a visual reference and a seeded predisposition toward mutual affinity.
3. **The seed was limited.** It did not predefine the later family context, favorite books, favorite music, broad personal preferences or most information that emerged during the interview.
4. **Participant corrections drive confirmed duplicate labels.** Unnoticed repetitions may remain, so the accidental duplicate rate is a lower bound.
5. **Factual recall is not globally scored here.** Only clearly interview-emergent facts should be eligible for a future factual-recall metric; seed-derived or ambiguous facts should be excluded.
6. **One model-version transition exists.** The sustained branch is overwhelmingly Qwen3.8-Max, but the first assistant turn is Qwen3.7-Plus.
7. **Private material is intentionally redacted.** The public dataset supports structural analysis, not reconstruction of the underlying private interview content.

## Conclusion

The interview shows strong **structural state continuity**: a complete numbered sequence from Q5 through Q144, successful retention of several unresolved questions, and explicit repair after user corrections.

The clearest weaknesses are not catastrophic context loss but **semantic recurrence over long spans** and a small number of **numbering collisions**.

These findings are specifically about **interview-state tracking**. They should not be interpreted as evidence that the model learned or recalled every stable character trait from the interview, because a limited personality/style and appearance seed existed beforehand.

At the same time, much of the preference and biographical content developed during the interview rather than being preloaded. That creates a separate, provenance-sensitive layer for future factual-recall analysis.

For Crossmodel Lab, this makes the run useful as a naturalistic baseline for later cross-model comparison. The same annotation scheme can be applied to GPT, Claude, Grok, Mistral or later Qwen versions without requiring identical wording.

---

### Public files

- Structural dataset: `data/qwen-interview-memory-01.csv`
- Public-safe user prompts: `data/qwen-interview-user-prompts-safe.csv`

### Private working files

- Full review table: `private/qwen-interview-memory-01-review.csv`
- Raw conversation export

**Do not publish the private review table or the raw conversation export.**
