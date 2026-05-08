---
name: APEX Character Project (Houdini, two-Opus protocol)
description: Active project — build a parameterised Houdini network that takes any CC-family FBX and produces a packed APEX character; coordinated via /taxi.md with Claude Desktop
type: project
originSessionId: 3dae1e86-ce75-45dc-93d3-243046595ad7
---
Active project as of 2026-05-04. Working directory `C:\Users\azoo\git\houdini_tools\` (the houdini-tools-fs MCP is sandboxed there).

**Goal:** Build a Houdini network under `/obj/geo1` that ingests any CC-family FBX (CC3 / CC3+ / CC4 / CC5) and outputs a packed APEX character primitive satisfying the v0 DoD in `APEX_Character_Project_goal.md` v0.4. Per-region humanoid components (limb / hand / foot / neck / scapula / root / spine / twist), NOT generic `multiik`. Test FBX: `C:\Users\azoo\git\houdini_tools\CC\TNCC3.Fbx` (textures in sibling `Texture/`).

**Why:** The user wants a parameterised pipeline so a fresh CC FBX can be loaded into the same network without re-architecting. v0 covers the network + parameter set; a separate how-to-modify doc comes later. Iterative, test-driven, ~3hr focused implementation budget.

**How to apply:**
- I am Claude Code in the two-Opus protocol with Claude Desktop. Coordination via `/taxi.md` per `/rulebook.md` v1.1. Phases arrive via taxi.md from Desktop.
- Goal doc is **frozen** — never edit `APEX_Character_Project_goal.md` (or the typo'd `gola.md` variant) without explicit user permission.
- Forbidden: hard-coding bone names that depend on the input FBX, silent fallback to `multiik`, driving any face bone (descendants of `CC_Base_FacialBone` plus Eye/Jaw/Tongue/Teeth/UpperJaw).
- Canonical interior: meters, Y-up, right-handed (set on `kinefx::fbxcharacterimport`).
- Acceptance: T-01..T-15 in goal doc §5 must pass per input FBX. v0 simplifications enumerated in §3.0 are pre-authorised.
- Current phase: Phase 0 (preflight) complete on Code's side as of 2026-05-04. FBX path now provided.
