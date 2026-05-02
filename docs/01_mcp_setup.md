# MCP setup - houdini-mcp installation and bug-fix status

**Goal:** A working `houdini-mcp` MCP server that exposes Houdini's API to a code-capable LLM, with four upstream bugs patched.

**Inputs you provide:**
- A code-capable LLM with MCP support (Claude Code, Gemini Code, GPT Codex)
- Houdini Indie 21.0+ on Windows / macOS / Linux

**Outputs you should see at the end:**
- `python scripts/verify_setup.py` returns `[PASS]` for `mcp-listener`
- The five LLM-mediated probes in [`prompts/01_setup.md`](../prompts/01_setup.md) all return PASS

---

## 1. Fork lineage

`houdini-mcp` is a community-maintained MCP server for Houdini. As of early 2026 the upstream is:

- **Upstream:** [`kleer001/houdini-mcp`](https://github.com/kleer001/houdini-mcp)

Four bugs in upstream were discovered and patched during the investigation that produced this repo. The patches:

- Live as a private fork of `kleer001/houdini-mcp` on a developer machine.
- Are being submitted upstream as a Pull Request. **PR URL: TODO - link will be added here once filed.**

Until merged, follow § 3 below to apply the patches locally.

## 2. The four bugs

All four originate in two missing call patterns in upstream's handler code: `hou.Parm.label()` (which doesn't exist - the correct API is `parmTemplate().label()`) and `hou.Color` (returned without conversion to a JSON-serialisable list/tuple).

| ID | MCP tool | Symptom (upstream, unfixed) | Severity |
|----|----------|-----------------------------|----------|
| B1 | `get_parameter_schema` | `'Parm' object has no attribute 'label'` on default-state nodes | Always fails |
| B2 | `get_node_info` | `'Color' object is not iterable` on default-state nodes | Always fails |
| B3 | `validate_vex` | `'text' object has no attribute 'vexSyntaxCheck'` on any input | Always fails |
| B4 | `get_parameter` | `'Parm' object has no attribute 'label'` on any parm | Always fails (same root cause as B1) |

B1, B2, B3 surfaced during the AAAA Phase 1.5 probe of `attribadjustarray` and `kinefx::rigattribwrangle`. B4 surfaced during the same fix session against `box.sizex` (different node, same root cause as B1).

## 3. Apply the fix locally

Until the upstream PR merges, three steps:

### 3.1 Clone the fork with patches applied

```sh
# When the PR is up but unmerged, clone the PR's branch:
git clone https://github.com/<fork-author>/houdini-mcp.git
cd houdini-mcp
git checkout <fix-branch-name>
```

(The exact fork URL and branch name will be added here when the PR is filed.)

### 3.2 Install into Houdini's Python path

Run the install script from the cloned repo:

```sh
python scripts/install.py
```

This **copies** the `houdinimcp` package into Houdini's Python search path (e.g. on Windows: `C:\Users\<you>\Documents\houdini21.0\scripts\python\houdinimcp\`). The repo and installed copy are then independent - editing the repo does NOT update the installed copy until you re-install or `robocopy` over.

**This is a sharp edge.** If you later modify the repo and forget to re-deploy, Houdini will still load the unmodified installed copy. The only symptom is "my edit doesn't take effect" with no error to point at the cause.

To re-sync after edits (Windows PowerShell):

```powershell
robocopy "C:\Users\<you>\git\houdini-mcp\src\houdinimcp" `
         "C:\Users\<you>\Documents\houdini21.0\scripts\python\houdinimcp" /E /R:1 /W:1
```

### 3.3 Restart Houdini

The shelf "Toggle MCP Server" sometimes does not auto-restart cleanly. The reliable way is **File → Quit → relaunch Houdini**, then load the MCP server from the shelf. On a clean launch, the new module is imported fresh.

## 4. Add the MCP server to your LLM client

For Claude Desktop / Claude Code, add to the MCP config (`claude_desktop_config.json` on Claude Desktop, or your code-LLM's equivalent):

```json
{
  "mcpServers": {
    "houdini": {
      "command": "uv",
      "args": [
        "--directory", "C:\\Users\\<you>\\git\\houdini-mcp",
        "run", "python", "houdini_mcp_server.py"
      ]
    }
  }
}
```

(Adjust the `--directory` path to your local clone.)

## 5. Verify

Two-stage verification:

### 5.1 Standalone Python (no LLM needed)

```sh
python scripts/verify_setup.py
```

Expect `[PASS]` for `mcp-listener`. If FAIL, the plugin is not loaded - re-do § 3.3.

### 5.2 LLM-mediated (proves the patches are applied)

Open your LLM client and follow [`prompts/01_setup.md`](../prompts/01_setup.md). It runs five probes through the MCP layer. All five must PASS. If any fail with the historical signatures listed there, your installed copy is unfixed - re-do § 3.2.

## 6. PR status

The PR upstream to `kleer001/houdini-mcp`:

- **Status:** TODO - update when filed
- **URL:** TODO

When the PR is merged, this section will be updated to point at the merge commit and you can `git pull` from upstream rather than the fork. Until then, the fork is canonical.

## 7. Why this matters for the rest of the procedure

Every subsequent phase in this repo invokes one or more of B1-B4 as part of its workflow:

- AAAA tag application → reads parm schemas via B1
- Component inspection → uses B2
- VEX snippet sanity → uses B3
- Spare-parm value setting → uses B4

If any of those bugs are unfixed in your environment, the LLM will hit a Python traceback at an unrelated-looking moment in a later phase. Failing fast here is much cheaper than debugging it three steps later.

## 8. References

- Upstream: https://github.com/kleer001/houdini-mcp
- Original investigation log (private): `houdini_tools/aaaa/PHASE_1_5_PROBE_NOTES.md` § 6 (bug discovery), `houdini_tools/houdini_mcp_fix_3bugs_2026-05-01.md` (fix session log)
- This repo's verification scripts: `scripts/verify_setup.py`, `prompts/01_setup.md`
