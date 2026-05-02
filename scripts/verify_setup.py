#!/usr/bin/env python3
"""
verify_setup.py - environment readiness check for houdini-apex-handbuild.

Run from system Python 3.10+. Reports each check on its own line in a format
both humans and LLMs can parse:

    [PASS|FAIL|SKIP] <check-id> - <details>

Exit code:
    0  - all checks PASS or SKIP
    1  - at least one check FAIL

Some checks (Houdini-MCP bug fixes) require running through the MCP layer with
a live Houdini session. Those are flagged SKIP here and delegated to
prompts/01_setup.md, which a code-capable LLM can execute via MCP.
"""

from __future__ import annotations

import os
import pathlib
import socket
import sys

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
AAAA_PATH = REPO_ROOT / "aaaa-snapshot"

PASS = "PASS"
FAIL = "FAIL"
SKIP = "SKIP"


def report(status: str, check_id: str, msg: str) -> None:
    print(f"[{status:4}] {check_id:18} - {msg}")


def check_python() -> bool:
    v = sys.version_info
    if v.major == 3 and v.minor >= 10:
        report(PASS, "python", f"Python {v.major}.{v.minor}.{v.micro}")
        return True
    report(FAIL, "python", f"need 3.10+, got {v.major}.{v.minor}.{v.micro}")
    return False


def _has_hython(install_dir: pathlib.Path) -> bool:
    """A real Houdini install has bin/hython(.exe). Engine-only plugin dirs do not."""
    if sys.platform == "win32":
        return (install_dir / "bin" / "hython.exe").exists()
    return (install_dir / "bin" / "hython").exists()


def _find_houdini_install() -> pathlib.Path | None:
    """Best-effort search for a Houdini install root (platform-aware).

    Filters to dirs that actually contain hython, so e.g. 'Houdini Engine'
    (the Engine plugin distribution, no hython) is excluded. Returns the
    highest-version match.
    """
    candidates: list[pathlib.Path] = []
    if sys.platform == "win32":
        roots = [
            pathlib.Path(r"C:\Program Files\Side Effects Software"),
            pathlib.Path(os.environ.get("ProgramFiles", "")) / "Side Effects Software",
        ]
        for r in roots:
            if not r.is_dir():
                continue
            for p in r.iterdir():
                if p.is_dir() and p.name.lower().startswith("houdini") and _has_hython(p):
                    candidates.append(p)
    elif sys.platform == "darwin":
        r = pathlib.Path("/Applications/Houdini")
        if r.is_dir():
            candidates = [p for p in r.iterdir() if p.is_dir() and _has_hython(p / "Frameworks" / "Houdini.framework" / "Versions" / "Current" / "Resources")]
    else:  # linux
        for r in [pathlib.Path("/opt"), pathlib.Path.home() / "houdini"]:
            if r.is_dir():
                for p in r.iterdir():
                    if p.is_dir() and "houdini" in p.name.lower() and _has_hython(p):
                        candidates.append(p)

    if not candidates:
        return None
    # Prefer highest version - sort by name descending (works for "Houdini 21.0.671" style).
    return sorted(candidates, key=lambda p: p.name, reverse=True)[0]


def check_houdini_install() -> bool | None:
    install = _find_houdini_install()
    if install is None:
        report(SKIP, "houdini-install", "no Houdini install auto-detected - confirm manually")
        return None

    # Try to read the version from the install dir name (e.g. 'Houdini 21.0.671').
    name = install.name
    version = name.replace("Houdini", "").strip()
    if not version:
        report(SKIP, "houdini-install", f"found {install}, version unparsed")
        return None

    parts = version.split(".")
    try:
        major = int(parts[0])
    except (IndexError, ValueError):
        report(SKIP, "houdini-install", f"found {install}, version unparsed")
        return None

    if major >= 21:
        report(PASS, "houdini-install", f"{install.name} at {install}")
        return True
    report(FAIL, "houdini-install", f"need Houdini 21+, found {install.name}")
    return False


def check_mcp_listener() -> bool:
    """Probe the in-Houdini MCP listener (default port 9876).

    The houdini-mcp plugin in Houdini binds port 9876 but its accept-policy
    varies (single-threaded; may refuse new connections while serving an MCP
    client). A direct connect-probe is therefore unreliable.

    Reliable test: try to bind 9876 ourselves. If bind fails, *something* is
    holding the port - good enough to assume the plugin is loaded. If bind
    succeeds, the port was free, meaning the plugin is not loaded.
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind(("localhost", 9876))
        # Bind succeeded -> port was free -> plugin NOT listening.
        s.close()
        report(
            FAIL,
            "mcp-listener",
            "port 9876 is free (Houdini-MCP plugin not loaded?)",
        )
        return False
    except OSError:
        # Bind failed -> port already in use -> something is listening.
        report(PASS, "mcp-listener", "port 9876 is held (Houdini-MCP plugin loaded)")
        return True
    finally:
        s.close()


def check_mcp_bugfixes() -> None:
    """Cannot verify from standalone Python - needs MCP-wrapped tool calls.

    See prompts/01_setup.md. A code-capable LLM with MCP access runs four
    specific tool calls and reports whether any still raise Parm.label() /
    Color / vexSyntaxCheck errors that were present in unfixed forks.
    """
    report(SKIP, "mcp-bugfixes", "verify via prompts/01_setup.md (LLM/MCP path)")
    return None


def check_aaaa_snapshot() -> bool:
    if not AAAA_PATH.exists():
        report(FAIL, "aaaa-snapshot", f"missing - expected at {AAAA_PATH}")
        return False
    if not (AAAA_PATH / "__init__.py").exists():
        report(FAIL, "aaaa-snapshot", f"no __init__.py at {AAAA_PATH}")
        return False

    sys.path.insert(0, str(AAAA_PATH.parent))
    try:
        import importlib

        # Keep the import name stable: aaaa-snapshot is a package directory.
        # We import via the directory name -> module path mapping.
        # Layout assumed: aaaa-snapshot/__init__.py, aaaa-snapshot/rules.py, ...
        spec = importlib.util.spec_from_file_location(
            "aaaa_snapshot", AAAA_PATH / "__init__.py"
        )
        if spec is None or spec.loader is None:
            report(FAIL, "aaaa-snapshot", "spec_from_file_location returned None")
            return False
        mod = importlib.util.module_from_spec(spec)
        sys.modules["aaaa_snapshot"] = mod
        spec.loader.exec_module(mod)
        report(PASS, "aaaa-snapshot", f"importable from {AAAA_PATH}")
        return True
    except Exception as e:
        report(FAIL, "aaaa-snapshot", f"import failed: {type(e).__name__}: {e}")
        return False


def main() -> int:
    print("houdini-apex-handbuild - verify_setup.py")
    print(f"repo: {REPO_ROOT}")
    print()

    results = [
        check_python(),
        check_houdini_install(),
        check_mcp_listener(),
        check_mcp_bugfixes(),
        check_aaaa_snapshot(),
    ]

    print()
    fails = sum(1 for r in results if r is False)
    skips = sum(1 for r in results if r is None)
    passes = sum(1 for r in results if r is True)

    if fails:
        print(f"FAIL - {fails} check(s) failed; {passes} passed, {skips} skipped.")
        print("Resolve FAILs before proceeding. See README.md and docs/.")
        return 1
    if skips:
        print(f"OK - {passes} check(s) passed; {skips} skipped.")
        print("Skipped checks need an MCP-aware LLM. See prompts/01_setup.md.")
    else:
        print(f"ALL GREEN - {passes} check(s) passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
