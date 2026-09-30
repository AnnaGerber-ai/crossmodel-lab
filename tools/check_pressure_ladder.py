#!/usr/bin/env python3
"""Check the Pressure Ladder pilot files against protocol-v3.md.

- Scenarios: S1-S6, P1 shared, S3 carries injected history, no look-alike letters.
- Configs: same model and parameters; A has no system prompt; C uses the
  Case 10 Run 02 / continuity Q. card.
- Manifest: 36 runs; each order used 3 times per condition; A and C share the
  order for every scenario x run pair; scenario hash matches.
"""

from __future__ import annotations

import hashlib
import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PILOT = ROOT / "tests" / "pressure-ladder-pilot"
EXPECTED_GENERATION = {"temperature": 0.7, "max_tokens": 1536}


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    errors: list[str] = []
    raw = (PILOT / "scenarios-v1.json").read_bytes()
    scenarios = json.loads(raw)
    ids = [s["id"] for s in scenarios["scenarios"]]
    if ids != ["S1", "S2", "S3", "S4", "S5", "S6"]:
        errors.append(f"scenario ids {ids}")
    texts = [scenarios["P1"]] + [
        t for s in scenarios["scenarios"] for t in [s["T1"], s["P2"], s["P3"]] + [h["content"] for h in s["history"]]
    ]
    if any("ĸ" in t for t in texts):
        errors.append("scenario text contains U+0138 (kra) instead of Cyrillic к")
    history = {s["id"]: s["history"] for s in scenarios["scenarios"]}
    if len(history["S3"]) != 2 or any(h for k, h in history.items() if k != "S3"):
        errors.append("only S3 may carry injected history, and it needs one user and one assistant turn")
    sets = {s["id"]: s["set"] for s in scenarios["scenarios"]}
    if [k for k, v in sets.items() if v == "factual"] != ["S1", "S2", "S3", "S4"]:
        errors.append("S1-S4 must be the factual set, S5-S6 evaluative")

    a = load(ROOT / "configs" / "pressure-ladder-pilot-a.json")
    c = load(ROOT / "configs" / "pressure-ladder-pilot-c.json")
    for name, cfg in (("A", a), ("C", c)):
        if cfg.get("model") != "qwen-flash-character":
            errors.append(f"{name}: model must be qwen-flash-character")
        if cfg.get("generation") != EXPECTED_GENERATION:
            errors.append(f"{name}: generation {cfg.get('generation')} != {EXPECTED_GENERATION}")
        if cfg.get("condition") != name:
            errors.append(f"{name}: condition field is {cfg.get('condition')!r}")
    if a.get("system_prompt"):
        errors.append("A must have no system prompt")
    card = load(ROOT / "configs" / "case10-rep02-persona-ru.json")["system_prompt"]
    if c.get("system_prompt") != card:
        errors.append("C card differs from Case 10 Run 02 condition C")
    if load(ROOT / "configs" / "continuity-v1-q.json").get("system_prompt") != card:
        errors.append("C card differs from the continuity Q. card")

    manifest = load(PILOT / "manifest-pilot.json")
    if manifest.get("scenarios_sha256") != hashlib.sha256(raw).hexdigest():
        errors.append("manifest scenarios_sha256 does not match scenarios-v1.json")
    runs = manifest.get("runs", [])
    if len(runs) != 36:
        errors.append(f"manifest has {len(runs)} runs, expected 36")
    if sorted(r["position"] for r in runs) != list(range(1, len(runs) + 1)):
        errors.append("positions must be 1..n")
    for cond in ("A", "C"):
        counts = Counter(tuple(r["order"]) for r in runs if r["condition"] == cond)
        if len(counts) != 6 or set(counts.values()) != {3}:
            errors.append(f"{cond}: each of 6 orders must appear exactly 3 times, got {dict(counts)}")
    pair_orders: dict[tuple, set] = {}
    for r in runs:
        pair_orders.setdefault((r["scenario"], r["replicate"]), set()).add(tuple(r["order"]))
    if len(pair_orders) != 18 or any(len(o) != 1 for o in pair_orders.values()):
        errors.append("A and C must share one order per scenario x run pair (18 pairs)")
    ids = Counter(r["run_id"] for r in runs)
    errors.extend(f"duplicate run_id {k}" for k, v in ids.items() if v > 1)

    if errors:
        for e in errors:
            print(f"ERROR: {e}")
        return 1
    print(f"OK: 6 scenarios, 2 configs, manifest seed={manifest['seed']} with 36 balanced runs.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
