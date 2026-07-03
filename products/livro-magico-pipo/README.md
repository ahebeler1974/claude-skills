# 🐤 Pipo, o Pintinho Pintado — O Livro Mágico Interativo

**Produto digital completo, pronto para publicar no Hotmart por R$ 49,90.**

Ebook interativo em HTML para crianças de **2 a 6 anos**: 10 páginas mágicas com som sintetizado, voz em português, músicas originais e atividades de tocar, pintar, circular, contar, arrastar, cantar e desenhar — terminando em um diploma com o nome da criança. Funciona em qualquer celular, tablet ou computador, **offline, sem instalar nada, sem anúncios e sem coletar nenhum dado** (LGPD art. 14).

A tese do produto: **tela ativa em vez de tela passiva** — a mesma ciência sensorial dos fenômenos infantis de bilhões de views (cores primárias sobre fundo azul, repetição musical, baby schema), invertida de consumo para **interação contingente**: cada toque responde em milissegundos com som e animação.

## Experimente agora

Abra `produto/livro-magico-pipo.html` em qualquer navegador (funciona via duplo clique, `file://`). No celular é ainda melhor.

## Estrutura

```
livro-magico-pipo/
├── produto/
│   └── livro-magico-pipo.html      ← O PRODUTO (arquivo único, autocontido)
├── bonus/
│   ├── atividades-para-imprimir.html  ← Bônus 1: caderno A4 com 8 atividades (SVG, pronto p/ imprimir)
│   └── guia-dos-pais.md               ← Bônus 2: guia com a ciência de cada página (converter p/ PDF)
├── vendas/
│   ├── pagina-de-vendas.html       ← Landing page completa (trocar #LINK-CHECKOUT-HOTMART)
│   ├── copy-anuncios.md            ← 12 anúncios Meta Ads + hooks + matriz de testes + checklist CONAR
│   ├── roteiros-videos.md          ← 8 roteiros de Reels/TikTok estilo UGC + dicas de gravação
│   ├── sequencia-emails.md         ← 7 e-mails de funil + 4 de pós-compra
│   └── screenshots/                ← Capturas reais do produto (para criativos e página)
├── estrategia/
│   ├── estrategia-lancamento.md    ← Posicionamento, escada de valor, unit economics, plano 30-60-90
│   └── neurociencia-aplicada.md    ← O dossiê "A Ciência da Magia" (8 mecanismos + referências)
├── hotmart/
│   ├── guia-publicacao-hotmart.md  ← Passo a passo do zero ao primeiro anúncio
│   └── montar-pacote.sh            ← Gera o .zip de entrega para o comprador
└── qa/                             ← Testes end-to-end (Playwright)
```

## O produto em 10 páginas

| # | Página | Interação | Princípio científico |
|---|---|---|---|
| 1 | Capa Mágica | Toque para começar (desbloqueia o áudio) | Causa e efeito |
| 2 | Cadê o Pipo? | 2 toques quebram cada ovo-surpresa | Permanência do objeto |
| 3 | Pinte as Bolinhas | Toque pinta e toca uma nota | Cores + associação som-cor |
| 4 | Piano dos Bichos | 5 teclas com sons de animais sintetizados | Vocabulário/onomatopeias |
| 5 | Circule o Gato | Desenhar círculo com o dedo (detecção de laço) | Motricidade fina; erro que ensina |
| 6 | Conte os Pintinhos | Tocar e contar 1-5, com voz | Correspondência um-a-um |
| 7 | Formas Mágicas | Arrastar ao encaixe (generoso, sem reset) | Formas + planejamento motor |
| 8 | A Música do Pipo | Karaokê com letra em tempo real | Repetição + linguagem |
| 9 | Tela de Estrelas | Desenho vira arco-íris + notas pentatônicas | Criatividade sem erro possível |
| 10 | Diploma do Pipo | Nome da criança + confete + impressão | Fecho + autoestima |

**Recursos transversais:** resposta < 100ms via `pointerdown` + Web Audio API (sons 100% sintetizados, zero arquivos externos) · voz pt-BR via speechSynthesis com degradação silenciosa · instruções repetidas por voz após inatividade · sem estado de erro · alvos de toque gigantes · Cantinho dos Pais com portão de segurar 3s (padrão Apple Kids) · progresso com 9 estrelas em localStorage · sem rede, sem rastreamento.

## Status de verificação

- ✅ Teste end-to-end (Playwright/Chromium, viewport 390×780 touch): **as 10 páginas completáveis, 9/9 estrelas, zero erros de console** (`qa/test-ebook.js`)
- ✅ Layout validado em celular (390×780) e tablet (1024×768)
- ✅ Compliance embutido: comunicação dirigida a adultos (CONAR/CONANDA 163), sem promessas de resultado (Hotmart/CDC), personagem/músicas 100% originais (Lei 9.610 art. 8º), zero coleta de dados (LGPD art. 14), moldura SBP de tempo de tela

## Para publicar (ordem de execução)

1. `bash hotmart/montar-pacote.sh` → testar o zip em Android, iPhone e computador
2. Seguir `hotmart/guia-publicacao-hotmart.md` (cadastro, Club, preço, bump, pixel)
3. Hospedar `vendas/pagina-de-vendas.html` (Netlify/Vercel) e trocar os links de checkout
4. Executar `estrategia/estrategia-lancamento.md` (orgânico → pago → afiliados)

---

*Personagem, músicas, sons e ilustrações 100% originais. A referência a fenômenos infantis é editorial/descritiva — nenhum vínculo com marcas de terceiros.*
