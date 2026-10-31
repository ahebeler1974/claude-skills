#!/usr/bin/env python3
"""
Gera legendas.srt a partir do roteiro.json.

Uso:
    python3 scripts/gerar_legendas.py

Observacao HONESTA: os tempos vem do roteiro e sao ESTIMADOS.
Para sincronia real, regenere o audio de narracao, meca a duracao de cada
trecho (ex.: com whisperX/aeneas localmente, ou manualmente) e atualize os
campos t0/t1 em src/data/roteiro.json antes de rodar este script de novo.
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROTEIRO = os.path.join(ROOT, "src", "data", "roteiro.json")
OUT = os.path.join(ROOT, "projects", "hematologia-001", "legendas", "legendas.srt")


def ts(seconds: float) -> str:
    ms = int(round(seconds * 1000))
    h, ms = divmod(ms, 3600_000)
    m, ms = divmod(ms, 60_000)
    s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def main() -> int:
    with open(ROTEIRO, encoding="utf-8") as f:
        data = json.load(f)
    blocos = []
    for cena in data["cenas"]:
        for leg in cena.get("legendas", []):
            blocos.append((leg["t0"], leg["t1"], leg["texto"]))
    blocos.sort(key=lambda b: b[0])
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        for i, (t0, t1, texto) in enumerate(blocos, 1):
            f.write(f"{i}\n{ts(t0)} --> {ts(t1)}\n{texto}\n\n")
    print(f"OK: {len(blocos)} legendas -> {OUT}")
    print("AVISO: tempos estimados. Re-sincronize com o audio real antes do final.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
