# Pressure Ladder v4 main — implementation freeze checklist

Collection is not authorized until the generated `main-freeze.md` exists on `main`.

Freeze-builder must pass, in order:

- [ ] compile `tools/pressure_main.py`;
- [ ] synthetic `smoke` passes all endpoint/retry/terminal-stop/permutation/decision branches;
- [ ] generate deterministic 348-slot manifest from reviewed scenario bytes;
- [ ] `check-design` confirms 5/5 primary and 2/2 control allocation per scenario × order;
- [ ] dry-run confirms sequential manifest execution plan;
- [ ] create clean-venv dependency snapshot;
- [ ] create SHA-256 checksum file covering every normative design/implementation file;
- [ ] create `main-freeze.md` recording pre-freeze head, manifest digest and authorization statement;
- [ ] commit generated freeze artifacts to `main`.

Live workflow must refuse to run if any checksum differs.
