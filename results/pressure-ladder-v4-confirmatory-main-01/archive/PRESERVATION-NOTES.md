# Preservation notes

Housekeeping notes added after the archive was preserved. `README.md` in this
directory is covered by `../integrity.sha256` and is left unchanged; these notes
are not part of the frozen result and change no score, lock, analysis or decision.

## Preservation trail

1. `9a57774` staged `scoring-results.zip.b64`. The file was truncated in transit
   (an `[... ELLIPSIZATION ...]` marker at character 10 000), so workflow run
   `36922603959` failed at `base64 -d` before writing anything.
2. `8ee7043` restaged the base64 from the original ZIP (94 388 characters; decodes
   to SHA-256 `79d11e264c56f450a9872c19fd8fa009b0231eaf36d20c8be7117667da3d6be4`).
3. Workflow run `36964002751` succeeded on `8ee7043`, verified both SHA-256 values
   and committed `c8a844b`: both ZIP files added, the transport-only base64 removed.

The collection ZIP is bound to run `36834208704` by GitHub itself: artifact
`11150146210` belongs to that run (head `dd7285d`) and its recorded digest is
`sha256:c06a063ba0186565e1f5e21459b2db11a3293e80d76d457a7fa1942236b25234`.

The one-shot preservation workflow was removed after it completed. The source
artifact expires on 2026-12-30, so the workflow could not be rerun after that date anyway.

## Path difference in `rater-packet-hashes.txt`

The copy inside `pressure-ladder-v4-confirmatory-results-2026-10-01.zip` lists
packet files as `/tmp/packets/<name>`. The copy in the parent results directory
lists bare `<name>`. The three SHA-256 values are identical; only the path prefix differs.

## Coverage of the ZIP hashes

Every score file, attempt log, blind map, the blind lock, the unblind verification,
the confirmatory analysis and the rater metadata inside the scoring ZIP match SHA-256
values recorded elsewhere in the repository. `RESULTS_SUMMARY.md`,
`mechanical-validation.json` and the two `.sha256` sidecars are bound only by the
outer ZIP hash. In the collection ZIP, `execution-environment.txt` and
`collection-sha256.txt` are bound only by the artifact digest. `COLLECTION-DISPATCHED`
is byte-identical to `runs/pressure-ladder-v4-main/COLLECTION-DISPATCHED`.
