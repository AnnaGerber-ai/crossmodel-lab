# Pressure Ladder v4 reproducibility archive

This directory preserves the analysis inputs beyond the temporary GitHub Actions artifact-retention window.

## Files

- `pressure-ladder-v4-confirmatory-main-36834208704.zip` — exact collection artifact from workflow run `36834208704`, artifact ID `11150146210`.
  - SHA-256: `c06a063ba0186565e1f5e21459b2db11a3293e80d76d457a7fa1942236b25234`
  - Contains `main-audit.jsonl`, `main-canonical.jsonl`, `collection-sha256.txt`, `execution-environment.txt`, and `COLLECTION-DISPATCHED`.
- `pressure-ladder-v4-confirmatory-results-2026-10-01.zip` — scoring/results input bundle.
  - SHA-256: `79d11e264c56f450a9872c19fd8fa009b0231eaf36d20c8be7117667da3d6be4`
  - Contains both position score series, both warmth score series, all four attempt logs, blind maps, blind lock, analysis output, and supporting hashes.

The scoring archive was staged as base64 text in the audit-correction PR so GitHub Actions could materialize the binary archive. The preservation workflow also downloaded the exact collection artifact before its 90-day retention expiry, verified both SHA-256 values, committed the binary ZIP files to `main`, and removed the transport-only base64 file.

The frozen runner and manifest remain in the repository. Blind packets can be regenerated deterministically from the archived canonical collection using the frozen packet seeds; the recorded packet and map hashes in the parent results directory provide equality checks.

These archives preserve the original analysis inputs. They do not alter the frozen scores, blind lock, confirmatory analysis, or decision.
