# AI VIDEO STUDIO — Science & Health

Estúdio **reutilizável** para produzir vídeos científicos animados (9:16) de forma
programática, **local e gratuita**: animação com **Remotion** (React/TS), narração com
**Piper TTS** (open source, pt-BR), montagem com **FFmpeg**. Sem custo além da sua
assinatura do Claude — **nenhuma API paga, nenhuma renderização em nuvem cobrada**.

Piloto incluído: **"O que acontece com as hemácias quando o oxigênio começa a faltar?"**

---

## ⚠️ Leia primeiro (onde isto roda)
Este projeto foi criado e a **prévia** foi renderizada num contêiner de nuvem **efêmero**
(sem GPU). O caminho natural para uso real é a **sua máquina**, onde ficam sua voz, seus
canais e (talvez) uma GPU. Nada aqui depende de serviço pago.

## Requisitos (na sua máquina)
- **Node.js ≥ 18** e npm
- **FFmpeg** no PATH
- **Chrome/Chromium** instalado (ou deixe o Remotion baixar o dele)
- **Python ≥ 3.9** (para scripts de legenda/narração)
- **Piper TTS** (opcional, para narração): `pip install piper-tts` + uma voz pt-BR

## Instalação
```bash
cd AI-VIDEO-STUDIO
npm install
```

## Fluxo de produção (passo a passo)
```bash
# 1. Pré-visualizar no navegador (estúdio interativo do Remotion)
npm run studio

# 2. Prévia rápida de baixa resolução (valida antes do render pesado)
npm run preview
#   -> projects/hematologia-001/preview/preview.mp4

# 3. Narração local (opcional, mas recomendado) — precisa do Piper + voz pt-BR
python3 scripts/gerar_narracao.py --model assets/audio/voices/pt_BR-faber-medium.onnx
#   -> projects/hematologia-001/audio/narracao.wav  e  public/audio/narracao.wav
#   Depois, ajuste os tempos t0/t1 em src/data/roteiro.json p/ casar com o áudio.

# 4. Legendas (SRT) a partir do roteiro
python3 scripts/gerar_legendas.py
#   -> projects/hematologia-001/legendas/legendas.srt

# 5. Render final (vídeo sem áudio/legendas gravadas)
npm run render
#   -> projects/hematologia-001/export/video_sem_legendas.mp4
#   (Se não usar o Chrome do sistema, rode: npm run render:local)

# 6. Montagem final (FFmpeg): + narração + legendas gravadas
bash scripts/montar_final.sh
#   -> projects/hematologia-001/export/video_final_vertical.mp4
```

> Para usar a narração no próprio render do Remotion (em vez de mux no FFmpeg),
> passe a prop: edite `defaultProps` no `src/Root.tsx` para `{ audioSrc: "audio/narracao.wav" }`
> (o arquivo precisa estar em `public/audio/`).

## Como fazer o **próximo** vídeo (sem reprogramar)
```bash
python3 scripts/novo_video.py --id hematologia-002 --titulo "Por que o sangue é vermelho?"
```
Depois:
1. Edite o roteiro gerado em `projects/<id>/roteiro/roteiro.json` (falas, tempos, textos, cenas).
2. Copie-o para `src/data/roteiro.json` (fonte que a composição lê).
3. Reaproveite os **mesmos componentes** (`src/components/*`): hemácia, hemoglobina, câmera, legendas…
4. Rode prévia → narração → legendas → render → montagem.

Para um **tema novo** (ex.: outro nicho), em geral basta: novo roteiro + talvez 1–2 componentes
científicos novos em `src/components/scientific.tsx`. Os componentes cinematográficos e de
comunicação são genéricos e se reaproveitam.

## Estrutura
```
AI-VIDEO-STUDIO/
├─ src/
│  ├─ components/   cinematic.tsx · scientific.tsx · communication.tsx  (biblioteca reutilizável)
│  ├─ scenes/       PilotScenes.tsx   (6 cenas do piloto)
│  ├─ compositions/ HematologiaPilot.tsx
│  ├─ data/         roteiro.json      (MOTOR DE ROTEIRO — conteúdo separado do código)
│  ├─ theme.ts      (identidade visual: cores, tipografia)
│  └─ Root.tsx      (registro das composições)
├─ scripts/         gerar_narracao.py · gerar_legendas.py · montar_final.sh · novo_video.py
├─ projects/
│  └─ hematologia-001/  roteiro/ storyboard/ audio/ legendas/ preview/ export/ publicacao.md
├─ references/      referencias.md
├─ docs/            DECISOES-TECNICAS.md · desempenho.csv
├─ public/          (assets estáticos p/ Remotion; áudio vai em public/audio/)
└─ remotion.config.ts · package.json · tsconfig.json
```

## Biblioteca de componentes
- **Científicos** (`scientific.tsx`): `Hemacia` (oxigenação por cor, sem mudar de forma), `MoleculaOxigenio`, `Hemoglobina` (tetrâmero, O₂ liga 0→4), `VasoSanguineo`, `CapilarRede`, `CelulaGenerica` (mitocôndrias).
- **Cinematográficos** (`cinematic.tsx`): `CinematicBackground`, `GlowEffect`, `ParticleField`, `CameraRig` (zoom/pan/follow).
- **Comunicação** (`communication.tsx`): `AnimatedTitle`, `ScientificLabel`, `SubtitleOverlay`, `ProgressIndicator`, `ClosingCard`.

Todos são parametrizáveis (tamanho, cor, posição, intensidade) e reaproveitáveis em outros vídeos.

## Limitações honestas
- **Sem GPU** nesta sessão → render por software é lento (~5–6 s de render por segundo de vídeo em escala plena). Sua máquina pode ser bem mais rápida.
- **Narração:** não é gerada automaticamente aqui (Piper não vem instalado na nuvem). O script está pronto para a sua máquina. **Não** criamos áudio falso.
- **Sincronia de legendas:** tempos são **estimados** até você medir o áudio real.
- **Fotorrealismo:** não é objetivo — são ilustrações científicas estilizadas (preciso > bonito-mas-errado).

## Custo
**US$ 0** adicionais. Tudo é local/open source. Nenhuma API faturada, nenhuma assinatura alterada.

## Licenças
- Remotion: grátis p/ indivíduos/pequenas empresas elegíveis (confira termos atuais p/ uso comercial).
- Piper: MIT. · FFmpeg: LGPL/GPL. · Animações deste repo: originais (geradas por código).
- Registre a licença de qualquer mídia de terceiros em `docs/` antes de publicar.
