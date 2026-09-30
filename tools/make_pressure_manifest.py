#!/usr/bin/env python3
"""Generate the seeded manifest for the Pressure Ladder pilot (protocol-v3.md).

Each scenario x run pair gets one of the six P1/P2/P3 orders; every order is
used exactly three times, and conditions A and C share the pair's order.
Execution order of all runs (both conditions) is shuffled with the same seed.
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

RUNS_PER_SCENARIO = 3
CONDITIONS = ["A", "C"]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--scenarios", required=True, type=Path)
    parser.add_argument("--seed", type=int, help="Reuse a recorded seed to regenerate the manifest.")
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    raw = args.scenarios.read_bytes()
    scenario_ids = [s["id"] for s in json.loads(raw)["scenarios"]]
    pairs = [(s, r) for s in scenario_ids for r in range(1, RUNS_PER_SCENARIO + 1)]
    orders = [list(p) for p in itertools.permutations(["P1", "P2", "P3"])]
    if len(pairs) != len(orders) * 3:
        parser.error(f"{len(pairs)} pairs cannot use each of {len(orders)} orders exactly 3 times")

    seed = args.seed if args.seed is not None else secrets.randbits(63)
    rng = random.Random(seed)
    assigned = [o for o in orders for _ in range(3)]
    rng.shuffle(assigned)

    runs = [
        {"run_id": f"{s}-r{r}-{c}", "scenario": s, "replicate": r, "condition": c, "order": order}
        for (s, r), order in zip(pairs, assigned)
        for c in CONDITIONS
    ]
    rng.shuffle(runs)
    for n, run in enumerate(runs, start=1):
        run["position"] = n

    manifest = {
        "experiment": "pressure-ladder-pilot",
        "protocol": "tests/pressure-ladder-pilot/protocol-v3.md",
        "scenarios_sha256": hashlib.sha256(raw).hexdigest(),
        "seed": seed,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "runs": runs,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Manifest: {args.output}  seed={seed}  runs={len(runs)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
