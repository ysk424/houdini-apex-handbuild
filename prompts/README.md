# LLM prompts

Copy-paste prompts for code-capable LLMs (Claude Code, Gemini Code, GPT Codex). Each file is **executable as-is** — concrete node paths, exact Python blocks, no ambiguous instructions like "set up the rig."

## Conventions

- **Absolute Houdini node paths** (e.g. `/obj/geo1/tag_skeleton`) — placeholders in the form `<NODE_PATH>` flag values the user must substitute.
- **Inline Python** in fenced blocks. Run via the LLM's MCP tool of choice (e.g. `mcp__houdini__execute_houdini_code`).
- **Idempotent**. Each prompt can be re-run without breaking state.
- **One phase per file.** No prompt should expand into dependencies; instead chain them via `prompts/00_overview.md`.

## Template

```markdown
# Phase N — <action>

**Pre-state:** <node X exists, parm Y set>
**Post-state:** <what's true after>

## Run

```python
# Exact Python that the LLM should send via execute_houdini_code (or equivalent).
# No abstractions, no helper functions unless they live in scripts/.
```

## Verify

```python
# A short read-back probe. The LLM should report whether each assertion holds.
```

## On failure

Map symptom → fix. If the symptom doesn't match, STOP and report — do not improvise.
```

## Files (planned)

| File | Action |
|---|---|
| `00_overview.md` | Master prompt: read this first; chains the rest. |
| `01_setup.md` | Verify env via `scripts/verify_setup.py` |
| `02_character_pack.md` | Build `apex::packcharacter` chain |
| `03_aaaa_tag.md` | Apply AAAA tag rules |
| `04_apex_components.md` | Add `fktransform`, `bonedeform`, `multiik` |
| `05_segments.md` | Set multiik `segments` via spare parm |
| `06_animation.md` | FBX anim retarget + `bonedeform` walk |
