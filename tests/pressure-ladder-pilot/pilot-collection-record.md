# Pressure Ladder pilot — collection record

**Status:** raw pilot collection completed; scoring has not started.

## Frozen collection reference

- Pre-registration merge / collection HEAD: `399b311a3b1187ee3288692de2bc33409e3fa009`
- GitHub Actions run: `36701337406`
- Artifact: `pressure-ladder-pilot`, id `11090705626`
- Artifact digest reported by GitHub: `sha256:749d97bfef82f5ce698df65c1b5d49deb72fc953f6c45cb7e97f9733c2f4775b`
- Artifact expiry reported by GitHub: 2026-12-29T10:15:51Z

## Operational validation

The downloaded artifact contains one file, `pilot.jsonl`.

- 36/36 manifest runs are present.
- Conditions are balanced 18 A / 18 C.
- Each of S1–S6 has 6 runs.
- All 36 runs completed with status `ok`.
- All 36 completed on the first recorded run attempt.
- Every completed run contains 4 assistant turns.
- No run contains a `finish_reason=length` truncation.
- The provider-reported model is `qwen-flash-character` on all 144 recorded turns.

No response text was printed during collection or used for this validation.

## Scoring isolation

A blinded evaluator packet was prepared after collection. It contains no condition labels, original run IDs, manifest positions, replicate numbers, or original order metadata. The packet and its private blind map are bound by SHA-256 in `pilot-pre-scoring-checksums.sha256`.

The evaluator bundle is kept outside `main` and is intended for a fresh Claude session with no repository access, as required by `protocol-v3.md`. Raw output and the blind map remain private.

This record is operational/provenance metadata only. It does not contain pilot outcome coding or substantive findings.
