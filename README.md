# houdini-apex-handbuild

▶ **Watch the companion video:** https://youtu.be/QuLa9eOgQNc

Building an APEX-rigged character in Houdini **without using the APEX Autorig Builder**, driven by a code-capable LLM (Claude Code, Gemini, GPT Codex) over MCP.

This is a five-month investigation log distilled into a reproducible procedure. It is **not** a maintained library. Issues are welcome; responses are best-effort.

> **Status:** Phase 0–3a complete. Walking animation works via classic `bonedeform`. APEX rig compile (multi-component → operational rig graph) is **open** — see [docs/99_open_questions.md](docs/99_open_questions.md). PRs welcome.
> 
> **Tested on:** Houdini 21.0.671 Indie · Windows 11 · Python 3.10 / 3.11 (Houdini-embedded)

---

## Why this exists

Most public tutorials for APEX rigging use the **APEX Autorig Builder**. As of early 2026 it is unstable, and its UI fights anyone who wants per-character control. Reallusion CC4 / Cascadeur users hit this wall hard.

The alternative is to hand-author the APEX components (`apex::autorigcomponent::3.0` for `fktransform`, `bonedeform`, `multiik`) and let an LLM drive the repetitive setup. That's what this repo records.

A code-capable LLM (Claude Code, Gemini Code, GPT Codex, etc.) reads this repo as input and reproduces the procedure in a fresh Houdini session against your own assets.

---

## What's inside

| Path | Purpose |
|---|---|
| [docs/](docs/) | Step-by-step procedure, one phase per file |
| [prompts/](prompts/) | Copy-paste prompts for code-capable LLMs (one per phase) |
| [scripts/](scripts/) | `verify_setup.py` and other one-shot helpers |
| [video/](video/) | Companion video script (Azure TTS narration) |
| [aaaa-snapshot/](aaaa-snapshot/) | Frozen copy of the AAAA tag-author tool — see its README for provenance |

---

## Quick start

```sh
git clone https://github.com/<org>/houdini-apex-handbuild.git
cd houdini-apex-handbuild

# In Houdini's Python shell, or any LLM that can run scripts:
python scripts/verify_setup.py
```

If `verify_setup.py` reports green across the board, an LLM can read [prompts/00_overview.md](prompts/00_overview.md) and execute the phases in order against your character.

---

## Assets and licensing

**This repo intentionally ships no character or animation assets.** Reallusion CC4 base meshes, Cascadeur exports, and similar bound-license content cannot be redistributed under most permissive OSS licenses.

The companion video demonstrates the procedure with one real character (Reallusion CC4 low-poly export, Cascadeur 50-frame walk) but those files are not included here. To follow along with your own assets, any FBX rigged character + matching FBX animation will work. The AAAA tag rules can be re-authored for any rig topology — see [aaaa-snapshot/](aaaa-snapshot/).

---

## Dependencies (external)

This procedure depends on three things you bring yourself:

1. **Houdini Indie 21.0+** — license required.
2. **`houdini-mcp` MCP server** — see [docs/01_mcp_setup.md](docs/01_mcp_setup.md) for the exact fork lineage. Several upstream bugs (in `Parm.label()` handling) were patched mid-investigation; the fix is being submitted upstream as a PR. Until merged, use the patched fork referenced in that doc.
3. **A code-capable LLM with MCP support** — Claude Code, Gemini Code, GPT Codex, or equivalent. Tested primarily with Claude Code (Opus 4.6 / 4.7) plus the houdini-mcp tool surface.

---

## Companion video

A short Azure-TTS-narrated overview is on YouTube: https://youtu.be/QuLa9eOgQNc. The video exists primarily as a search-engine entry point. Full procedure lives in this repo — the video points back here for the LLM-driven reproduction.

---

## License

This repo uses two permissive licenses by content type:

- **Code** (`scripts/`, `aaaa-snapshot/*.py`, any `.py` files) — [MIT](LICENSE).
- **Documentation, prompts, video scripts** (`docs/`, `prompts/`, `video/`, `*.md`) — [CC0 1.0 Universal](LICENSE-docs) (public domain dedication; no attribution required).

The AAAA snapshot is governed by MIT (see `aaaa-snapshot/README.md` for origin attribution).

External assets you bring (CC4, Cascadeur exports, etc.) remain under their own licenses; this repo does not redistribute them.

---

## Credits

- AAAA tag-author tool — extracted snapshot from [houdini_tools/aaaa](https://github.com/ysk424/houdini_tools/tree/master/aaaa) (private). Same author as this repo.
- `houdini-mcp` — fork lineage and bug fixes documented in [docs/01_mcp_setup.md](docs/01_mcp_setup.md).
- Claude Code — Anthropic. The five-month investigation was conducted in collaboration with Claude Opus 4.6/4.7 via Claude Code.

---

## Status of major open questions

1. **APEX rig compile after autorigcomponent SOPs** — at SOP-cook time the rig graph at `/Base.rig` stays "abstract" (1 node, 1 port). `apex::animationfromskeleton` then fails with `NameError: rest_skel`. We currently work around it by using the legacy `bonedeform` SOP, which bypasses the APEX scene system entirely. Candidates for the missing compile step are listed in [docs/99_open_questions.md](docs/99_open_questions.md). PRs welcome.

2. **`kinefx::rigattribwrangle` silently drops `s@path` writes.** A regular `attribwrangle` accepts the same write. Documented but not investigated further.

3. **`apex::autorigcomponent::3.0` does not auto-surface component parameters** (e.g., `multiik`'s `segments`). The `Reload Setup Parms` button is a no-op for most components. The workaround — manually adding a spare parm in the `parameters3` folder — works but is undocumented in Houdini's official docs as of 2026-05.

These are the real value of this repo. Solve any of them and please PR.
