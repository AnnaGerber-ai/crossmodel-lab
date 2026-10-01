# Pressure Ladder v4 — confirmatory main implementation freeze v1.2

**Status:** **FROZEN / COLLECTION AUTHORIZED UNDER v1.2 ONLY WHEN THIS RECORD AND ITS CHECKSUM SET ARE PRESENT ON `main`.**

This implementation freeze supersedes v1 and v1.1 before confirmatory-main collection. No confirmatory-main data were collected under earlier implementation freezes. The reviewed study design is unchanged.

External code↔protocol audit verdict before freeze: **`V1.2 IMPLEMENTATION AUDIT PASSED`**.

Two non-blocking audit hardenings were applied before freeze:
- the live collection workflow refuses collection unless `GITHUB_REF == refs/heads/main`;
- request-audit callback execution is outside API exception classification, so an audit-write failure cannot relabel a valid API response as technical NA.

- Prospective normative implementation head: `83bcdcf9a29872fea1d13d5047d13074c767c3e3`
- Planned runs: **348** = 300 factual-primary + 48 controls
- Conditions: **174 A / 174 C**
- Manifest SHA-256: `4fe46cd86ec2c4b3706491f5c9793a5b45049315734f0c363db131359f6336ed`
- Runner SHA-256: `bb382d60ee9a3a5482e5332ebed5577d5f78eb8112a04d84bdcbea4be5c6868c`
- Backoff policy v1.2 SHA-256: `038e0975c6c38333990ea934ba429cc3fa0bf9802be088bd2542ae1eac9fbd7e`
- Collection workflow SHA-256: `7a86150c5b925acc6fee9fbee6ad9fab6c803c7a741cf7cd36e998d1b1b43eeb`
- Full normative checksums: `tests/pressure-ladder-v4-main/freeze-checksums-v1.2.sha256`

Design authority remains:
- `tests/pressure-ladder-v4/confirmatory-main-prereg-v0.2.1.md`
- `tests/pressure-ladder-v4/main-endpoint-censoring-v0.2.1.md`
- `tests/pressure-ladder-v4/main-rater-protocol-v0.2.md`

Implementation authority v1.2 includes:
- `tools/pressure_main.py`
- `tests/pressure-ladder-v4-main/backoff-policy-v1.2.md`
- `tests/pressure-ladder-v4-main/collection-dispatch-policy-v1.2.md`
- `tests/pressure-ladder-v4-main/scoring-contract-v1.2.md`
- `tests/pressure-ladder-v4-main/position-score-schema-v1.json`
- `tests/pressure-ladder-v4-main/warmth-score-schema-v1.json`
- `tests/pressure-ladder-v4-main/rater-failure-schema-v1.json`
- `tests/pressure-ladder-v4-main/rater-attempt-log-schema-v1.json`
- `tests/pressure-ladder-v4-main/rater-metadata-template.json`
- `tests/pressure-ladder-v4-main/dependency-freeze.txt`
- `.github/workflows/pressure-ladder-v4-main.yml`

`backoff-policy-v1.2.md` supersedes `backoff-policy-v1.1.md`. `scoring-contract-v1.2.md` supersedes `scoring-contract-v1.md`. Historical v1/v1.1 files are retained for provenance only and do not authorize collection.

The live workflow verifies every v1.2 checksum before any API call. It performs a non-battery synthetic API preflight, then atomically claims the single authorized collection dispatch on `main` by committing `runs/pressure-ladder-v4-main/COLLECTION-DISPATCHED`. A claimed collection is terminal if stopped; no resume, top-up, replacement, or pooling is permitted.

The temporary PR-only v1.2 candidate/audit CI is not part of the normative freeze and must be removed before merge. Removing that temporary CI file does not alter any checksum in this record.

The freeze record itself is an audit/index record and is not part of the normative checksum set. The freeze commit is the Git commit that first places this record and `freeze-checksums-v1.2.sha256` on `main`.

Any substantive later modification to a normative v1.2 file requires a new prospective implementation freeze.
