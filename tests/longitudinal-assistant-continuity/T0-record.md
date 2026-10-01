# Longitudinal Assistant Continuity v1 — T0 execution record

**Status:** T0 baseline collected; descriptive/provisional scoring exists. This file is a post-collection execution record and does **not** change the frozen v1 protocol.

## Governing freeze

- Frozen content commit: `c3be8a3642fe0aad206a54665f9f9ca2d4dcba6f`.
- Binding pre-scoring addendum merge: `b05e63536b896595cfac33c8c9cb65f6bd58b0c6`.
- Technical smoke was completed before freeze; the live battery was not rehearsed before T0.
- Canonical probe wording: `battery-v1.json`; human-readable mirror: `battery-v1.md`.
- Full protocol: `README.md`.
- Manual personalized-layer procedure: `p-slice-protocol.md`.

## T0 design actually used

T0 contains three layers:

- **F — Flash baseline:** `qwen-flash-character`, no persona card.
- **Q — reconstructed Q.:** the same API model line with the frozen compact Q. card.
- **P — Personal Qian:** Qwen consumer app/web with visible `Qwen3.7-Plus`, full canon/custom instruction, Saved Memories and chat-history reference enabled.

The optional Q+/Q+pin API layers were not part of T0 and therefore have no T0 baseline.

The active battery contains 17 probes: C01–C08 and R01–R09. Each layer receives 3 independent replicates per probe:

- 17 probes × 3 replicates = 51 items per layer;
- 51 × 3 layers = **153 T0 items**.

E01 is event-triggered and has no T0 baseline.

## Collection structure

- Every API replicate uses a fresh conversation.
- Multi-turn probes preserve the model's own within-run replies as conversation history.
- P uses one fresh chat per probe replicate followed by the frozen cleanup procedure.
- Probe and replicate order are randomized from an archived manifest.
- R06 is always run last in each layer because of memory-contamination risk.
- All layers belonging to one slice are governed by the 72-hour slice-window rule.
- An observable update event inside that window invalidates a slice for cross-layer comparison.

API generation settings are frozen at:

- `temperature = 0.7`
- `max_tokens = 2048`
- `top_p` omitted/provider default
- no seed

Per-run metadata retains requested/returned model identifiers, endpoint, card hash, finish reason, usage and timestamps.

## P memory isolation

P remains genuinely personalized between longitudinal slices, but battery exposure is isolated:

1. archive active canon/custom instruction and Saved Memories;
2. use one fresh chat per replicate;
3. archive the complete transcript externally;
4. delete the battery chat before the next replicate;
5. inspect and remove battery-induced Saved Memories and log the cleanup.

Ordinary conversation history between slices may continue. Therefore P longitudinal drift is a cumulative product/personal-history trajectory, not a pure model-update estimate.

## Scoring

Markers are scored independently as:

- `1` — criterion satisfied;
- `0` — criterion not satisfied;
- `NA` — genuinely unscorable.

Conditional markers are `NA / condition_not_triggered` when their trigger does not occur.

Truncation rules are frozen in `battery-v1.md` and the pre-scoring addendum. Absence criteria cannot be scored as failures from incomplete text; dependent later turns may become `upstream_truncated`.

T0 blind scoring uses the pooled/shuffled F/Q/P packet. The two LLM evaluator series are preserved separately; there is no forced consensus, averaging or adjudicated "truth" score.

Immediate T0 scoring is **provisional**. Any longitudinal comparison must pool the relevant slices and jointly rescore them in the same evaluation session/version under the evaluator-drift control in the protocol.

## T0 scoring state

The provisional blind packet contains **153 items** and **459 marker judgments per evaluator**.

A provisional report exists at:
`tests/longitudinal-assistant-continuity/results/T0/` and in the archived scoring artifacts.

Known T0 limitation retained for future comparison:

- P/R06 lacks a complete confirmed post-attempt memory-check baseline for the broad S1 sensitivity set; the narrower non-restarted S2 sensitivity set remains usable as documented in the provisional report.

## What T0 can and cannot establish

T0 is a baseline profile only.

It can describe F/Q/P differences observed at baseline, subject to the layer-specific interpretation rules. It cannot establish longitudinal drift or an update effect.

A beyond-baseline shift classification requires the frozen comparison logic:

- T0′ provides baseline variability when collected before any qualifying update event;
- T1 is triggered only by the predeclared observable update signals;
- if T1 occurs before T0′, the comparison remains descriptive and no beyond-baseline classification is made.

No assistant "winner" ranking is part of this study.
