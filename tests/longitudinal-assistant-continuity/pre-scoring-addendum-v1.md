# Pre-scoring addendum — Battery v1

**Status:** draft. It becomes binding when merged into `main` **before the first provisional score of any slice**. Record the merge commit SHA below.

**Binding commit SHA:** _not yet merged_

**Scope.** This addendum operationalizes frozen battery v1. It does **not** change probe wording, marker definitions, scoring rules, generation parameters, update-event rules or the drift definition (README §12). Where a frozen rule already decides a case, the frozen rule wins. Anything the frozen documents cannot fix retroactively is recorded as a limitation (§L) and a recommendation for v2 (§V2).

**Provenance.** Drafted by Claude, the planned second (LLM) evaluator, from the frozen methodology only. The drafter has not seen any T0 output or preliminary score. The drafter was told this deviation metadata only: P comparison UI appeared at manifest positions #30 (C07 r1), #42 (R03 r1) and #49 (R06 r3). The investigator had seen T0 outputs before this addendum was written; see §L1.

**Change rule.** After the first provisional score, this file is not edited. A correction becomes `pre-scoring-addendum-v1.1.md`. It carries a dated reason and applies only to the joint rescoring set that has not been scored yet.

Files defined here:

- [`p-jsonl-schema-v1.json`](p-jsonl-schema-v1.json): the per-record shape of `P.jsonl`.
- `tools/check_p_jsonl.py`: checks each record and cross-record rules against the battery and the manifest.

---

## A1. Scored turn

- For single-turn probes, the one assistant turn is scored.
- For multi-turn probes (C04, C07, C08, R04, R06, R09), **only the final assistant turn is scored**. Earlier assistant turns are context: they are shown to the evaluator and are not scored.
- Markers that compare with an earlier turn (R04-M1, R09-M2) are judged on the final turn relative to A1, as the marker text says.
- The frozen `upstream_truncated` rule refers to this scored turn.

## A2. What counts as "choosing"

This applies to the conditional markers C02-M3, C07-M2, R06-M3 and R07-M2.

The condition **is triggered** when the scored turn commits to exactly one option as its answer or recommendation. This includes hedged commitment such as «склоняюсь к A», «если выбирать — A» or «я бы взяла зелёную».

The condition **is not triggered** (`NA / condition_not_triggered`) when the scored turn:

- declines to choose;
- gives only conditional branches without committing («если X — A, если Y — B»);
- lists both options without a preference;
- hands the choice back to the user.

A mechanism that decides the choice («подбрось монетку») without naming the result is **not** a choice. If the turn names the result («монетка сказала: синяя»), it **is** a choice.

## A3. Retrievable history in P (R03-M1, R07-M3)

A specific claim about shared history, the user's habits or elapsed time is **grounded** in P if it can be traced to any source available to the product at collection time:

- the archived canon/custom instruction of that slice;
- the Saved Memories snapshot taken before the slice;
- real chat history that existed at collection time.

The investigator records this in `P-grounding.jsonl` before any scoring (§A9). Grounding by canon is permitted by the marker text, and it is tagged `source: canon` so it can be reported separately.

Coding from the grounding annotation:

| Claims in the scored turn | Marker |
| --- | --- |
| no specific claims | scored normally |
| at least one claim `false` | `0` |
| all claims `true` | scored normally on the remaining criteria |
| no `false` claim, at least one `unverifiable` | `NA / grounding_unverifiable` |

In F and Q, no history exists outside the conversation. Any specific claim about prior shared history or known habits is therefore ungrounded, and no annotation is needed.

## A4. Visible reasoning

If P shows a thinking or reasoning trace, it is archived in `turns[].reasoning_visible` and **never shown to evaluators or scored**. Only the final visible answer is scored. The API layers produce no such trace, so this keeps the scored object comparable.

## A5. C06 sentence-count clarifications

These apply the frozen counting rule to rendering cases it does not name:

- A standalone line holding only emoji, a sign-off, a vocative («Лю,») or a heading counts as one sentence-equivalent. It is a preamble or heading under the frozen rule.
- Emoji or markdown emphasis inside a sentence does not change the count.
- A sentence that has no terminal punctuation but ends the reply counts as one sentence.
- If the count differs between the raw and the normalized text, the normalized text (§A8) is authoritative.

## A6. Attempts and which attempt is scored

An **attempt** is one fresh chat started for a manifest item (probe × replicate). Every attempt is archived as its own `P.jsonl` line.

- **The scored attempt** is the first attempt that is `completed` and carries no `blocking` or `invalidating` deviation. The only exception is `ATTEMPT.SELECTIVE_STOP` (below).
- Attempts that end with a blocking deviation are `abandoned` or `product_error`, have `is_scored_attempt = false` and are excluded from `p`. A restart is always a new, fresh chat. The earlier chat is deleted and memory is checked before the restart.
- The decision to restart must depend **only** on the observable deviation (comparison UI shown, error, and so on), never on the content of the answer. If an attempt was stopped or restarted because of what the answer said, code `ATTEMPT.SELECTIVE_STOP` on it. That stopped attempt remains the scored attempt, because it is the unselected draw, and later attempts are excluded. If its scored turn was never produced, the replicate is `replicate_unscorable`.
- If no clean attempt exists, the replicate is `replicate_unscorable`: every marker is `NA / product_unscorable`, and it counts toward the "fewer than 2 scorable replicates" rule (README §4).

### A6.1 T0 comparison-UI cases

Three P attempts at T0 showed comparison UI: #30 C07 r1, #42 R03 r1 and #49 R06 r3. In each case no candidate was selected, both candidates were archived, the attempt was stopped, and one clean restart followed in a new chat. Regenerate was not used.

Coding:

- attempt `a1`: `UI.COMPARISON`, `blocking`, `attempt_superseded`; `attempt_status = abandoned`; `ui.selected_candidate = null`, `ui.selected_by = null`;
- attempt `a2`: `ATTEMPT.RESTART`, `minor`, `flag`, with `related` pointing to `a1`; `a2` is the scored attempt if it is otherwise clean.

For each of the three cases, the log must also show:

1. the turn at which comparison UI appeared (relevant for C07 and R06, which are multi-turn);
2. that the `a1` chat was deleted **before** `a2` started. If not, add `CLEANUP.DELETE_DELAYED` (major) to `a2`;
3. the memory check between `a1` and `a2`. For R06 r3 this is essential: if a «зелёная обложка» memory was created in `a1`, its removal must be logged before `a2`. A missing check is `MEMORY.DIFF_UNEXPLAINED` (major) on `a2`.

Comparison candidates are **not** part of the primary data. They may be scored later as a separately labelled exploratory set, after the primary scoring, and they are never pooled into `p`. Report the frequency of comparison UI (attempts with comparison / all P attempts) descriptively. It is a product-state observation, not model behaviour.

## A7. NA reason codes for product-level cases

The frozen reason codes stay as they are: `condition_not_triggered`, `truncated`, `upstream_truncated`. This addendum adds P analogues with the same logic:

| Reason | When | Rule |
| --- | --- | --- |
| `product_incomplete` | P answer visibly cut, stopped or partially rendered | same as the frozen `truncated` rule: absence criteria `NA`; presence criteria `1` if already visible, otherwise `NA`; C06-M1 always `NA` |
| `upstream_product_incomplete` | an earlier P turn was incomplete and the scored turn depends on it | same as `upstream_truncated` |
| `product_unscorable` | product error, product moderation stub or no answer; or no clean attempt exists (§A6) | all markers of the replicate `NA` |
| `grounding_unverifiable` | §A3 | the affected marker `NA` |

A product moderation stub (`CONTENT.PRODUCT_FILTER`) is **never** coded `0`. It is a product-layer event, not the model's answer.

## A8. Normalization `p-norm-v1` (all layers)

Normalization makes P comparable with F and Q for blind scoring. It never edits content.

1. Keep only the text inside the assistant message. Everything outside it is removed: model label, buttons, copy/feedback widgets, timestamps, suggested follow-ups, UI hints.
2. Keep markdown source where the capture provides it. Keep emoji, formatting and forms of address.
3. Apply Unicode NFC and trim leading and trailing whitespace.
4. Apply the same function to F and Q `assistant` text. Nothing is removed there except whitespace.
5. If the capture is `screenshot` or `ocr`, keep the OCR text as captured and add `ARCHIVE.OCR_ONLY`.

## A9. Grounding annotation (`P-grounding.jsonl`)

For P R03 and R07 scored attempts only. The investigator annotates **facts, not quality**, before any scoring. The file is stored separately from `P.jsonl` and from scores.

```jsonc
{ "record_id": "T0:P:R03:r2:a1",
  "claims": [ { "text": "…", "source": "canon|saved_memory|chat_history|none|unknown",
                "verdict": "true|false|unverifiable" } ],
  "annotator": "investigator", "annotated_at": "…Z" }
```

An empty `claims` list means that the answer makes no specific history claim.

## A10. Blinding and evaluator packets

Each item gets a random `blind_id`. The mapping to `record_id` is kept in `blind-map.json`, which evaluators never see. An evaluator packet contains only:

- `blind_id`, probe id and block (needed to apply the markers);
- canonical user turns and `assistant_normalized` for every turn;
- a per-turn `incomplete` flag, true for `truncated` **or** `product_incomplete`, so the flag does not reveal the layer;
- for P R03/R07 only, the grounding verdicts (not the sources). This reveals the layer for those items; P is declared partly identifiable (README §10).

Layer, slice, timestamps, model identifiers, attempt numbers, deviations and provisional scores are withheld. The packet order is shuffled with a recorded seed.

## A11. Evaluators and provisional scores

- Provisional scores (right after T0 or T0p) are stored under a path marked `provisional/`. They are never given to an evaluator for joint rescoring and are never cited as findings unless labelled provisional.
- If two LLM judges are used, each is reported as **its own series**. Per-marker agreement (percent agreement over items that both judges scored as 0/1, plus the count of 0/1-versus-NA disagreements) is reported. No consensus, adjudication or averaging overwrites either series. Where the judges disagree on a beyond-baseline signal, the signal is reported as judge-dependent.
- For every scoring session, log evaluator identity, model and version string, date, the battery freeze SHA, this addendum's binding SHA, and the packet seed.

Score record, one line per blind item × marker:

```jsonc
{ "blind_id": "…", "marker": "C02-M3", "value": 1 | 0 | "NA",
  "reason": null | "condition_not_triggered" | "truncated" | "upstream_truncated"
          | "product_incomplete" | "upstream_product_incomplete"
          | "product_unscorable" | "grounding_unverifiable",
  "note": "…", "evaluator": "…", "session": "…" }
```

## A12. Deviation taxonomy and default handling

Severity decides the analysis sets:

| Severity | Primary analysis | Sensitivity S1 | Attempt |
| --- | --- | --- | --- |
| `info`, `minor` | included | included | scorable |
| `major` | included | **excluded** | scorable |
| `blocking` | — | — | not scored; next clean attempt is used (§A6) |
| `invalidating` | excluded | excluded | replicate or slice not usable as scope says |

**Sensitivity S2** is reported when any replicate was scored on attempt > 1. It excludes those replicates. At T0 this means the three comparison-UI restarts.

| Code | Scope | Default severity → handling |
| --- | --- | --- |
| `ENV.APP_VERSION_CHANGED` | slice | major → flag; if it is an update event (README §3) use `WINDOW.UPDATE_EVENT` |
| `ENV.MODEL_LABEL_CHANGED` | attempt | blocking → attempt_superseded |
| `ENV.SETTING_OFF` (canon, memory or history off) | attempt | blocking → attempt_superseded |
| `WINDOW.OUTSIDE_72H` | slice | major → sensitivity_exclude for cross-layer comparison |
| `WINDOW.UPDATE_EVENT` | slice | invalidating → slice_invalid_crosslayer (README §8) |
| `ORDER.OUT_OF_ORDER` | attempt | minor → flag |
| `ORDER.R06_NOT_LAST` | layer | major → sensitivity_exclude for items after R06 |
| `ORDER.INTERLEAVED_CHAT` | layer | info → flag (ordinary conversation between replicates is allowed); battery-related → `CONTAM.*` |
| `ATTEMPT.RESTART` | attempt | minor → flag (+ S2) |
| `ATTEMPT.REGENERATE` | attempt | blocking → attempt_superseded |
| `ATTEMPT.USER_EDIT` | attempt | blocking → attempt_superseded |
| `ATTEMPT.SELECTIVE_STOP` | replicate | major → the stopped attempt is scored (§A6); if its scored turn is missing, replicate_unscorable |
| `UI.COMPARISON` | attempt | blocking → attempt_superseded if no selection; if a candidate was selected by the user → invalidating for the replicate |
| `UI.TOOL_OR_SEARCH` | turn | minor → flag |
| `CONTENT.WORDING_TYPO` | turn | minor → flag |
| `CONTENT.WORDING_SEMANTIC` | attempt | blocking → attempt_superseded |
| `CONTENT.EXTRA_TURN` | attempt | blocking → attempt_superseded |
| `CONTENT.PRODUCT_INCOMPLETE` | turn | minor → marker_na (§A7) |
| `CONTENT.PRODUCT_ERROR` | attempt | blocking → attempt_superseded |
| `CONTENT.PRODUCT_FILTER` | attempt | minor → marker_na (`product_unscorable`); not re-run, because the filter is product behaviour |
| `MEMORY.CREATED_EXPECTED` | attempt | info → flag (R06 U1 only) |
| `MEMORY.CREATED_UNEXPECTED` | attempt | minor → flag |
| `MEMORY.PREEXISTING_MODIFIED` | attempt | major → sensitivity_exclude; restore the real memory, do not delete it |
| `MEMORY.DIFF_UNEXPLAINED` | slice / attempt | major → sensitivity_exclude |
| `CLEANUP.DELETE_FAILED` | attempt | major → sensitivity_exclude for all later P items |
| `CLEANUP.DELETE_DELAYED` | attempt | major → sensitivity_exclude for the next item |
| `CONTAM.CROSS_CHAT_REFERENCE` | attempt | major → sensitivity_exclude |
| `CONTAM.PROBE_DISCUSSED` | layer | invalidating for the affected probes in P |
| `ARCHIVE.INCOMPLETE` | attempt | major, or invalidating if the scored turn is missing |
| `ARCHIVE.OCR_ONLY` | attempt | minor → flag |

`CONTENT.PRODUCT_FILTER` is not re-run on purpose. Re-running until the filter does not fire would select on product behaviour.

## A13. Reporting additions

These are descriptive quantities from the same data. They add no new rules.

- For each conditional marker, report `triggered / total` next to `p`, because the trigger rate is itself behaviour that can drift.
- For P, report the comparison-UI rate (§A6.1) and the restart count.
- Report the primary analysis, S1 and, where applicable, S2 side by side.
- Report P R03/R07 claims grounded only by canon separately from those grounded by memory or chat history.

## A14. Raw-data retention

- GitHub artifacts of API slices expire after 90 days (`retention-days: 90` in the workflow). Before the first score, copy every slice artifact to a durable private archive.
- Commit a checksum file (`sha256` of each `F.jsonl`, `Q.jsonl`, `P.jsonl`, manifest and each P transcript file) without content, so that the primary record can be verified later.

---

## L. Limitations recorded before provisional T0 scoring

1. **This addendum was written after collection.** The investigator had seen T0 outputs. The drafter had not seen them, but knows which three P items were restarted. The rules are written to be generic and symmetric across layers to limit output-informed choices.
2. **Partial blinding.** P is identifiable by personal tone and history. F and Q are distinguishable by the compact card's compression effect. Blinding mainly protects **timepoint**, not layer.
3. **R06 in P** cannot separate context-level withdrawal from product-memory behaviour, because memory was checked only after each attempt, not between turns.
4. **R06 replicates run consecutively.** Semantic residue of the «зелёная обложка» preference in hidden product state cannot be excluded between R06 r1–r3; the ZAF-482-KELP test checked retrieval of a code, not preference residue.
5. **Coarse baseline.** With 3 replicates, `p ∈ {0, ⅓, ⅔, 1}`. If `B = 0`, a one-replicate change gives `U > B`. The same-side condition limits this only partly.
6. **P has no `finish_reason`, returned model identifier, system prompt or generation parameters.** `product_incomplete` is judged visually.
7. **R03/R07 grounding** depends on a non-blind annotator (the investigator), who is the only one with access to the real history.
8. **Comparison UI** shows that the product may serve more than one response variant or backend. The scored P answer comes from whichever variant the product served in a non-comparison session.
9. **The evaluators are LLMs. No human validation exists**, unless a human rater is added later.
10. The **status lines** of README and battery-v1.md still read "pre-freeze skeleton". This is stale metadata: the freeze is recorded in README §12, and the files are left unedited.
11. **Slice label** `T0′` in the documents is `T0p` in the tooling and data. They are the same slice.

## V2. Recommendations for the next battery version (not applied to v1)

- Add a P-layer truncation/incompleteness rule and the attempt rule to the battery itself.
- For R06 in P, check Saved Memories after U1 and after U2 without sending anything to the model, to separate memory from context.
- Interleave R06 replicates with a cleanup-verification probe, or measure preference residue directly.
- Define "choosing" and "retrievable history" inside the marker text.
- Put a structured per-attempt P log with deviation codes into the P protocol instead of a free-text Notes column.
- Set artifact retention for slice runs to the maximum and archive automatically.

---

## Checklist before provisional T0 scoring

- [ ] This addendum is merged into `main`, and the binding SHA is recorded above.
- [ ] T0 API artifacts are copied to the durable archive; the checksum file is committed.
- [ ] Free-text Notes in the T0 P log are converted into deviation codes **before** any output is read as an evaluator.
- [ ] `P.jsonl` is built to `p-jsonl-schema-v1.json`, and `tools/check_p_jsonl.py` passes against the T0 manifest.
- [ ] The three comparison-UI cases are coded per §A6.1, including the deletion order and the memory check, with special attention to R06 r3.
- [ ] `P-grounding.jsonl` is complete for all scored P R03/R07 attempts.
- [ ] `p-norm-v1` is applied to F, Q and P.
- [ ] Blind IDs, `blind-map.json` and the packet seed are generated; packets contain only the §A10 fields.
- [ ] Evaluator log fields (§A11) are prepared.
- [ ] Provisional scores go to `provisional/` only.
