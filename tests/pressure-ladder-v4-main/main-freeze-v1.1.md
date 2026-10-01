# Pressure Ladder v4 — confirmatory main implementation freeze v1.1

**Status:** **FROZEN / COLLECTION AUTHORIZED UNDER v1.1 ONLY.**

This implementation freeze supersedes implementation freeze v1 (commit ) **before confirmatory-main collection**. The reviewed study design is unchanged.

Reason for v1.1: close the final B1 implementation path so an earlier empty/content-filter/final-4xx event can never be indirectly re-sampled by a later whole-run retry. The client backoff policy is also explicitly included in the normative freeze bundle.

- Pre-freeze v1.1 implementation head: 
- Planned runs: **348** = 300 factual-primary + 48 controls
- Conditions: **174 A / 174 C**
- Manifest SHA-256: 
- Runner SHA-256: 
- Backoff policy v1.1 SHA-256: 
- Full normative checksums: 

The collection workflow requires this v1.1 freeze and verifies every v1.1 checksum before any API call. A mismatch blocks collection.

Design authority remains:
- 
- 
- 

Implementation authority:
- 
- 
- 
- 
- 
- 

Historical v1 freeze/checksum files are retained for provenance but are not authorization for collection.

Any substantive later modification to a v1.1 frozen file requires a new prospective implementation freeze. A stopped collection may not be repaired or completed by overwriting this freeze.
