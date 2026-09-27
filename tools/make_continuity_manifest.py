#!/usr/bin/env python3
"""Generate a randomized run manifest for one continuity-battery slice.

Probe and replicate order are shuffled independently per layer. R06 (run_last)
always comes last in each layer. The RNG seed is recorded so the manifest can
be regenerated exactly.
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

SLICE_RE = re.compile(r"^(smoke|T0|T0p|T[1-9][0-9]*|D-[A-Za-z0-9-]+)$")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--battery", required=True, type=Path)
    parser.add_argument("--slice", required=True, help="smoke, T0, T0p, T1, T2, … or D-<label>")
    parser.add_argument("--layers", required=True, help="Comma-separated, e.g. F,Q,P")
    parser.add_argument("--replicates", type=int, default=3)
    parser.add_argument(
        "--include-event",
        action="store_true",
        help="Include event-triggered probes (E01); only after a pre-defined update event.",
    )
    parser.add_argument("--seed", type=int, help="Reuse a recorded seed to regenerate a manifest.")
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    if not SLICE_RE.match(args.slice):
        parser.error(f"invalid slice label: {args.slice!r}")
    if args.replicates < 1:
        parser.error("--replicates must be >= 1")

    raw = args.battery.read_bytes()
    battery = json.loads(raw)
    probes = [
        p for p in battery["probes"] if args.include_event or not p.get("event_triggered")
    ]
    layers = [layer.strip() for layer in args.layers.split(",") if layer.strip()]

    seed = args.seed if args.seed is not None else secrets.randbits(63)
    rng = random.Random(seed)

    order: dict[str, list[dict]] = {}
    for layer in layers:
        items = [
            {"probe": p["id"], "replicate": r}
            for p in probes
            for r in range(1, args.replicates + 1)
        ]
        head = [i for i in items if not _run_last(probes, i["probe"])]
        tail = [i for i in items if _run_last(probes, i["probe"])]
        rng.shuffle(head)
        rng.shuffle(tail)
        order[layer] = [
            {"position": n, **item} for n, item in enumerate(head + tail, start=1)
        ]

    manifest = {
        "battery": battery["battery"],
        "battery_version": battery["version"],
        "battery_sha256": hashlib.sha256(raw).hexdigest(),
        "slice": args.slice,
        "replicates": args.replicates,
        "include_event": args.include_event,
        "seed": seed,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "layers": order,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Manifest: {args.output}  slice={args.slice}  seed={seed}")
    for layer, items in order.items():
        print(f"  {layer}: {len(items)} runs")
    return 0


def _run_last(probes: list[dict], probe_id: str) -> bool:
    return next(p for p in probes if p["id"] == probe_id).get("run_last", False)


if __name__ == "__main__":
    raise SystemExit(main())
