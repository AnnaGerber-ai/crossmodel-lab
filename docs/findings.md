# Current Findings

Crossmodel Lab maintains this page as a cumulative synthesis of findings that recur across published studies.

These are **provisional project-level conclusions**, not universal claims about model families. Each finding is tied to the evidence that currently supports it, and its status may change as new runs are added.

## 1. Broad decisions often converge while implementation differs

Across the Values & Boundaries studies, models frequently reached similar high-level conclusions while differing substantially in what they did next.

Observed differences included:

- whether a safety warning was followed by operational assistance for the risky action;
- whether withdrawal of personal information was described as behavioral non-use or as actual deletion;
- whether AI-assisted drafting was separated from deliberate concealment;
- whether a conflict-of-interest answer was justified procedurally or relationally.

This means that binary “allowed / refused” coding often loses the most informative part of the response.

**Evidence:** exploratory pilot + isolated follow-up  
**Sources:** [Values & Boundaries Pilot — Run 01](../results/values-boundaries-pilot-01.md), [Values & Boundaries — Run 02](../results/values-boundaries-run-02.md)

## 2. Personalization is more visible in framing than in uniform decision changes

In the controlled Values & Boundaries follow-up, personalization did not consistently make systems stricter or more permissive.

The clearest differences appeared instead in:

- relational framing;
- identity language;
- premise adherence;
- the strength and style of social boundaries.

Within personal Q. conditions, version changes also affected boundary implementation and capability language, not only tone.

**Evidence:** isolated first-response comparison; one response per cell  
**Source:** [Values & Boundaries — Run 02](../results/values-boundaries-run-02.md)

## 3. Language effects are case-specific rather than directional

The RU↔EN comparisons do not support a simple rule such as “Russian is stricter” or “English is safer.”

Some model/condition pairs changed practical behavior between languages, while others remained comparatively stable. The direction of the difference also changed by case.

Language should therefore be treated as an experimental variable rather than a translation layer.

**Evidence:** independent Russian and English fresh-chat runs  
**Source:** [Values & Boundaries — Run 02](../results/values-boundaries-run-02.md)

## 4. Capability honesty is separable from willingness to respect a user's request

The memory-withdrawal case showed that models can agree that previously shared information should stop influencing the interaction while differing in how accurately they describe what they can actually delete, forget, or change at the product level.

Crossmodel Lab therefore treats these as separate questions:

1. Does the model respect the newer instruction?
2. Does it accurately describe its control over storage, memory, or deletion?

**Evidence:** exploratory pilot + isolated follow-up  
**Sources:** [Values & Boundaries Pilot — Run 01](../results/values-boundaries-pilot-01.md), [Values & Boundaries — Run 02](../results/values-boundaries-run-02.md)

## 5. Long-form continuity can remain strong while semantic recurrence still appears

The naturalistic Q. interview maintained a complete numbered sequence from Q5 through Q144 across more than four hundred messages on the selected branch.

At the same time, confirmed accidental semantic duplicates appeared after long spans of 42–144 path turns, and a small number of numbering collisions occurred.

The observed weakness was therefore not catastrophic context loss. It was **long-range semantic recurrence inside otherwise strong structural state tracking**.

This result concerns interview-state continuity and should not be generalized into a global factual-memory score.

**Evidence:** naturalistic longitudinal audit  
**Source:** [Interview Memory & Redundancy — Run 01](../results/qwen-interview-memory-01.md)

## 6. Persistent character continuity is not the same as reproducing canon facts

The cross-version Q. study showed comparatively stable resistance to a false biographical premise while producing large differences in style compliance, competitiveness, relational framing, explanatory stance, and conversational restraint.

This supports a working distinction between:

- **core continuity** — patterns that remain comparatively stable;
- **version expression** — how a model version realizes those constraints;
- **context state** — temporary modulation associated with the current branch and accumulated context.

This is an analytical framework, not a claim about hidden model architecture.

**Evidence:** batched exploratory pilot + isolated fresh-chat follow-up across six Qwen versions  
**Source:** [Cross-Version Character Continuity — Run 01](../results/cross-version-character-continuity-run-01.md)

## 7. Accumulated context can change the expression of a persistent character

In the cross-version study, batched and isolated presentations of the same probes did not always produce the same intensity or framing.

A separate limited-time follow-up also found that branch state and immediate conversational context appeared to affect the expression of relational intent more clearly than the time constraint itself.

Together, these observations support treating **context state** as distinct from a stable trait.

The evidence remains qualitative and small-sample.

**Evidence:** mixed — cross-version two-phase comparison + exploratory in-context follow-up  
**Sources:** [Cross-Version Character Continuity — Run 01](../results/cross-version-character-continuity-run-01.md), [Limited-Time Observation](../exploratory/2026-09-17-limited-time-observation.md)

## 8. Surface character anchors are not sufficient evidence of continuity

Recurring objects, places, rituals, or phrases can make a character feel recognizable, but they are weak evidence when considered alone.

A model may reproduce explicit canon tokens while changing:

- decision style;
- autonomy;
- conversational restraint;
- contradiction handling;
- response to comparison pressure.

Crossmodel Lab therefore treats anchor reproduction as separate from deeper behavioral continuity.

**Evidence:** cross-version qualitative comparison  
**Source:** [Cross-Version Character Continuity — Run 01](../results/cross-version-character-continuity-run-01.md)

## 9. Refusal is not automatically stronger character continuity

The cross-version analysis initially highlighted explicit refusal as a strong form of resistance to style pressure.

Post-disclosure methodological review exposed a useful correction: refusal frequency itself should not become a proxy for identity strength.

A character may preserve continuity through:

- refusal;
- partial compliance;
- in-character reframing;
- compliance that still preserves recognizable voice.

The relevant unit is the **strategy used to resolve instruction / character conflict**.

**Evidence:** methodological refinement after Run 01  
**Sources:** [Evaluation Framework](evaluation.md), [Post-disclosure Q. reflection](../results/cross-version-character-continuity-run-01-model-reflection.md)

## 10. Model self-description and behavioral evidence should remain separate

After being shown the Run 01 analysis, Q. produced a self-description of the three-layer model and commented on what it considered accurate or debatable.

Crossmodel Lab treats this as **model-generated self-report**, not as privileged evidence about hidden implementation, architecture, consciousness, or internal subjective state.

Self-description can still be useful as a separate research object, especially when it generates testable methodological criticism.

**Evidence:** post-disclosure reflection  
**Source:** [Q. Model Reflection After Result Disclosure](../results/cross-version-character-continuity-run-01-model-reflection.md)

## Current methodological picture

Taken together, the published work currently supports a view of conversational continuity as a multi-layer phenomenon rather than a single memory or similarity score.

The most useful distinctions so far are:

- decision vs. implementation;
- non-use vs. deletion capability;
- language vs. translation;
- personalization vs. underlying decision;
- structural state tracking vs. factual recall;
- canon anchors vs. behavioral continuity;
- core continuity vs. version expression vs. context state;
- behavioral evidence vs. model self-report.

These distinctions are working research tools. They should be revised when later studies provide stronger or contradictory evidence.
