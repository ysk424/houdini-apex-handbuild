# Correspondence table — audio × figure × footage × timing

The mapping you'd hand to a video editor (or use yourself in Premiere). Each row is one segment of the final video.

**Conventions:**
- **Audio** — WAV file in `video/audio/` (gitignored, regenerate via Azure TTS — see `script.md`).
- **Figure** — SVG in `video/figures/`. Open in browser, screenshot at 100% zoom, drop into Premiere.
- **Footage** — screen recording you capture yourself. The repo ships none (license).
- **Timing** — narration duration only. Add ~1-2s breathing room before/after each segment.

---

## Timeline

| Seg | Time (cum) | Audio | Figure | Footage on screen | Audio dur |
|----:|-----------:|-------|--------|-------------------|----------:|
| 1   | 0:00–0:12  | `T0_title.wav`            | `T0_title.svg`            | E1 walking-character clip (looping behind text) | 11.7s |
| 2   | 0:12–0:36  | `D0_overall.wav`          | `D0_overall.svg`          | None — figure full-screen                       | 23.4s |
| 3   | 0:36–1:04  | `D1_subsystems.wav`       | `D1_subsystems.svg`       | E2 Houdini network early-state (5s mid-segment) | 28.4s |
| 4   | 1:04–1:24  | `D2a_character_nodes.wav` | `D2a_character_nodes.svg` | None — figure full-screen                       | 19.9s |
| 5   | 1:24–1:45  | `D2b_aaaa_tags.wav`       | `D2b_aaaa_tags.svg`       | None — figure full-screen                       | 21.1s |
| 6   | 1:45–2:10  | `D2c_multiik_segments.wav`| `D2c_multiik_segments.svg`| E3 multiik segments setting moment (~10s mid)   | 24.8s |
| 7   | 2:10–2:31  | `D3a_animation_nodes.wav` | `D3a_animation_nodes.svg` | None — figure full-screen                       | 20.6s |
| 8   | 2:31–3:01  | `D3b_skeleton_mismatch.wav`| `D3b_skeleton_mismatch.svg`| E1 walking-character clip (10s, behind text)   | 30.5s |
| 9   | 3:01–3:17  | `D4a_llm_mcp_houdini.wav` | `D4a_llm_mcp_houdini.svg` | None — figure full-screen                       | 16.2s |
| 10  | 3:17–3:34  | `D4b_repo_tree.wav`       | `D4b_repo_tree.svg`       | E5 LLM panel + prompt paste (5s mid)            | 17.2s |
| 11  | 3:34–3:57  | `D5_user_steps.wav`       | `D5_user_steps.svg`       | E4 verify_setup ALL GREEN (5s) + E6/E7 misc     | 22.5s |
| 12  | 3:57–4:14  | `D6_status.wav`           | `D6_status.svg`           | E8 GitHub Issues page (3s end of segment)       | 17.6s |
| 13  | 4:14–4:28  | `T1_outro.wav`            | `T1_outro.svg`            | None — outro card full-screen                   | 13.9s |

**Total runtime:** ~4:28 narration + ~30s breathing/transitions = ~5:00 video.

---

## Footage clips you'll capture

Plan once, record in one Houdini session. Approximate target lengths shown.

| ID | Source app | Description | Used in segments |
|----|-----------|-------------|-----------------|
| E1 | Houdini viewport | Walking character, side angle, looping. Loop point = 50 frames. | Seg 1 (T0), Seg 8 (D3-b) |
| E2 | Houdini network editor | Pan over the full `/obj/geo1` network with all SOPs visible. | Seg 3 (D1) |
| E3 | Houdini split (Python panel + multiik node UI) | Run `set_component_parms`, watch the spare parm appear. | Seg 6 (D2-c) |
| E4 | Terminal | Run `python scripts/verify_setup.py`, show ALL GREEN output. | Seg 11 (D5) |
| E5 | Claude Code (or your LLM client) | Paste a prompt, watch the LLM execute it. | Seg 10 (D4-b) |
| E6 | Terminal | `git clone github.com/ysk424/houdini-apex-handbuild` | Seg 11 (D5) |
| E7 | Browser / file explorer | Open the cloned repo, scroll README briefly. | Seg 11 (D5) |
| E8 | Browser | github.com/ysk424/houdini-apex-handbuild/issues | Seg 12 (D6) |

**Total footage to record:** ~50-60 seconds raw material, edited down to ~30-40 seconds in final.

---

## Premiere assembly notes

- Each segment is independent — drop figure SVG (rasterized to 1920x1080 PNG) on V1, audio WAV on A1, footage clip on V2 with appropriate transparency / picture-in-picture.
- For figures with no footage (Seg 2, 4, 5, 7, 9, 13), V2 is empty. Figure occupies full frame.
- For figures with footage overlay, scale the figure to ~70% and the footage to ~25% in a corner. Or alternate: full-screen figure for first half of segment, full-screen footage for second.
- Crossfade audio between segments: 200ms each end. Crossfade video: 300ms.
- Background music: optional. If used, keep at -28 dB so narration sits clearly.
- Final export: 1920x1080, H.264, 12-15 Mbps, AAC 256kbps audio.

---

## Replacement guidance

If you re-record / re-narrate later:

- **Single segment edit** — regenerate that one WAV (10 seconds), replace in Premiere, done.
- **Tone change** — edit `script.md`, regenerate all 13 WAVs (~1 minute total at Azure F0). The figure-by-figure structure is unchanged so re-cutting is fast.
- **Figure update** — edit the SVG, re-screenshot, re-drop. Audio unchanged.
- **Polished figures via Claude Design** — see `figure_specs.md` for prompts. Replace SVG screenshots with Design's PNG export.

---

## Sanity check before you start cutting

1. Open every WAV, listen end-to-end (~5 minutes total).
2. Open every SVG, scroll through (~2 minutes).
3. Read this table once.
4. Then start in Premiere.

The narrations and figures are designed to be self-contained per segment. You can shuffle order or delete a segment without breaking anything else (except the running time math).
