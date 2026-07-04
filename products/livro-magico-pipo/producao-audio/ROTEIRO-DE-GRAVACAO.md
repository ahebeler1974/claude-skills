# 🎙️ Roteiro de Produção de Áudio — O Livro Mágico do Pipo

Este roteiro gera a versão com **voz natural + músicas de verdade** em ~30 minutos, usando duas ferramentas de IA (as duas têm plano gratuito que dá conta):

- **Músicas → Suno** (suno.com) — você cola a letra e o estilo, ele devolve a música cantada
- **Voz → ElevenLabs** (elevenlabs.io) — você cola a frase, ele devolve a fala em voz natural

Depois: coloque todos os MP3s numa pasta e rode `python3 embutir-audios.py pasta/` — **ou envie os MP3s no chat do Claude, que ele embute e devolve o arquivo pronto.**

⚠️ **Nomeie cada arquivo EXATAMENTE como indicado** (minúsculas, com hífen, extensão .mp3).

---

## PARTE 1 — As 2 músicas (Suno)

### `tema.mp3` — O Tema do Pipo (toca na capa, em loop)

**Prompt de estilo (cole no campo Style):**
> música infantil brasileira alegre e chiclete, estilo abertura de desenho animado, xilofone, ukulele e palmas, vozes de coral infantil, 112 bpm, animada, curta

**Letra (cole no campo Lyrics):**
```
Pipo! Pipo! O pintinho pintado!
Piu piu piu, vem brincar do meu lado!
Pipo! Pipo! De bolinha colorida!
Toque na tela, começou a brincadeira!
```
**Dica:** peça 30-60 segundos; escolha a versão mais animada; como toca em loop, prefira uma que termine "redonda".

### `musica-pipo.mp3` — A Música do Pipo (página do karaokê)

**Prompt de estilo:**
> música infantil brasileira dançante e repetitiva, estilo cantiga de roda moderna, xilofone, violão e bateria leve, voz infantil feminina alegre, 100 bpm, fácil de cantar junto

**Letra (EXATAMENTE esta — a tela destaca cada verso em ordem):**
```
Pipo, Pipo, pintinho pintado
Pula, pula, não fica parado
Bate a asinha: piu, piu, piu!
Bolinha vermelha, bolinha azul
Pipo, Pipo, pintinho pintado
Canta comigo: piu, piu, PIU!
```
**Dica:** a letra tem 6 versos; o destaque na tela divide a duração da música por 6 — prefira versões onde os versos têm duração parecida (sem introdução instrumental longa; se tiver, corte a intro num editor ou peça "sem introdução").

---

## PARTE 2 — As falas do Pipo (ElevenLabs)

**Configuração:** escolha uma voz feminina jovem/infantil em português BR (procure na Voice Library por "brazilian child" ou "jovem brasileira"; ex.: vozes tipo "Bella BR", "Camila"). Model: Multilingual v2. Style: alegre. Grave TODAS com a mesma voz.

**Tom de interpretação:** professora de educação infantil animada, sorrindo ao falar, energia alta sem gritar.

### Instruções das páginas (10 arquivos)

| Arquivo | Frase a gravar |
|---|---|
| `voz-instrucao-capa.mp3` | Oi! Eu sou o Pipo! Toque no botão amarelo para brincar comigo! |
| `voz-instrucao-ovos.mp3` | Olha, três ovos com surpresa! Toque num ovo para ver quem mora ali! |
| `voz-instrucao-pintar.mp3` | Toque nas bolinhas cinzas para pintar. Cada cor faz uma musiquinha! |
| `voz-instrucao-piano.mp3` | Toque num bichinho para ouvir o som dele. Imite junto comigo! |
| `voz-instrucao-circular.mp3` | O gato faz miau! Desenhe uma bolinha em volta do gato! |
| `voz-instrucao-contar.mp3` | Toque nos pintinhos, um de cada vez, e conte comigo! |
| `voz-instrucao-formas.mp3` | Arraste cada forma até a casinha igualzinha a ela! |
| `voz-instrucao-musica.mp3` | Toque no botão verde e cante comigo! |
| `voz-instrucao-desenhar.mp3` | Passe o dedo na tela! Seu desenho vira arco-íris e faz música! |
| `voz-instrucao-diploma.mp3` | Você chegou ao final! Peça a um adulto para escrever o seu nome! |

### Comemorações e navegação (2 arquivos)

| Arquivo | Frase |
|---|---|
| `voz-parabens.mp3` | Iupiii! Muito bem! Você ganhou uma estrela! |
| `voz-proxima.mp3` | Vamos para a próxima página? |

### Os bichos do piano (5 arquivos)

| Arquivo | Frase |
|---|---|
| `voz-vaca.mp3` | A vaca faz muuu! |
| `voz-gato.mp3` | O gato faz miau! |
| `voz-cachorro.mp3` | O cachorro faz au au! |
| `voz-pato.mp3` | O pato faz quá quá! |
| `voz-pipo.mp3` | E eu faço piu piu! |

### As cores (6 arquivos)

| Arquivo | Frase |
|---|---|
| `voz-cor-0.mp3` | Vermelho! Que cor linda! |
| `voz-cor-1.mp3` | Azul, como o céu! |
| `voz-cor-2.mp3` | Verde, como as folhas! |
| `voz-cor-3.mp3` | Laranja, como o meu bico! |
| `voz-cor-4.mp3` | Rosa! Que fofo! |
| `voz-cor-5.mp3` | Roxo! Uau! |

### Os números (5 arquivos)

| Arquivo | Frase |
|---|---|
| `voz-num-1.mp3` | Um! |
| `voz-num-2.mp3` | Dois! |
| `voz-num-3.mp3` | Três! |
| `voz-num-4.mp3` | Quatro! |
| `voz-num-5.mp3` | Cinco! |

### As surpresas dos ovos (3 arquivos)

| Arquivo | Frase |
|---|---|
| `voz-ovo-estrela.mp3` | Olha! Uma estrela brilhante! |
| `voz-ovo-lila.mp3` | É a Lila, minha melhor amiga! |
| `voz-ovo-pipo.mp3` | Achou! Sou eu, o Pipo! |

**Total: 2 músicas + 31 falas = 33 arquivos.**

---

## PARTE 3 — Montagem final (2 minutos)

```bash
# 1. coloque os 33 MP3s numa pasta, ex.: meus-audios/
# 2. rode:
python3 embutir-audios.py meus-audios/
# 3. o arquivo final aparece em produto/livro-magico-pipo-com-audio.html
# 4. teste no celular e use ESTE arquivo no zip do Hotmart
```

**Como funciona por dentro:** o livro tenta tocar o áudio profissional primeiro; se algum arquivo não foi gravado, ele usa o som sintetizado só naquele ponto. Você pode começar apenas com `tema.mp3` + `musica-pipo.mp3` + `voz-parabens.mp3` (os 3 de maior impacto) e completar o resto depois.

**Direitos:** músicas e vozes geradas nas suas contas Suno/ElevenLabs seguem as licenças comerciais dessas plataformas (nos planos pagos/starter a licença comercial é explícita — confirme o plano antes de vender). Guarde os prompts e datas como registro de produção.
