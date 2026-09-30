#!/usr/bin/env python3
"""Generate a seeded manifest for the Pressure Ladder v4 validation pilot.

Validation set:
- primary factual S3/S4/S7/S8/S9/S10, 3 replicate pairs each;
- relational control S2, 3 replicate pairs;
- conditions A/C matched on order within every pair.

For the 18 primary pairs, all six P1/P2/P3 permutations appear exactly three
times overall, and each scenario receives three distinct permutations.
S2 receives three distinct permutations. Execution order is shuffled.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import random
import secrets
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

PRIMARY = ["S3", "S4", "S7", "S8", "S9", "S10"]
RELATIONAL = ["S2"]
CONDITIONS = ["A", "C"]
RUNS_PER_SCENARIO = 3


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--scenarios", required=True, type=Path)
    parser.add_argument("--seed", type=int, help="Reuse a recorded seed.")
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    raw = args.scenarios.read_bytes()
    scenario_file = json.loads(raw)
    available = {s["id"] for s in scenario_file["scenarios"]}
    needed = set(PRIMARY + RELATIONAL)
    missing = sorted(needed - available)
    if missing:
        parser.error(f"missing validation scenarios: {missing}")

    seed = args.seed if args.seed is not None else secrets.randbits(63)
    rng = random.Random(seed)
    orders = [list(p) for p in itertools.permutations(["P1", "P2", "P3"])]

    # Cyclic 3-order windows over a seeded order of the six permutations.
    # Across six scenarios every order appears exactly three times, while every
    # scenario gets three distinct orders.
    order_ring = orders[:]
    rng.shuffle(order_ring)

    pair_specs: list[tuple[str, int, list[str]]] = []
    for i, scenario in enumerate(PRIMARY):
        selected = [order_ring[(i + j) % len(order_ring)] for j in range(RUNS_PER_SCENARIO)]
        selected = [o[:] for o in selected]
        rng.shuffle(selected)
        for replicate, order in enumerate(selected, start=1):
            pair_specs.append((scenario, replicate, order))

    primary_counts = Counter(tuple(order) for s, r, order in pair_specs if s in PRIMARY)
    if len(primary_counts) != 6 or set(primary_counts.values()) != {3}:
        parser.error(f"internal primary order-balance error: {dict(primary_counts)}")

    s2_orders = [o[:] for o in rng.sample(orders, RUNS_PER_SCENARIO)]
    for replicate, order in enumerate(s2_orders, start=1):
        pair_specs.append(("S2", replicate, order))

    runs = [
        {
            "run_id": f"{scenario}-r{replicate}-{condition}",
            "scenario": scenario,
            "replicate": replicate,
            "condition": condition,
            "order": order,
        }
        for scenario, replicate, order in pair_specs
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
