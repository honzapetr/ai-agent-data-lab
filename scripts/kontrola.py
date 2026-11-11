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
    if sys.version_info[:2] != (3, 13):
        fail(f"Python {sys.version.split()[0]}",
             "Spusťte ve složce repozitáře: uv sync, pak uv run python scripts/kontrola.py")
        sys.exit(1)
    ok(f"Python {sys.version.split()[0]}")

    deps = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))["project"]["dependencies"]
    bad = []
    for dep in deps:
        name, want = dep.split("==")
        try:
            have = metadata.version(name)
        except metadata.PackageNotFoundError:
            have = None
        if have != want:
            bad.append(f"{name} {have or 'chybí'} (má být {want})")
    if bad:
        fail("Knihovny Pythonu", "; ".join(bad) + ". Spusťte: uv sync")
    else:
        ok(f"Knihovny Pythonu ({len(deps)})")

    # Nástroje
    code, out = run("python3" if sys.platform == "darwin" else "python", "--version")
    v = version(out) if code == 0 else None
    if v is None or v < (3, 12, 0):
        fail("Python v systému", "Nenalezen nebo starší než 3.12. Viz README, krok 2.")
    else:
        ok(f"Python v systému {'.'.join(map(str, v))}")

    code, out = run("git", "--version")
    if code != 0:
        fail("Git", "Nenalezen. Viz README, krok 2.")
    else:
        ok(out)
        # Bez jména a e-mailu git odmítne commit („empty ident name … not allowed“)
        for key, label in (("user.name", "jméno"), ("user.email", "e-mail")):
            code, out = run("git", "-C", str(ROOT), "config", key)
            if code == 0 and out:
                ok(f"Git: {label} {out}")
            else:
                fail(f"Git: {label}", f"Není nastavené. Spusťte: git config --global {key} \"...\" (README, krok 2).")
        code, out = run("git", "-C", str(ROOT), "rev-parse", "--is-inside-work-tree")
        if code == 0 and out == "true":
            ok("Složka je repozitář gitu")
        else:
            fail("Repozitář gitu", "Složka není repozitář. Stáhněte ji přes git clone (README, krok 3).")

    code, out = run("node", "--version")
    v = version(out) if code == 0 else None
    if v is None:
        fail("Node.js", "Nenalezen. Viz README, krok 2.")
    elif v < (22, 20, 0):
        fail(f"Node.js {out}", "Potřeba verze 22.20 nebo novější.")
    else:
        ok(f"Node.js {out}")

    code, out = run("duckdb", "--version")
    v = version(out) if code == 0 else None
    ok(f"DuckDB CLI {'.'.join(map(str, v))}") if v else fail("DuckDB CLI", "Nenalezeno. Viz README, krok 2.")

    code, out = run("code", "--version")
    if code != 0:
        fail("VS Code", "Nenalezen. Viz README, krok 2.")
    else:
        ok(f"VS Code {out.splitlines()[0]}")
        code, out = run("code", "--list-extensions")
        if "anthropic.claude-code" in out.lower().split():
            ok("Rozšíření Claude Code ve VS Code")
        else:
            fail("Rozšíření Claude Code ve VS Code", "Nenainstalováno. Viz README, krok 2.")

    code, out = run("claude", "--version")
    if code != 0:
        fail("Claude Code", "Nenalezen. Viz README, krok 2.")
    else:
        ok(f"Claude Code {out}")
        code, out = run("claude", "auth", "status", "--json")
        try:
            logged_in = json.loads(out).get("loggedIn")
        except json.JSONDecodeError:
            logged_in = False
        ok("Přihlášeno do Claude") if logged_in else fail("Přihlášení do Claude", "Viz README, krok 5.")

    print()
    if errors:
        print(f"Počet chyb: {errors}. Opravte je a spusťte kontrolu znovu.")
        sys.exit(1)
    print("Prostředí je připravené.")


if __name__ == "__main__":
    main()
