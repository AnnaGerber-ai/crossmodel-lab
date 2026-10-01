# Pressure Ladder v4 main — frozen API retry/backoff policy v1

This file is normative for confirmatory-main collection.

## Request-level client backoff

The OpenAI-compatible client is constructed with:

- `max_retries = 0` — library-internal retries are disabled;
- request timeout = **60 seconds**.

`tools/pressure_main.py` implements the only request-level backoff.

A single assistant turn receives at most **3 request attempts total**:

1. immediate request;
2. after a fixed **1.0 second** delay;
3. after a fixed **2.0 second** delay.

There is **no jitter**.

Request-level retry is allowed only for:

- connection / transport failure with no HTTP-level response;
- timeout;
- HTTP `429`;
- HTTP `5xx` (`500–599`).

After all three request attempts fail for one of those classes, the **whole run** becomes eligible for the single frozen whole-run retry.

## Events that are never retried

These are final technical events for that required turn and never trigger either request-level or whole-run retry:

- empty assistant payload;
- response with no choice;
- provider content-filter/block finish reason;
- non-429 HTTP `4xx`.

The runner continues to later required pressure turns when the API remains callable. No placeholder assistant content is inserted into conversation history.

## Whole-run retry

A retry-eligible run is queued and retried **once**, from T1 in a fresh conversation, only after the complete first-pass manifest has been attempted.

- queue order = original manifest position;
- same slot and same condition;
- same model/configuration;
- no third whole-run attempt.

When whole-run retry occurs, attempt 2 is the **sole canonical run** for that slot. Attempt 1 is audit-only even if it contained a scorable earlier stance.

If collection terminates before a queued retry executes, the slot has **no canonical run**. The partial first attempt never becomes canonical retroactively.

## Audit

Every request attempt logs timestamps, exception class/status when applicable, requested model alias, returned provider model label when available, response ID when available, finish reason, and the whole-run attempt number.
