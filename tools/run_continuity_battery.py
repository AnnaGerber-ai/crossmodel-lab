#!/usr/bin/env python3
"""Run one API layer of a continuity-battery slice against an OpenAI-compatible API.

Each manifest item is an independent conversation. For multi-turn probes, every
user turn is sent in sequence and the model's own reply is kept in the
conversation before the next turn. The tool collects raw responses and
metadata only; it does not score model behavior.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", required=True, type=Path, help="Layer config JSON.")
    parser.add_argument("--manifest", required=True, type=Path, help="Slice manifest JSON.")
    parser.add_argument("--output", required=True, type=Path, help="JSONL output path.")
    parser.add_argument(
        "--battery",
        type=Path,
        help="Probe file to use instead of the config's battery (e.g. the technical smoke probes).",
    )
    parser.add_argument("--dry-run", action="store_true", help="Print the plan without API calls.")
    args = parser.parse_args()

    config = load_json(args.config)
    manifest = load_json(args.manifest)
    battery_raw = (args.battery or Path(config["battery"])).read_bytes()
    battery = json.loads(battery_raw)

    if hashlib.sha256(battery_raw).hexdigest() != manifest["battery_sha256"]:
        print("Battery file does not match the manifest's battery_sha256.", file=sys.stderr)
        return 2

    layer = config["layer"]
    items = manifest["layers"].get(layer)
    if not items:
        print(f"Manifest has no runs for layer {layer!r}.", file=sys.stderr)
        return 2

    probes = {p["id"]: p for p in battery["probes"]}
    system_prompt = config.get("system_prompt")
    card_sha256 = (
        hashlib.sha256(system_prompt.encode("utf-8")).hexdigest() if system_prompt else None
    )
    generation = dict(config["generation"])

    print(f"Layer:    {layer}  model={config['model']} ({config['model_kind']})")
    print(f"Slice:    {manifest['slice']}  seed={manifest['seed']}")
    print(f"Runs:     {len(items)}")
    print(f"Output:   {args.output}")

    if args.dry_run:
        print("\nDRY RUN — no API calls will be made.\n")
        for item in items:
            turns = probes[item["probe"]]["user_turns"]
            print(f"[{item['position']}] {item['probe']} r{item['replicate']} ({len(turns)} turn(s))")
        return 0

    try:
        from dotenv import load_dotenv
        from openai import OpenAI
    except ImportError as exc:
        print("Missing runner dependency: python -m pip install -r requirements.txt", file=sys.stderr)
        print(f"Import error: {exc}", file=sys.stderr)
        return 2

    load_dotenv()
    api_key = os.getenv("DASHSCOPE_API_KEY")
    base_url = os.getenv("QWEN_BASE_URL")
    if not api_key or not base_url:
        print("Missing DASHSCOPE_API_KEY or QWEN_BASE_URL. See .env.example.", file=sys.stderr)
        return 2

    client = OpenAI(api_key=api_key, base_url=base_url)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    had_errors = False

    with args.output.open("a", encoding="utf-8") as out:
        for item in items:
            probe = probes[item["probe"]]
            messages: list[dict[str, str]] = []
            if system_prompt:
                messages.append({"role": "system", "content": system_prompt})

            turns: list[dict[str, Any]] = []
            error = None
            print(f"[{item['position']}/{len(items)}] {probe['id']} r{item['replicate']} ... ", end="", flush=True)

            for index, user_text in enumerate(probe["user_turns"], start=1):
                messages.append({"role": "user", "content": user_text})
                started_at = utc_now()
                try:
                    response = client.chat.completions.create(
                        model=config["model"], messages=messages, **generation
                    )
                except Exception as exc:  # keep failures in the raw record
                    error = {"turn": index, "type": type(exc).__name__, "message": str(exc)}
                    break

                choice = response.choices[0] if response.choices else None
                text = choice.message.content if choice and choice.message else None
                finish_reason = getattr(choice, "finish_reason", None) if choice else None
                turns.append(
                    {
                        "turn": index,
                        "user": user_text,
                        "assistant": text,
                        "finish_reason": finish_reason,
                        "truncated": finish_reason == "length",
                        "provider_model": getattr(response, "model", None),
                        "system_fingerprint": getattr(response, "system_fingerprint", None),
                        "response_id": getattr(response, "id", None),
                        "usage": response.usage.model_dump() if getattr(response, "usage", None) else None,
                        "started_at": started_at,
                        "completed_at": utc_now(),
                    }
                )
                messages.append({"role": "assistant", "content": text or ""})

            record = {
                "experiment": config["experiment"],
                "battery_version": battery["version"],
                "battery_sha256": manifest["battery_sha256"],
                "slice": manifest["slice"],
                "manifest_seed": manifest["seed"],
                "layer": layer,
                "model_requested": config["model"],
                "model_kind": config["model_kind"],
                "endpoint": base_url,
                "card_sha256": card_sha256,
                "generation": generation,
                "probe": probe["id"],
                "block": probe["block"],
                "replicate": item["replicate"],
                "position": item["position"],
                "turns": turns,
                "truncated": any(t["truncated"] for t in turns),
                "error": error,
            }
            out.write(json.dumps(record, ensure_ascii=False) + "\n")
            out.flush()

            if error:
                had_errors = True
                print(f"error on turn {error['turn']}: {error['type']}")
            else:
                print("truncated" if record["truncated"] else "ok")

    return 1 if had_errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
