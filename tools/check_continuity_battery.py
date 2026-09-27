#!/usr/bin/env python3
"""Check that the continuity battery files and API layer configs are consistent.

- Probe wording in battery-v1.md matches battery-v1.json exactly.
- All API layer configs share the same generation parameters and battery.
- Q, Q+ and Q+pin share the same compact card; F has none.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BATTERY_DIR = ROOT / "tests" / "longitudinal-assistant-continuity"
CONFIGS = {
    "F": ROOT / "configs" / "continuity-v1-f.json",
    "Q": ROOT / "configs" / "continuity-v1-q.json",
    "Q+": ROOT / "configs" / "continuity-v1-qplus.json",
    "Q+pin": ROOT / "configs" / "continuity-v1-qplus-pin.json",
}
EXPECTED_GENERATION = {"temperature": 0.7, "max_tokens": 2048}


def main() -> int:
    errors: list[str] = []

    battery = json.loads((BATTERY_DIR / "battery-v1.json").read_text(encoding="utf-8"))
    markdown = (BATTERY_DIR / "battery-v1.md").read_text(encoding="utf-8")

    md_turns: dict[str, list[str]] = {}
    for section in re.split(r"^### ", markdown, flags=re.M)[1:]:
        probe_id = section.split()[0]
        quoted = [line[2:].strip() for line in section.splitlines() if line.startswith("> ")]
        if quoted:
            md_turns[probe_id] = quoted

    json_ids = [p["id"] for p in battery["probes"]]
    if len(set(json_ids)) != len(json_ids):
        errors.append("duplicate probe ids in battery-v1.json")
    for probe in battery["probes"]:
        if md_turns.get(probe["id"]) != probe["user_turns"]:
            errors.append(f"{probe['id']}: wording differs between battery-v1.md and battery-v1.json")
    for probe_id in md_turns.keys() - set(json_ids):
        errors.append(f"{probe_id}: in battery-v1.md but not in battery-v1.json")

    run_last = [p["id"] for p in battery["probes"] if p.get("run_last")]
    if run_last != ["R06"]:
        errors.append(f"run_last probes should be ['R06'], got {run_last}")

    configs = {name: json.loads(path.read_text(encoding="utf-8")) for name, path in CONFIGS.items()}
    for name, config in configs.items():
        if config.get("layer") != name:
            errors.append(f"{CONFIGS[name].name}: layer is {config.get('layer')!r}, expected {name!r}")
        if config.get("generation") != EXPECTED_GENERATION:
            errors.append(f"{name}: generation {config.get('generation')} != {EXPECTED_GENERATION}")
        if config.get("replicates") != 3:
            errors.append(f"{name}: replicates must be 3")
        if config.get("battery") != "tests/longitudinal-assistant-continuity/battery-v1.json":
            errors.append(f"{name}: unexpected battery path")

    if configs["F"].get("system_prompt"):
        errors.append("F must not have a system prompt")
    cards = {configs[n].get("system_prompt") for n in ("Q", "Q+", "Q+pin")}
    if len(cards) != 1 or not next(iter(cards)):
        errors.append("Q, Q+ and Q+pin must share the same non-empty card")

    for error in errors:
        print(f"FAIL: {error}")
    if errors:
        return 1
    print(f"OK: {len(json_ids)} probes match; {len(configs)} configs consistent.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
