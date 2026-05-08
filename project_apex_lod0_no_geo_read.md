---
name: APEX Character Project — TNCC3 is LOD0, do NOT read geometry
description: Test FBX TNCC3.Fbx is LOD0 (highest detail); reading geometry via MCP triggers context compact. Use disk dumps + summary printing only.
type: project
originSessionId: 3dae1e86-ce75-45dc-93d3-243046595ad7
---
**Fact:** The test FBX `C:\Users\azoo\git\houdini_tools\CC\TNCC3.Fbx` is **LOD0** (highest CC detail level — 19,987 skin pts / 19,530 prims / 7 meshes / 85-joint deformation skel). User confirmed 2026-05-04 after the post-compact resume.

**Why it matters:** Any MCP call that returns the full geometry stream (e.g., raw `get_points`, `get_prims` without filter, `execute_houdini_code` that prints prim/point lists) blows up stdout. With LOD0 the response is large enough to consume the context window and trigger an automatic compact mid-task — which has high recovery cost (snapshot file write, re-read, etc.).

**How to apply:**
- For any geometry inspection: write the data to a JSON file on disk first (e.g., `C:\Users\azoo\git\houdini_tools\__probe_*.json`), then print only a compact summary (counts, first-N samples, type histograms).
- Patterns proven safe so far: total_prims count, packed prim names list (≤10 unique), apex.Graph node_count + node_types histogram + first-20-names sample, parameter readbacks.
- Patterns that already caused trouble: dumping raw `intrinsicValue('packedprimname')` for all 19,533 prims (mostly empty strings), printing full pCaptPath arrays, full point/prim enumerations.
- If a probe must return many strings (e.g., bone names), filter or limit before printing — never `json.dumps` an unbounded list to stdout.
- This applies to any future LOD0 CC FBX (CC4 full character at LOD0 will be in the same scale or larger).
