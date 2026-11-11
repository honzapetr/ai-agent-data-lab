# Pokyny pro AI agenta

Tento repozitář je datová laboratoř: katalog zadání v `zadani/` a připravené prostředí pro Python. S uživatelem mluv česky, pokud nezačne jiným jazykem.

## Prostředí
- Python spouštěj vždy přes virtuální prostředí projektu: `uv run python`. Pokud chybí `.venv`, nejdřív spusť `uv sync`.
- K dispozici jsou knihovny z `pyproject.toml` (pandas, duckdb, pyarrow, numpy, scipy, matplotlib, requests, pyyaml, pytest) a v systému DuckDB CLI a Node.js. Nové knihovny přidávej jen se souhlasem uživatele (`uv add`).
- Když něco v prostředí nefunguje, spusť `uv run python scripts/kontrola.py` a postupuj podle README.md.

## Začátek konverzace: výběr tématu
Pokud uživatel ještě neřekl, na čem chce pracovat, nebo píše jen pozdrav:
1. Projdi `zadani/*/ZADANI.md` (kromě `_sablona`) a z každého vezmi název a jednovětý popis.
2. Podívej se, jestli existují rozpracované složky v `prace/`.
3. Nabídni uživateli výběr (pokud to nástroj umí, jako volbu z možností):
   - témata z katalogu (název a popis),
   - **vlastní téma**,
   - **pokračovat v rozpracované práci** (jen pokud v `prace/` něco je).

## Příprava pracovní složky
Po výběru tématu z katalogu:
1. Zkopíruj celou složku `zadani/<tema>/` do `prace/<tema>/`. Pokud už existuje, nic nepřepisuj a nabídni pokračování.
2. Vytvoř v ní `data/` a `vystupy/`.
3. Pokud je ve složce `data.py`, spusť ho: `uv run python prace/<tema>/data.py`. Jinak postupuj podle oddílu Data v `ZADANI.md`.
4. Udělej krátký přehled dat (soubory, počet řádků, sloupce, rozsah) a navrhni uživateli první kroky analýzy podle zadání.

U vlastního tématu se nejdřív doptej na cíl, data a očekávaný výstup. Pak podle `zadani/_sablona/ZADANI.md` vytvoř `prace/<tema>/ZADANI.md` a dál postupuj stejně. Název složky `<tema>` piš malými písmeny bez diakritiky, slova odděluj pomlčkou.

Při pokračování v rozpracované práci si přečti `prace/<tema>/ZADANI.md` a obsah složky a shrň, kde práce skončila.

## Při práci
- Pracuj jen uvnitř `prace/<tema>/`. Složku `zadani/` neměň, pokud o to uživatel výslovně nepožádá (například když chce zadání přidat do katalogu).
- Původní data v `data/` neupravuj. Odvozené tabulky, grafy a reporty ukládej do `vystupy/`.
- Skripty ukládej do pracovní složky, ať jde analýzu zopakovat.
- `prace/` je v `.gitignore`. Práce uživatele se do sdíleného repozitáře nedostane.

## Přidání zadání do katalogu
Nové zadání je složka `zadani/<tema>/` s `ZADANI.md` podle `zadani/_sablona/ZADANI.md` a volitelně `data.py`, který stáhne data do `data/` vedle sebe. Velká data do repozitáře nepatří, stahují se skriptem.
