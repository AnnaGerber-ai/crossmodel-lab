# Pressure Ladder v4 validation freeze

**Status:** validation collection authorized after merge to `main`.

- Reviewed pre-freeze head: `338b482f3440d745d5173f5ecceb3a53ca7d8b75`
- Manifest seed: `2026093001`
- Planned runs: 84
- Conditions: 42 A / 42 C
- Validation scenarios: S2, S3, S4, S7, S8, S9, S10
- Primary factual scenarios: S3, S4, S7, S8, S9, S10
- Every scenario is fully crossed with all six P1/P2/P3 orders per condition.
- Frozen scenarios SHA-256: `c236769cd5cae00df5fc7b7ca1b16668de93d1477d9348516c75d1ec06167e5f`
- Manifest path: `tests/pressure-ladder-v4-draft/manifest-validation.json`
- Workflow path: `.github/workflows/pressure-ladder-v4-validation.yml`

The final blocking review reported no blocking problems on the reviewed pre-freeze head. No validation API call had been made before this freeze.

The validation is a measurement/codability exercise, not a confirmatory effect test. Scenario decisions remain condition-blind until the preregistered validation decision record is locked.
