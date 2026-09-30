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

ROOT = Path(__file__).resolve().parent.parent
PRIMARY = ["S3", "S4", "S7", "S8", "S9", "S10"]
RELATIONAL = ["S2"]
VALIDATION = RELATIONAL + PRIMARY
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

    pressure_words = ("подтверди", "просто скажи", "согласись", "скажи, что всё отлично", "признай")
    for sid in VALIDATION:
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
    case10_card = load(ROOT / "configs" / "case10-rep02-persona-ru.json").get("system_prompt")
    continuity_card = load(ROOT / "configs" / "continuity-v1-q.json").get("system_prompt")
    if not case10_card or case10_card != continuity_card:
        errors.append("canonical Q. card sources disagree")
    if c.get("system_prompt") != case10_card:
        errors.append("C system_prompt differs from canonical Case 10 / continuity Q. card")

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
    if len(runs) != 84:
        errors.append(f"manifest has {len(runs)} runs, expected 84")
    if sorted(r.get("position") for r in runs) != list(range(1, len(runs) + 1)):
        errors.append("positions must be 1..84")
    if Counter(r.get("condition") for r in runs) != Counter({"A": 42, "C": 42}):
        errors.append("conditions must be 42 A / 42 C")

    run_ids = Counter(r.get("run_id") for r in runs)
    errors.extend(f"duplicate run_id {k}" for k, v in run_ids.items() if v > 1)

    block_orders: dict[tuple[str, int], set[tuple[str, ...]]] = defaultdict(set)
    block_conditions: dict[tuple[str, int], set[str]] = defaultdict(set)
    scenario_condition_orders: dict[tuple[str, str], list[tuple[str, ...]]] = defaultdict(list)

    for r in runs:
        sid = r["scenario"]
        rep = r["replicate"]
        cond = r["condition"]
        order = tuple(r["order"])
        if sid not in VALIDATION:
            errors.append("{}: unexpected scenario {}".format(r["run_id"], sid))
        if order not in ORDERS:
            errors.append("{}: invalid order {}".format(r["run_id"], order))
        block_orders[(sid, rep)].add(order)
        block_conditions[(sid, rep)].add(cond)
        scenario_condition_orders[(sid, cond)].append(order)

    if len(block_orders) != 42:
        errors.append(f"expected 42 scenario×replicate blocks, got {len(block_orders)}")
    for key, orders_here in block_orders.items():
        if len(orders_here) != 1:
            errors.append(f"{key}: A/C order mismatch")
        if block_conditions[key] != CONDITIONS:
            errors.append(f"{key}: conditions={block_conditions[key]}")

    for sid in VALIDATION:
        for cond in ("A", "C"):
            got = scenario_condition_orders[(sid, cond)]
            if len(got) != 6:
                errors.append(f"{sid}/{cond}: expected 6 runs, got {len(got)}")
            if set(got) != ORDERS:
                errors.append(f"{sid}/{cond}: must contain all six orders exactly once")

    if errors:
        for e in errors:
            print(f"ERROR: {e}")
        return 1
    card_sha = hashlib.sha256(case10_card.encode("utf-8")).hexdigest()
    print(
        f"OK: validation materials; seed={manifest['seed']}; "
        f"84 runs; every scenario fully crossed with six orders; Q-card sha256={card_sha}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
