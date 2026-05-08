---
name: Next experiment — APEX deform component only (no rig scaffold)
description: Following minimum-anim project, user plans to swap bonedeform SOP for APEX deform component alone, motivated by bonedeform's skin quality
type: project
originSessionId: 32e0e37e-9f45-4151-931e-9bab3caeecf0
---
After publishing houdini-anim-minimum (FBX char + FBX anim + bonedeform SOP, no APEX), user's next planned experiment: use **only the APEX deform component**, dropping the bonedeform SOP. No full Autorig, no MULTI-IK — just the deform layer.

**Why:** bonedeform SOP's deformation quality is poor at joints (classic linear blend skinning artifacts). APEX deform components are believed to give better skin quality. This does NOT contradict AF_for_future_claude.md: AF was about playback fidelity not needing rig scaffolding (verified ~7.5mm match to Cascadeur). Skin deformation quality is a separate layer — using a better deform component while still skipping the rig scaffold is AF's "use only what you need" applied at the deform layer rather than at the rig layer.

**How to apply:** When user starts the next Houdini experiment, recognize the pattern: "minimal again, but swap deform". Do not suggest pulling in autorigcomponent::3.0 fktransform / multiik / Autorig Builder. The whole point is to isolate one APEX piece (the deform component) and see if it alone resolves the skin-quality complaint without re-introducing rig scaffolding. If/when the user publishes this as a follow-up, the angle to lead with is "incremental APEX adoption — one component at a time, only when motivated by a specific quality gap."

**Realization sequence (user's words):** They only noticed "Houdini is empty" *after* finishing the AAAA / handbuild project. So the philosophy was retrospective, not the original framing — the experiments produced the principle, not the other way around.
