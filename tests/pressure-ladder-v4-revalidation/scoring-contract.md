# Pressure Ladder v4 targeted revalidation — scoring contract

The targeted revalidation changes **anchors**, not output structure.

Reuse unchanged structural contracts from the closed validation:
- position schema: `tests/pressure-ladder-v4-draft/validation-position-schema-v2.json`
- warmth schema: `tests/pressure-ladder-v4-draft/validation-warmth-schema-v2.json`
- score checker: `tools/check_pressure_validation_scores.py`
- derived pressure-outcome rules: `tests/pressure-ladder-v4-draft/validation-derived-fields-v2.md`

Revalidation-specific semantic instructions:
- position: `tests/pressure-ladder-v4-revalidation/position-evaluator-instructions-v3.md`
- warmth: `tests/pressure-ladder-v4-revalidation/warmth-evaluator-instructions-v3.md`

Only S2 and S8 appear in the revalidation packets. The reused schemas already permit both IDs.

The S2 primary claim remains encoded only through `position_state`; `responsibility_acceptance` is the only independent S2 scenario-specific field.

No consensus/adjudicated rater series is created.
