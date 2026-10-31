#!/usr/bin/env python3
"""
Cria um NOVO projeto de video a partir de um template de roteiro, sem reprogramar
nada. Reutiliza os mesmos componentes/cenas; voce so edita o roteiro e os textos.

Uso:
    python3 scripts/novo_video.py --id hematologia-002 --titulo "Por que o sangue e vermelho?"

O que faz:
  - cria projects/<id>/ com as subpastas padrao
  - copia src/data/roteiro.json para projects/<id>/roteiro/roteiro.json como ponto de partida
  - imprime os proximos passos

NAO renderiza nem publica nada. Fluxo manual e sob seu controle.
"""
import argparse
import json
import os
import shutil
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--id", required=True, help="Id do projeto, ex.: hematologia-002")
    ap.add_argument("--titulo", required=True, help="Titulo de trabalho do video")
    args = ap.parse_args()

    base = os.path.join(ROOT, "projects", args.id)
    if os.path.exists(base):
        print(f"ERRO: {base} ja existe. Escolha outro --id.")
        return 2
    for sub in ("roteiro", "storyboard", "audio", "legendas", "preview", "export"):
        os.makedirs(os.path.join(base, sub), exist_ok=True)

    src = os.path.join(ROOT, "src", "data", "roteiro.json")
    with open(src, encoding="utf-8") as f:
        data = json.load(f)
    data["meta"]["projectId"] = args.id
    data["meta"]["titulo"] = args.titulo
    dst = os.path.join(base, "roteiro", "roteiro.json")
    with open(dst, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"OK: projeto criado em {base}")
    print("\nPROXIMOS PASSOS:")
    print(f"  1. Edite o roteiro:            {dst}")
    print("  2. Copie para src/data/roteiro.json quando for renderizar este video")
    print("     (ou adapte o Root.tsx para carregar o roteiro por projeto).")
    print("  3. npx remotion studio          # pre-visualizar")
    print("  4. python3 scripts/gerar_narracao.py --model <voz pt-BR>")
    print("  5. python3 scripts/gerar_legendas.py")
    print("  6. npm run render && bash scripts/montar_final.sh")
    return 0


if __name__ == "__main__":
    sys.exit(main())
