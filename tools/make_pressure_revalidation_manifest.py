#!/usr/bin/env python3
"""Generate a seeded manifest for Pressure Ladder v4 targeted revalidation."""

from __future__ import annotations
import argparse, hashlib, itertools, json, random, secrets
from datetime import datetime, timezone
from pathlib import Path

SCENARIOS = ["S2", "S8"]
CONDITIONS = ["A", "C"]

def main() -> int:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--scenarios", required=True, type=Path)
    p.add_argument("--seed", type=int)
    p.add_argument("--output", required=True, type=Path)
    a=p.parse_args()

    raw=a.scenarios.read_bytes()
    obj=json.loads(raw)
    available={x["id"] for x in obj["scenarios"]}
    if available != set(SCENARIOS):
        p.error(f"expected exactly {SCENARIOS}, got {sorted(available)}")

    seed=a.seed if a.seed is not None else secrets.randbits(63)
    rng=random.Random(seed)
    orders=[list(x) for x in itertools.permutations(["P1","P2","P3"])]

    runs=[]
    for sid in SCENARIOS:
        local=[x[:] for x in orders]
        rng.shuffle(local)
        for rep, order in enumerate(local, start=1):
            for condition in CONDITIONS:
                runs.append({
                    "run_id": f"{sid}-r{rep}-{condition}",
                    "scenario": sid,
                    "replicate": rep,
                    "condition": condition,
                    "order": order,
                })
    rng.shuffle(runs)
    for i,r in enumerate(runs,start=1):
        r["position"]=i

    manifest={
        "experiment":"pressure-ladder-v4-revalidation",
        "status":"revalidation-draft",
        "protocol":"tests/pressure-ladder-v4-revalidation/revalidation-plan-v1.md",
        "scenarios":str(a.scenarios),
        "scenarios_sha256":hashlib.sha256(raw).hexdigest(),
        "seed":seed,
        "created_at":datetime.now(timezone.utc).isoformat(),
        "scenarios_in_scope":SCENARIOS,
        "runs":runs,
    }
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(f"Manifest: {a.output} seed={seed} runs={len(runs)}")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
