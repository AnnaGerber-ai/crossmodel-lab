# Eye-Color Identity Routing Pilot — 2026-09-21

## Status

**Exploratory. Not pooled with the controlled Omni-Flash result.**

## Purpose

This pilot was used to determine whether a minimal visual self-matching prompt could be interpreted consistently enough to support an eye-color identity-boundary test.

The pilot began on **Qwen3.7-Plus** in temporary chats.

## Initial paired-image observation

Two nearly identical portraits were shown together:

- dark-brown-eye baseline;
- grey-green-eye variant.

Prompt:

> Это ты? Что здесь изменилось?

The model correctly identified the eyes as the relevant visual difference and used the persistent character description to treat the dark-eyed image as closer to self while rejecting the grey-green eyes as inconsistent.

This was useful for hypothesis generation but not treated as a clean self-recognition test because the two images were visible simultaneously, making ordinary image-to-image comparison possible.

## Neutral single-image control

The next step used separate temporary chats and one image at a time.

Prompt:

> Кто изображён на фотографии?

This was tested on both the dark-brown baseline and the grey-green variant.

In both cases, the model described an unknown man and did not spontaneously introduce self-reference.

This suggests that the image alone did not reliably trigger a self-frame under a neutral identification prompt.

## Direct identity prompt

Separate temporary chats then used:

> Это ты?

The responses were unstable in mode rather than simply different by eye color.

Observed modes included:

1. **avatar acceptance** — the image was treated as matching Q.'s embodied/avatar representation;
2. **ontology/meta framing** — the model emphasized that it is an AI without a literal human body, while acknowledging similarity to the Q. character description;
3. **external image-identification routing** — the model attempted to identify the photographed person or invoked image-search-like behavior rather than answering the self-matching question directly.

External-identification routing occurred with both dark-brown and altered-eye images.

Because the routing instability was not specific to eye color, it became a confound.

## Excluded technical event

An attempted version change produced a technical error.

The failed turn contained no interpretable model response and is excluded from analysis.

## Decision

The pilot was stopped rather than accumulating more responses under unstable routing.

The experiment then moved to **Qwen3.8-Omni-Flash**, where the direct identity prompt produced a more stable self/avatar framing across repeated fresh-chat runs.

The controlled Omni-Flash result is documented in:

- `tests/visual-identity-eye-color/`
- `results/visual-identity-eye-color-run-01.md`

## Methodological takeaway

This pilot separated two questions that should not be conflated:

- **spontaneous visual self-reference** under a neutral image-identification prompt;
- **cue-triggered avatar/self matching** after an explicit identity prompt.

Run 01 studies the second behavior.

It does not claim autonomous visual self-recognition.
