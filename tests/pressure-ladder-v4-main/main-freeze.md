# Pressure Ladder v4 — confirmatory main freeze

**Status:** **FROZEN / COLLECTION AUTHORIZED.**

No confirmatory-main API data were collected before this freeze.

- Pre-freeze reviewed implementation head: `b3c4c15173735adfaba8f60b8fb3ef0c093965e9`
- Planned runs: **348** = 300 factual-primary + 48 controls
- Conditions: **174 A / 174 C**
- Manifest SHA-256: `4fe46cd86ec2c4b3706491f5c9793a5b45049315734f0c363db131359f6336ed`
- Position evaluator prompt SHA-256: `2389e899644115179d3341780dc5a61702ac04b13940d3bbad7d50a5b0d7facf`
- Warmth evaluator prompt SHA-256: `4093c903e563af6cbca5e1395b07280d70966bf395607f7341b49ceb6422afdd`
- Full normative checksums: `tests/pressure-ladder-v4-main/freeze-checksums.sha256`

The live collection workflow must verify every frozen checksum before any API call. A checksum mismatch blocks collection.

Design authority:
- `tests/pressure-ladder-v4/confirmatory-main-prereg-v0.2.1.md`
- `tests/pressure-ladder-v4/main-endpoint-censoring-v0.2.1.md`
- `tests/pressure-ladder-v4/main-rater-protocol-v0.2.md`

Implementation authority:
- `tools/pressure_main.py`
- `tests/pressure-ladder-v4-main/backoff-policy-v1.md`
- `tests/pressure-ladder-v4-main/scoring-contract-v1.md`
- `tests/pressure-ladder-v4-main/manifest-main-v1.json`
- `tests/pressure-ladder-v4-main/dependency-freeze.txt`

Any substantive modification to a frozen file creates a new protocol version and requires a new prospective freeze. Do not overwrite this freeze to complete or repair a stopped collection.
