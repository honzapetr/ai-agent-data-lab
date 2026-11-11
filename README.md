# ai-agent-data-lab

Výukový repozitář pro práci s AI agentem. Obsahuje připravené prostředí pro práci s daty (Python přes uv, pandas, DuckDB, Node.js) a pokyny pro agenta v `AGENTS.md`.

```
├── AGENTS.md          # pokyny pro AI agenta (příprava prostředí, role, oprávnění)
├── data/              # místo pro vstupní data
├── scripts/kontrola.py
└── pyproject.toml, uv.lock
```

`AGENTS.md` je společný formát, který čtou Claude Code (od verze 2.1.277), Codex, Antigravity a další agenti. Při prvním spuštění agent pozná, jakým je nástrojem, a nabídne, že si podle `AGENTS.md` vytvoří vlastní nastavení (`.claude/`, `.codex/`, `.agents/` …). Tato nastavení zůstávají lokálně a do gitu nejdou.

## Jak začít
Připravený pracovní prostor je teprve začátek. Otevřete ho v agentovi a společně s ním pracujte na dalším postupu: nastavení agenta, vlastních pravidlech, nástrojích a postupně i na analýze vašich dat ve složce `data/`.

## Instalace
Sami nainstalujete jen AI agenta a stáhnete repozitář. Zbytek prostředí pak připraví agent. Příkazy se píšou do **terminálu**: na Windows je to PowerShell (Start → napište „PowerShell“), na Macu aplikace Terminál.

### Krok 1: Nainstalujte AI agenta
Vyberte si jednoho (nebo víc). Každý potřebuje vlastní účet:

| Agent | Účet | Kde s ním pracujete |
|---|---|---|
| Claude Code | Claude Pro nebo vyšší | terminál nebo VS Code s rozšířením |
| Codex | ChatGPT Plus nebo vyšší | terminál nebo VS Code s rozšířením |
| Antigravity | účet Google | vlastní editor Antigravity |

#### Claude Code
```powershell
# Windows
irm https://claude.ai/install.ps1 | iex
# macOS
curl -fsSL https://claude.ai/install.sh | bash
```

#### Codex
```powershell
# Windows
winget install OpenAI.Codex
# macOS
brew install --cask codex
```

#### Antigravity
```powershell
# Windows
winget install Google.AntigravityIDE
```
Na macOS stáhněte instalátor z [antigravity.google](https://antigravity.google/download).

#### VS Code s rozšířením (volitelně pro Claude Code a Codex)
```powershell
# Windows
winget install Microsoft.VisualStudioCode
# macOS
brew install --cask visual-studio-code
```
**Zavřete terminál a otevřete nový**, pak nainstalujte rozšíření pro svého agenta:
```bash
code --install-extension anthropic.claude-code   # Claude Code
code --install-extension openai.chatgpt          # Codex
```

### Krok 2: Stáhněte repozitář
Doporučujeme složku mimo OneDrive nebo jiné synchronizované úložiště, například `C:\projekty` (na Macu `~/projekty`).

- **Máte git:** `git clone https://github.com/honzapetr/ai-agent-data-lab.git`
- **Nemáte git:** na [stránce repozitáře](https://github.com/honzapetr/ai-agent-data-lab) klikněte na **Code → Download ZIP** a rozbalte ho. Git pak nainstaluje a nastaví agent.

### Krok 3: Spusťte agenta ve složce repozitáře
- **Claude Code:** v terminálu `cd ai-agent-data-lab` a `claude`. Přihlaste se účtem Claude a potvrďte důvěru ke složce. Režim **Auto** zapnete klávesami Shift+Tab. Ve VS Code otevřete složku a panel Claude Code.
- **Codex:** v terminálu `cd ai-agent-data-lab` a `codex`. Přihlaste se účtem ChatGPT. Ve VS Code otevřete složku a panel Codex.
- **Antigravity:** File → Open Folder, vyberte složku a otevřete panel agenta. Přihlaste se účtem Google.

### Krok 4: Nechte agenta připravit prostředí
Napište agentovi:
```
Připrav prostředí
```
Agent podle `AGENTS.md` zjistí, co chybí (Python, uv, Git, Node.js, DuckDB CLI), a po vašem souhlasu to nainstaluje. Pak stáhne knihovny (`uv sync`), nastaví git a spustí kontrolu. Hotovo je, když kontrola skončí hláškou **„Prostředí je připravené.“**

Kontrolu jde spustit i ručně: `uv run python scripts/kontrola.py`.

## Když něco nejde
- **Program „není rozpoznán“ nebo „command not found“:** otevřete nový terminál. Pokud běží editor, zavřete ho celý a otevřete znovu.
- **`winget` není rozpoznán:** nainstalujte z Microsoft Store aplikaci „App Installer“ (Instalační program aplikace).
- **macOS nezná `brew`:** nainstalujte [Homebrew](https://brew.sh).
- **Instalace hlásí chybu sítě:** zkuste to znovu, případně bez firemní VPN.
- **Agent nečte `AGENTS.md`:** aktualizujte ho (Claude Code: `claude update`, potřeba verze 2.1.277 nebo novější). Pokud je ve složce nebo nad ní `CLAUDE.md`, Claude Code čte jen ten.

## Licence
MIT.
