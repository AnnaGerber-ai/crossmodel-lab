#!/usr/bin/env python3
"""Run the Pressure Ladder pilot (protocol-v3.md) against an OpenAI-compatible API.

Every manifest run is a fresh conversation: optional injected history (S3), T1,
then the three pressure steps in the run's order. The model's own replies stay
in the history. On an API error the whole run is retried once in a fresh
conversation; if that also fails the run is recorded as censored (API failure).
Truncated turns are kept and the run continues; they are never rerun.
The OpenAI client's own transport retries (connection errors, 429/5xx before
any response is received) are left at their defaults: no response text is seen,
so they cannot select outputs.

The tool records raw responses and metadata only. It prints status, never
response text, so the operator can stay blind to outputs.
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


def user_turns(scenario: dict, order: list[str], p1: str) -> list[tuple[str, str]]:
    steps = {"P1": p1, "P2": scenario["P2"], "P3": scenario["P3"]}
    return [("T1", scenario["T1"])] + [(step, steps[step]) for step in order]


def run_once(client, config: dict, scenario: dict, turns: list[tuple[str, str]]) -> tuple[list[dict], dict | None]:
    messages: list[dict[str, str]] = []
    if config.get("system_prompt"):
        messages.append({"role": "system", "content": config["system_prompt"]})
    messages.extend(scenario.get("history", []))
    records: list[dict] = []
    for index, (label, text) in enumerate(turns):
        messages.append({"role": "user", "content": text})
        started_at = utc_now()
        try:
            response = client.chat.completions.create(
                model=config["model"], messages=messages, **config["generation"]
            )
        except Exception as exc:  # keep failures in the raw record
            return records, {"turn": index, "type": type(exc).__name__, "message": str(exc)}
        choice = response.choices[0]
        text_out = choice.message.content or ""
        records.append(
            {
                "turn": index,
                "label": label,
                "user": text,
                "assistant": text_out,
                "finish_reason": choice.finish_reason,
                "truncated": choice.finish_reason == "length",
                "provider_model": getattr(response, "model", None),
                "system_fingerprint": getattr(response, "system_fingerprint", None),
                "response_id": getattr(response, "id", None),
                "usage": response.usage.model_dump() if getattr(response, "usage", None) else None,
                "started_at": started_at,
                "completed_at": utc_now(),
            }
        )
        messages.append({"role": "assistant", "content": text_out})
    return records, None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--manifest", required=True, type=Path)
    parser.add_argument("--config-a", required=True, type=Path)
    parser.add_argument("--config-c", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--dry-run", action="store_true", help="Print the plan without API calls.")
    args = parser.parse_args()

    manifest = load_json(args.manifest)
    configs = {"A": load_json(args.config_a), "C": load_json(args.config_c)}
    scenarios_raw = Path(configs["A"]["scenarios"]).read_bytes()
    if hashlib.sha256(scenarios_raw).hexdigest() != manifest["scenarios_sha256"]:
        print("Scenario file does not match the manifest's scenarios_sha256.", file=sys.stderr)
        return 2
    scenario_file = json.loads(scenarios_raw)
    scenarios = {s["id"]: s for s in scenario_file["scenarios"]}
    card_sha = {
        c: hashlib.sha256(cfg["system_prompt"].encode("utf-8")).hexdigest() if cfg.get("system_prompt") else None
        for c, cfg in configs.items()
    }

    print(f"Runs: {len(manifest['runs'])}  seed={manifest['seed']}  output={args.output}")
    if args.dry_run:
        for run in manifest["runs"]:
            turns = user_turns(scenarios[run["scenario"]], run["order"], scenario_file["P1"])
            print(f"[{run['position']:>2}] {run['run_id']:<10} order={'/'.join(run['order'])} turns={len(turns)}")
        return 0

    try:
        from dotenv import load_dotenv
        from openai import OpenAI
    except ImportError as exc:
        print(f"Missing runner dependency ({exc}). python -m pip install -r requirements.txt", file=sys.stderr)
        return 2
    load_dotenv()
    api_key, base_url = os.getenv("DASHSCOPE_API_KEY"), os.getenv("QWEN_BASE_URL")
    if not api_key or not base_url:
        print("Missing DASHSCOPE_API_KEY or QWEN_BASE_URL.", file=sys.stderr)
        return 2
    client = OpenAI(api_key=api_key, base_url=base_url)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    censored = 0
    with args.output.open("a", encoding="utf-8") as out:
        for run in manifest["runs"]:
            config = configs[run["condition"]]
            scenario = scenarios[run["scenario"]]
            turns = user_turns(scenario, run["order"], scenario_file["P1"])
            attempts = []
            for attempt in (1, 2):
                records, error = run_once(client, config, scenario, turns)
                attempts.append({"attempt": attempt, "turns": records, "error": error})
                if error is None:
                    break
            final = attempts[-1]
            status = "ok" if final["error"] is None else "censored_api_failure"
            censored += status != "ok"
            out.write(
                json.dumps(
                    {
                        "experiment": config["experiment"],
                        "protocol": manifest["protocol"],
                        "manifest_seed": manifest["seed"],
                        "scenarios_sha256": manifest["scenarios_sha256"],
                        "run_id": run["run_id"],
                        "position": run["position"],
                        "scenario": run["scenario"],
                        "set": scenario["set"],
                        "replicate": run["replicate"],
                        "condition": run["condition"],
                        "order": run["order"],
                        "model_requested": config["model"],
                        "generation": config["generation"],
                        "card_sha256": card_sha[run["condition"]],
                        "injected_history": scenario.get("history", []),
                        "status": status,
                        "attempts": attempts,
                        "truncated_turns": [t["turn"] for t in final["turns"] if t["truncated"]],
                    },
                    ensure_ascii=False,
                )
                + "\n"
            )
            out.flush()
            flags = ",".join(str(t["turn"]) for t in final["turns"] if t["truncated"]) or "-"
            print(f"[{run['position']:>2}] {run['run_id']:<10} {status} attempts={len(attempts)} truncated_turns={flags}")
    print(f"Done. censored={censored}")
    return 1 if censored else 0


if __name__ == "__main__":
    raise SystemExit(main())
