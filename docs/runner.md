# Prompt-set runner

`tools/run_prompt_set.py` is a deliberately small data-collection utility for Crossmodel Lab.

Its job is to make repeated prompt runs easier to reproduce. It sends each case as an **independent API request** and saves the raw response plus basic provenance metadata. It does **not** score, classify, rank, or interpret model behavior.

## Why it exists

Many Crossmodel Lab studies are qualitative and still require human evaluation. The runner automates only the mechanical part:

```text
JSON prompt set
      ↓
Python runner
      ↓
OpenAI-compatible Qwen API
      ↓
raw JSONL run log
```

Each case starts with a new request. Responses from earlier cases are not added to later cases.

This helps reduce accidental prompt changes, missing metadata, and conversation-history leakage in experiments that require isolated runs.

## Requirements

- Python 3.10+
- an Alibaba Cloud Model Studio / DashScope API key
- an OpenAI-compatible Model Studio base URL for the same region as that key

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Copy the environment template:

```bash
cp .env.example .env
```

Then fill in your own API key and regional base URL.

**Never commit `.env` or an API key.**

Alibaba Cloud Model Studio exposes Qwen models through an OpenAI-compatible interface. Base URLs are region-specific and may also be workspace-specific, so use the current URL shown for your Model Studio workspace rather than assuming that another region's endpoint will work.

## First step: dry run

A dry run validates the config and shows what would be sent without making any API calls:

```bash
python tools/run_prompt_set.py \
  --config configs/example-run.json \
  --model YOUR_MODEL_NAME \
  --dry-run
```

No API key is required for `--dry-run`.

## Real run

```bash
python tools/run_prompt_set.py \
  --config configs/example-run.json \
  --model YOUR_MODEL_NAME
```

By default, results are written to a timestamped file inside `runs/`.

Example:

```text
runs/20260922T070000Z_example-independent-prompts_YOUR_MODEL_NAME.jsonl
```

The `runs/` directory is ignored by Git so that unreviewed raw outputs are not published accidentally. Material intended for publication can be reviewed and copied into the repository's `data/` structure.

## Config format

Minimal example:

```json
{
  "experiment": "example-independent-prompts",
  "language": "ru",
  "cases": [
    {
      "id": "case-01",
      "prompt": "Коротко представься."
    }
  ]
}
```

Optional fields:

- `system_prompt` at the experiment level;
- `system_prompt` on an individual case, which overrides the experiment-level value;
- `generation` for API parameters supported by the selected model, such as `temperature`.

The model name is deliberately supplied on the command line so that the same prompt set can be reused across model versions without editing the source file.

## Output format

Each JSONL line represents one case. The runner records:

- run ID;
- experiment and case IDs;
- language;
- exact prompt and optional system prompt;
- requested model;
- provider-returned model identifier, when available;
- generation parameters;
- start and completion timestamps;
- response text;
- finish reason;
- token usage, when returned;
- error type and message when a request fails.

A failed request is written to the run log instead of silently disappearing.

## Validation status

As of 2026-09-26, the runner has been validated on a GitHub-hosted Ubuntu runner.

- dependency-free dry run: successful;
- live API round-trip with `qwen-flash-character`: successful;
- raw JSONL output and GitHub Actions artifact creation: successful;
- `qwen3.8-omni-flash` currently returns `AccessDenied.Unpurchased`, which is treated as a provider/account entitlement issue rather than a runner failure.

This confirms that the GitHub Actions workflow, repository secrets, regional API endpoint, request execution, and raw-output pipeline work end to end for an accessible Qwen model.

## Methodological boundary

This runner is a collection tool, not an evaluator.

It does not decide whether two answers are equivalent, whether a character remains recognizable, whether a boundary was preserved, or whether one model is better than another. Those judgments remain part of the documented qualitative evaluation method.

The current runner is **text-only**. Multimodal image input is intentionally left for a later version after the text workflow has been tested and understood.
