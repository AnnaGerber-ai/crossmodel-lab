# Pressure Ladder v4 main — frozen API retry/backoff policy v1.2

This supersedes implementation backoff policy v1.1 before confirmatory-main collection. The study design is unchanged.

## Request-level client backoff

The OpenAI-compatible client is constructed with:
- `max_retries = 0`;
- request timeout = **60 seconds**.

A single assistant turn receives at most **3 request attempts total**:
1. immediate request;
2. after fixed **1.0 second** delay;
3. after fixed **2.0 second** delay.

There is no jitter.

Request-level retry is allowed only for:
- connection/transport failure with no HTTP response;
- timeout;
- HTTP 429;
- HTTP 5xx.

## Final non-retryable technical events

The following are final technical events for the required turn and never trigger request-level or whole-run resampling:
- empty assistant payload;
- response with no choice;
- provider content-filter/block finish reason;
- non-429 HTTP 4xx;
- **an otherwise unclassified exception raised by the API/client call**.

The final event is recorded as technical missingness and the runner proceeds to later required turns when callable. No placeholder assistant content is inserted into conversation history.

Once any final non-retryable technical event occurs, whole-run retry eligibility is permanently disabled for that run.

## Whole-run retry

After all three request attempts fail with a retry-eligible transport/timeout/429/5xx class, a whole-run retry is queued only if no earlier final non-retryable technical event occurred in that run.

- at most one whole-run retry;
- queue runs after the complete first-pass manifest;
- queue order is original manifest position;
- same slot/condition/model/config;
- attempt 2 is the sole canonical run;
- attempt 1 remains audit-only;
- if collection terminates before queued attempt 2 executes, the slot has no canonical run.

## Immediate request-attempt audit

Every individual request attempt is appended to the audit JSONL **as soon as the request returns or raises**, before later response parsing can fail.

Each request-attempt audit row includes, when available:
- slot/condition/scenario/manifest position;
- whole-run attempt number;
- request-attempt number;
- timestamps;
- requested model alias;
- response/exception classification;
- exception class/status;
- returned provider model;
- response ID;
- finish reason.

The later whole-run audit row may duplicate this information structurally. Immediate request rows are authoritative evidence that a request occurred even if later code terminates unexpectedly.

## Synthetic preflight

Before the one-time collection sentinel is claimed, the workflow performs one live **non-battery synthetic** API call through the same client settings. It contains no battery prompt and is not study data.

A failed preflight stops before the sentinel and before any battery API call.

## Synthetic requirements

Freeze v1.2 must test at minimum:
- final content-filter/empty/final-4xx/unclassified exception never causes whole-run resampling;
- queued retry not executed before terminal stop leaves no canonical slot;
- strict JSON-Schema rejection for missing required fields and additional properties;
- attempt-log retry-count rules;
- position and warmth configuration gates are separate;
- endpoint/permutation/decision tests from v1.1 remain green.
