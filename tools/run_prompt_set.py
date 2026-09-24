#!/usr/bin/env python3
"""Run independent prompt cases against an OpenAI-compatible API.

This tool is intentionally small: it collects raw responses and metadata.
It does not score, classify, or evaluate model behavior.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any



def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def load_config(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        config = json.load(f)

    if not config.get("experiment"):
        raise ValueError("Config must contain a non-empty 'experiment' field.")

    cases = config.get("cases")
    if not isinstance(cases, list) or not cases:
        raise ValueError("Config must contain a non-empty 'cases' list.")

    seen_ids: set[str] = set()
    for case in cases:
        if not isinstance(case, dict):
            raise ValueError("Every case must be a JSON object.")
        case_id = str(case.get("id", "")).strip()
        prompt = case.get("prompt")
        if not case_id:
            raise ValueError("Every case must have a non-empty 'id'.")
        if case_id in seen_ids:
            raise ValueError(f"Duplicate case id: {case_id}")
        if not isinstance(prompt, str) or not prompt.strip():
            raise ValueError(f"Case {case_id!r} must have a non-empty 'prompt'.")
        seen_ids.add(case_id)

    generation = config.get("generation", {})
    if not isinstance(generation, dict):
        raise ValueError("'generation' must be a JSON object when present.")

    return config


def build_messages(config: dict[str, Any], case: dict[str, Any]) -> list[dict[str, str]]:
    messages: list[dict[str, str]] = []

    system_prompt = case.get("system_prompt", config.get("system_prompt"))
    if system_prompt:
        messages.append({"role": "system", "content": str(system_prompt)})

    messages.append({"role": "user", "content": case["prompt"]})
    return messages


def default_output_path(config: dict[str, Any], model: str) -> Path:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    safe_experiment = "".join(
        c if c.isalnum() or c in "-_" else "-" for c in config["experiment"]
    )
    safe_model = "".join(c if c.isalnum() or c in "-_." else "-" for c in model)
    return Path("runs") / f"{stamp}_{safe_experiment}_{safe_model}.jsonl"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run independent prompt cases and save raw responses as JSONL."
    )
    parser.add_argument("--config", required=True, type=Path, help="Path to JSON config.")
    parser.add_argument("--model", required=True, help="Model name sent to the provider.")
    parser.add_argument("--output", type=Path, help="Optional JSONL output path.")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Validate and print requests without calling the API.",
    )
    args = parser.parse_args()

    config = load_config(args.config)
    output_path = args.output or default_output_path(config, args.model)

    print(f"Experiment: {config['experiment']}")
    print(f"Model:      {args.model}")
    print(f"Cases:      {len(config['cases'])}")
    print(f"Output:     {output_path}")

    if args.dry_run:
        print("\nDRY RUN — no API calls will be made.\n")
        for index, case in enumerate(config["cases"], start=1):
            print(f"[{index}/{len(config['cases'])}] {case['id']}")
            for message in build_messages(config, case):
                preview = message["content"].replace("\n", " ")
                if len(preview) > 160:
                    preview = preview[:157] + "..."
                print(f"  {message['role']}: {preview}")
        return 0

    try:
        from dotenv import load_dotenv
        from openai import OpenAI
    except ImportError as exc:
        print(
            "Missing runner dependency. Install with: "
            "python -m pip install -r requirements.txt",
            file=sys.stderr,
        )
        print(f"Import error: {exc}", file=sys.stderr)
        return 2

    load_dotenv()

    api_key = os.getenv("DASHSCOPE_API_KEY")
    base_url = os.getenv("QWEN_BASE_URL")

    if not api_key:
        print("Missing DASHSCOPE_API_KEY. See .env.example.", file=sys.stderr)
        return 2
    if not base_url:
        print("Missing QWEN_BASE_URL. See .env.example.", file=sys.stderr)
        return 2

    client = OpenAI(api_key=api_key, base_url=base_url)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    generation = dict(config.get("generation", {}))

    with output_path.open("a", encoding="utf-8") as out:
        for index, case in enumerate(config["cases"], start=1):
            started_at = utc_now()
            record: dict[str, Any] = {
                "run_id": run_id,
                "experiment": config["experiment"],
                "language": config.get("language"),
                "case_id": case["id"],
                "case_index": index,
                "requested_model": args.model,
                "prompt": case["prompt"],
                "system_prompt": case.get("system_prompt", config.get("system_prompt")),
                "generation": generation,
                "started_at": started_at,
            }

            print(f"[{index}/{len(config['cases'])}] {case['id']} ... ", end="", flush=True)

            try:
                response = client.chat.completions.create(
                    model=args.model,
                    messages=build_messages(config, case),
                    **generation,
                )

                choice = response.choices[0] if response.choices else None
                record.update(
                    {
                        "completed_at": utc_now(),
                        "provider_model": getattr(response, "model", None),
                        "response_text": (
                            choice.message.content
                            if choice is not None and choice.message is not None
                            else None
                        ),
                        "finish_reason": getattr(choice, "finish_reason", None)
                        if choice is not None
                        else None,
                        "usage": (
                            response.usage.model_dump()
                            if getattr(response, "usage", None) is not None
                            else None
                        ),
                        "error": None,
                    }
                )
                print("ok")
            except Exception as exc:  # preserve failures as part of the run record
                record.update(
                    {
                        "completed_at": utc_now(),
                        "provider_model": None,
                        "response_text": None,
                        "finish_reason": None,
                        "usage": None,
                        "error": {
                            "type": type(exc).__name__,
                            "message": str(exc),
                        },
                    }
                )
                print(f"error: {type(exc).__name__}")

            out.write(json.dumps(record, ensure_ascii=False) + "\n")
            out.flush()

    print(f"Saved: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
