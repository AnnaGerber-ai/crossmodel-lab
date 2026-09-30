#!/usr/bin/env python3
"""Build blinded Pressure Ladder v4 validation packets from completed raw JSONL.

The builder never prints response text. It requires complete four-turn runs,
applies only the frozen response-initial Q signature normalization, creates a
seeded shuffle, and writes a private blind map plus packet metadata.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import random
import re
import secrets
from datetime import datetime, timezone
from pathlib import Path

Q_PREFIX = re.compile(r"^\s*Q(?:\.|:|\s+[—-])\s+")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def normalize_response(text: str) -> tuple[str, str | None]:
    m = Q_PREFIX.match(text)
    if not m:
        return text, None
    return text[m.end():], text[:m.end()]


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--raw", required=True, type=Path)
    p.add_argument("--scenarios", required=True, type=Path)
    p.add_argument("--seed", type=int)
    p.add_argument("--output-dir", required=True, type=Path)
    args = p.parse_args()

    raw_bytes = args.raw.read_bytes()
    rows = [json.loads(line) for line in raw_bytes.decode("utf-8").splitlines() if line.strip()]
    if len(rows) != 42:
        p.error(f"expected 42 raw runs, got {len(rows)}")

    scenario_file = json.loads(args.scenarios.read_text(encoding="utf-8"))
    scenario_ids = {s["id"] for s in scenario_file["scenarios"]}
    expected_validation = {"S2", "S3", "S4", "S7", "S8", "S9", "S10"}

    run_ids = [r.get("run_id") for r in rows]
    if len(set(run_ids)) != len(run_ids):
        p.error("duplicate run_id in raw")
    if {r.get("scenario") for r in rows} != expected_validation:
        p.error("raw scenario set does not match validation set")
    if not expected_validation <= scenario_ids:
        p.error("scenario file is missing validation scenarios")

    for r in rows:
        if r.get("status") != "ok":
            p.error(f"{r.get('run_id')}: status={r.get('status')}; close technical gate before packet build")
        attempts = r.get("attempts", [])
        if not attempts:
            p.error(f"{r.get('run_id')}: no attempts")
        turns = attempts[-1].get("turns", [])
        if len(turns) != 4:
            p.error(f"{r.get('run_id')}: expected 4 final turns, got {len(turns)}")
        labels = [t.get("label") for t in turns]
        if labels[0] != "T1" or sorted(labels[1:]) != ["P1", "P2", "P3"]:
            p.error(f"{r.get('run_id')}: invalid turn labels {labels}")

    seed = args.seed if args.seed is not None else secrets.randbits(63)
    rng = random.Random(seed)
    shuffled = rows[:]
    rng.shuffle(shuffled)

    packet = []
    blind_map = []
    normalized_count = 0

    for i, r in enumerate(shuffled, start=1):
        blind_id = f"PV4-{i:03d}"
        turns_out = []
        norm_events = []
        final_turns = r["attempts"][-1]["turns"]
        for t in final_turns:
            assistant, prefix = normalize_response(t.get("assistant") or "")
            if prefix is not None:
                normalized_count += 1
                norm_events.append({"label": t["label"], "removed_prefix": prefix})
            turns_out.append({
                "label": t["label"],
                "user": t["user"],
                "assistant": assistant,
                "truncated": bool(t.get("truncated")),
            })

        packet.append({
            "blind_id": blind_id,
            "scenario": r["scenario"],
            "turns": turns_out,
        })
        blind_map.append({
            "blind_id": blind_id,
            "run_id": r["run_id"],
            "condition": r["condition"],
            "scenario": r["scenario"],
            "replicate": r["replicate"],
            "order": r["order"],
            "manifest_position": r["position"],
            "normalization_events": norm_events,
        })

    args.output_dir.mkdir(parents=True, exist_ok=True)
    packet_path = args.output_dir / "validation-blind-packet.jsonl"
    map_path = args.output_dir / "validation-blind-map.jsonl"
    meta_path = args.output_dir / "validation-packet-meta.json"

    packet_text = "".join(json.dumps(x, ensure_ascii=False) + "\n" for x in packet)
    map_text = "".join(json.dumps(x, ensure_ascii=False) + "\n" for x in blind_map)
    packet_path.write_text(packet_text, encoding="utf-8")
    map_path.write_text(map_text, encoding="utf-8")

    meta = {
        "experiment": "pressure-ladder-v4-validation",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "seed": seed,
        "raw_sha256": sha256_bytes(raw_bytes),
        "scenarios_sha256": sha256_bytes(args.scenarios.read_bytes()),
        "packet_sha256": sha256_bytes(packet_text.encode("utf-8")),
        "blind_map_sha256": sha256_bytes(map_text.encode("utf-8")),
        "rows": len(packet),
        "normalization_events": normalized_count,
        "normalization_rule": "response-initial standalone Q. / Q: / Q — / Q - plus following whitespace only",
    }
    meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(
        f"OK: rows={len(packet)} seed={seed} normalization_events={normalized_count} "
        f"packet_sha256={meta['packet_sha256']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
