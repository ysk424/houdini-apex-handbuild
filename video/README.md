# Companion video

Short Azure-TTS-narrated overview. Purpose: **search-engine entry point**, not full procedure delivery.

## Structure (planned)

| Section | Length | Content |
|---|---|---|
| Cold open | ~10 s | One-line hook: "APEX rig in Houdini — without the Autorig Builder." |
| Why | ~30 s | Autorig Builder is unstable; CC4 / Cascadeur users hit a wall. |
| What | ~60 s | Cascadeur and Character Designer screen captures showing how the asset is prepared (no asset distribution). |
| How | ~90 s | Repo structure tour — point at README, prompts, scripts. |
| Result | ~30 s | Walking character clip. |
| Outro | ~10 s | "Read the repo. Run the prompts. PRs welcome." |

Target total: ~3:30. Tight enough that retention stays high; long enough that YouTube's algorithm treats it as content not a teaser.

## Files (planned)

- `script.md` — full narration script with section markers and reading speed notes.
- `screen_recording_plan.md` — shot list for the Cascadeur / Character Designer / Houdini captures.
- `audio/` — Azure TTS output WAVs (gitignored; rendered locally).
- `render/` — final video output (gitignored).

## Voice

Azure Speech SDK, English voice. Candidates to A/B test (low end of stiffness):

- `en-US-JennyNeural` — neutral, well-paced
- `en-US-AriaNeural` — slightly warmer
- `en-US-NancyNeural` — a touch more measured

Pick by ear. Keep prosody natural; avoid SSML over-direction.
