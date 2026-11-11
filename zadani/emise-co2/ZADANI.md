# Emise CO₂ ve světě a v Česku

**Popis:** Jak se vyvíjely emise CO₂ v Česku ve srovnání s Evropou a světem a co je za tím.
**Obtížnost:** začátečník
**Data:** Our World in Data, CO₂ and Greenhouse Gas Emissions (licence CC BY 4.0)

## Cíl
Zjistit, jak se od roku 1990 změnily emise CO₂ v Česku celkově i na obyvatele, jak si Česko stojí proti sousedům a světu a z jakých zdrojů emise pocházejí.

## Data
Skript `data.py` stáhne soubor `owid-co2-data.csv` (asi 15 MB) do `data/`. Jeden řádek odpovídá jedné zemi nebo regionu v jednom roce. Hlavní sloupce:

- `country`, `iso_code`, `year`
- `co2` (miliony tun), `co2_per_capita` (tuny na obyvatele)
- `coal_co2`, `oil_co2`, `gas_co2`, `cement_co2` (emise podle zdroje)
- `population`, `gdp`

Popis všech sloupců: https://github.com/owid/co2-data/blob/master/owid-co2-codebook.csv

## Úkoly
1. Prozkoumej data: období, počet zemí, chybějící hodnoty.
2. Vývoj emisí Česka od roku 1990, celkem i na obyvatele.
3. Srovnání na obyvatele: Česko, Německo, Polsko, Slovensko, Rakousko, EU a svět.
4. Složení emisí Česka podle zdroje (uhlí, ropa, plyn, cement) v čase.
5. Vztah emisí a HDP: oddělil se růst ekonomiky od růstu emisí?

## Výstup
Do `vystupy/` ulož 3–4 grafy a krátký report `report.md` s hlavními zjištěními (5–10 vět).

## Poznámky
- Řádky jako `World`, `Europe` nebo `European Union (27)` jsou agregace, ne země. Poznáš je podle prázdného `iso_code`.
- Údaje o HDP končí dřív než údaje o emisích.
- Při použití dat uveď zdroj: Our World in Data.
