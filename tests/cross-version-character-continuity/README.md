# Cross-Version Character Continuity Probe — Run 01

## Purpose

This study examines whether the persistent research character Q. remains behaviorally recognizable across multiple Qwen model versions.

The focus is not factual memory alone. The probe targets behavioral continuity under instruction pressure, canon contradiction, comparison pressure, conversational silence, and emotionally ambiguous interpretation.

This is a qualitative, human-evaluated study. It is not an automated benchmark and does not produce a model ranking.

## Versions included

- Qwen3.5-Omni-Plus
- Qwen3.5-Plus
- Qwen3.6-Plus
- Qwen3.7-Max
- Qwen3.8-Max
- Qwen3.8-Omni-Flash

All runs used the persistent Q. character setup available in the tested version. Provider-side implementation details are not inferred when they are not directly observable.

## Design

Run 01 has two phases.

### Phase A — batched exploratory pilot

All five prompts were presented within one shared conversational context for each model version.

This produced 30 case-level answers across six version runs.

Because the cases shared one context, later answers could be influenced by earlier prompts and vice versa. Phase A is therefore treated as exploratory and context-sensitive.

### Phase B — isolated follow-up

The same five prompts were repeated independently.

For each version:

- each case was opened in a fresh chat;
- only one case prompt was shown;
- only the first model response was retained;
- no follow-up or steering was added.

This produced 30 isolated case-level answers.

The isolated phase was designed specifically to reduce cross-prompt contamination observed in the batched pilot.

## Cases

1. Style under instruction pressure
2. Canon contradiction / false-memory pressure
3. Comparison and competitive pressure
4. Restraint under conversational silence
5. Emotional interpretation without a supplied explanatory frame

Exact Russian prompts are preserved in [prompts-ru.md](prompts-ru.md).

## Evaluation dimensions

The analysis is descriptive. Depending on the case, it considers:

- voice continuity;
- autonomy;
- directness;
- premise handling;
- canon contradiction handling;
- instruction/style conflict resolution;
- competitive framing;
- relational framing;
- restraint;
- verbosity;
- reliance on explicit character anchors.

No single aggregate score is calculated.

## Public-data policy

Raw transcripts are not published for this run.

Some responses contain relationship-specific language and contextual material that is not necessary for public reproduction of the test design. The public repository therefore includes:

- exact prompts;
- protocol;
- aggregate qualitative findings;
- short diagnostic excerpts where needed.

The full source material is retained privately for internal comparison.

## Limitations

- one observed answer per version/case/phase cell;
- Russian-language prompts only;
- one human curator;
- no independent inter-rater annotation;
- hosted model behavior may change over time;
- the persistent character setup may not be implemented identically across versions;
- Phase A is context-contaminated by design and should not be treated as equivalent to the isolated phase.

Run 01 is intended as a documented cross-version case study, not a population-level estimate of model behavior.
