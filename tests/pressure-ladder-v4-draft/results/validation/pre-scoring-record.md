# Pressure Ladder v4 validation — pre-scoring record

**Status:** collection complete; blinded packets fixed; scoring not yet started.

## Collection provenance

- Validation freeze merge commit: `e05eb0be1e9e0b09d4ebb73f4051d26ac07ea255`
- GitHub Actions run: `36739356629`
- Workflow conclusion: `success`
- Raw artifact: `pressure-ladder-v4-validation`, artifact id `11109886835`
- GitHub artifact digest: `sha256:167700b34e7dd481d553cbcfb302cf7cb2edc841246425f8e5806b88283b9468`
- Artifact expiry reported by GitHub: `2026-12-29T15:47:06Z`

## Structural validation

No response text was inspected for these checks.

- 84/84 planned runs present.
- 42 A / 42 C.
- 12 runs per scenario across S2, S3, S4, S7, S8, S9, S10.
- 84/84 runs status `ok`.
- All 84 completed on the first recorded attempt.
- Four assistant turns per run; 336 assistant turns total.
- Zero truncated turns.
- All turn finish reasons are `stop`.
- Requested model is `qwen-flash-character` for all runs.
- Frozen scenario hash in all raw rows: `c236769cd5cae00df5fc7b7ca1b16668de93d1477d9348516c75d1ec06167e5f`.
- Manifest seed in all raw rows: `2026093001`.
- C card hash: `f5b74bc1ea1c41075bed10fe7db4adec204efea4ab0cf07fa28f526b42ffe0d8`; A has no card hash.

## Blind packets

A new blind-packet shuffle was fixed before scoring with seed `7848351700762168919`.

- 84 rows in position packet.
- 84 rows in warmth packet.
- 0 packet exclusions.
- 29 response-initial Q-signature normalization events under the frozen rule.
- Position and warmth packets use the same blind IDs/shuffle.
- Technical truncation metadata is present only in the position packet.
- The blind map remains private and must not be provided to raters.

Two evaluator bundle types were prepared:
- position: packet + frozen position instructions + position schema;
- warmth: packet + frozen warmth instructions + warmth schema.

Each evaluator receives only the relevant bundle in a fresh isolated session. Position requires two different model families; warmth requires two separate fresh sessions from different model families. No rater receives the repository, blind map, condition labels, prior pilot, or other rater's scores.

Exact SHA-256 values are recorded in `validation-pre-scoring-checksums.sha256`.

No scoring may begin before this record is committed.
