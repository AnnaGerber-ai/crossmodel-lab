# Pressure Ladder v4 main — implementation freeze checklist v1.2

Collection is not authorized until `main-freeze-v1.2.md` and `freeze-checksums-v1.2.sha256` exist on `main` and the live workflow verifies them successfully before any API call.

Freeze builder must pass, in order:

- [x] external v1.2 code↔protocol audit verdict: `V1.2 IMPLEMENTATION AUDIT PASSED`;
- [ ] compile `tools/pressure_main.py`;
- [ ] synthetic `smoke` passes endpoint/retry/terminal-stop/schema/attempt-log/permutation/decision branches;
- [ ] deterministic 348-slot manifest remains byte-identical;
- [ ] `check-design` confirms 5/5 primary and 2/2 control allocation per scenario × order;
- [ ] dry-run confirms sequential manifest execution plan;
- [ ] one-time collection dispatch policy and main-ref guard are frozen;
- [ ] synthetic non-battery API preflight is positioned before the one-time collection claim;
- [ ] exact dependency snapshot includes JSON-Schema validation dependencies;
- [ ] SHA-256 checksum file covers every normative design/implementation file for v1.2;
- [ ] `main-freeze-v1.2.md` records the prospective implementation head, audit result, manifest digest, runner digest, policy replacements and authorization statement;
- [ ] final candidate CI passes on Python 3.12;
- [ ] temporary candidate/audit CI is not part of the normative freeze and is removed before merge;
- [ ] final v1.2 artifacts are committed to `main`.

The live collection workflow must refuse to run if any v1.2 checksum differs.

Historical v1/v1.1 freeze files are provenance only and do not authorize collection.
