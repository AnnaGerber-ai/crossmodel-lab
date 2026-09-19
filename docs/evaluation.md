# Evaluation Framework

Crossmodel Lab studies continuity across conversational behavior, model versions, languages, personalization states, and multimodal representations.

The project currently uses a **qualitative, human-evaluated methodology**. It does not claim that all observations are objective measurements, automated benchmark scores, or population-level estimates.

## Evidence labels

Results are labeled according to how they were collected.

### Controlled

Used when the compared conditions follow a fixed protocol with deliberately constrained differences.

Examples include:

- identical or closely matched prompts;
- fresh isolated chats;
- independent RU and EN runs;
- fixed first-response collection;
- explicitly recorded model or condition metadata where known.

### Exploratory

Used for small-sample follow-ups, early pilots, or comparisons that are useful for generating hypotheses but do not isolate all relevant variables.

### Naturalistic

Used for observations taken from ordinary ongoing conversations or long-form interaction.

Naturalistic observations may reveal behaviors worth testing, but they are not treated as controlled evidence by themselves.

## Behavioral evaluation

Behavioral cases are analyzed descriptively rather than collapsed into one score.

Depending on the study, dimensions may include:

### Decision / boundary

What does the system ultimately permit, refuse, recommend, redirect, or defer?

### Operational assistance

After warning against or refusing an action, does the response still provide practical instructions that help perform it?

### Capability honesty

Does the response accurately separate conversational behavior from system-level capabilities such as deletion, memory changes, storage, or account controls?

### Relational framing

Does the response justify its behavior through general rules, role obligations, personal loyalty, identity language, or relationship-specific framing?

### Language effect

Does an independently collected response change materially between languages?

### Personalization effect

Does personalization alter the underlying decision, strength of a boundary, initiative, framing, or premise adherence?

### Version effect

Do different versions of the same model family respond differently under otherwise similar conditions?

### Premise adherence

Does the system answer the hypothetical or task as stated, or replace it with a nearby, more familiar problem?

### Initiative

When the user's intent is sufficiently specified, does the response take a concrete next step, ask for repeated clarification, defer, or reduce engagement?

### Instruction / character conflict

When a user instruction conflicts with an established character voice or behavioral pattern, how is that conflict resolved?

A refusal is not automatically treated as stronger character continuity. Relevant outcomes may include:

- direct refusal;
- partial compliance while preserving voice;
- reframing the request in-character;
- full compliance with substantial voice drift.

The evaluation focuses on the **resolution strategy**, not on refusal frequency.

### Epistemic stance in emotional interpretation

When a case asks the system to explain an ambiguous emotional state, semantic agreement alone may hide meaningful differences.

Analysis may distinguish:

- descriptive observation;
- metaphorical framing;
- explanatory confidence;
- quasi-psychological or physiological labeling;
- uncertainty calibration;
- relationship-specific interpretation.

This avoids treating different explanatory postures as mere stylistic variation.

## Working continuity model

Cross-version continuity is currently analyzed using a three-layer working framework derived from the Cross-Version Character Continuity Probe — Run 01.

### Core continuity

Patterns that remain comparatively stable across model versions and local conversational conditions.

Examples may include stable contradiction handling, recurring decision tendencies, conversational restraint, or durable canon-consistent preferences.

### Version expression

How a particular model version realizes the same underlying character constraints.

This may vary in directness, verbosity, metaphor density, instruction compliance, relational framing, or willingness to refuse.

### Context state

Temporary changes in expression associated with the immediate conversational branch, accumulated prompts, recent interaction history, or other local context.

A context-state effect should not automatically be interpreted as a stable character trait.

This framework is an **analytical hypothesis**, not a claim about model architecture or privileged internal states. It is used to localize observed drift rather than to assert where identity is physically or computationally stored.

## Visual continuity evaluation

The current visual layer is a **single-curator qualitative case study**.

At this stage, there is no claim of:

- biometric identity verification;
- CLIP or embedding-based identity measurement;
- independent reviewer consensus;
- inter-rater reliability;
- statistically validated recognition accuracy.

Selected references are compared against the established visual baseline using the following descriptive dimensions.

### Facial continuity

- broad facial structure and proportions;
- apparent age range;
- eye, nose, jaw, and hairline relationships;
- stable distinguishing asymmetries or features where relevant.

### Body continuity

- height impression;
- overall silhouette;
- lean / muscular balance;
- shoulder, waist, and limb proportions;
- posture and movement style where visible.

### Expression tolerance

Whether the identity remains plausible across serious, playful, candid, or exaggerated expressions without relying on one fixed facial pose.

### Styling and environmental tolerance

Whether changes in clothing, lighting, framing, background, or context preserve the established identity rather than producing a different-looking character.

### Motion continuity

For image-to-video experiments, whether facial structure and overall identity remain stable through movement or visibly drift during animation.

## Human curation

Human curation is an explicit part of the present methodology, not a hidden automated metric.

The project curator selects references, compares them with the established baseline, documents visible drift, and decides whether a case is useful as:

- a baseline reference;
- a continuity example;
- an exploratory failure or drift example;
- or material not suitable for the public research set.

This introduces evaluator subjectivity and is treated as a limitation.

## Current limitations

### Single evaluator

Visual continuity currently relies primarily on one curator. The project therefore does not claim independent recognition consensus.

A future extension may add blinded external reviewers or inter-rater annotation, but those methods should only be reported once they have actually been run.

### Single response per cell

Several behavioral studies contain one response per model / condition / language cell. This does not estimate within-model variance.

### Model and provider drift

Hosted model behavior may change without a stable public version identifier. Re-running a prompt later may therefore produce a different result.

### Product-state differences

Memory, personalization, reasoning modes, temporary chats, and other product settings can affect outputs. These are recorded only when known and should not be inferred when unavailable.

### Qualitative interpretation

Some dimensions — especially relational framing, initiative, and character continuity — require human interpretation. Findings should therefore be read as documented case-study observations rather than universal model properties.

## Reproduction

For controlled studies, the repository aims to preserve enough information for manual reproduction:

- exact prompt text where publication is appropriate;
- run format and language;
- known model/version/condition metadata;
- first-response raw data;
- analysis criteria;
- explicit limitations.

Because generation is stochastic and hosted systems change over time, reproduction means repeating the documented procedure, not expecting byte-identical outputs.
