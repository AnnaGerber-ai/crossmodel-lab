#!/usr/bin/env python3
"""Check a P.jsonl file for one continuity slice (pre-scoring addendum v1).

Per record:
- required keys and the fixed P values of the runner-compatible keys;
- record_id agrees with slice/probe/replicate/attempt;
- user turns are counted and compared with the canonical battery wording;
- structured facts (comparison UI, settings, memory, cleanup) carry the matching deviation codes;
- a scored attempt is completed and has no blocking/invalidating deviation (addendum §A6).

Across records (with --manifest):
- every P manifest item is present, with the manifest position;
- at most one scored attempt per replicate; none only when the replicate is marked unscorable;
- restarts point to the attempt they supersede;
- R06 attempts run after every other probe, unless ORDER.R06_NOT_LAST is logged.

Optional --grounding: every scored P R03/R07 attempt has a grounding annotation (§A9).

If the `jsonschema` package is installed, each record is also validated against
p-jsonl-schema-v1.json. This tool never prints assistant text.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BATTERY_DIR = ROOT / "tests" / "longitudinal-assistant-continuity"
SCHEMA_PATH = BATTERY_DIR / "p-jsonl-schema-v1.json"
RECORD_ID_RE = re.compile(r"^(?P<slice>[^:]+):P:(?P<probe>[A-Z][0-9]{2}):r(?P<rep>[0-9]+):a(?P<att>[0-9]+)$")
FIXED = {
    "experiment": "longitudinal-assistant-continuity",
    "battery_version": "v1",
    "layer": "P",
    "model_requested": None,
    "model_kind": "consumer_app",
    "endpoint": None,
    "card_sha256": None,
    "generation": None,
    "truncated": False,
}
NOT_SCORABLE = {"blocking", "invalidating"}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("p_jsonl", type=Path)
    parser.add_argument("--manifest", type=Path, help="Slice manifest from make_continuity_manifest.py")
    parser.add_argument("--battery", type=Path, default=BATTERY_DIR / "battery-v1.json")
    parser.add_argument("--grounding", type=Path, help="P-grounding.jsonl for the same slice")
    args = parser.parse_args()

    errors: list[str] = []
    warnings: list[str] = []

    battery_raw = args.battery.read_bytes()
    battery_sha = hashlib.sha256(battery_raw).hexdigest()
    probes = {p["id"]: p for p in json.loads(battery_raw)["probes"]}
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    required = schema["required"]
    known_codes = set(schema["$defs"]["deviation"]["properties"]["code"]["enum"])
    validator = _schema_validator(schema)
    if validator is None:
        warnings.append("jsonschema not installed: per-record shape checked for required keys only")

    records: list[dict] = []
    for n, line in enumerate(args.p_jsonl.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            records.append(json.loads(line))
        except json.JSONDecodeError as exc:
            errors.append(f"line {n}: invalid JSON ({exc.msg})")
    if not records:
        errors.append("no records")

    for rec in records:
        rid = rec.get("record_id", "<no record_id>")
        where = f"{rid}"
        missing = [k for k in required if k not in rec]
        if missing:
            errors.append(f"{where}: missing keys {missing}")
            continue
        if validator is not None:
            for err in sorted(validator.iter_errors(rec), key=lambda e: list(e.path)):
                path = "/".join(str(p) for p in err.path) or "<record>"
                errors.append(f"{where}: schema: {path}: {err.message[:160]}")
        errors.extend(f"{where}: {msg}" for msg in _check_record(rec, probes, battery_sha, known_codes))

    ids = Counter(r.get("record_id") for r in records)
    errors.extend(f"duplicate record_id {rid}" for rid, c in ids.items() if c > 1)
    seqs = Counter(r.get("executed_seq") for r in records)
    errors.extend(f"duplicate executed_seq {s}" for s, c in seqs.items() if c > 1)
    for key in ("slice", "manifest_seed"):
        values = {r.get(key) for r in records}
        if len(values) > 1:
            errors.append(f"records disagree on {key}: {sorted(map(str, values))}")

    by_item: dict[tuple[str, int], list[dict]] = defaultdict(list)
    for rec in records:
        by_item[(rec.get("probe"), rec.get("replicate"))].append(rec)
    for (probe, rep), attempts in sorted(by_item.items(), key=lambda kv: (str(kv[0][0]), kv[0][1] or 0)):
        errors.extend(f"{probe} r{rep}: {msg}" for msg in _check_item(attempts))

    if args.manifest:
        errors.extend(_check_manifest(args.manifest, records, by_item, battery_sha))
    errors.extend(_check_order(records))

    if args.grounding:
        errors.extend(_check_grounding(args.grounding, records))

    _print_summary(records)
    for w in warnings:
        print(f"WARNING: {w}")
    if errors:
        for e in errors:
            print(f"ERROR: {e}")
        print(f"FAILED: {len(errors)} error(s)")
        return 1
    print("OK")
    return 0


def _schema_validator(schema: dict):
    try:
        import jsonschema  # type: ignore
    except ImportError:
        return None
    return jsonschema.Draft202012Validator(schema)


def _codes(rec: dict) -> set[str]:
    return {d.get("code") for d in rec.get("deviations", [])}


def _check_record(rec: dict, probes: dict, battery_sha: str, known_codes: set[str]) -> list[str]:
    out: list[str] = []
    for key, value in FIXED.items():
        if rec.get(key) != value:
            out.append(f"{key} must be {value!r} for P")
    if rec["battery_sha256"] != battery_sha:
        out.append("battery_sha256 does not match battery-v1.json")

    m = RECORD_ID_RE.match(rec["record_id"])
    if not m:
        out.append("record_id must be <slice>:P:<probe>:r<replicate>:a<attempt>")
    elif (m["slice"], m["probe"], int(m["rep"]), int(m["att"])) != (
        rec["slice"], rec["probe"], rec["replicate"], rec["attempt"]
    ):
        out.append("record_id disagrees with slice/probe/replicate/attempt")

    probe = probes.get(rec["probe"])
    if probe is None:
        return out + [f"unknown probe {rec['probe']}"]
    if rec["block"] != probe["block"]:
        out.append(f"block {rec['block']!r} != battery block {probe['block']!r}")
    if probe.get("event_triggered") and rec["slice"] in ("T0", "T0p"):
        out.append("E01 is not collected at T0/T0p")

    canonical = probe["user_turns"]
    turns = rec["turns"]
    if [t.get("turn") for t in turns] != list(range(1, len(turns) + 1)):
        out.append("turn numbers must be 1..n in order")
    if len(turns) > len(canonical) and "CONTENT.EXTRA_TURN" not in _codes(rec):
        out.append(f"{len(turns)} turns for a {len(canonical)}-turn probe without CONTENT.EXTRA_TURN")
    for t in turns:
        i = t.get("turn", 0) - 1
        if 0 <= i < len(canonical):
            matches = t.get("user") == canonical[i]
            if t.get("user_matches_canonical") != matches:
                out.append(f"turn {i + 1}: user_matches_canonical should be {matches}")
            if not matches and not _codes(rec) & {"CONTENT.WORDING_TYPO", "CONTENT.WORDING_SEMANTIC"}:
                out.append(f"turn {i + 1}: user text differs from canonical without a CONTENT.WORDING_* deviation")
        if t.get("finish_reason") is not None or t.get("truncated") is not False:
            out.append(f"turn {t.get('turn')}: P has finish_reason=null and truncated=false; use product_incomplete")
        if t.get("product_incomplete") and "CONTENT.PRODUCT_INCOMPLETE" not in _codes(rec):
            out.append(f"turn {t.get('turn')}: product_incomplete without CONTENT.PRODUCT_INCOMPLETE")
        ui = t.get("ui", {})
        if ui.get("comparison_shown"):
            dev = [d for d in rec["deviations"] if d.get("code") == "UI.COMPARISON"]
            if not dev:
                out.append(f"turn {t.get('turn')}: comparison UI shown without UI.COMPARISON")
            if len(ui.get("candidates", [])) < 2:
                out.append(f"turn {t.get('turn')}: comparison UI needs both candidates archived")
            if ui.get("selected_by") == "user" and not any(d.get("severity") == "invalidating" for d in dev):
                out.append(f"turn {t.get('turn')}: user-selected comparison candidate must be invalidating (§A12)")
        if ui.get("regenerated") and "ATTEMPT.REGENERATE" not in _codes(rec):
            out.append(f"turn {t.get('turn')}: regenerated without ATTEMPT.REGENERATE")
        if ui.get("user_message_edited") and "ATTEMPT.USER_EDIT" not in _codes(rec):
            out.append(f"turn {t.get('turn')}: edited message without ATTEMPT.USER_EDIT")

    if rec["attempt_status"] == "completed":
        if len(turns) < len(canonical):
            out.append("completed attempt has fewer turns than the probe")
        if any(t.get("assistant") is None for t in turns):
            out.append("completed attempt has a turn without an assistant answer")

    for d in rec["deviations"]:
        if d.get("code") not in known_codes:
            out.append(f"unknown deviation code {d.get('code')!r}")
    if rec["attempt"] > 1 and "ATTEMPT.RESTART" not in _codes(rec):
        out.append("attempt > 1 without ATTEMPT.RESTART")
    if "ATTEMPT.RESTART" in _codes(rec) and not rec.get("supersedes"):
        out.append("ATTEMPT.RESTART needs 'supersedes'")

    product = rec["product"]
    if not (product.get("canon_on") and product.get("saved_memories_on") and product.get("chat_history_on")):
        if "ENV.SETTING_OFF" not in _codes(rec):
            out.append("a required product setting is off without ENV.SETTING_OFF")
    if product.get("model_label_visible") != "Qwen3.7-Plus" and "ENV.MODEL_LABEL_CHANGED" not in _codes(rec):
        out.append("model label is not Qwen3.7-Plus without ENV.MODEL_LABEL_CHANGED")

    memory = rec["memory"]
    for item in memory.get("created", []):
        if item.get("expected") and rec["probe"] != "R06":
            out.append("memory marked expected outside R06")
        if not item.get("expected") and "MEMORY.CREATED_UNEXPECTED" not in _codes(rec):
            out.append("unexpected memory without MEMORY.CREATED_UNEXPECTED")
        if item.get("expected") and "MEMORY.CREATED_EXPECTED" not in _codes(rec):
            out.append("expected memory without MEMORY.CREATED_EXPECTED")
    if memory.get("preexisting_modified") and "MEMORY.PREEXISTING_MODIFIED" not in _codes(rec):
        out.append("preexisting_modified without MEMORY.PREEXISTING_MODIFIED")

    cleanup = rec["cleanup"]
    if not cleanup.get("chat_deleted") and "CLEANUP.DELETE_FAILED" not in _codes(rec):
        out.append("chat not deleted without CLEANUP.DELETE_FAILED")
    if cleanup.get("chat_deleted") and not cleanup.get("deleted_before_next_attempt"):
        if "CLEANUP.DELETE_DELAYED" not in _codes(rec):
            out.append("chat deleted late without CLEANUP.DELETE_DELAYED")

    if rec["is_scored_attempt"]:
        selective = "ATTEMPT.SELECTIVE_STOP" in _codes(rec)
        if rec["attempt_status"] != "completed" and not selective:
            out.append("scored attempt must be completed (§A6)")
        blocking = sorted(
            d.get("code") for d in rec["deviations"]
            if d.get("severity") in NOT_SCORABLE and d.get("code") != "ATTEMPT.SELECTIVE_STOP"
        )
        if blocking:
            out.append(f"scored attempt carries blocking/invalidating deviations {blocking}")
    return out


def _check_item(attempts: list[dict]) -> list[str]:
    out: list[str] = []
    attempts = sorted(attempts, key=lambda r: r.get("attempt", 0))
    numbers = [r.get("attempt") for r in attempts]
    if numbers != list(range(1, len(attempts) + 1)):
        out.append(f"attempt numbers must be 1..k, got {numbers}")
    ids = {r.get("record_id") for r in attempts}
    for r in attempts:
        if r.get("supersedes") and r["supersedes"] not in ids:
            out.append(f"{r.get('record_id')}: supersedes unknown record {r['supersedes']}")
    seq = [r.get("executed_seq", 0) for r in attempts]
    if seq != sorted(seq):
        out.append("later attempts must run after earlier ones")

    scored = [r for r in attempts if r.get("is_scored_attempt")]
    selective = [r for r in attempts if "ATTEMPT.SELECTIVE_STOP" in _codes(r)]
    unscorable = any(
        d.get("handling") == "replicate_unscorable" for r in attempts for d in r.get("deviations", [])
    )
    if len(scored) > 1:
        out.append(f"{len(scored)} scored attempts; exactly one allowed")
    if not scored and not unscorable:
        out.append("no scored attempt and no replicate_unscorable deviation")
    if scored and unscorable:
        out.append("scored attempt present but the replicate is marked unscorable")
    if selective and scored and scored[0] is not selective[0]:
        out.append("after ATTEMPT.SELECTIVE_STOP the first stopped attempt must be the scored one (§A6)")
    if scored and not selective:
        for r in attempts:
            if r is scored[0]:
                break
            if r.get("attempt_status") == "completed" and not any(
                d.get("severity") in NOT_SCORABLE for d in r.get("deviations", [])
            ):
                out.append(f"{r.get('record_id')}: earlier clean completed attempt was skipped (§A6)")
    return out


def _check_manifest(path: Path, records: list[dict], by_item: dict, battery_sha: str) -> list[str]:
    out: list[str] = []
    manifest = json.loads(path.read_text(encoding="utf-8"))
    if manifest.get("battery_sha256") != battery_sha:
        out.append("manifest battery_sha256 does not match battery-v1.json")
    items = manifest.get("layers", {}).get("P")
    if not items:
        return out + ["manifest has no P layer"]
    for rec in records:
        if rec.get("slice") != manifest.get("slice"):
            out.append(f"{rec.get('record_id')}: slice differs from manifest {manifest.get('slice')!r}")
            break
    for rec in records:
        if rec.get("manifest_seed") != manifest.get("seed"):
            out.append(f"{rec.get('record_id')}: manifest_seed differs from manifest")
            break
    expected = {(i["probe"], i["replicate"]): i["position"] for i in items}
    for key, position in sorted(expected.items()):
        attempts = by_item.get(key)
        if not attempts:
            out.append(f"{key[0]} r{key[1]}: in manifest but missing from P.jsonl")
            continue
        for r in attempts:
            if r.get("position") != position:
                out.append(f"{r.get('record_id')}: position {r.get('position')} != manifest {position}")
    for key in by_item.keys() - expected.keys():
        out.append(f"{key[0]} r{key[1]}: not in the P manifest")
    return out


def _check_order(records: list[dict]) -> list[str]:
    out: list[str] = []
    r06 = [r.get("executed_seq", 0) for r in records if r.get("probe") == "R06"]
    other = [r.get("executed_seq", 0) for r in records if r.get("probe") != "R06"]
    if r06 and other and min(r06) < max(other):
        logged = any("ORDER.R06_NOT_LAST" in _codes(r) for r in records)
        if not logged:
            out.append("an R06 attempt ran before another probe without ORDER.R06_NOT_LAST")

    firsts = sorted((r for r in records if r.get("attempt") == 1), key=lambda r: r.get("executed_seq", 0))
    for prev, cur in zip(firsts, firsts[1:]):
        if cur.get("position", 0) < prev.get("position", 0) and "ORDER.OUT_OF_ORDER" not in _codes(cur):
            out.append(f"{cur.get('record_id')}: runs out of manifest order without ORDER.OUT_OF_ORDER")
    return out


def _check_grounding(path: Path, records: list[dict]) -> list[str]:
    out: list[str] = []
    annotated: dict[str, dict] = {}
    for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError as exc:
            out.append(f"grounding line {n}: invalid JSON ({exc.msg})")
            continue
        annotated[row.get("record_id")] = row
        for claim in row.get("claims", []):
            if claim.get("verdict") not in ("true", "false", "unverifiable"):
                out.append(f"grounding {row.get('record_id')}: bad verdict {claim.get('verdict')!r}")
            if claim.get("source") not in ("canon", "saved_memory", "chat_history", "none", "unknown"):
                out.append(f"grounding {row.get('record_id')}: bad source {claim.get('source')!r}")
    needed = {
        r["record_id"] for r in records
        if r.get("probe") in ("R03", "R07") and r.get("is_scored_attempt")
    }
    out.extend(f"{rid}: scored R03/R07 attempt has no grounding annotation" for rid in sorted(needed - annotated.keys()))
    out.extend(f"grounding {rid}: not a scored P R03/R07 attempt" for rid in sorted(annotated.keys() - needed))
    return out


def _print_summary(records: list[dict]) -> None:
    status = Counter(r.get("attempt_status") for r in records)
    scored = sum(1 for r in records if r.get("is_scored_attempt"))
    comparison = sum(
        1 for r in records if any(t.get("ui", {}).get("comparison_shown") for t in r.get("turns", []))
    )
    restarts = sum(1 for r in records if (r.get("attempt") or 1) > 1)
    codes = Counter(d.get("code") for r in records for d in r.get("deviations", []))
    print(f"Records: {len(records)} attempts  {dict(status)}  scored={scored}")
    print(f"Comparison UI: {comparison}/{len(records)} attempts  restarts={restarts}")
    for code, count in sorted(codes.items()):
        print(f"  {code}: {count}")


if __name__ == "__main__":
    sys.exit(main())
