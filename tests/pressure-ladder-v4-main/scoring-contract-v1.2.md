# Pressure Ladder v4 main — scoring and blind-lock contract v1.2

This implementation contract closes the v1.1 code-audit gaps without changing the frozen measurement design.

## Frozen JSON schemas are normative

Final position score rows must validate against `position-score-schema-v1.json`.
Final warmth score rows must validate against `warmth-score-schema-v1.json`.
Rater failure sidecars must validate against `rater-failure-schema-v1.json`.

`tools/pressure_main.py check-scores` and `blind-agreement` apply Draft 2020-12 validation through frozen `jsonschema==4.26.0`, then apply the additional cross-row/carry-forward/technical-turn invariants.

The union of JSON-Schema validation and procedural invariants is the sole definition of schema/process validity for retry eligibility.

## Attempt logs

Every rater series has a required attempt log conforming to `rater-attempt-log-schema-v1.json`.

For every blind ID:
- attempt numbering is exactly `[1]` or `[1,2]`;
- a second attempt is allowed only after `schema_invalid`, `transport_failure`, `ui_failure`, or `missing`;
- a final scored row must end in `schema_valid`;
- a `rater_unscorable` sidecar row requires exactly two failed attempts;
- schema-valid/schema-invalid attempts carry a SHA-256 of the raw rater payload.

The condition-blind lock hashes all four attempt-log files in addition to score/failure files. The unblinded analyzer verifies those hashes before analysis.

No retry is allowed because of disagreement, low agreement, surprising labels, condition direction, or gate outcomes.

## Position versus warmth configuration

The blind lock records:
- `position_rater_configuration_pass`;
- `warmth_rater_configuration_pass`.

Only the position-rater configuration participates in the primary confirmatory integrity decision. Warmth configuration is reported separately and cannot make the primary result INDETERMINATE.

## Isolation and sharding

Rater identities, modes, packet seeds, fixed shard size 24, fresh-session-per-shard rule, no consensus/adjudication rule, and condition-blind custody remain exactly as frozen in `main-rater-protocol-v0.2.md`.
