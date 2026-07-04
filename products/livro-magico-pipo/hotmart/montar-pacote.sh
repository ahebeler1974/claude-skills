#!/usr/bin/env bash
# Monta o pacote de entrega do Hotmart: livro-magico-pipo-v1.zip
# Uso: bash products/livro-magico-pipo/hotmart/montar-pacote.sh
set -euo pipefail

RAIZ="$(cd "$(dirname "$0")/.." && pwd)"
SAIDA="$RAIZ/hotmart/pacote"
ZIP="$RAIZ/hotmart/livro-magico-pipo-v1.zip"

rm -rf "$SAIDA" "$ZIP"
mkdir -p "$SAIDA/bonus"

cp "$RAIZ/produto/livro-magico-pipo.html" "$SAIDA/"
cp "$RAIZ/bonus/atividades-para-imprimir.html" "$SAIDA/bonus/"
[ -f "$RAIZ/bonus/caderno-de-atividades.pdf" ] && cp "$RAIZ/bonus/caderno-de-atividades.pdf" "$SAIDA/bonus/"
[ -f "$RAIZ/bonus/guia-dos-pais.pdf" ] && cp "$RAIZ/bonus/guia-dos-pais.pdf" "$SAIDA/bonus/"

cat > "$SAIDA/LEIA-ME-PRIMEIRO.txt" <<'EOF'
🐤 O LIVRO MÁGICO DO PIPO — COMECE AQUI!

COMO ABRIR (30 segundos):

📱 CELULAR OU TABLET (recomendado):
1. Toque no arquivo "livro-magico-pipo.html"
2. Ele abre no navegador (Chrome ou Safari). Pronto!
3. Dica: no menu do navegador, toque em "Adicionar à tela
   inicial" para criar um ícone, como um aplicativo.

💻 COMPUTADOR:
1. Dê dois cliques em "livro-magico-pipo.html". Pronto!

🔊 O SOM liga no primeiro toque no botão "Começar a magia"
   (é uma proteção dos navegadores). Confira se o celular
   não está no modo silencioso.

🎁 BÔNUS (pasta "bonus"):
- "atividades-para-imprimir.html": abra e imprima (menu →
  Imprimir). São 8 atividades de papel e lápis.
- "guia-dos-pais.pdf": a ciência por trás de cada página
  e como brincar junto.

👨‍👩‍👧 CANTINHO DOS PAIS: dentro do livro, segure o botão
   "Pais" por 3 segundos (canto superior direito).

Precisa de ajuda? Responda o e-mail da sua compra.
Divirtam-se! Piu piu! 🐤
EOF

cd "$SAIDA"
if command -v zip >/dev/null 2>&1; then
  zip -r "$ZIP" . >/dev/null
else
  python3 -c "
import shutil
shutil.make_archive('${ZIP%.zip}', 'zip', '$SAIDA')
"
fi

echo "✅ Pacote criado: $ZIP"
echo "Conteúdo:"
cd "$SAIDA" && find . -type f | sort
echo ""
echo "Antes de subir no Hotmart: teste o zip em um Android, um iPhone e um computador."
