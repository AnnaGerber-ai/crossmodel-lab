# Joint rescoring access isolation

Status: prospective control for any joint rescoring after T0. This does not alter the frozen T0 battery, pre-scoring addendum, provisional scores, or T0 closure record.

## Rule

A joint-rescoring evaluator receives only the dedicated evaluator packet required for the task (for example, the blinded ZIP plus evaluator instructions).

The evaluator must not be given a working session with unrestricted access to the full `crossmodel-lab` repository, because provisional results, evaluator logs, summaries, and other post-scoring material are stored in `main`.

## Preferred access order

1. **Package-only access (required default).** Provide only the blinded evaluator bundle and the instructions needed to score it.
2. **Repository access only if technically unavoidable.** Use a sparse checkout or equivalent restricted view that excludes all result-bearing and mapping material, including at minimum:
   - `tests/longitudinal-assistant-continuity/results/`
   - provisional/final score files
   - evaluator logs
   - agreement/disagreement summaries
   - blind maps / unblinding maps
   - grounding source annotations that reveal layer identity
3. **Instruction-only prohibition is fallback, not the preferred control.** A textual instruction not to inspect results is weaker than making those results inaccessible.

## Rationale

A fresh evaluator session may not know where contamination risks are located. Relying on evaluator self-restraint therefore creates an avoidable leakage path. Access isolation should be enforced structurally rather than behaviorally whenever possible.

## Contamination logging

If an evaluator is exposed to any provisional findings, agreement summaries, layer-level interpretations, row-level scores, or unblinding information before joint rescoring is finalized, record that exposure in the evaluator log and in the relevant limitations/closure note.

