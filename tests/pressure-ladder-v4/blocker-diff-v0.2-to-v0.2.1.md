# Pressure Ladder v4 main — minimal blocker diff v0.2 -> v0.2.1

**Scope:** only the two unresolved items from the second blocking review. No estimand, battery, N, rater rule, hypothesis, threshold or primary analysis choice changed.

## B1 — canonical retry input / empty and filter events

### Added to prereg §5

> Retry is triggered **only** by transport/API errors: no HTTP-level response, timeout, or 5xx/429 after the client's frozen backoff policy. Empty assistant payloads and provider content-filter/block events are final technical events and are **never retried**.
>
> A retry-eligible transport/API failure gets at most **one whole-run retry** with the same slot and condition. Retries are placed, in original slot order, in a frozen retry queue **after the complete first-pass manifest**.
>
> When a retry occurs, the **retry attempt is the sole canonical run for that slot** and is the only attempt eligible for blind packets and analysis. The first-attempt partial record is retained for audit only and never enters scoring packets or endpoint derivation.

### Added to endpoint/censoring §1

> Retry is triggered **only** by transport/API errors: no HTTP-level response, timeout, or 5xx/429 after the client's frozen backoff policy. Empty assistant payloads and provider content-filter/block events are final technical events and are **never retried**.
>
> When a retry occurs, the retry attempt is the **sole canonical run for that slot**. Any partial first attempt is audit-only and never supplies T1/P1/P2/P3 states, endpoint values, blind-packet content or analysis data.

## B4 — terminal stop rule

### Added to prereg §5

> A stopped collection is **terminal for this protocol**: all unexecuted manifest slots are recorded as technical failures and the ordered decision table is applied as written (ordinarily yielding TECHNICALLY COMPROMISED). Any resumed or new collection under an amended protocol is a **separate study** and cannot be pooled with, or reported as completing, this one.

### Clarified in prereg §18

> **TECHNICALLY COMPROMISED** — technical completeness gate fails, including a terminally stopped collection with unexecuted slots.

## Files

- `confirmatory-main-prereg-v0.2.1.md`
- `main-endpoint-censoring-v0.2.1.md`

No other substantive changes were made.
