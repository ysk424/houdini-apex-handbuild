# Narration script

All narration generated via Azure Neural TTS, voice `en-US-NancyNeural`, with `prosody pitch="-3%" rate="0.97"`. Output format: RIFF 48kHz 16-bit mono PCM (WAV).

Tone: confident on technical claims, considerate of the viewer's context. Not professorial, not falsely humble — a fellow practitioner sharing notes.

WAV files live in `video/audio/` (gitignored). Regenerate any time via the SSML below using `scripts/build_narration.sh` (see end of file).

---

## T0 - Title card

**File:** `audio/T0_title.wav` (~11.7s)

> If you've tried APEX rigging in Houdini, you've probably met the Autorig Builder. _After five months with it, I went a different way._ Here's what worked.

---

## D0 - Overall picture

**File:** `audio/D0_overall.wav` (~23.4s)

> Four things go in. One walking character comes out. The character is a rigged FBX. The animation is a separate FBX, also yours. The control is a code-capable language model talking to Houdini through MCP. Procedure lives in this repo. Six phases.

---

## D1 - Three subsystems

**File:** `audio/D1_subsystems.wav` (~28.4s)

> Three subsystems run in parallel. The character pipeline brings the FBX in, tags every joint, adds the APEX components. The animation pipeline brings the animation FBX in, remaps it to match the character, and deforms the skin. The control plane is you, the model, MCP, and Houdini. You only steer the leftmost column. The other two follow.

---

## D2-a - Character nodes

**File:** `audio/D2a_character_nodes.wav` (~19.9s)

> Six SOPs in the character chain. Most just cook quietly. The work is in two of them. Tag skeleton, where AAAA writes per-joint VEX. And multiik, where we set the segments parameter manually. We'll look at both.

---

## D2-b - AAAA tags

**File:** `audio/D2b_aaaa_tags.wav` (~21.1s)

> Each joint gets a list of tags. Some tags name the chain — L underscore arm, R underscore leg. Others name the role inside the chain — IK root, IK polevec, IK tip. Multi-I-K queries by tag intersection. Get the tags right, the IK works.

---

## D2-c - multiik segments

**File:** `audio/D2c_multiik_segments.wav` (~24.8s)

> Multi-I-K reads its segments from a manually added spare parameter. The official Reload button doesn't surface it. The promoted parm trick doesn't either. What does work is adding a string spare parm in the parameters3 folder by hand. The H-D-A's internal pickup wires it through. That took a while to figure out.

---

## D3-a - Animation nodes

**File:** `audio/D3a_animation_nodes.wav` (~20.6s)

> Animation side. The FBX import goes through three remap nodes, then into bone deform. The remap exists because Cascadeur exported the canonical CC4 skeleton, and our character is the low-poly variant. They have different joint names. We bridge.

---

## D3-b - Skeleton mismatch

**File:** `audio/D3b_skeleton_mismatch.wav` (~30.5s)

> Cascadeur sends 101 joints. Our character has 80. The gap is the canonical primary joints — Upperarm, Forearm, Thigh, Calf — which the low-poly skeleton skipped. After remap, every character joint has a name match in the animation. If your character is canonical CC4, you can skip this whole pipeline. If your animation source uses Mixamo or your own naming, you rewrite the remap.

---

## D4-a - LLM/MCP/Houdini stack

**File:** `audio/D4a_llm_mcp_houdini.wav` (~16.2s)

> Four layers. You talk to the model. The model talks to the MCP server. The MCP server talks to Houdini. Houdini cooks. Results bubble back up.

---

## D4-b - Repo tree

**File:** `audio/D4b_repo_tree.wav` (~17.2s)

> The repo holds five things. Procedure docs to read first. Prompts to feed your model. A verify script to check your environment. The AAAA tag tool. And the diagrams from this video.

---

## D5 - User steps

**File:** `audio/D5_user_steps.wav` (~22.5s)

> Four steps. Clone the repo. Install MCP — that includes patching four bugs upstream that weren't merged when I shipped this. Run the verify script. Then feed each prompt to your model in order. The model does the wiring. You read its decisions and approve.

---

## D6 - Status

**File:** `audio/D6_status.wav` (~17.6s)

> What's solved. What's worked around. What's open. The big open one is the APEX scene compile. I haven't cracked it. If you have, please share — pull request or issue, either works.

---

## T1 - Outro

**File:** `audio/T1_outro.wav` (~13.9s)

> Repository is in the description. Try it on your own character. Tell me what breaks. Tell me what works better. See you there.

---

## Total

**Narration only:** ~267.8s = ~4:28

Add visual reveal time, transitions, footage, and the actual video runs ~5:00-5:30.

---

## Phonetic notes

- **Multi-IK** is written as "Multi-I-K" so Nancy spells out the letters rather than saying "ick".
- **HDA** is written as "H-D-A" for the same reason.
- **L_arm** is verbalized "L underscore arm" — slightly clunky but unambiguous in audio.
- **CC4 / Cascadeur / Houdini** read naturally without spelling.

---

## Regeneration

Voice / prosody changes — edit the SSML, re-run. The full batch took ~10 seconds end-to-end. Voice is `en-US-NancyNeural`; alternative low-female candidates are listed in `figure_specs.md`.

To re-run, the bash one-liner pattern:

```sh
KEY=$(az cognitiveservices account keys list --name speech-handbuild \
        --resource-group rg-ai-hello --query key1 -o tsv)
# build SSML, then:
curl -X POST "https://japaneast.tts.speech.microsoft.com/cognitiveservices/v1" \
  -H "Ocp-Apim-Subscription-Key: $KEY" \
  -H "Content-Type: application/ssml+xml" \
  -H "X-Microsoft-OutputFormat: riff-48khz-16bit-mono-pcm" \
  -H "User-Agent: houdini-apex-handbuild" \
  --data-binary @your.ssml \
  -o your.wav
```
