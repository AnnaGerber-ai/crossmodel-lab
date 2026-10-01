# Pressure Ladder v4 main — one-time collection dispatch policy v1.2

This is implementation-level enforcement of the frozen no-resume/no-top-up rule. It does not change the study design.

## Canonical dispatch claim

The confirmatory-main workflow uses one global GitHub Actions concurrency group with `cancel-in-progress: false`.

Before any battery prompt is sent, after dependency/design/synthetic checks and the non-battery API preflight, the workflow must atomically claim the collection by creating and pushing:

`runs/pressure-ladder-v4-main/COLLECTION-DISPATCHED`

The sentinel records the GitHub workflow run ID, run attempt, commit SHA and UTC timestamp.

- If the sentinel already exists on `origin/main`, the workflow exits before any battery API call.
- If the sentinel commit/push fails, the workflow exits before any battery API call.
- The **first workflow dispatch that successfully pushes this sentinel is the only authorized confirmatory-main collection dispatch**.
- Re-running that workflow run or starting a later dispatch is invalid and must terminate before battery collection.
- If the claimed collection stops or is cancelled after the sentinel is written, the collection is terminal under preregistration v0.2.1. It may not be resumed, completed, replaced or pooled.

The sentinel is audit state, not a normative design/analysis file; creating it after freeze does not alter the frozen checksum set.
