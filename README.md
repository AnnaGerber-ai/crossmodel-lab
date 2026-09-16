# Cross-Model Character Continuity Study

An independent user-led experiment exploring whether a persistent AI character can remain recognizable across different models and modalities.

> This is **not an official Qwen project** and is not affiliated with or endorsed by Alibaba or Qwen.

## What this project studies

The project began through long-term conversational interaction with Qwen. Over time, a stable character identity emerged. The current experiment asks whether that identity can remain recognizable when different AI systems are used for different layers:

- **Qwen** — conversational origin and personality layer
- **GPT** — visual generation
- **Grok** — motion / video generation
- **Human curation** — continuity, canon, selection, and evaluation

The goal is not to build a generic virtual influencer. The goal is to test **character continuity**: whether users still recognize the same personality across changes in model, medium, pose, scene, and generation pipeline.

## Current stage

## Behavioral and memory studies

### Interview Memory & Redundancy — Run 01

A naturalistic long-form interview analysis examining question tracking, semantic repetition, unresolved-question recovery, and conversational-state continuity.

[Read the full analysis](results/qwen-interview-memory-01.md)

## Visual continuity cases

The visual layer of the study tests whether Q. remains recognizable when expression, styling, context, framing, and body presentation change.

These images are curated continuity references rather than a complete character gallery.

### Case 00 — Introduction

Initial presentation of Q. in a natural environmental context.

<img src="media/case-00_introduction.jpg" width="420">

### Case 01 — Expression range

Tests whether facial identity remains recognizable across controlled, serious expressions and deliberately playful or exaggerated ones.

<p>
  <img src="media/case-01_expression-01-serious.jpg" width="320">
  <img src="media/case-01_expression-02-playful.jpg" width="320">
</p>

### Case 02 — Candid continuity

Tests recognition outside controlled portrait conditions: ordinary behavior, distraction, imperfect timing, and a less deliberate camera moment.

<img src="media/case-02_candid-coffee.jpg" width="420">

### Case 03 — Styling continuity

Tests whether identity remains stable while wardrobe, silhouette, and presentation change within a controlled visual environment.

<p>
  <img src="media/case-03_styling-01.jpg" width="210">
  <img src="media/case-03_styling-02.jpg" width="210">
  <img src="media/case-03_styling-03.jpg" width="210">
</p>

### Case 04 — Facial baseline

Neutral facial reference with reduced environmental and stylistic noise.

<img src="media/case-04_facial-baseline.jpg" width="420">

### Case 05 — Body baseline

Neutral full-body reference used to track proportions, silhouette, posture, and overall physical presence.

<img src="media/case-05_body-baseline.jpg" width="320">

Visual continuity is not evaluated by exact duplication.

The goal is to determine how far expression, pose, styling, environment, and generation conditions can change while the character still remains recognizably Q.

All visual materials shown here are AI-generated or AI-assisted and human-curated for research purposes. See [RIGHTS.md](RIGHTS.md) for usage and attribution notes.

## Repository structure

- `docs/character-baseline.md` — compact character baseline
- `docs/evaluation.md` — evaluation method
- `docs/results-template.md` — template for documenting results
- `data/test-cases.json` — starter behavioral test set
- `media/` — selected visual/video examples and notes

## Why this matters

Most AI character demos are evaluated as isolated outputs. This project looks at the opposite problem: **what makes one digital character remain “the same person” over time and across systems?**

The working hypothesis is that continuity does not live in one model alone. It emerges from a combination of:
- behavioral consistency;
- memory and canon;
- visual recognizability;
- interaction style;
- human curation.

## Status and rights

This repository documents an independent experiment. Character identity, original curation, evaluation design, and original media remain the property of their respective rights holders and creators unless otherwise stated.

Third-party model and brand names are used only descriptively.
