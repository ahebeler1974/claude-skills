# Decisões Técnicas

## Stack escolhida
- **Remotion 4.x** (React + TypeScript) para animação programática → render MP4 via Chromium headless + FFmpeg.
  - Motivo: controle total, componentes reutilizáveis, texto nítido, zero custo de API. Alinhado ao método do vídeo de referência.
  - **Licença Remotion:** gratuita para indivíduos e empresas pequenas elegíveis; há licença de empresa para times maiores. **Confirme os termos atuais** em remotion.dev antes de uso comercial em escala. (Isto não é aconselhamento jurídico.)
- **Chromium/Chrome do sistema** via `--browser-executable` → evita baixar o navegador próprio do Remotion (economiza banda/disco).
- **FFmpeg** (já no sistema) para montagem final, mux de áudio e gravação de legendas.
- **Piper TTS** (open source, MIT) para narração pt-BR local e gratuita. Alternativa a ElevenLabs/Voicebox, sem conta paga.

## Por que não as opções do briefing
- **ElevenLabs/Runway/Kling:** pagos → proibidos pelo orçamento zero.
- **Voicebox (jamiepine):** não verificado nesta sessão (YouTube/rede bloqueados); **não** afirmamos suas capacidades. Piper é a escolha segura e comprovadamente gratuita. Se você validar o Voicebox localmente e preferir, dá para trocar só o `scripts/gerar_narracao.py`.
- **Clonagem de voz (XTTS-v2 etc.):** possível localmente, porém o modelo XTTS tem **licença não-comercial** → risco para monetização. Use só a **sua** voz ou voz com autorização explícita.

## Ambiente onde o piloto foi testado (nuvem, efêmero)
- Ubuntu 24.04 · 4 vCPU · 15 GB RAM · **sem GPU** · ~30 GB livres · Node 22 · Python 3.13 · FFmpeg 6.1 · Chrome do sistema.
- **Sem GPU** → render por software (swiftshader/swangle). Funciona, mas é lento: ~5–6 s de render por segundo de vídeo em escala plena. Na **sua** máquina (com GPU ou mais núcleos) tende a ser mais rápido.

## Parâmetros de render
- Prévia: `--frames=0-239 --scale=0.5` (rápida, p/ validar).
- Final: escala 1.0, H.264 (`Config.setCodec("h264")`), `jpeg` como formato de frame (mais rápido que png).
- Concurrency = 4 (ajuste ao nº de núcleos da sua máquina).

## Sincronia de legendas (limitação honesta)
- Os tempos em `roteiro.json` são **estimados** (~2,5 palavras/s). Sincronia precisa exige medir o **áudio real**. Fluxo: gerar narração → ajustar `t0/t1` → `gerar_legendas.py`. Opcional: alinhamento automático local com WhisperX/aeneas.

## Economia de tokens / custo
- Inspeção de ambiente feita **uma vez**.
- Conteúdo (roteiro/legendas) separado do código → trocar vídeo não reprograma nada.
- Render de prévia antes do final; cache do Remotion entre renders.
- **Custo adicional efetivo identificado: US$ 0** (tudo local/open source; nenhuma API faturada; assinatura inalterada).
