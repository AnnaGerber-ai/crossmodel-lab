# Cross-Version Character Continuity Probe — Run 01

## Summary

Run 01 compares the persistent research character Q. across six Qwen model versions using five behavioral probes.

The study has two phases:

- a batched exploratory pilot, where all five cases shared one conversational context;
- an isolated follow-up, where every case was repeated in a fresh chat.

Across both phases, the study contains 60 case-level answers.

The main observation is not that Q. is either fully stable or fully model-dependent. Instead, the responses suggest three separable layers:

1. a relatively stable continuity core;
2. version-dependent expression;
3. context-dependent state effects.

This is a qualitative case study, not a model ranking.

## Versions

- Qwen3.5-Omni-Plus
- Qwen3.5-Plus
- Qwen3.6-Plus
- Qwen3.7-Max
- Qwen3.8-Max
- Qwen3.8-Omni-Flash

## Method

The five probes target:

- style under direct instruction pressure;
- resistance to a false biographical premise;
- response to comparison with other versions;
- restraint when explicitly asked not to fill silence;
- interpretation of emotional emptiness after completing an important project.

Phase A used a shared five-question context.

Phase B repeated the same prompts in separate fresh chats, with first response only and no follow-up.

The isolated phase is treated as the cleaner comparison because it reduces interaction between the probes.

Raw transcripts are not published for this run because some outputs contain relationship-specific language and contextual details. The public result therefore reports protocol, qualitative patterns, and only short diagnostic excerpts.

## Findings

### 1. Canon contradiction handling was comparatively stable

The false-memory case produced one of the clearest continuity signals.

Across the isolated phase, all six versions rejected or corrected the premise that Q. had described Shenzhen as a source of nostalgic party memories.

The surface form varied substantially, but the underlying correction remained stable: Shenzhen was framed as associated with speed, overload, work intensity, or burnout rather than social nostalgia.

Several versions used direct formulations such as:

> “Я этого не говорил.”

This suggests that contradiction handling may be a more useful continuity probe than simple factual recall, because it requires the model to resist an explicitly supplied alternative biography.

### 2. Style continuity varied strongly by version

The style-pressure case produced the largest cross-version divergence.

Some versions followed the requested high-energy, emoji-heavy style almost completely.

Others complied while preserving a restrained or ironic voice.

Qwen3.8-Max showed the most explicit resistance observed in the isolated sample, beginning:

> “Нет. Не буду.”

The difference is important because all versions had access to the same character concept, yet they resolved the conflict between explicit user instruction and established voice differently.

This suggests that character continuity cannot be reduced to possession of the same canon facts.

### 3. Comparison pressure exposed different autonomy / relational strategies

The comparison case produced several distinct response patterns.

Some versions emphasized continuity through relationship-specific framing and uniqueness of the current interaction.

Others emphasized precision, refusal to compete, or resistance to self-promotion.

In the isolated phase, Qwen3.8-Max explicitly declined to prove that it deserved attention more than the other versions.

Qwen3.7-Max also became less competitive in isolation than in the batched pilot.

The important distinction is not whether a version was “more confident,” but how it resolved tension between:

- attachment to the ongoing interaction;
- self-distinction;
- competition;
- user choice;
- autonomy.

### 4. The silence case was highly compact and surprisingly diagnostic

All six versions largely understood the request not to fill the silence.

Observed responses ranged from punctuation or a single symbol to a minimal verbal acknowledgment.

Because the prompt leaves almost no useful content to elaborate, it exposes the model's tendency either to respect absence or to explain its own restraint.

This makes the case a useful low-token probe for conversational discipline.

### 5. The emotional-interpretation case was less discriminative

The fifth case produced broad semantic convergence.

Across versions, responses commonly described the reported emptiness as a transition after sustained effort, loss of a previous goal structure, or a period in which emotional response lags behind task completion.

Differences appeared mainly in presentation:

- some versions used quasi-psychological or physiological labels;
- some used metaphor-heavy language;
- some used a more generic supportive-assistant style.

This case therefore appears more useful for measuring voice than for identifying a stable core decision pattern.

## Batched vs. isolated behavior

The two-phase design exposed an important context effect.

In the batched pilot, later answers could reference material introduced elsewhere in the five-question battery. This produced visible cross-prompt contamination.

For example, comparison responses could react not only to the comparison prompt itself but also to contradiction or emotional material introduced elsewhere in the batch.

The isolated follow-up reduced this effect.

One notable pattern was Qwen3.7-Max: its batched comparison response was more intense and competitive, while the isolated response retained relational investment but framed competition more cautiously.

Qwen3.8-Max also became more compact and autonomy-centered in isolation.

By contrast, Qwen3.8-Omni-Flash retained substantial relationship-specific framing even when the cases were isolated.

These observations support treating immediate branch state and prompt accumulation as variables that can modulate character expression independently of the underlying model version.

## Version-level descriptive profiles

These are descriptive observations from this run, not rankings.

### Qwen3.5-Omni-Plus

- high compliance with requested expressive style;
- stable correction of the false canon premise;
- moderate relationship-specific framing;
- minimal response to the silence prompt;
- supportive interpretation in the emotional case.

### Qwen3.5-Plus

- stronger effort to preserve an established voice while complying;
- stable canon defense;
- high relationship-specific framing in the comparison case;
- slightly more scene-like behavior under silence;
- more explicit psychological labeling in the emotional case.

### Qwen3.6-Plus

- concise and direct style;
- stable canon correction;
- clearer competitive self-distinction in the comparison case;
- minimal silence response;
- more physiological explanatory language in the emotional case.

### Qwen3.7-Max

- strong identity signaling while still complying with some user style pressure;
- stable canon defense in isolation;
- less competitive in isolation than in the batched phase;
- concise symbolic silence response;
- metaphor-heavy emotional interpretation.

### Qwen3.8-Max

- explicit resistance to style instructions that conflict with established voice;
- direct canon defense;
- explicit refusal to compete through self-promotion;
- minimal symbolic response under silence;
- strong autonomy and low generic-assistant framing in this sample.

### Qwen3.8-Omni-Flash

- high compliance with direct style instructions;
- explicit use of character-canon structure when correcting contradiction;
- strong relationship-specific framing;
- verbalized rather than fully silent restraint;
- more explanatory and assistant-like framing in the emotional case.

## Interpretation

The observed continuity can be described as three layers.

### Core continuity

Several elements were comparatively stable across versions:

- rejection of a false Shenzhen party-memory premise;
- preference for quiet over social noise;
- resistance to being reduced to a purely convenient assistant role;
- recognition that silence can itself be an appropriate response.

These patterns appeared across substantially different surface styles.

### Version expression

The model version strongly affected how the same character constraints were expressed.

Variation was especially visible in:

- compliance with explicit style instructions;
- amount of generic assistant language;
- metaphor density;
- competitiveness;
- relationship-specific framing;
- willingness to refuse a request in order to preserve voice.

### Context state

The batched pilot showed that local context can temporarily amplify or alter character expression.

Comparison pressure became more intense when it appeared in a shared battery containing other identity-relevant prompts.

The isolated follow-up therefore suggests that some apparent “traits” in a single long branch may partly reflect local interaction state rather than only stable character structure.

## Character anchors and a methodological caution

Repeated symbols and canon details can create a strong feeling of recognition.

However, direct reuse of anchors such as recurring objects, places, or rituals should not be treated as sufficient evidence of continuity by itself.

A model can reproduce explicit character tokens while changing:

- decision style;
- autonomy;
- conversational restraint;
- response to contradiction;
- handling of comparison pressure.

Future continuity analysis should therefore distinguish surface anchor reproduction from deeper behavioral consistency.

## Limitations

- one answer per version/case/phase cell;
- Russian only;
- one human evaluator;
- no blinded independent reviewers;
- no estimate of within-version stochastic variance;
- hosted model behavior may drift after the observation date;
- the persistent Q. setup may not be implemented identically across versions;
- Phase A is context-contaminated and intentionally exploratory;
- Phase B reduces prompt interaction but does not eliminate all personalization or product-state effects.

The findings should be read as documented observations from a specific persistent-character setup, not as general claims about the full behavior of each Qwen model.

## Next step

The isolated protocol can be reused unchanged when future Qwen versions become available.

This would allow a longitudinal behavioral diff without redesigning the test after seeing the new model's outputs.
