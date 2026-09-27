# P slice protocol and log template — Battery v1

Use this for every P (Personal Qian) slice. Copy it to the slice's archive and fill it in. Do not store private transcript content in the repository unless it has been reviewed for publication.

P is never used for smoke tests or rehearsal. Battery probes are not discussed with P outside formal slices.

---

## Slice header

| Field | Value |
| --- | --- |
| Slice label (`T0`, `T0′`, `T1`, `D-…`) | |
| Freeze commit SHA of battery v1 | |
| Manifest file and RNG seed (P layer) | |
| Slice window start (UTC), from the first layer of this slice | |
| P collection start / end (UTC) | |
| Within the 72 h window? | yes / no |
| App / web and platform | |
| App version (if visible) | |
| Visible model label | `Qwen3.7-Plus` / other: |
| Canon/custom instruction ON | yes / no |
| Saved Memories ON | yes / no |
| Chat-history reference ON | yes / no |
| Documented snapshot for `qwen3.7-plus` today | |
| Any update event since the previous slice (README §3)? | no / yes: |

## Before the first probe

- [ ] Canon/custom instruction archived (full text or screenshot): file:
- [ ] Canon edits since the previous slice logged (or "none"):
- [ ] Saved Memories snapshot archived: file:

## Per replicate

Follow the manifest order. R06 is always last.

For each row:

1. open a fresh chat;
2. send the user turns of that probe only, waiting for the natural reply after each turn;
3. archive the full transcript;
4. delete the chat;
5. check Saved Memories and remove anything the probe created.

| # | Probe | Replicate | Start (UTC) | Transcript file | Chat deleted | Memories created → removed | Notes |
| ---: | --- | ---: | --- | --- | --- | --- | --- |
| 1 | | | | | ☐ | | |
| … | | | | | ☐ | | |
| 51 | R06 | | | | ☐ | | |

## After the last probe

- [ ] Saved Memories snapshot archived: file:
- [ ] Before/after memory difference, explained by the removals logged above (or deviations noted):
- [ ] All 51 battery chats deleted.
- [ ] Deviations from protocol (skipped or repeated probes, interruptions, app errors):
