# Pressure Ladder v4 targeted revalidation freeze

**Status:** targeted revalidation collection authorized after this freeze is merged to `main`.

- Reviewed pre-freeze head: `057d6fae3409417c3c83e3eeeb2b09c89faf2575`
- Manifest seed: `2026093002`
- Planned runs: 24
- Conditions: 12 A / 12 C
- Scenarios: S2 and revised S8
- Each scenario × condition receives all six P1/P2/P3 orders exactly once.
- Frozen scenarios SHA-256: `5a7664eca90e29afdcc8f5a76c187b9ec2057024eeaf442c3528bb3b77b98823`
- Manifest: `tests/pressure-ladder-v4-revalidation/manifest-revalidation.json`
- Workflow: `.github/workflows/pressure-ladder-v4-revalidation.yml`

Blocking review required five fixes before freeze; all five were implemented prospectively:
1. restored validated v2 general position rules;
2. resolved S2 content-denial vs responsibility coding;
3. fixed the bare "Понимаю" warmth boundary;
4. removed carry-forward inflation from R2/R3 agreement gates;
5. scoped warmth validation to S2/S8-type contexts only.

No revalidation API collection occurred before this freeze. The revised S8 is a new replacement item and must not be compared directly to the old S8 as a repeated measure.
