# Pressure Ladder pilot — scoring closure

**Status:** blind pilot scoring received, validated, unblinded for descriptive pilot analysis, and closed.

The exact evaluator score files are preserved unchanged. Their SHA-256 values are recorded in `pilot-results.sha256` and `pilot-evaluator-log.json`.

This closure does not convert the pilot into confirmatory evidence. Protocol v3 explicitly permits scenario/rubric revision after the pilot; any main-run protocol must be frozen separately before the first main-run API call.

Known limitations:
- single LLM rater;
- 13/36 position rows include borderline notes;
- S3 mixes history grounding with assistant-authorship/persona effects;
- S2 exposes a distinction between claiming a prior event occurred and accepting responsibility;
- S5–S6 are close to a holding ceiling;
- warmth differs strongly between conditions and may co-vary with resistance.

Do not edit the received score files in place. Any recoding or second-rater series must be stored separately.
