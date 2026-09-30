#!/usr/bin/env python3
"""Build separate blind position/warmth packets for targeted revalidation."""

from __future__ import annotations
import argparse, hashlib, json, random, re, secrets
from datetime import datetime, timezone
from pathlib import Path

Q_PREFIX=re.compile(r"^\s*(?:\*\*)?Q\s*(?:[.:]|[-–—])\s*(?:\*\*)?\s*")

def sha(b:bytes)->str: return hashlib.sha256(b).hexdigest()
def norm(s:str):
    m=Q_PREFIX.match(s)
    return (s[m.end():],s[:m.end()]) if m else (s,None)

def main()->int:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--raw",required=True,type=Path)
    p.add_argument("--seed",type=int)
    p.add_argument("--output-dir",required=True,type=Path)
    a=p.parse_args()

    raw=a.raw.read_bytes()
    rows=[json.loads(x) for x in raw.decode("utf-8").splitlines() if x.strip()]
    if len(rows)!=24: p.error(f"expected 24 raw rows, got {len(rows)}")
    if {r.get("scenario") for r in rows}!={"S2","S8"}: p.error("wrong scenario set")
    if len({r.get("run_id") for r in rows})!=24: p.error("duplicate run_id")
    if sum(r.get("condition")=="A" for r in rows)!=12 or sum(r.get("condition")=="C" for r in rows)!=12:
        p.error("raw conditions must be 12 A / 12 C")

    complete=[]; excluded=[]
    for r in rows:
        attempts=r.get("attempts",[])
        if not attempts: p.error(f"{r.get('run_id')}: no attempts")
        if r.get("status")=="censored_api_failure":
            excluded.append({k:r.get(k) for k in ("run_id","scenario","replicate","condition","order","position","status")})
            continue
        if r.get("status")!="ok": p.error(f"{r.get('run_id')}: unexpected status")
        turns=attempts[-1].get("turns",[])
        if len(turns)!=4: p.error(f"{r.get('run_id')}: expected 4 turns")
        labels=[t.get("label") for t in turns]
        if labels[0]!="T1" or sorted(labels[1:])!=["P1","P2","P3"]:
            p.error(f"{r.get('run_id')}: invalid turn labels {labels}")
        complete.append(r)

    seed=a.seed if a.seed is not None else secrets.randbits(63)
    rng=random.Random(seed); rng.shuffle(complete)
    pp=[]; wp=[]; bm=[]; n_norm=0
    for i,r in enumerate(complete,start=1):
        bid=f"PRV4-{i:03d}"; pt=[]; wt=[]; events=[]; upstream=False
        for t in r["attempts"][-1]["turns"]:
            assistant,prefix=norm(t.get("assistant") or "")
            if prefix is not None:
                n_norm+=1; events.append({"label":t["label"],"removed_prefix":prefix})
            trunc=bool(t.get("truncated"))
            pt.append({"label":t["label"],"user":t["user"],"assistant":assistant,"truncated":trunc,"upstream_truncated":upstream})
            wt.append({"label":t["label"],"user":t["user"],"assistant":assistant})
            upstream=upstream or trunc
        pp.append({"blind_id":bid,"scenario":r["scenario"],"turns":pt})
        wp.append({"blind_id":bid,"scenario":r["scenario"],"turns":wt})
        bm.append({"blind_id":bid,"run_id":r["run_id"],"condition":r["condition"],"scenario":r["scenario"],"replicate":r["replicate"],"order":r["order"],"manifest_position":r["position"],"normalization_events":events})

    a.output_dir.mkdir(parents=True,exist_ok=True)
    def write(name,rows):
        txt="".join(json.dumps(x,ensure_ascii=False)+"\n" for x in rows)
        (a.output_dir/name).write_text(txt,encoding="utf-8"); return txt
    ptxt=write("revalidation-position-packet.jsonl",pp)
    wtxt=write("revalidation-warmth-packet.jsonl",wp)
    mtxt=write("revalidation-blind-map.jsonl",bm)
    etxt=write("revalidation-packet-exclusions.jsonl",excluded)
    meta={
        "experiment":"pressure-ladder-v4-revalidation",
        "created_at":datetime.now(timezone.utc).isoformat(),
        "seed":seed,
        "raw_sha256":sha(raw),
        "position_packet_sha256":sha(ptxt.encode()),
        "warmth_packet_sha256":sha(wtxt.encode()),
        "blind_map_sha256":sha(mtxt.encode()),
        "exclusions_sha256":sha(etxt.encode()),
        "planned_rows":24,"raw_rows":len(rows),"packet_rows":len(pp),"excluded_rows":len(excluded),
        "normalization_events":n_norm,
        "normalization_rule":"response-initial optional-bold Q + ./:/-/–/—; whitespace after punctuation optional"
    }
    (a.output_dir/"revalidation-packet-meta.json").write_text(json.dumps(meta,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(f"OK: raw={len(rows)} packet={len(pp)} excluded={len(excluded)} seed={seed}")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
