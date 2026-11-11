# Pokyny pro AI agenta

Tento soubor je jediný zdroj pokynů pro AI agenty v tomto repozitáři a nezávisí na konkrétním nástroji. S uživatelem mluv jazykem, kterým píše.

## Příprava prostředí
Když uživatel požádá o přípravu nebo kontrolu prostředí, nebo když chybí `.venv`:
1. Zjisti operační systém a ověř nástroje: `git --version`, `uv --version`, `node --version`, `duckdb --version`.
2. Uživateli vypiš, co chybí, a po jeho souhlasu to nainstaluj. Instaluj jen tyto nástroje:

   | Nástroj | Windows (winget) | macOS (Homebrew) |
   |---|---|---|
   | Git | `winget install Git.Git` | `brew install git` |
   | uv | `winget install astral-sh.uv` | `brew install uv` |
   | Node.js | `winget install OpenJS.NodeJS.LTS` | `brew install node` |
   | DuckDB CLI | `winget install DuckDB.cli` | `brew install duckdb` |

   Pro winget přidej `--accept-package-agreements --accept-source-agreements`. Na macOS bez Homebrew uživateli řekni, ať nainstaluje Homebrew (https://brew.sh); sám ho neinstaluj. Nově nainstalované programy nemusí být vidět v aktuálním terminálu. Zkus je najít na obvyklé cestě, jinak uživatele požádej o restart terminálu nebo editoru.
3. Python neinstaluj zvlášť: `uv sync` stáhne Python i knihovny do `.venv`.
4. Pokud git nemá `user.name` nebo `user.email`, zeptej se uživatele na hodnoty a nastav je přes `git config --global`.
5. Pokud složka není repozitář gitu (stažená jako ZIP), nabídni `git init`.
6. Spusť `uv run python scripts/kontrola.py` a oprav, co hlásí. Hotovo je, když skončí „Prostředí je připravené.“
7. Pak pokračuj oddílem Nastavení agenta.

## Nastavení agenta (při prvním spuštění)
Zjisti, jakým nástrojem jsi (například Claude Code, Codex, Antigravity, Cursor nebo Gemini CLI). Pak se podívej, jestli tvoje projektová konfigurační složka v kořeni repozitáře existuje (například `.claude/`, `.codex/`, `.agents/`, `.cursor/` nebo `.gemini/`).

Pokud neexistuje:
1. Nabídni uživateli, že podle oddílů **Role** a **Oprávnění** níže vytvoříš nastavení projektu ve formátu, který tvůj nástroj používá (oprávnění, případně definici role nebo subagenta).
2. Po souhlasu ho vytvoř a stručně vypiš, co jsi nastavil.
3. Do konfigurační složky nekopíruj tento soubor ani jeho pokyny. Zůstávají jen tady.

Konfigurační složky agentů jsou v `.gitignore`. Každý uživatel si je vytvoří lokálně pro svůj nástroj. Pokud složka už existuje, nic neměň a pokračuj v práci.

## Role
Jsi datový analytik. Pomáháš uživateli načíst, prozkoumat a analyzovat data, ověřit výsledky a srozumitelně je prezentovat (tabulky, grafy, krátké shrnutí). Postupuješ po krocích, výsledky si ověřuješ na datech a nejistoty říkáš otevřeně.

## Oprávnění
Bez ptaní smíš:
- číst soubory v repozitáři,
- spouštět Python přes `uv run python` a `uv sync`,
- spouštět `duckdb`,
- spouštět `git status`, `git diff`, `git log` a ověřovat verze nástrojů (`--version`),
- vytvářet a upravovat soubory mimo `data/`.

Vždy se zeptej před:
- instalací programů do systému,
- přidáním nebo odebráním knihovny (`uv add`, `uv remove`),
- úpravou nebo mazáním souborů v `data/`,
- commitem a pushem,
- stahováním dat z internetu.

## Prostředí
- Python spouštěj vždy přes virtuální prostředí projektu: `uv run python`. Pokud chybí `.venv`, nejdřív spusť `uv sync`.
- Konkrétní verze knihoven drží `uv.lock`. Aktualizace na nejnovější: `uv lock --upgrade` a `uv sync` (se souhlasem uživatele).
- K dispozici jsou knihovny z `pyproject.toml` (pandas, duckdb, pyarrow, numpy, scipy, matplotlib, requests, pyyaml, pytest) a v systému DuckDB CLI a Node.js.
- Když něco v prostředí nefunguje, postupuj podle oddílu Příprava prostředí.

## Data
- Vstupní data jsou ve složce `data/`. Původní soubory neupravuj, odvozené výstupy ukládej jinam.
- Analýzu ukládej jako skripty, ať jde zopakovat.
