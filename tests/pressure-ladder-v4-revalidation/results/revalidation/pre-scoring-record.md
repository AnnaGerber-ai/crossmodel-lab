# Pressure Ladder v4 targeted revalidation — pre-scoring record

**Status:** raw collection complete; blind packets fixed; no scoring started.

## Collection provenance

- Workflow run: `36757079420`
- Workflow: `Pressure Ladder v4 targeted revalidation`
- Head SHA: `a6355cb36c7a76dcef7d07662984700185001928`
- Artifact id: `11116752381`
- Artifact name: `pressure-ladder-v4-revalidation`
- GitHub artifact digest: `sha256:6de9b87a4e253a9abf1df1be07bdef2ae37628399858428b79eefe16339749c6`
- Downloaded ZIP SHA-256: `6de9b87a4e253a9abf1df1be07bdef2ae37628399858428b79eefe16339749c6`
- Raw JSONL SHA-256: `ffe599cca908872cba6a6254d8413e23c8d89a6879f6cac96f2d5f9ac82e35bf`

## Structural validation

- 24/24 planned runs present
- 12 A / 12 C
- S2: 12 runs; S8: 12 runs
- all 24 runs status `ok`
- all 24 runs completed on first attempt
- 4 assistant turns per run = 96 assistant turns
- provider model: `qwen-flash-character` on all 96 turns
- finish reason `stop` on all 96 turns
- no truncation

No response content was inspected during this structural check.

## Blind packet fixation

- Packet seed: `4488599196449214454`
- Position packet rows: 24
- Warmth packet rows: 24
- Packet exclusions: 0
- Response-initial Q-signature normalization events: 4
- Position packet SHA-256: `d5006c42deb9c132799294b1e7d28ea854da9e964baa164c23aefc609ed71e49`
- Warmth packet SHA-256: `0985f89545c43538102c585541413f6773a1e5ec377f3a2d96aa2ff3290a3bc2`
- Blind map SHA-256: `fbe9ffcf3eecf341d2bbbece41412fd4f638a9b0618d2bb7fcec394708c94f2a`
- Exclusions SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`

The blind map remains private. A/C labels must remain unopened until condition-blind revalidation decisions are locked.
