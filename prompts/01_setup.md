# Setup verification (LLM/MCP path)

**Pre-state:** You are a code-capable LLM (Claude Code, Gemini Code, GPT Codex, etc.) with `houdini-mcp` configured as an MCP server. Houdini is running with the houdini-mcp plugin loaded.

**Post-state:** The four MCP tools that previously had bugs in upstream forks are confirmed working in this environment. Any FAIL means the operator's `houdini-mcp` is unfixed and needs the patches referenced in `docs/01_mcp_setup.md`.

---

## Background

Four `houdini-mcp` tools had `'Parm' object has no attribute 'label'` / `'Color' object is not iterable` / `'text' object has no attribute 'vexSyntaxCheck'` errors in upstream as of early 2026. They were fixed in a private fork; a PR is being submitted upstream. This phase confirms the operator's local plugin has the fix.

If any of these probes returns an error matching the historical signatures listed below, **STOP** and direct the operator to apply the fork patch (see `docs/01_mcp_setup.md`).

---

## Run

Confirm Houdini is reachable, then run the four probes in order. Report each as PASS / FAIL.

```python
# 1. Sanity ping.
mcp__houdini__ping()
# Expected: {"alive": true, ...}
```

```python
# 2. Probe get_parameter_schema (was: 'Parm' object has no attribute 'label').
mcp__houdini__get_parameter_schema(
    node_path="/obj",
    parm_name="show",
)
# PASS criterion: returns a dict with a "label" field, no Python traceback.
# FAIL signature: error containing "'Parm' object has no attribute 'label'".
```

```python
# 3. Probe get_node_info (was: 'Color' object is not iterable).
mcp__houdini__get_node_info(
    node_path="/obj",
)
# PASS criterion: returns a dict with a "color" field that is a list of 3 floats.
# FAIL signature: error containing "'Color' object is not iterable".
```

```python
# 4. Probe validate_vex (was: 'text' object has no attribute 'vexSyntaxCheck').
mcp__houdini__validate_vex(
    snippet="@P.x = 1.0;",
)
# PASS criterion: returns {"valid": bool, "errors": str|null}.
# FAIL signature: error containing "'text' object has no attribute 'vexSyntaxCheck'".
```

```python
# 5. Probe get_parameter (was: 'Parm' object has no attribute 'label' on default node).
mcp__houdini__get_parameter(
    node_path="/obj",
    parm_name="show",
)
# PASS criterion: returns a dict with parm value and label, no traceback.
# FAIL signature: error containing "'Parm' object has no attribute 'label'".
```

---

## Verify

Report the result of each probe in this format:

```
[PASS|FAIL] mcp-bugfix-1  ping
[PASS|FAIL] mcp-bugfix-2  get_parameter_schema
[PASS|FAIL] mcp-bugfix-3  get_node_info
[PASS|FAIL] mcp-bugfix-4  validate_vex
[PASS|FAIL] mcp-bugfix-5  get_parameter
```

If any FAIL, halt the procedure. Do not retry; the cause is upstream and needs the operator to apply the fork patch.

If all PASS, the MCP layer is verified. Continue with whichever subsequent prompt the operator runs. (Other prompt files in this directory will be added as the procedure is documented.)

---

## On failure

| FAIL signature | Cause | Fix |
|---|---|---|
| `'Parm' object has no attribute 'label'` (probes 2 or 5) | `_parm_utils.parm_label()` helper missing or broken | Apply the fork patch from `docs/01_mcp_setup.md` |
| `'Color' object is not iterable` (probe 3) | `Color` returned without conversion to list/tuple | Apply the fork patch |
| `'text' object has no attribute 'vexSyntaxCheck'` (probe 4) | `validate_vex` calls a non-existent hou.text method | Apply the fork patch (uses temp `kinefx::rigattribwrangle` cook instead) |
| Connection error / timeout | Houdini not running, or plugin crashed | Restart Houdini and reload the plugin; do **not** loop-retry |

---

## Why these specific probes

These four tools are exercised throughout the rest of the procedure. If they don't work, downstream phases will fail with the same root cause but at much less obvious points (e.g. mid-AAAA apply, or while configuring multiik). Failing fast here saves debugging time later.
