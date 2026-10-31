#!/usr/bin/env python3
"""
Gera a narracao em portugues do Brasil LOCALMENTE e de graca usando o Piper TTS.

Por que Piper (e nao ElevenLabs/Voicebox): Piper e open source (MIT), roda em CPU,
tem vozes pt-BR e NAO exige nenhuma conta paga nem chamada de API. Qualidade boa
para narracao (nao e clonagem). Se voce quiser SUA voz, veja a nota no fim.

PRE-REQUISITOS (rodar UMA vez, na sua maquina):
  pip install piper-tts
  # Baixe uma voz pt-BR (arquivos .onnx + .onnx.json), por ex. da colecao oficial:
  #   https://github.com/rhasspy/piper   (modelos em huggingface rhasspy/piper-voices)
  #   vozes pt-BR comuns: pt_BR-faber-medium, pt_BR-edresson-low
  # Coloque os dois arquivos em  assets/audio/voices/

Uso:
  python3 scripts/gerar_narracao.py --model assets/audio/voices/pt_BR-faber-medium.onnx

Saida:
  projects/hematologia-001/audio/cena_s1.wav ... cena_s6.wav
  projects/hematologia-001/audio/narracao.wav   (concatenado)
  public/audio/narracao.wav                     (copia p/ o Remotion usar via staticFile)

IMPORTANTE: este script NAO inventa audio. Se o Piper nao estiver instalado ou o
modelo nao for encontrado, ele PARA e explica o que falta — nada de arquivo falso.
"""
import argparse
import json
import os
import shutil
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROTEIRO = os.path.join(ROOT, "src", "data", "roteiro.json")
AUDIO_DIR = os.path.join(ROOT, "projects", "hematologia-001", "audio")
PUBLIC_AUDIO = os.path.join(ROOT, "public", "audio")


def have(cmd: str) -> bool:
    return shutil.which(cmd) is not None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True, help="Caminho do modelo .onnx do Piper (voz pt-BR).")
    ap.add_argument("--length-scale", default="1.0", help="Ritmo da fala (1.0 normal; >1 mais lento).")
    args = ap.parse_args()

    if not have("piper"):
        print("ERRO: 'piper' nao encontrado no PATH.")
        print("Instale com:  pip install piper-tts   e baixe uma voz pt-BR (.onnx + .onnx.json).")
        print("Depois rode de novo. Nenhum audio foi gerado.")
        return 2
    if not os.path.exists(args.model):
        print(f"ERRO: modelo nao encontrado: {args.model}")
        print("Baixe uma voz pt-BR do Piper e aponte --model para o arquivo .onnx.")
        return 2
    if not have("ffmpeg"):
        print("ERRO: ffmpeg nao encontrado (necessario para concatenar/normalizar).")
        return 2

    with open(ROTEIRO, encoding="utf-8") as f:
        data = json.load(f)

    os.makedirs(AUDIO_DIR, exist_ok=True)
    os.makedirs(PUBLIC_AUDIO, exist_ok=True)

    partes = []
    for cena in data["cenas"]:
        wav = os.path.join(AUDIO_DIR, f"cena_{cena['id']}.wav")
        texto = cena["narracao"]
        print(f"-> sintetizando {cena['id']}: {texto[:48]}...")
        subprocess.run(
            ["piper", "--model", args.model, "--length_scale", args.length_scale, "--output_file", wav],
            input=texto.encode("utf-8"), check=True,
        )
        partes.append(wav)

    # Concatena com pequena pausa entre cenas e normaliza volume (loudnorm).
    lista = os.path.join(AUDIO_DIR, "_concat.txt")
    with open(lista, "w", encoding="utf-8") as f:
        for p in partes:
            f.write(f"file '{p}'\n")
    bruto = os.path.join(AUDIO_DIR, "_bruto.wav")
    final = os.path.join(AUDIO_DIR, "narracao.wav")
    subprocess.run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", lista, "-c", "copy", bruto], check=True)
    subprocess.run(["ffmpeg", "-y", "-i", bruto, "-af", "loudnorm=I=-16:TP=-1.5:LRA=11", final], check=True)
    shutil.copy(final, os.path.join(PUBLIC_AUDIO, "narracao.wav"))

    print(f"\nOK: narracao em {final}")
    print("Copiada para public/audio/narracao.wav (use audioSrc='audio/narracao.wav' na composicao).")
    print("PROXIMO PASSO: ajuste os tempos t0/t1 em src/data/roteiro.json para casar com o audio real,")
    print("e regenere as legendas:  python3 scripts/gerar_legendas.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
