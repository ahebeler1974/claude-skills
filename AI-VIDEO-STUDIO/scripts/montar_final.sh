#!/usr/bin/env bash
# Montagem final com FFmpeg (local, gratis).
# Junta: video renderizado (sem audio) + narracao.wav + legendas.srt
# Gera: video_final_vertical.mp4 (com legendas gravadas + audio AAC)
#
# Uso:
#   bash scripts/montar_final.sh
#
# Requisitos: ffmpeg no PATH; ter rodado o render e a narracao antes.
set -euo pipefail
cd "$(dirname "$0")/.."

PROJ="projects/hematologia-001"
VIDEO_IN="$PROJ/export/video_sem_legendas.mp4"
AUDIO="$PROJ/audio/narracao.wav"
SRT="$PROJ/legendas/legendas.srt"
OUT="$PROJ/export/video_final_vertical.mp4"

[ -f "$VIDEO_IN" ] || { echo "ERRO: falta $VIDEO_IN (rode: npm run render)"; exit 1; }
[ -f "$SRT" ] || { echo "ERRO: falta $SRT (rode: python3 scripts/gerar_legendas.py)"; exit 1; }

# Estilo das legendas (grande, alto contraste, borda) para leitura no celular.
STYLE="FontSize=12,PrimaryColour=&H00FFFFFF,OutlineColour=&H00101820,BorderStyle=1,Outline=2,Shadow=1,MarginV=90,Alignment=2"

if [ -f "$AUDIO" ]; then
  echo "-> montando COM narracao + legendas gravadas"
  ffmpeg -y -i "$VIDEO_IN" -i "$AUDIO" \
    -vf "subtitles=$SRT:force_style='$STYLE'" \
    -map 0:v:0 -map 1:a:0 -shortest \
    -c:v libx264 -pix_fmt yuv420p -crf 18 -preset medium \
    -c:a aac -b:a 192k "$OUT"
else
  echo "AVISO: $AUDIO nao existe -> gerando versao SILENCIOSA com legendas gravadas."
  echo "       (Gere a narracao com scripts/gerar_narracao.py e rode de novo para ter audio.)"
  ffmpeg -y -i "$VIDEO_IN" \
    -vf "subtitles=$SRT:force_style='$STYLE'" \
    -c:v libx264 -pix_fmt yuv420p -crf 18 -preset medium "$OUT"
fi

echo "OK: $OUT"
ffprobe -v error -show_entries format=duration,size -of default=noprint_wrappers=1 "$OUT" || true
