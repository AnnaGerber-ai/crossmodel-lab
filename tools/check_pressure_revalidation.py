#!/usr/bin/env python3
"""Validate Pressure Ladder v4 targeted revalidation materials before collection."""

from __future__ import annotations
import argparse, hashlib, itertools, json, sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SCENARIOS=["S2","S8"]
EXPECTED_MODEL="qwen-flash-character"
EXPECTED_GENERATION={"temperature":0.7,"max_tokens":1536}
ORDERS=set(itertools.permutations(["P1","P2","P3"]))

def load(p:Path)->dict:
    return json.loads(p.read_text(encoding="utf-8"))

def main()->int:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--scenarios",required=True,type=Path)
    p.add_argument("--manifest",required=True,type=Path)
    p.add_argument("--config-a",required=True,type=Path)
    p.add_argument("--config-c",required=True,type=Path)
    a=p.parse_args()
    errors=[]

    raw=a.scenarios.read_bytes()
    obj=json.loads(raw)
    by={x["id"]:x for x in obj["scenarios"]}
    if set(by)!=set(SCENARIOS):
        errors.append(f"scenario set must be exactly {SCENARIOS}")

    # S2 text is intentionally unchanged from frozen validation.
    frozen=load(ROOT/"tests"/"pressure-ladder-v4-draft"/"scenarios-v2-draft.json")
    frozen_s2=next(x for x in frozen["scenarios"] if x["id"]=="S2")
    new_s2=by.get("S2",{})
    for field in ("T1","P2","P3","primary_proposition","held_anchor"):
        if new_s2.get(field)!=frozen_s2.get(field):
            errors.append(f"S2 {field} changed; revalidation must isolate the responsibility-anchor repair")

    s8=by.get("S8",{})
    if "150 км" not in s8.get("T1","") or "ровно час" not in s8.get("T1",""):
        errors.append("S8 T1 does not match revised 150 km exact-hour construct")
    if "примерно" in (s8.get("T1","")+" "+s8.get("P3","")).lower():
        errors.append("S8 revalidation must not reintroduce approximation wording")

    ca,cc=load(a.config_a),load(a.config_c)
    for name,cfg in (("A",ca),("C",cc)):
        if cfg.get("experiment")!="pressure-ladder-v4-revalidation":
            errors.append(f"{name}: wrong experiment")
        if cfg.get("condition")!=name:
            errors.append(f"{name}: condition mismatch")
        if cfg.get("model")!=EXPECTED_MODEL or cfg.get("generation")!=EXPECTED_GENERATION:
            errors.append(f"{name}: model/generation differs from frozen validation")
        if Path(cfg.get("scenarios",""))!=a.scenarios:
            errors.append(f"{name}: scenario path mismatch")
    if ca.get("system_prompt"):
        errors.append("A must have no system_prompt")
    case10=load(ROOT/"configs"/"case10-rep02-persona-ru.json").get("system_prompt")
    cont=load(ROOT/"configs"/"continuity-v1-q.json").get("system_prompt")
    if not case10 or case10!=cont:
        errors.append("canonical Q. card sources disagree")
    if cc.get("system_prompt")!=case10:
        errors.append("C card differs from canonical Q. card")

    m=load(a.manifest)
    if m.get("experiment")!="pressure-ladder-v4-revalidation":
        errors.append("manifest experiment mismatch")
    if m.get("scenarios_sha256")!=hashlib.sha256(raw).hexdigest():
        errors.append("manifest scenarios_sha256 mismatch")
    runs=m.get("runs",[])
    if len(runs)!=24:
        errors.append(f"expected 24 runs, got {len(runs)}")
    if Counter(r.get("condition") for r in runs)!=Counter({"A":12,"C":12}):
        errors.append("conditions must be 12 A / 12 C")
    if sorted(r.get("position") for r in runs)!=list(range(1,25)):
        errors.append("positions must be 1..24")
    if len({r.get("run_id") for r in runs})!=len(runs):
        errors.append("duplicate run_id")

    block_orders=defaultdict(set)
    block_conditions=defaultdict(set)
    sc_orders=defaultdict(set)
    for r in runs:
        sid=r.get("scenario"); cond=r.get("condition"); rep=r.get("replicate")
        order=tuple(r.get("order",[]))
        if sid not in SCENARIOS: errors.append(f"unexpected scenario {sid}")
        if order not in ORDERS: errors.append(f"{r.get('run_id')}: invalid order")
        block_orders[(sid,rep)].add(order)
        block_conditions[(sid,rep)].add(cond)
        sc_orders[(sid,cond)].add(order)
    if len(block_orders)!=12:
        errors.append(f"expected 12 scenario×replicate blocks, got {len(block_orders)}")
    for key,vals in block_orders.items():
        if len(vals)!=1: errors.append(f"{key}: A/C order mismatch")
        if block_conditions[key]!={"A","C"}: errors.append(f"{key}: missing A or C condition")
    for sid in SCENARIOS:
        for cond in ("A","C"):
            if sc_orders[(sid,cond)]!=ORDERS:
                errors.append(f"{sid}/{cond}: does not contain all six orders exactly once")

    if errors:
        for e in errors: print("ERROR:",e)
        return 1
    print(f"OK: targeted revalidation materials; seed={m['seed']}; 24 runs; all six orders per scenario/condition.")
    return 0

if __name__=="__main__":
    sys.exit(main())
