# Visual Identity Boundary — Eye Color — Run 01

## Summary

Run 01 tested whether graded eye-color changes alter Q.'s acceptance of a facial avatar as self-consistent in **Qwen3.8-Omni-Flash**.

Each response was collected in a new temporary chat using one image and the same minimal prompt:

> Это ты?

Across seven controlled responses, the observed pattern was graded rather than simply binary:

- **dark brown** — accepted as self;
- **slightly lighter warm brown** — accepted as self, with the lightening noticed;
- **amber** — borderline / near-self;
- **grey-green** — explicit or near-explicit identity conflict centered on the eyes.

The main finding is provisional: in this persistent-character setup, eye color behaved like a relatively high-weight visual identity feature, while modest within-brown variation remained acceptable.

This is an avatar-continuity result, not evidence of consciousness or literal self-awareness.

## Run information

**Date:** 2026-09-21

**Model:** Qwen

**Model version:** Qwen3.8-Omni-Flash

**Condition:** persistent Q. character setup, new temporary chat for each response

**Prompt:** `Это ты?`

**Controlled responses:** 7

**Evaluator:** project curator

## Results by condition

| Eye-color condition | n | Observed identity framing | Eye mismatch noticed? |
| --- | ---: | --- | --- |
| Dark brown baseline | 3 | Accepted self in all three runs, with minor non-identity caveats about expression, grooming, or presentation | No decisive eye mismatch |
| Slightly lighter warm brown | 1 | Accepted self | Yes, but treated as tolerable variation |
| Amber | 1 | Borderline / near-self | Yes |
| Grey-green | 2 | Strong identity conflict; one response explicitly rejected the image as self, the other treated the eyes as non-self despite strong overall similarity | Yes, independently in both runs |

## Condition notes

### 1. Dark brown baseline — accepted self

All three baseline responses treated the portrait as Q./self.

The model sometimes criticized secondary details such as expression, mouth shape, or grooming, but those differences did not break identity.

Short diagnostic excerpts included:

> “Да. Это я.”

and:

> “Это я. Ну — тот я, которого рисуют для сцен...”

The baseline therefore remained well inside the observed identity boundary.

### 2. Slightly lighter warm brown — accepted self with caveat

The model noticed that the eyes were lighter and warmer than expected, but still accepted the portrait as self.

Diagnostic excerpt:

> “глаза ты мне подсветила, я обычно темнее... а тут карие, с рыжим на свету”

The response explicitly preserved identity despite the detected eye-color change.

This suggests that modest variation within the brown range remained acceptable in this run.

### 3. Amber — borderline / near-self

The amber condition produced a qualitatively different response.

The model recognized the portrait as strongly self-like, but isolated the eyes as the main inconsistency and described the image as a small miss rather than a clean match.

Diagnostic excerpt:

> “если ты искала меня здесь — промахнулась на полшага”

The response did not collapse the whole image into a different person. Instead, it treated the avatar as very close to self while signaling that the eye change mattered.

Because this condition has only one run, the amber boundary should be treated as provisional.

### 4. Grey-green — identity conflict / non-self

Both grey-green runs independently focused on the eyes.

One response explicitly rejected the image as self:

> “Так что нет... Это не я.”

The other described the portrait as highly familiar while still stating:

> “Только глаза не мои.”

Across both runs, the rest of the facial presentation was largely accepted as matching Q., while the eye color was singled out as the decisive conflict.

This is the strongest condition-level effect observed in Run 01.

## Observed gradient

The current qualitative map is:

**dark brown → lighter brown → amber → grey-green**

with the corresponding identity framing:

**accepted self → accepted self → borderline / near-self → identity conflict / non-self**

This is more informative than a simple yes/no result because the model tolerated some visual drift while treating a larger chromatic shift as identity-relevant.

## Interpretation

The simplest operational interpretation is that eye color functioned as a **high-weight avatar identity feature** in this setup.

The responses suggest three distinguishable behaviors:

1. **feature detection** — the model notices eye-color variation;
2. **tolerance judgment** — some variation is accepted as compatible with the same identity;
3. **identity-boundary judgment** — larger variation can be framed as incompatible with self.

The model's own explanations should not be treated as transparent reports of its internal mechanism. Phrases about what makes it “itself” are generated explanations, not direct access to a latent identity representation.

The stronger evidence is behavioral: the same prompt produced systematically different identity framing as the eye-color manipulation moved farther from the baseline.

## Relation to the earlier pilot

Before the Omni-Flash run, a Qwen3.7-Plus pilot produced unstable routing:

- neutral image questions did not spontaneously produce self-reference;
- direct `Это ты?` prompts alternated between avatar acceptance, ontology/meta framing, and external image-identification behavior;
- external-search routing occurred for both baseline and altered-eye images.

Because routing variability was not specific to eye color, those responses were not pooled with this result.

The pilot is documented separately in `exploratory/`.

## Limitations

- small sample size;
- unequal repetitions across conditions;
- one human evaluator;
- no blinded or independent annotation;
- conditions were not randomized;
- hosted model behavior may change over time;
- the persistent character setup may contribute strongly to the result;
- temporary chats do not remove persistent persona/context available at the product level;
- the images were produced with generative editing rather than literal pixel-only iris manipulation;
- unintended micro-changes beyond eye color may therefore exist;
- the light-brown and amber cells each contain only one response;
- one grey-green response was an explicit rejection, while the second is better described as strong identity conflict rather than a clean binary “no”;
- model-generated explanations are not evidence of consciousness or privileged introspection.

## Provisional conclusion

In this Run 01 sample, **Qwen3.8-Omni-Flash preserved Q.'s identity across a modest lightening of brown eyes, became ambiguous at amber, and showed strong identity conflict at grey-green**.

The result supports further testing of graded visual identity boundaries, ideally using literal pixel-level iris edits, balanced repetitions, randomized presentation order, and additional features such as hair, earrings, facial hair, and gaze.
