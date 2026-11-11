"""Kontrola prostředí pro ai-agent-data-lab.

Spuštění ve složce repozitáře:
    uv run python scripts/kontrola.py

Vypíše [OK] nebo [CHYBA] s poznámkou, co udělat. Nic nemění.
"""
import json
import os
import re
import shutil
import subprocess
import sys
import tomllib
from importlib import metadata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(errors="replace")

errors = 0


def ok(what):
    print(f"[OK]    {what}")


def fail(what, note):
    global errors
    errors += 1
    print(f"[CHYBA] {what}\n        {note}")


def info(what):
    print(f"[INFO]  {what}")


def run(*cmd):
    # Bez .venv projektu, ať se najde program nainstalovaný v systému (uv run ji dává na začátek PATH)
    venv = str((ROOT / ".venv").resolve()).lower()
    path = os.pathsep.join(p for p in os.environ.get("PATH", "").split(os.pathsep)
                           if not str(Path(p).resolve()).lower().startswith(venv))
    exe = shutil.which(cmd[0], path=path)
    if exe is None:
        return None, ""
    p = subprocess.run([exe, *cmd[1:]], capture_output=True, text=True,
                       encoding="utf-8", errors="replace", timeout=60)
    return p.returncode, (p.stdout + p.stderr).strip()


def version(text):
    m = re.search(r"(\d+)\.(\d+)\.(\d+)", text)
    return tuple(int(x) for x in m.groups()) if m else None


def main():
    # Python a knihovny
    if sys.version_info < (3, 12):
        fail(f"Python {sys.version.split()[0]}",
             "Spusťte ve složce repozitáře: uv sync, pak uv run python scripts/kontrola.py")
        sys.exit(1)
    ok(f"Python {sys.version.split()[0]}")

    deps = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))["project"]["dependencies"]
    bad = []
    for dep in deps:
        name = re.split(r"[<>=!~;\[ ]", dep, maxsplit=1)[0]
        try:
            metadata.version(name)
        except metadata.PackageNotFoundError:
            bad.append(f"{name} chybí")
    if bad:
        fail("Knihovny Pythonu", "; ".join(bad) + ". Spusťte: uv sync")
    else:
        ok(f"Knihovny Pythonu ({len(deps)})")

    # Nástroje (instaluje je agent podle AGENTS.md, oddíl Příprava prostředí)
    code, out = run("git", "--version")
    if code != 0:
        fail("Git", "Nenalezen. Nainstalujte ho (AGENTS.md, Příprava prostředí).")
    else:
        ok(out)
        # Bez jména a e-mailu git odmítne commit („empty ident name … not allowed“)
        for key, label in (("user.name", "jméno"), ("user.email", "e-mail")):
            code, out = run("git", "-C", str(ROOT), "config", key)
            if code == 0 and out:
                ok(f"Git: {label} {out}")
            else:
                fail(f"Git: {label}", f"Není nastavené. Spusťte: git config --global {key} \"...\"")
        code, out = run("git", "-C", str(ROOT), "rev-parse", "--is-inside-work-tree")
        if code == 0 and out == "true":
            ok("Složka je repozitář gitu")
        else:
            fail("Repozitář gitu", "Složka není repozitář. Spusťte: git init")

    code, out = run("node", "--version")
    v = version(out) if code == 0 else None
    if v is None:
        fail("Node.js", "Nenalezen. Nainstalujte ho (AGENTS.md, Příprava prostředí).")
    else:
        ok(f"Node.js {out}")

    code, out = run("duckdb", "--version")
    v = version(out) if code == 0 else None
    ok(f"DuckDB CLI {'.'.join(map(str, v))}") if v else fail(
        "DuckDB CLI", "Nenalezeno. Nainstalujte ho (AGENTS.md, Příprava prostředí).")

    # AI agenti a editory: jen informace, stačí kterýkoli
    found = []
    for name, cmd in (("Claude Code", "claude"), ("Codex", "codex"),
                      ("Antigravity", "antigravity"), ("VS Code", "code")):
        code, out = run(cmd, "--version")
        if code == 0:
            found.append(f"{name} {out.splitlines()[0] if out else ''}".strip())
            # Starší Claude Code nečte AGENTS.md
            if cmd == "claude" and (version(out) or (0, 0, 0)) < (2, 1, 277):
                fail(f"Claude Code {out}", "Nečte AGENTS.md, potřeba 2.1.277 nebo novější. Spusťte: claude update")
    info("Nalezení agenti a editory: " + (", ".join(found) if found else "žádný v PATH"))

    print()
    if errors:
        print(f"Počet chyb: {errors}. Opravte je a spusťte kontrolu znovu.")
        sys.exit(1)
    print("Prostředí je připravené.")


if __name__ == "__main__":
    main()
