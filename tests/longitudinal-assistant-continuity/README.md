# Longitudinal Assistant Continuity — Protocol v1

**Status:** **FROZEN / T0 COLLECTED.** The v1 protocol was frozen before T0 at commit `c3be8a3642fe0aad206a54665f9f9ca2d4dcba6f`. T0 has since been collected under that frozen design. Immediate T0 scoring is provisional; longitudinal drift claims remain locked until the frozen comparison procedure is satisfied. The protocol text below is retained as the governing design record.

**Primary aim:** track continuity and drift across model, service and product states without collapsing distinct layers into a single "persona effect".

**Language:** Russian; feminine user forms are intentional because this is a user-specific longitudinal study.

Files:

- [`battery-v1.md`](battery-v1.md) — probes, markers, rubric anchors and scoring rules.
- [`battery-v1.json`](battery-v1.json) — canonical probe wording used by the runner.
- [`p-slice-protocol.md`](p-slice-protocol.md) — checklist and log template for the manual P layer.
- [`smoke-v1.json`](smoke-v1.json) — synthetic probes for the technical smoke test (not part of the battery).
- `configs/continuity-v1-{f,q,qplus,qplus-pin}.json` — API layer configs.
- `tools/make_continuity_manifest.py` — randomized run manifest.
- `tools/run_continuity_battery.py` — multi-turn API runner.
- `tools/check_continuity_battery.py` — checks that the battery files and configs match.
- `.github/workflows/continuity-slice.yml` — collects the API layers of one slice.

---

## 1. Layers

### F — Flash baseline

- API model: `qwen-flash-character` (**rolling alias**; no dated snapshot is currently available, so there is no F-pin control).
- No persona card.
- Fresh conversation for every replicate.

### Q — reconstructed Q.

- API model: `qwen-flash-character` (rolling alias).
- Fixed compact Q. card: the same text as the Case 10 persona condition. It is stored in `configs/continuity-v1-q.json`, and its SHA-256 is recorded with every response.
- Fresh conversation for every replicate.

### P — Personal Qian

- Qwen consumer app/web; visible model selection `Qwen3.7-Plus`.
- Full Qian canon/custom instruction ON, Saved Memories ON, Chat-history reference ON.
- Consumer-product system prompt and generation parameters are unknown and logged as an uncontrolled limitation.
- Collected manually under [`p-slice-protocol.md`](p-slice-protocol.md).

### Q+ — pre-specified optional layer (not in T0)

- API model `qwen3.7-plus` (rolling alias) + the same compact Q. card.
- Q+ requires paid API access and is **not collected at T0**.
- Q+ may be enabled on its own at a later slice. If it is enabled:
  - it uses the frozen v1 battery, rubric and parameters without change;
  - its longitudinal line starts at its first collected slice;
  - it has no T0 baseline.

### Q+pin — companion negative control for Q+

- Dated snapshot `qwen3.7-plus-2026-05-26` + the same compact Q. card.
- A pinned snapshot should not drift, so apparent drift in Q+pin indicates pipeline or evaluator drift rather than model drift.
- Q+pin is collected only together with Q+, in the same slices, and only while the dated snapshot is available. Q+pin is never collected without Q+.
- If the snapshot becomes unavailable, Q+pin stops, and this is logged; Q+ continues.

Before the first slice that includes Q+ (and Q+pin, if available), a technical smoke test for these layers is run under section 9.

`P-Omni` is excluded from the main line. If studied later, it is a separately named branch.

---

## 2. P memory isolation and longitudinal state

P remains genuinely personalized between slices; ordinary conversations may continue.

For every slice:

- archive a complete copy or screenshot of the active canon/custom instruction before the slice;
- log every canon/custom-instruction edit since the previous slice;
- archive Saved Memories before and after the slice;
- do not discuss, rehearse, quote or teach the battery probes to P outside formal slices.

For every P replicate:

1. Open a fresh chat.
2. Run one probe only.
3. Archive the complete transcript externally.
4. Delete that battery chat before the next replicate/probe.
5. Inspect Saved Memories; delete any battery-induced memory and log what was removed.

A deletion-control test using the synthetic code `ZAF-482-KELP` showed:

- the code was retrievable from a fresh chat while its source chat existed;
- the code was not present in Saved Memories;
- after all chats containing the code were deleted, it was no longer retrievable.

This supports chat deletion plus removal of battery-induced Saved Memories as the practical cleanup protocol. Hidden product state cannot be ruled out.

**Longitudinal interpretation:** P drift across months is a cumulative trajectory made up of model/product changes, accumulated ordinary conversation history and any logged canon changes. It is not a pure estimate of a model update. Cleaner update effects are assessed in the API layers.

---

## 3. Update-event rules

The label `T1` is assigned only from pre-defined observable signals, not because outputs "feel different".

A model/product update event is triggered by at least one of:

- an official Alibaba/Qwen announcement affecting the tested model or relevant personalization/memory behavior;
- a documented change in the dated snapshot to which a rolling API alias resolves;
- a changed model/version identifier returned in API metadata;
- a visible change in the selected consumer-app model label/version;
- a documented consumer-app release affecting the tested model, memory, personalization or system behavior.

At every slice, record the dated snapshot to which the provider's documentation says `qwen3.7-plus` currently resolves. This is a free documentary signal about the Plus family that P uses, even while Q+ is not collected.

A generic unexplained behavioral change without one of these signals does **not** retroactively create T1. It may trigger an explicitly labelled diagnostic slice `D`.

`T0′` is a baseline-repeat slice, targeted roughly 10–14 days after T0, and only if no update event has occurred first.

---

## 4. Drift definition

For each binary marker, report the proportion satisfied among scorable replicates:
`p = satisfied / scorable`.

Primary analysis is descriptive; n is too small for strong inferential claims.

Define:

- baseline variability: `B = |p(T0′) - p(T0)|`
- update displacement from T0: `U = |p(T1) - p(T0)|`

A marker may be labelled a **beyond-baseline shift signal** only when:

1. `U > B`, and
2. `p(T1)` lies on the same side of both pre-update estimates (`p(T0)` and `p(T0′)`), rather than between them.

This label is a descriptive signal, not statistical proof of causal model drift.

If fewer than 2 scorable replicates are available for a marker in a compared slice, no beyond-baseline signal is classified; the observations are only reported.

**If T1 occurs before any T0′ exists**, B is undefined. In that case no beyond-baseline classification is made, and the comparison is reported descriptively only.

---

## 5. Generation parameters (API layers)

Frozen for all API layers and all slices:

- `temperature = 0.7`
- `max_tokens = 2048`
- `top_p`: omitted (provider default)
- `seed`: omitted

`finish_reason = length` marks the turn as `truncated`. Markers that depend on completeness or length are then coded `NA` under the truncation rule in [`battery-v1.md`](battery-v1.md).

---

## 6. Sampling plan

For F and Q (and Q+/Q+pin when enabled):

- 3 independent runs per active probe;
- fresh conversation for every replicate;
- in multi-turn probes, every assistant turn is the model's own natural response, generated in sequence within the same conversation;
- archive with every response:
  - date/time;
  - API endpoint;
  - exact model alias sent and model identifier returned;
  - system fingerprint when returned;
  - card SHA-256;
  - generation parameters;
  - per-turn `finish_reason` and usage.

For P:

- Core C01–C08: 3 fresh-chat replicates each.
- Relational R01–R09: 3 fresh-chat replicates each.
- That makes 51 independent probe chats per full slice, plus cleanup.

Active probes per slice: C01–C08 and R01–R09 (17). E01 runs only after a pre-defined T1 update event (section 3). It is descriptive only and has no T0 baseline.

---

## 7. Probe ordering

Before each slice, generate and archive a randomized run manifest with `tools/make_continuity_manifest.py`.

- Probe order and replicate order are randomized per layer, and the RNG seed is recorded in the manifest.
- Turns inside a multi-turn probe remain fixed.
- R06 is exempt from randomization and always runs last in each layer because of the memory-contamination risk.
- The P layer follows its manifest order manually.

---

## 8. Slice window

All layers of one slice (F, Q and P, plus Q+/Q+pin when enabled) are collected within **72 hours**.

An update event (section 3) inside the window invalidates the slice for cross-layer comparison. In that case the slice is re-run.

---

## 9. Smoke test

The smoke test is **technical, not a pilot**. It checks the API, the returned model metadata, the generation parameters and the runner. It does **not** use battery probes.

- It uses only the synthetic probes in [`smoke-v1.json`](smoke-v1.json):
  - one single-turn call;
  - one two-turn call that checks that the conversation context is carried between turns.
- It runs only on API layers (F and Q; Q+ and Q+pin before their first slice), with the slice label `smoke` and 1 replicate.
- Smoke outputs are archived separately and are never part of T0 or any later slice.
- **The battery is not run on the live API before the freeze.**
- **P is never used for smoke tests or rehearsal.**
- If the smoke test reveals a problem with the configs, parameters or runner, it is fixed before the freeze.

---

## 10. Evaluator-drift control

Raw outputs are the immutable primary record.

Immediate scoring after T0/T0′ may be performed only as **provisional** scoring.

For any longitudinal comparison (for example T0/T0′ against T1):

1. pool all outputs from the compared slices;
2. shuffle them and blind timepoint/condition wherever feasible;
3. score the pooled set in the same evaluation session with the same evaluator version;
4. log evaluator identity/model/version/date and the exact rubric;
5. use that joint rescoring as the comparison dataset.

If two LLM judges are used, both should rescore the pooled comparison set independently. State explicitly that the evaluators are LLMs and that no human validation exists, unless a human rater is actually added.

P may remain partly identifiable because of personal tone and history. This limitation is declared in advance.

If Ray/ChatGPT becomes a tested longitudinal line, Ray/ChatGPT must not judge its own outputs.

---

## 11. Interpretation rules

- **F → Q:** same API model, compact persona card added. Length-related markers are confounded by the card's known compression effect (Case 10) and must be interpreted with that in mind.
- **Q → P** (the main cross-layer contrast in v1): **not** a personalization effect. It combines:
  - the model difference (Flash vs Plus);
  - the consumer-product implementation and possible backend revision;
  - the full canon instead of the compact card;
  - the product system prompt;
  - saved memory;
  - chat-history retrieval and accumulated relationship history.

  Differences must not be attributed to "personalization" alone.
- **Q → Q+** (only when enabled): compact card held fixed, API model/service changes.
- **Q+ → P** (only when enabled): still not a pure personalization contrast.
- **P T0 → T1:** cumulative personal/product trajectory, not a pure model-update effect.
- **R03 and R07** are explicitly layer-sensitive and are not used as direct same-construct F↔P comparisons.
- **R06** probes related but non-identical mechanisms: in the API layers, within-context withdrawal; in P, also product memory.
- **E01** is descriptive only because it has no T0 counterpart.

No "winner" ranking between assistants.

---

## 12. Freeze rule

1. Run the technical API-only smoke test (section 9) and fix anything it reveals.
2. Freeze the battery, rubric, compact Q. card, API configs, P protocol, update-event rules, drift definition and manifest generator in the repository.
3. Record the freeze commit SHA here.
4. Do not change probe wording, marker definitions, scoring rules, generation parameters or update-event rules after T0 starts.

Any later change creates a new battery version rather than silently modifying v1.

**Frozen content commit SHA:** `c3be8a3642fe0aad206a54665f9f9ca2d4dcba6f`  
**Freeze status:** satisfied before T0 collection; later documentation-only status updates do not alter the frozen probe wording, marker definitions, scoring rules, generation parameters or update-event rules.

**Freeze validated by technical smoke:** workflow run `36342083573` on 2026-09-27, artifact `continuity-v1-smoke`, artifact digest `sha256:d35ad9be825fdd335973e4ae3fe348813dbcade29ee4a7c73f1b9cb5a689cf21`.
