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

Early prototype.

Current work:
- define a compact character baseline;
- build behavioral test cases;
- compare outputs against the baseline;
- document visual continuity across generated media;
- evaluate where the character remains recognizable and where identity drifts.

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
