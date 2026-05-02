# Scripts

Helper scripts. Single-file, single-purpose, dependency-light.

## `verify_setup.py` (planned)

One-shot environment probe. Writes a green/red status line per check. Designed to be the **first thing an LLM runs** after cloning this repo.

Checks:

| # | Check | Pass criterion |
|---|---|---|
| 1 | Python version | 3.10 or higher |
| 2 | Houdini installation | `hou` importable inside Houdini's python; version ≥ 21.0 |
| 3 | MCP server reachable | `mcp__houdini__ping` returns alive |
| 4 | houdini-mcp bug fixes present | 4 specific calls succeed (probe `Parm.label()` chain) |
| 5 | AAAA snapshot importable | `import aaaa` works from `aaaa-snapshot/` on path |

Usage:

```sh
python scripts/verify_setup.py
```

Output is a flat report — one line per check, suitable for an LLM to parse.

## Other scripts (planned)

- `bootstrap_character.py` — programmatic stub character generator (synthetic 80-joint skeleton + box-mesh skin) for users without a CC4/Cascadeur asset, so the whole procedure can be exercised against a free fixture.
