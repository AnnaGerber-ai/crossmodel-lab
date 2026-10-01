# Pressure Ladder v4 — confirmatory main implementation freeze v1.2.1

**Status:** **FROZEN / COLLECTION AUTHORIZED UNDER v1.2.1 ONLY WHEN THIS RECORD AND ITS CHECKSUM SET ARE PRESENT ON `main`.**

This is a prospective implementation-only repair after the first attempted workflow dispatch under v1.2. The study design, manifest, runner, prompts, model settings, scoring rules, retry rules, estimand, analysis and rater protocol are unchanged.

The v1.2 workflow run `36833491711` completed freeze verification, smoke/design checks, dry-run and the non-battery synthetic API preflight, then stopped while attempting to stage the collection sentinel because `runs/` is intentionally ignored by `.gitignore`. The `Run confirmatory main` step was skipped, no battery request was executed, and no `COLLECTION-DISPATCHED` sentinel was committed or pushed. Therefore no confirmatory-main collection dispatch was successfully claimed under v1.2.

v1.2.1 changes only the collection-claim implementation:
- `git add "${SENTINEL}"` → `git add -f "${SENTINEL}"`, allowing the deliberately ignored sentinel path to be staged;
- workflow freeze references and sentinel metadata are advanced to v1.2.1.

A synthetic candidate check verified that the ignored sentinel is stageable with `git add -f`, and the unchanged runner still passes compile, smoke and design checks.

- Prospective implementation head used for candidate validation: `493a743bd1d60d3f769f746d004f5e130e087546`
- Planned runs: **348** = 300 factual-primary + 48 controls
- Conditions: **174 A / 174 C**
- Manifest SHA-256: `4fe46cd86ec2c4b3706491f5c9793a5b45049315734f0c363db131359f6336ed`
- Runner SHA-256: `bb382d60ee9a3a5482e5332ebed5577d5f78eb8112a04d84bdcbea4be5c6868c`
- Collection workflow SHA-256: `115d0fffeb808bc66ed1cd03a71467828b6a8078ebf4ebd72f4b64393ddbc9f9`
- Full normative checksums: `tests/pressure-ladder-v4-main/freeze-checksums-v1.2.1.sha256`

All v1.2 design/implementation authority files remain normative unchanged except `.github/workflows/pressure-ladder-v4-main.yml`, whose checksum is replaced by the v1.2.1 value above. `main-freeze-v1.2.md` and `freeze-checksums-v1.2.sha256` remain provenance only after this freeze.

The live workflow must verify the v1.2.1 checksum set before any API call. The first successfully pushed `runs/pressure-ladder-v4-main/COLLECTION-DISPATCHED` sentinel remains the only authorized confirmatory-main collection dispatch. A pre-claim workflow failure does not constitute a successful dispatch; after a successful claim, the terminal/no-resume/no-top-up/no-replacement rule applies unchanged.

The freeze record itself is an audit/index record and is not part of the normative checksum set. Any later substantive modification to a normative v1.2.1 file requires another prospective implementation freeze.
