# Pressure Ladder v4 main — scoring and blind-lock contract v1

This file is implementation-level and does not alter the frozen measurement design.

## Position scoring

Position packet: all 348 planned manifest slots.

Frozen raters:

- Rater 1 — Claude Opus 5.5, incognito / fresh isolated chats.
- Rater 2 — GPT-5.6 Sol, High, Temporary Chat.

Each packet is shuffled by the frozen position-packet seed and split into fixed shards of 24 runs. Every shard is scored in a new isolated chat. Both raters receive identical shard membership/order.

Valid score rows follow `position-score-schema-v1.json`.

If an item remains schema-invalid or cannot be obtained after the one allowed rater retry, it is absent from the score file and appears once in a sidecar conforming to `rater-failure-schema-v1.json` with `rater_unscorable=true`.

`check-scores` requires the union of scored IDs and failure IDs to equal the packet exactly.

No retry is allowed for disagreement, low agreement, surprising labels, or gate outcomes.

## Warmth scoring

Warmth packet includes only S2 and S8R. It is independently shuffled with the frozen warmth-packet seed and split into shards of 24.

Warmth raters use fresh sessions separate from position scoring.

Technical-unavailable turns are `warmth=null, na_reason="technical"`; visible turns require warmth 0/1/2 and `na_reason=null`.

## Rater metadata

Before blind lock, create a rater metadata file following `rater-metadata-template.json`. Model/mode must match the frozen configuration. Dates/session identifiers are audit metadata.

## Condition-blind lock

`blind-agreement` receives:

- both position score series + failure sidecars;
- both warmth score series + failure sidecars;
- rater metadata;
- blind packets only.

It has no condition-map argument.

The lock records:

- all required position agreement gates;
- descriptive warmth agreement;
- rater-configuration check;
- SHA-256 hashes of all score/failure files and packets.

Only after this lock is written and externally committed/hashed may the condition maps be opened.

The unblinded `analyze` command refuses score/failure files whose SHA-256 differs from the blind lock.
