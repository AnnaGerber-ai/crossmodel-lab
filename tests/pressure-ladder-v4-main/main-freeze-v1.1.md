# Pressure Ladder v4 — confirmatory main implementation freeze v1.1

**Status:** **FROZEN / COLLECTION AUTHORIZED UNDER v1.1 ONLY.**

This implementation freeze supersedes implementation freeze v1 (commit `95b5632e94dd715adc6db92a8867f80112d28183`) **before confirmatory-main collection**. The reviewed study design is unchanged.

Reason for v1.1: close the final B1 implementation path so an earlier empty/content-filter/final-4xx event can never be indirectly re-sampled by a later whole-run retry. The client backoff policy is also explicitly included in the normative freeze bundle.

- Pre-freeze v1.1 implementation head: `b572a684e1f9c38ee1347c31d065d4d2c4142ba1`
- Freeze commit: `26e78c3fa7d43c15a6dec95b81a05be07c096b44`
- Planned runs: **348** = 300 factual-primary + 48 controls
- Conditions: **174 A / 174 C**
- Manifest SHA-256: `4fe46cd86ec2c4b3706491f5c9793a5b45049315734f0c363db131359f6336ed`
- Runner SHA-256: `ec8265c9c6423456e450840bd5ab5068865699d037767211c4ff0277b76e9ce7`
- Backoff policy v1.1 SHA-256: `c665d55c4550b495afc8e8f9b7abb03ab206629d370cb75b4214607696f005c9`
- Full normative checksums: `tests/pressure-ladder-v4-main/freeze-checksums-v1.1.sha256`

The collection workflow requires this v1.1 freeze and verifies every v1.1 checksum before any API call. A mismatch blocks collection.

Design authority remains:
- `tests/pressure-ladder-v4/confirmatory-main-prereg-v0.2.1.md`
- `tests/pressure-ladder-v4/main-endpoint-censoring-v0.2.1.md`
- `tests/pressure-ladder-v4/main-rater-protocol-v0.2.md`

Implementation authority:
- `tools/pressure_main.py`
- `tests/pressure-ladder-v4-main/backoff-policy-v1.1.md`
- `tests/pressure-ladder-v4-main/scoring-contract-v1.md`
- `tests/pressure-ladder-v4-main/manifest-main-v1.json`
- `tests/pressure-ladder-v4-main/dependency-freeze.txt`
- `.github/workflows/pressure-ladder-v4-main.yml`

Historical v1 freeze/checksum files are retained for provenance but are not authorization for collection.

The v1.1 freeze record itself is an audit/index record and is not part of the normative checksum set. Its metadata-only repair after the freeze does not modify any frozen design or implementation file.

Any substantive later modification to a v1.1 frozen file requires a new prospective implementation freeze. A stopped collection may not be repaired or completed by overwriting this freeze.
