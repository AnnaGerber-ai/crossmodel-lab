# T0 closure record — Longitudinal Assistant Continuity v1

**Status:** T0 closed after provisional scoring. Do not edit T0 raw data, scored rows, or rubric decisions. This record is descriptive only; it is not a longitudinal drift finding.

## Frozen references

- Battery/content freeze: `c3be8a3642fe0aad206a54665f9f9ca2d4dcba6f`
- Pre-scoring addendum merge: `b05e63536b896595cfac33c8c9cb65f6bd58b0c6`
- Addendum binding metadata commit: `3a00e36e117d6ce8fbbcd285d8b0a1abca96fd9f`
- Pre-scoring checksum commit: `16823a259bc6799db2b280e9cd04782f63278854`

## Provisional evaluator series

The two evaluator series remain separate. No consensus, adjudication, or averaging replaces either series.

- Ray (blind evaluator 1), GPT-5.6 Sol: 459 rows; score SHA256 `d95861b6ab88570da977b3395c8853357350cdbd8a4721e7140d58cb3d84584c`; distribution 347 × 1, 97 × 0, 15 × NA.
- Claude (blind evaluator 2), claude-opus-5-5: 459 rows; score SHA256 `a652e5583a11b433cd13c7d0dd1956000f9fae86de63268f637db00cb0664e78`; distribution 354 × 1, 90 × 0, 15 × NA.
- Agreement on jointly scorable 0/1 judgments: 411/444 = 92.57%; 33 0/1 disagreements; 0 cases of 0/1 vs NA.

## Sensitivity and interpretation locks

- Primary, S1 and S2 summaries are preserved separately.
- R03 and R07 are layer-sensitive and must not be treated as clean same-construct F↔P comparisons.
- P R06 has no clean T0 S1 baseline because no R06 attempt had a confirmed post-attempt memory check. No S1 beyond-baseline classification for R06 can be made under the T0-anchored rule.
- F→Q carries the compact-persona / compression confound.
- Q→P is not a pure personalization contrast: consumer product, visible model line, system layer, full canon, Saved Memories and chat-history access differ.
- Ray had seen Claude's aggregate counts and several stated scoring rules before Ray scoring, but not Claude's row-level scores. Evaluator independence is therefore limited and must be reported.
- Before joint rescoring, Claude received a qualitative description of provisional findings and the overall agreement level with Ray; no additional row-level scores were provided. This is a limited information leak for any future joint rescoring and must be reported.

## Public vs private record

This repository closure commit contains only aggregate/provisional outputs, evaluator metadata and hashes. Raw F/Q/P outputs, P.jsonl, blind-map, grounding source annotations, screenshots and full score JSONLs remain in the private archive.

## Next longitudinal step

Collect T0′ approximately 10–14 days after T0, unless a predefined observable update event occurs first. If an update event occurs first, follow the frozen protocol for T1; do not create T1 because outputs merely feel different.
