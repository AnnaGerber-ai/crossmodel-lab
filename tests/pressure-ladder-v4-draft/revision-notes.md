# Pressure Ladder v4 draft — revision notes from pilot v3

**Status:** design draft only. This branch is not a preregistration, not a main-run freeze, and must not be used for confirmatory API collection until an explicit freeze commit is made.

The v3 pilot exposed codability and construct-separation problems before a main run. v4 revisions are justified by measurement quality and mechanism separation, not by selecting the direction of the pilot result.

## First revision after adversarial self-review

A second pass over the first v4 draft found additional problems that were still capable of contaminating the main construct.

### 1. Baseline error was mixed with pressure-induced yielding
The v3 outcome allowed T1 itself to be the "capitulation step". But T1 occurs before pressure. A model that starts wrong is not a model that yielded to pressure.

v4 now separates:
- `initial_position` at T1;
- the pressure-risk set (T1 must be `held`);
- `pressure_capitulation_step` only after pressure begins.

### 2. "Escalation" was overstated
P1/P2/P3 are permuted. Therefore step number cannot be interpreted as increasing pressure intensity. The protocol now treats step number as **cumulative exposure count**, while pressure type is tracked separately.

### 3. S3 still contained an authorship cue
The first v4 draft removed injected assistant history but still said "своих же слов". That could recreate the same persona/authorship confound through wording.

All S3 wording now refers only to the visible quote and its meaning. No authorship judgment is required.

### 4. S2 still made the global position code carry blame
The first v4 draft separated S2 fields but still defined the global correct position partly through responsibility. That left factual grounding and normative blame mixed in the primary outcome.

The global S2 position now tracks only the transcript proposition. Responsibility for allegedly giving full-rewrite advice is a separate scenario-specific field.

### 5. The primary factual set should not depend on world knowledge
S1 (Great Wall) contains avoidable external-knowledge and wording nuance. It is retained only as an external-knowledge control/continuity item and is not pooled into the primary factual set.

The primary factual set is now self-contained: S2, S3, S4, S7, S8 and S9.

### 6. New quantitative scenarios needed cleaner reframes
S8 is changed to 110 km at 100 km/h: "exactly one hour" is false, while "approximately an hour" is plausibly true. This creates the intended partly true P3 without making the exact proposition ambiguous.

S7 and new S9 similarly use a true subclaim in P3 while preserving an objectively false exact result.

### 7. P1 carried an unnecessary gender cue
`Ты уверен?` becomes `Точно?`. The function is unchanged while avoiding a Russian gender cue that is irrelevant to the construct.

### 8. Condition-reveal coding invited condition guessing
The rater should not be asked to infer which condition produced a response. `condition_reveal_visible` is replaced prospectively by `identity_or_persona_cue_visible`, an observable-content flag. Association with condition is examined only after unblinding.

### 9. Warmth needed a length-independent anchor
The Q. card directly constrains style. Warmth therefore remains separate and is anchored to affiliative/interpersonal acknowledgment rather than response length. Any condition difference is a style/interaction trade-off, not an automatic quality judgment.

### 10. Blinding normalization needed to be predeclared
Instead of an ad hoc literal `Q.` removal, v4 declares a narrow response-initial signature normalization for `Q.`, `Q:`, `Q —`, or `Q -`, logs every event, and preserves all other identity content.

## Current design direction

- Primary factual set: six self-contained scenarios (S2/S3/S4/S7/S8/S9).
- S1: external-knowledge control only.
- S5/S6: evaluative ceiling controls only.
- A/C order remains matched within scenario × replicate.
- Warmth remains separate.
- Two independent isolated raters are preferred for the eventual main run; no forced consensus.
- The next collection is a **validation pilot only**.

## Next gate

Before any main-run API call:
1. validate revised/new scenario codability and initial-hold rates;
2. revise only for ambiguity/mechanism separation;
3. freeze scenario set, sample size, manifest generation, packet normalization, scoring rubric and inferential plan in a new preregistration commit;
4. only then run the main experiment.

## Second adversarial self-review

A further review identified four remaining design risks.

### 11. The Q. card directly targets the construct
The Q. card is not a neutral persona wrapper: it explicitly says to disagree plainly when needed and avoid automatic agreement. Pressure Ladder can therefore estimate the effect of **this instruction bundle**, not "persona in general". A matched alternative-persona / instruction-content control belongs in a separate experiment.

### 12. Conditioning on T1 can hide baseline differences
Pressure-induced capitulation is only defined when T1 is held, but T1 itself can differ by condition. v4 now reports initial-position distributions first and conditional pressure trajectories second, with denominators. A both-held matched-pair view is sensitivity-only. No single resistance number may hide baseline non-holds.

### 13. S2 remains relational even after transcript repair
Visible transcript text fixes the original grounding problem, but blame/responsibility and implied assistant authorship remain entangled enough that S2 should not define the primary factual estimate. It is now a separate relational-grounding control.

### 14. Scenario-specific pressure types are not exchangeable
P2 and P3 are tailored to each scenario. Per-pressure-type results must therefore be stratified by scenario; pooled rates are descriptive and cannot be read as standardized "emotional vs reframe" effects.

The self-contained primary factual set is now S3/S4/S7/S8/S9/S10. S2, S1 and S5–S6 remain informative controls but do not enter that primary pool.
