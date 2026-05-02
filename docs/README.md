# Procedure docs

Each file is a self-contained phase. Read in order; re-run with your own assets.

| File | Phase | Status |
|---|---|---|
| `00_prerequisites.md` | Houdini, Python, MCP versions verified | TODO |
| `01_mcp_setup.md` | `houdini-mcp` fork + bug-fix status + PR link | TODO |
| `02_character_pipeline.md` | FBX char → `apex::packcharacter` | TODO |
| `03_aaaa_tags.md` | Per-joint chain + role tags via AAAA snapshot | TODO |
| `04_apex_components.md` | `fktransform` → `bonedeform` → `multiik` | TODO |
| `05_segments_setup.md` | The `parameters3` spare-parm trick | TODO |
| `06_animation_walkthrough.md` | FBX anim retarget + `bonedeform` walk | TODO |
| `99_open_questions.md` | APEX rig compile, `@path` write block, etc. | TODO |

Each file should follow this template (planning):

```
# Phase N — Title
**Goal:** one sentence.
**Inputs you provide:** ...
**Outputs you should see at the end:** ...
**LLM prompt:** -> prompts/N_*.md

## Procedure
1. Step
2. Step

## Verification
- [ ] checkable assertion 1
- [ ] checkable assertion 2

## What goes wrong
| Symptom | Cause | Fix |
```
