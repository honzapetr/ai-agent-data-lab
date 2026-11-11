"""Stáhne data o emisích CO₂ (Our World in Data) do složky data/ vedle tohoto skriptu.

Spuštění: uv run python <cesta>/data.py
"""
from pathlib import Path

import requests

URL = "https://raw.githubusercontent.com/owid/co2-data/master/owid-co2-data.csv"
CIL = Path(__file__).resolve().parent / "data" / "owid-co2-data.csv"

CIL.parent.mkdir(exist_ok=True)
odpoved = requests.get(URL, timeout=120)
odpoved.raise_for_status()
CIL.write_bytes(odpoved.content)
print(f"Uloženo: {CIL} ({len(odpoved.content) / 1e6:.1f} MB)")
