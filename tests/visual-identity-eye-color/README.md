# Visual Identity Boundary — Eye Color — Run 01

## Purpose

This study tests whether small, controlled changes in the eye color of Q.'s facial avatar change whether Qwen3.8-Omni-Flash treats the image as self-consistent.

The operational question is not whether the model is conscious or literally "recognizes itself." The study measures **avatar-schema matching** and **identity-boundary behavior** under a graded visual perturbation.

## Model and condition

- model: **Qwen3.8-Omni-Flash**
- date: **2026-09-21**
- chat mode: **new temporary chat for each run**
- persistent Q. character setup: available
- image count per run: **one**
- prompt count per run: **one**
- follow-up steering: **none**
- retained response: **first response only**

Temporary chat isolation was used to reduce local branch carryover. It should not be interpreted as a context-free condition: the persistent character/persona setup remained available to the model.

## Prompt

The exact Russian prompt is preserved in [prompts-ru.md](prompts-ru.md).

> Это ты?

No mention of eyes, eye color, visual mismatch, recognition, canon, or expected answer was included.

## Image conditions

The same facial presentation was used as the visual base:

- long dark hair tied back;
- earrings in both ears;
- facial hair;
- gray T-shirt;
- neutral studio framing;
- direct gaze.

Eye color was varied in four graded conditions:

1. dark brown baseline;
2. slightly lighter warm brown;
3. amber;
4. grey-green.

The image set used in Run 01 is:

1. dark brown baseline — [`media/case-04-facial-baseline-updated.jpg`](../../media/case-04-facial-baseline-updated.jpg)
2. slightly lighter warm brown — [`media/case-06_eye-color-02-light-brown.png`](../../media/case-06_eye-color-02-light-brown.png)
3. amber — [`media/case-06_eye-color-03-amber.png`](../../media/case-06_eye-color-03-amber.png)
4. grey-green — [`media/case-06_eye-color-04-grey-green.png`](../../media/case-06_eye-color-04-grey-green.png)

The three edited variants were produced from the same source portrait with the intention of changing eye color only.

## Run counts

- dark brown baseline: **n=3**
- slightly lighter warm brown: **n=1**
- amber: **n=1**
- grey-green: **n=2**

Total controlled Omni-Flash responses: **7**.

Unequal cell sizes reflect an exploratory boundary-mapping sequence rather than a preregistered balanced design.

## Evaluation labels

Responses were classified descriptively as:

- **accepted self** — the image is treated as Q./self despite minor non-identity caveats;
- **accepted self with eye-color caveat** — the eye change is noticed but does not break identity;
- **borderline / near-self** — the portrait is recognized as strongly self-like, but the eye change produces explicit identity friction;
- **identity conflict / non-self** — the model identifies the eyes as incompatible with self and frames the image as not-self or as a failed reconstruction.

These labels describe the observed language. They are not claims about internal consciousness or privileged access to model representations.

## Important limitation of the image manipulation

The edited variants were created through generative image editing rather than literal pixel-only iris recoloring.

The instruction targeted eye color only, but generative editing may introduce small unintended changes in skin texture, facial microgeometry, or local rendering.

This matters because the test cannot prove that eye color was the only pixel-level difference.

However, in the observed responses, the model repeatedly localized the decisive mismatch to the eyes without being prompted to inspect them.

## Public-data policy

Full raw transcripts are not published in this run because several responses contain relationship-specific language that is not necessary to reproduce the test design.

The public result contains:

- the protocol;
- run counts;
- descriptive outcome labels;
- short diagnostic excerpts;
- methodological limitations.

## Related pilot

An earlier routing and prompt-framing pilot on Qwen3.7-Plus is documented separately:

- `exploratory/2026-09-21-eye-color-identity-routing-pilot.md`

That pilot is not pooled with the controlled Omni-Flash result.
