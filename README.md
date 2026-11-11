# ai-agent-data-lab

Připravené prostředí pro analýzu dat s AI agentem: Python (uv, pandas, DuckDB a další), Node.js a pokyny pro agenta v `AGENTS.md`.

```
├── AGENTS.md          # pokyny pro AI agenta (role, oprávnění, prostředí)
├── data/              # sem patří vstupní data
├── scripts/kontrola.py
└── pyproject.toml, uv.lock, requirements.txt
```

`AGENTS.md` je společný formát, který čte řada AI agentů (Claude Code od verze 2.1.277, Codex, Cursor, Gemini CLI a další). Při prvním spuštění agent pozná, jakým je nástrojem, a nabídne, že si podle `AGENTS.md` vytvoří vlastní nastavení (`.claude/`, `.codex/` …). Tato nastavení zůstávají lokálně a do gitu nejdou.

## Jak začít
Po instalaci (níže) vložte data do `data/`, otevřete složku v agentovi a napište, co chcete zjistit.

## Instalace
Návod počítá s Claude Code, ale jiný agent, který čte `AGENTS.md`, poslouží stejně. Zabere asi 15–20 minut. Všechny příkazy se píšou do **terminálu**: na Windows je to PowerShell (Start → napište „PowerShell“), na Macu aplikace Terminál.

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
Na konci musí být **„Prostředí je připravené.“** Kontrola vyžaduje Claude Code 2.1.277 nebo novější (starší verzi aktualizujete příkazem `claude update`). U každé chyby skript napíše, co udělat. Můžete také agentovi napsat `Zkontroluj prostředí`.

## Když něco nejde
- **Program „není rozpoznán“ nebo „command not found“:** otevřete nový terminál. Pokud běží VS Code, zavřete ho celý a otevřete znovu.
- **`uv sync` hlásí chybu sítě:** zkuste to znovu, případně bez firemní VPN.
- **`python --version` otevře Microsoft Store:** Python ještě není nainstalovaný. Spusťte `winget install Python.Python.3.13` a otevřete nový terminál.
- **`winget` není rozpoznán:** nainstalujte z Microsoft Store aplikaci „App Installer“ (Instalační program aplikace).
- **Nemáte `uv`:** knihovny jdou nainstalovat i přes pip ze souboru `requirements.txt` (Python 3.13).

## Licence
MIT.
