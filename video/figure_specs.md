# Figure specs

This file contains:

1. The list of 11 figures used in the companion video
2. For each figure, an SVG path (immediately usable) AND a Claude Design prompt (for upgrading to a polished version)

## How to use

**Quick (15 minutes total):**
- Open each `.svg` file in your browser, take a 1920x1080 screenshot, drop into Premiere.

**Polished (1-2 hours total):**
- Open Claude Design (https://claude.ai/labs or wherever Anthropic Labs hosts it - requires Pro/Max/Team/Enterprise).
- Paste the prompt below. Iterate via inline comments and direct edits.
- Export as PNG (16:9, 1920x1080). Drop into Premiere.

The polished route gives nicer typography and color grading. The SVG route gives reproducibility and is editable in any text editor.

---

## T0 - Title card

**SVG:** [`figures/T0_title.svg`](figures/T0_title.svg)

**Use:** Cold open, 0:00-0:15, behind the walking-character clip.

**Claude Design prompt:**

> Create a 16:9 title slide with a dark navy background (#0a0a14). Top half: large bold white text "Houdini APEX rig" (90pt) and below it in italic light blue (#6ec1ff) "without the Autorig Builder" (56pt). Center divider line in muted gray. Below: subtitle in muted gray "5 minutes to learn - 1 hour to reproduce" and a green tagline "Driven by a code-capable LLM over MCP". At the bottom: monospace text "github.com/ysk424/houdini-apex-handbuild" and a tiny "Houdini 21.0.671 - May 2026" caption. Minimal, technical, no decorative elements. Inter / Helvetica typography.

---

## D0 - Overall picture

**SVG:** [`figures/D0_overall.svg`](figures/D0_overall.svg)

**Use:** 0:15-0:45. The "what does the whole thing do" diagram.

**Claude Design prompt:**

> A 16:9 dark technical diagram showing four input boxes at the top (FBX Character, FBX Animation, Code-LLM, This Repo) flowing via cyan arrows into a central highlighted box "6-phase Procedure", then flowing down to a green-bordered output box "Walking character". Dark navy background (#0a0a14). Box backgrounds slightly lighter (#1a1a28). Cyan accent color for the procedure box (#6ec1ff). Green output box (#7fdb7f). Each input box has 2-3 lines of caption underneath the title. Sans-serif typography. Title at top: "D0 Overall picture" with subtitle "Four inputs - one procedure - one walking character".

---

## D1 - Three subsystems

**SVG:** [`figures/D1_subsystems.svg`](figures/D1_subsystems.svg)

**Use:** 0:45-1:15. Three columns showing the three concurrent pipelines.

**Claude Design prompt:**

> A 16:9 three-column dark technical diagram. Each column is a tall rounded box with a colored header. Left column "Character pipeline" (cyan header), middle "Animation pipeline" (purple header), right "LLM/MCP control" (green header). Inside each column, list the 4-5 stages with monospace technical labels. Footer of each column points to a deeper detail diagram (D2, D3, D4). Bottom caption: "All three run in parallel - operator only steers the leftmost (LLM) column". Dark navy background. Inter typography for prose, Consolas/monospace for technical names.

---

## D2-a - Character pipeline node flow

**SVG:** [`figures/D2a_character_nodes.svg`](figures/D2a_character_nodes.svg)

**Use:** 1:15-1:35. The actual SOP nodes in the Houdini network for the character side.

**Claude Design prompt:**

> A 16:9 SOP node-graph diagram with six rounded boxes and cyan arrows showing data flow. Top row: fbxcharacterimport1 -> tag_skeleton (highlighted) -> apex_pack. Bottom row continues right-to-left: fktransform -> bonedeform -> multiik (highlighted). Each box has a node name in white, type in gray monospace, and a 1-line description. Below the diagram, two annotation boxes explain "tag_skeleton (AAAA-authored snippet)" and "multiik (segments parameter)" in detail. Dark navy background. Cyan highlight color (#6ec1ff) for the two key nodes. Caption at bottom: "All six SOPs cook silently. The work is in 'tag_skeleton' (AAAA emits VEX) and 'multiik' (segments spare parm)."

---

## D2-b - AAAA tag concept

**SVG:** [`figures/D2b_aaaa_tags.svg`](figures/D2b_aaaa_tags.svg)

**Use:** 1:35-1:50. Joint-name -> tag-list table, with IK-role rows highlighted.

**Claude Design prompt:**

> A 16:9 dark table-style diagram with three columns: Joint name, s[]@tags, Used by. Show 7 example rows with monospace joint names. Highlight three rows (the IK role joints) with a subtle cyan background. Use green text for plain chain tags, yellow text for IK role tags, and gray for orphan/empty. Below the table, a callout box titled "How multi-IK consumes the tags" with two example queries in monospace yellow: "%tag(ik_root) & (L_arm) -> CC_Base_L_UpperarmTwist01". Dark navy background, Inter / Consolas typography. Bottom caption: "All authored from external JSON. Re-run any time. Idempotent. Different rigs = different JSON."

---

## D2-c - multiik segments via parameters3 spare parm

**SVG:** [`figures/D2c_multiik_segments.svg`](figures/D2c_multiik_segments.svg)

**Use:** 1:50-2:15. Two side-by-side panels showing what doesn't work vs what works, plus the data-flow chain.

**Claude Design prompt:**

> A 16:9 diagram split horizontally in two top panels: left panel red-bordered titled "What does NOT work" listing three bullet points (Reload Setup Parms, Promoted Parms multiparm, rig graph patch) with explanations of why each fails. Right panel green-bordered titled "What WORKS" with a Python code snippet (in green monospace) showing the parmTemplateGroup().appendToFolder(...) call to add a string spare parm in the Parameters folder. Below the two panels, a horizontal data-flow chain with four boxes connected by cyan arrows: SOP UI -> get_parms -> PARMS -> editgraph1. Dark navy background. Caption at bottom: "aaaa.component_parms.set_component_parms() does this idempotently."

---

## D3-a - Animation pipeline node flow

**SVG:** [`figures/D3a_animation_nodes.svg`](figures/D3a_animation_nodes.svg)

**Use:** 2:15-2:35. The animation-side SOP graph.

**Claude Design prompt:**

> A 16:9 SOP node-graph diagram with six rounded boxes and arrows. Top row: fbxanimimport1 -> delete_anim_twists (purple highlight) -> rename_anim_lowpoly (purple). Continues to fix_paths_aw (purple) below. Then: walk_bone_deform (green highlight) -> viewport (green text). Each box has node name, type, and 1-line description. Below the diagram, two annotation boxes (purple-bordered) titled "Why three remap nodes" and "Why classic bonedeform (not APEX)" - each with 4-5 lines of explanation. Dark navy background. Purple (#c060ff) for the remap nodes, green (#7fdb7f) for the deform / viewport. Bottom caption about name-binding.

---

## D3-b - Skeleton mismatch table

**SVG:** [`figures/D3b_skeleton_mismatch.svg`](figures/D3b_skeleton_mismatch.svg)

**Use:** 2:35-3:00. Side-by-side hierarchy showing canonical vs low-poly, and the 8 rename pairs.

**Claude Design prompt:**

> A 16:9 three-panel diagram. Left panel (purple): "Canonical CC4 (anim, 101 joints)" with an indented monospace tree showing CC_Base_L_Clavicle -> Upperarm -> UpperarmTwist01 (marked DELETED in red) and similar. Center: a horizontal arrow labeled "remap" in purple. Right panel (green): "Low-poly CC4 (our char, 80 joints)" with the equivalent tree but no canonical primaries. Far right (cyan): "8 rename pairs" listing all 8 left -> right name pairs in monospace. Dark navy background. Bottom caption: "If your character is canonical CC4 and your animation is canonical CC4, skip this whole pipeline - feed the FBX animation directly into bonedeform."

---

## D4-a - LLM / MCP / Houdini stack

**SVG:** [`figures/D4a_llm_mcp_houdini.svg`](figures/D4a_llm_mcp_houdini.svg)

**Use:** 3:00-3:15. The four-layer architecture from operator to Houdini.

**Claude Design prompt:**

> A 16:9 vertical four-layer stack diagram. From top to bottom: "You (operator)" green box, "Code-LLM with MCP support" cyan box (subtext: Claude Code, Gemini Code, GPT Codex), "houdini-mcp server" purple box, "Houdini (with houdini-mcp plugin)" yellow box. Each layer is connected to the next by a vertical arrow with a label describing the protocol (prompts, MCP protocol JSON-RPC, TCP localhost:9876). On the left side, a dashed gray return-arrow runs from bottom layer back up to top, labeled "results / probes / errors". Dark navy background, modern technical look. Title "D4-a LLM / MCP / Houdini stack" with subtitle "Four layers - you only talk to the top one".

---

## D4-b - Repository structure

**SVG:** [`figures/D4b_repo_tree.svg`](figures/D4b_repo_tree.svg)

**Use:** 3:15-3:30. The folder tree of the GitHub repo with annotations.

**Claude Design prompt:**

> A 16:9 dark diagram split in two: left side shows a monospace ASCII-style folder tree of the houdini-apex-handbuild repo (about 18 lines, properly indented with pipe / dash characters). Folder names in green, file names in white, comments in gray. Right side: a "What goes where" panel listing 5 folder descriptions (docs, prompts, scripts, aaaa-snapshot, video/figures) each with title in green, one-line summary in white, one-line note in gray. Bottom centered tagline: "Clone, run verify_setup.py, then start with docs/01_mcp_setup.md." Dark navy background, Consolas monospace for the tree, Inter for prose.

---

## D5 - Four user steps

**SVG:** [`figures/D5_user_steps.svg`](figures/D5_user_steps.svg)

**Use:** 3:30-3:55. The numbered list of what the user does.

**Claude Design prompt:**

> A 16:9 numbered-step diagram with four large rounded boxes stacked vertically, each prefixed with a green numbered circle (1, 2, 3, 4) on the left. Box 1: "Clone" with monospace git clone command. Box 2: "Install MCP" with one-line instructions. Box 3: "Verify" with monospace python command. Box 4 (highlighted with cyan border): "Run prompts" with two-line description. Green arrows between each step. Dark navy background. Title "D5 What you do as a user" with subtitle "Four steps. The LLM does the rest." Bottom note: "Bring your own FBX character + FBX animation. Repo ships no assets (license)."

---

## D6 - Status (solved / worked-around / open)

**SVG:** [`figures/D6_status.svg`](figures/D6_status.svg)

**Use:** 3:55-4:15. Honest status with the open questions called out as call-to-action.

**Claude Design prompt:**

> A 16:9 traffic-light style status diagram. Three horizontal stacked rounded boxes: green top (titled "Solved" with checkmark icon, listing 3 items), yellow middle (titled "Worked around" with exclamation icon, listing 2 items), red bottom (titled "Open - PRs welcome" with X icon, listing 2 items with sub-bullets). Each item is a single line of plain text. Dark navy background. Bottom caption: "If you solve any 'open' item, please open a PR or an issue." with a link "github.com/ysk424/houdini-apex-handbuild/issues". Title "D6 Status of the procedure".

---

## T1 - Outro

**SVG:** [`figures/T1_outro.svg`](figures/T1_outro.svg)

**Use:** 4:15-4:30. Repo URL + CTA.

**Claude Design prompt:**

> A 16:9 minimal end-card. Dark navy background. Centered: "Repository" small label in gray, then large monospace cyan "github.com/ysk424/" on one line and "houdini-apex-handbuild" on the next. Divider line. Below: large white text "Reproduce. Comment. PR." with generous spacing between words. Tiny gray credits at the bottom: "All diagrams in this video: SVG in /video/figures/" and "Polished versions assisted by Claude Design (Anthropic Labs)". Minimal, no decorative elements.

---

## Notes

- The 11 SVGs are generated by Claude Code (this CLI session). They render correctly in any modern browser.
- For Premiere import, the simplest path is: open each SVG in browser at 100% zoom, full-screen the browser tab, screenshot at 1920x1080. Or use a CLI tool like `chrome --headless --screenshot --window-size=1920,1080 file:///path/to/figure.svg`.
- The Claude Design prompts above are written assuming you have a Pro / Max / Team / Enterprise plan with Claude Design access (introduced 2026-04-17).
- All figures use the same color palette for consistency:
  - Background: `#0a0a14` (dark navy)
  - Box bg: `#1a1a28`
  - Primary text: `#e8e8f0`, headers `#ffffff`
  - Cyan accent (character side / generic highlight): `#6ec1ff`
  - Purple accent (animation side): `#c060ff`
  - Green accent (control / success): `#7fdb7f`
  - Yellow accent (warnings / role tags): `#ffd560`
  - Red accent (errors / open issues): `#ff6060`
