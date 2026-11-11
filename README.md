# ai-agent-data-lab

Datová laboratoř pro analýzu dat s AI agentem. Obsahuje připravené prostředí pro Python a katalog zadání. Agent se na začátku zeptá, jaké téma chcete řešit, a připraví vám pracovní složku i s daty.

```
├── AGENTS.md          # pokyny pro AI agenta (CLAUDE.md na ně odkazuje)
├── zadani/            # katalog zadání: každé ve vlastní složce
│   └── _sablona/      # šablona pro nové zadání
├── prace/             # vaše analýzy (vzniká lokálně, do gitu nejde)
└── scripts/kontrola.py
```

Pokyny pro agenta jsou v `AGENTS.md`, společném formátu, který čte řada AI agentů. Návod níže počítá s Claude Code.

## Jak začít
Po instalaci (níže) otevřete složku repozitáře v agentovi a napište třeba `Ahoj`. Agent:
1. nabídne témata z `zadani/`, vlastní téma, nebo pokračování v rozpracované práci,
2. po výběru založí `prace/<tema>/` se zadáním, stáhne data a udělá jejich první přehled,
3. dál s vámi pracuje jen v této složce.

Nová zadání z katalogu získáte příkazem `git pull`. Vaše práce v `prace/` zůstává jen u vás.

## Instalace
Zabere asi 15–20 minut. Všechny příkazy se píšou do **terminálu**: na Windows je to PowerShell (Start → napište „PowerShell“), na Macu aplikace Terminál.

### Krok 1: Co potřebujete mít
- **Účet Claude Pro** (nebo vyšší). S free účtem Claude Code nefunguje.
- Počítač s Windows 10/11 nebo macOS 13+.
- Právo instalovat programy.

### Krok 2: Nainstalujte nástroje

| Program | K čemu |
|---|---|
| Python (3.12 nebo novější) | jazyk pro analýzu dat |
| Git | stažení repozitáře |
| uv | Python a knihovny |
| Node.js (verze 22.20 nebo novější) | pomocné nástroje |
| DuckDB CLI | práce s daty |
| Claude Code | AI agent |
| VS Code | editor |
| Rozšíření Claude Code do VS Code | agent přímo v editoru |

#### Windows
V PowerShellu spusťte jeden řádek po druhém a vždy počkejte, až doběhne:
```powershell
winget install Python.Python.3.13
winget install Git.Git
winget install astral-sh.uv
winget install OpenJS.NodeJS.LTS
winget install DuckDB.cli --version 1.5.6
irm https://claude.ai/install.ps1 | iex
winget install Microsoft.VisualStudioCode
```
Pokud se `winget` zeptá na souhlas s podmínkami, odpovězte `Y`.

#### macOS (postup zatím neověřený)
Potřebujete [Homebrew](https://brew.sh). V Terminálu spusťte:
```bash
brew install python git uv node duckdb
brew install --cask visual-studio-code
curl -fsSL https://claude.ai/install.sh | bash
```

#### Rozšíření do VS Code
**Zavřete terminál a otevřete nový**, jinak nové programy nebudou vidět. Pak spusťte:
```
code --install-extension anthropic.claude-code
```

#### Nastavení gitu
Pokud jste git ještě nepoužívali, nastavte jméno a e-mail (bez nich git odmítne uložit změny):
```bash
git config --global user.name "Jméno Příjmení"
git config --global user.email "vas@email.cz"
```

### Krok 3: Stáhněte repozitář
Doporučujeme složku mimo OneDrive nebo jiné synchronizované úložiště, například `C:\projekty` (na Macu `~/projekty`):
```bash
git clone https://github.com/honzapetr/ai-agent-data-lab.git
cd ai-agent-data-lab
```

### Krok 4: Připravte Python
```bash
uv sync
```
Stáhne Python 3.13 a všechny knihovny ve správných verzích do složky `.venv`.

### Krok 5: Přihlaste se do Claude Code
Ve složce repozitáře spusťte `claude`:
1. Projděte úvodní obrazovky (šipky a Enter) a jako přihlášení zvolte účet Claude s předplatným.
2. V prohlížeči se přihlaste a vraťte se do terminálu.
3. Potvrďte, že složce důvěřujete.
4. Pod polem pro zprávu by mělo být `auto mode on`. Pokud není, přepínejte režimy klávesami **Shift+Tab**.

Ve VS Code (`code .`) otevřete panel Claude Code. Pokud se zeptá na přihlášení, přihlaste se stejným účtem.

### Krok 6: Ověřte prostředí
```bash
uv run python scripts/kontrola.py
```
Na konci musí být **„Prostředí je připravené.“** U každé chyby skript napíše, co udělat. Můžete také agentovi napsat `Zkontroluj prostředí`.

## Přidání vlastního zadání
1. Zkopírujte `zadani/_sablona/` do `zadani/<nazev-tematu>/` (malá písmena, bez diakritiky, pomlčky).
2. Vyplňte `ZADANI.md`.
3. Pokud se data dají stáhnout, přidejte `data.py`, který je uloží do `data/` vedle sebe. Velká data do repozitáře nepatří.
4. Pošlete pull request. Nová zadání jsou vítaná.

## Když něco nejde
- **Program „není rozpoznán“ nebo „command not found“:** otevřete nový terminál. Pokud běží VS Code, zavřete ho celý a otevřete znovu.
- **`uv sync` hlásí chybu sítě:** zkuste to znovu, případně bez firemní VPN.
- **`python --version` otevře Microsoft Store:** Python ještě není nainstalovaný. Spusťte `winget install Python.Python.3.13` a otevřete nový terminál.
- **`winget` není rozpoznán:** nainstalujte z Microsoft Store aplikaci „App Installer“ (Instalační program aplikace).
- **Nemáte `uv`:** knihovny jdou nainstalovat i přes pip ze souboru `requirements.txt` (Python 3.13).

## Licence
MIT. Data v zadáních mají vlastní licence uvedené v jednotlivých `ZADANI.md`.
