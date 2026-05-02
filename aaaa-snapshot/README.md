# AAAA snapshot

This directory will hold a **frozen copy** of the AAAA tag-author tool from the private origin repo.

> AAAA stands for **APEX Auto Attribute Adjust Array** — Python tooling that authors per-joint chain tags and IK role tags onto a `kinefx::rigattribwrangle` SOP, driven by an external rule JSON.

## Provenance

- **Origin:** `houdini_tools/aaaa/` (private repository, owner: same author as this repo).
- **Snapshot date:** TBD — set when the copy is performed.
- **Origin commit:** TBD — record the exact SHA at copy time.

The snapshot is **not auto-synced**. Each Python file copied in will carry a one-line provenance comment at its top:

```python
# Snapshot from houdini_tools/aaaa @ <date> (commit <sha>). Not auto-synced.
```

## What gets copied (planned)

- `__init__.py`, `errors.py`, `rules.py`, `vexgen.py`, `apply_houdini.py`, `dryrun.py`, `inventory.py`, `report.py`, `component_parms.py`
- `definitions/cc4_default.json`, `definitions/cc4_full.json` — example rule files
- A trimmed-down `README.md` adapted from origin's spec, focused on the public-consumption use case

## What does NOT get copied

- The five `PHASE_*.md` investigation logs (they contain noise specific to the origin investigation; their findings are absorbed into this repo's `docs/` instead)
- `IMPLEMENTATION_LOG.md`, `ISSUES.md` (origin-only project records)
- Test fixtures specific to the author's own asset (license-bound)

## Why a snapshot, not a submodule

- The origin repo is private and not intended for public release.
- AAAA is small (≤ 10 files); the cost of drift is low and the benefit of no external clone is high for LLM consumers.
- Treating this as a frozen tutorial snapshot matches the "investigation log" framing of the parent repo.

If AAAA evolves enough to warrant maintenance separation, the right move is to extract it to its own public repo (`aaaa-tags` or similar) and add it as a submodule here.

## License

Inherited from the origin repo. **TODO:** confirm and copy origin LICENSE here at snapshot time.
