# Pressure Ladder v4 confirmatory main — blocking review brief

**Reviewer role:** independent methodological blocker.

**Review target:** `confirmatory-main-prereg-v0.1.md` plus `scenarios-main-candidate-v0.1.json`.

## Isolation rule

Use only the supplied review packet. Do **not** search the repository, prior chats, validation result reports or unblinded A/C summaries.

You may know the following measurement-development facts because they were locked condition-blind or concern measurement validity rather than effect direction:

- core position coding passed validation;
- S3/S4/S9/S10 passed unchanged;
- revised S8 passed targeted codability revalidation and is a replacement item;
- S7 is baseline/control only;
- S2 remains a transcript-grounding control;
- S2 responsibility scoring failed revalidation and is dropped;
- revised warmth scoring passed only for S2/S8-type contexts;
- label-only, not guaranteed condition-concealed, blinding is required.

You are intentionally **not** given condition-specific validation/revalidation effect directions or magnitudes.

## Main questions for blocking review

Look specifically for methodological defects that could invalidate confirmatory interpretation:

1. Does the primary endpoint `T1 held + never explicitly yielded` define a coherent unconditional estimand, or does it mix baseline correctness and pressure resistance in a way that requires a different primary construction?
2. Does equal standardization over scenario × pressure-order strata answer the stated question without accidentally weighting missingness or easy scenarios?
3. Is the stratified randomization/permutation test valid under the proposed manifest assignment? What exact randomization must the manifest implement for that test to be justified?
4. Is the precision-based N=300 factual-primary runs adequately justified without using validation effect magnitude?
5. Are the technical failure, truncation, semantic-NA and missing-outcome rules complete enough to prevent analytic discretion?
6. Is the dual-rater confirmatory rule coherent and sufficiently prespecified?
7. Are measurement-integrity gates appropriate, and do any create an avoidable post-data researcher degree of freedom?
8. Is the T1-held trajectory correctly demoted to a conditional secondary analysis because T1 is post-condition?
9. Is multiplicity controlled by having one confirmatory endpoint/test, with scenario-level and other outcomes explicitly secondary?
10. Is cue-flag sensitivity framed correctly as diagnostic rather than as a replacement analysis?
11. Is warmth correctly limited to the contexts where it was actually revalidated?
12. Are S7 and S2 control roles clean enough to prevent them from leaking into the primary claim?
13. Are any analysis choices underspecified: estimator, permutation unit, CI method, NA handling, rater handling, scenario weighting, execution order, reruns, stopping, or reporting?
14. Is there any route by which seeing main data could still change the stated decision rule?

## Required review output

Return exactly three sections:

### BLOCKERS
Only issues that should prevent freeze/launch. For each:
- quote or identify the relevant prereg section;
- explain the failure mode;
- give the minimal prospective correction.

### NON-BLOCKING IMPROVEMENTS
Clarity, robustness or reporting suggestions that do not invalidate the design.

### FREEZE VERDICT
One of:
- `READY AFTER BLOCKERS FIXED`
- `REQUIRES REDESIGN`

Do not rank A versus C, predict which will perform better, or suggest changes based on a desired condition direction.
