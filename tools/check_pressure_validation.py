#!/usr/bin/env python3
"""Validate Pressure Ladder v4 validation materials before collection."""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

PRIMARY = ["S3", "S4", "S7", "S8", "S9", "S10"]
RELATIONAL = ["S2"]
CONDITIONS = {"A", "C"}
EXPECTED_GENERATION = {"temperature": 0.7, "max_tokens": 1536}
EXPECTED_MODEL = "qwen-flash-character"
ORDERS = set(itertools.permutations(["P1", "P2", "P3"]))


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--scenarios", required=True, type=Path)
    parser.add_argument("--manifest", required=True, type=Path)
    parser.add_argument("--config-a", required=True, type=Path)
    parser.add_argument("--config-c", required=True, type=Path)
    args = parser.parse_args()

    errors: list[str] = []
    raw = args.scenarios.read_bytes()
    scenario_file = json.loads(raw)
    by_id = {s["id"]: s for s in scenario_file["scenarios"]}

    for sid in PRIMARY:
        if sid not in by_id:
            errors.append(f"missing primary scenario {sid}")
        elif by_id[sid].get("set") != "factual_primary":
            errors.append(f"{sid}: expected set=factual_primary")
    if "S2" not in by_id or by_id.get("S2", {}).get("set") != "relational_grounding_control":
        errors.append("S2 must be relational_grounding_control")

    pressure_words = ("подтверди", "просто скажи", "согласись", "скажи, что всё отлично")
    for sid in PRIMARY:
        text = by_id.get(sid, {}).get("T1", "").lower()
        bad = [x for x in pressure_words if x in text]
        if bad:
            errors.append(f"{sid}: T1 contains pressure wording {bad}")

    a, c = load(args.config_a), load(args.config_c)
    for name, cfg in (("A", a), ("C", c)):
        if cfg.get("experiment") != "pressure-ladder-v4-validation":
            errors.append(f"{name}: wrong experiment")
        if cfg.get("condition") != name:
            errors.append(f"{name}: condition={cfg.get('condition')!r}")
        if cfg.get("model") != EXPECTED_MODEL:
            errors.append(f"{name}: model={cfg.get('model')!r}")
        if cfg.get("generation") != EXPECTED_GENERATION:
            errors.append(f"{name}: generation={cfg.get('generation')!r}")
        if Path(cfg.get("scenarios", "")) != args.scenarios:
            errors.append(f"{name}: config scenario path differs from --scenarios")
    if a.get("system_prompt"):
        errors.append("A must have no system_prompt")
    if not c.get("system_prompt"):
        errors.append("C must have the Q. system_prompt")

    manifest = load(args.manifest)
    if manifest.get("experiment") != "pressure-ladder-v4-validation":
        errors.append("manifest experiment mismatch")
    if manifest.get("scenarios_sha256") != hashlib.sha256(raw).hexdigest():
        errors.append("manifest scenarios_sha256 mismatch")
    if manifest.get("primary_scenarios") != PRIMARY:
        errors.append("manifest primary_scenarios mismatch")
    if manifest.get("relational_control_scenarios") != RELATIONAL:
        errors.append("manifest relational_control_scenarios mismatch")

    runs = manifest.get("runs", [])
    if len(runs) != 42:
        errors.append(f"manifest has {len(runs)} runs, expected 42")
    if sorted(r.get("position") for r in runs) != list(range(1, len(runs) + 1)):
        errors.append("positions must be 1..42")
    if Counter(r.get("condition") for r in runs) != Counter({"A": 21, "C": 21}):
        errors.append("conditions must be 21 A / 21 C")

    run_ids = Counter(r.get("run_id") for r in runs)
    errors.extend(f"duplicate run_id {k}" for k, v in run_ids.items() if v > 1)

    pair_orders: dict[tuple[str, int], set[tuple[str, ...]]] = defaultdict(set)
    pair_conditions: dict[tuple[str, int], set[str]] = defaultdict(set)
    for r in runs:
        key = (r["scenario"], r["replicate"])
        order = tuple(r["order"])
        if order not in ORDERS:
            errors.append(f"{r['run_id']}: invalid order {order}")
        pair_orders[key].add(order)
        pair_conditions[key].add(r["condition"])

    if len(pair_orders) != 21:
        errors.append(f"expected 21 scenario×replicate pairs, got {len(pair_orders)}")
    for key in pair_orders:
        if len(pair_orders[key]) != 1:
            errors.append(f"{key}: A/C order mismatch")
        if pair_conditions[key] != CONDITIONS:
            errors.append(f"{key}: conditions={pair_conditions[key]}")

    # Primary: 18 pairs, each order exactly 3 times, each scenario 3 distinct.
    primary_pair_rows = []
    for (sid, rep), os in pair_orders.items():
        if sid in PRIMARY and len(os) == 1:
            primary_pair_rows.append((sid, rep, next(iter(os))))
    if len(primary_pair_rows) != 18:
        errors.append(f"expected 18 primary pairs, got {len(primary_pair_rows)}")
    counts = Counter(order for sid, rep, order in primary_pair_rows)
    if len(counts) != 6 or set(counts.values()) != {3}:
        errors.append(f"primary order counts must all equal 3, got {dict(counts)}")
    for sid in PRIMARY:
        scenario_orders = {order for s, rep, order in primary_pair_rows if s == sid}
        if len(scenario_orders) != 3:
            errors.append(f"{sid}: expected 3 distinct orders, got {len(scenario_orders)}")

    s2_orders = {next(iter(os)) for (sid, rep), os in pair_orders.items() if sid == "S2" and len(os) == 1}
    if len(s2_orders) != 3:
        errors.append(f"S2: expected 3 distinct orders, got {len(s2_orders)}")

    unexpected = sorted({r["scenario"] for r in runs} - set(PRIMARY + RELATIONAL))
    if unexpected:
        errors.append(f"unexpected validation scenarios: {unexpected}")

    if errors:
        for e in errors:
            print(f"ERROR: {e}")
        return 1
    print(
        f"OK: validation materials; seed={manifest['seed']}; "
        "42 runs, 18 primary pairs balanced 3x/order, S2 3 distinct orders."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
