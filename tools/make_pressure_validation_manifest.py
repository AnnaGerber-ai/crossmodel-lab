#!/usr/bin/env python3
"""Generate a seeded manifest for the Pressure Ladder v4 validation pilot.

Validation set: S2/S3/S4/S7/S8/S9/S10.
Each scenario receives all six P1/P2/P3 orders exactly once per condition.
A/C runs share only the scenario+order block; they are independent draws.
Execution order is shuffled with the recorded seed.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import random
import secrets
from datetime import datetime, timezone
from pathlib import Path

PRIMARY = ["S3", "S4", "S7", "S8", "S9", "S10"]
RELATIONAL = ["S2"]
VALIDATION = RELATIONAL + PRIMARY
CONDITIONS = ["A", "C"]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--scenarios", required=True, type=Path)
    parser.add_argument("--seed", type=int, help="Reuse a recorded seed.")
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    raw = args.scenarios.read_bytes()
    scenario_file = json.loads(raw)
    available = {s["id"] for s in scenario_file["scenarios"]}
    missing = sorted(set(VALIDATION) - available)
    if missing:
        parser.error(f"missing validation scenarios: {missing}")

    seed = args.seed if args.seed is not None else secrets.randbits(63)
    rng = random.Random(seed)
    orders = [list(p) for p in itertools.permutations(["P1", "P2", "P3"])]

    blocks = []
    for scenario in VALIDATION:
        scenario_orders = [o[:] for o in orders]
        rng.shuffle(scenario_orders)
        for replicate, order in enumerate(scenario_orders, start=1):
            blocks.append((scenario, replicate, order))

    runs = [
        {
            "run_id": f"{scenario}-r{replicate}-{condition}",
            "scenario": scenario,
            "replicate": replicate,
            "condition": condition,
            "order": order,
        }
        for scenario, replicate, order in blocks
        for condition in CONDITIONS
    ]
    rng.shuffle(runs)
    for position, run in enumerate(runs, start=1):
        run["position"] = position

    manifest = {
        "experiment": "pressure-ladder-v4-validation",
        "status": "validation-only",
        "protocol": "tests/pressure-ladder-v4-draft/validation-plan-v1.md",
        "scenarios": str(args.scenarios),
        "scenarios_sha256": hashlib.sha256(raw).hexdigest(),
        "seed": seed,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "primary_scenarios": PRIMARY,
        "relational_control_scenarios": RELATIONAL,
        "runs": runs,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Manifest: {args.output}  seed={seed}  runs={len(runs)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
