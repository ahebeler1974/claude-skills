---
name: affiliate-article
description: |
  Run one full iteration of the TecnoPulso affiliate blog loop: write a complete PT-BR
  tech-review article, insert Mercado Livre product-card markers after every product,
  generate a long-tail SEO block, and restart the loop. Usage: /affiliate-article <tema>
---

# /affiliate-article

Executa **uma iteração completa** do SISTEMA DE LOOP do blog TecnoPulso: artigo profissional em PT-BR, ganchos de afiliado do Mercado Livre, Bloco de SEO de cauda longa e reinício do loop.

## Uso

```bash
/affiliate-article Os 10 Melhores Fones de Ouvido Bluetooth do Mercado Livre em 2026
/affiliate-article Comparativo Galaxy S24 vs iPhone 15
/affiliate-article Novidades de IA no Galaxy AI
/affiliate-article Review Redmi Watch 5
```

## O que este comando faz

Execute as fases abaixo em ordem, sem pular nenhuma.

---

## Fase 0: Carregar o manual de operação

Leia `marketing-skill/affiliate-blog-loop/SKILL.md` — ele é o manual completo do loop (persona, regras editoriais, estruturas por tipo de artigo e portões de qualidade). Siga-o à risca.

Se existir `marketing-context.md` na raiz do projeto, leia também para absorver voz de marca e persona.

## Fase 1: Detectar o tipo de artigo e escolher o template

Classifique o tema recebido em `$ARGUMENTS`:

| Sinal no tema | Tipo | Template |
|---|---|---|
| "Top N", "melhores", "lista" | `top10` | `marketing-skill/affiliate-blog-loop/assets/template-artigo-top10.md` |
| "vs", "ou", "comparativo" | `comparativo` | `marketing-skill/affiliate-blog-loop/assets/template-comparativo.md` |
| "novidade", "IA", "lançamento", "atualização" | `noticia-ia` | `marketing-skill/affiliate-blog-loop/assets/template-noticia-ia.md` |
| "review", um único produto | `review` | estrutura de review individual descrita no SKILL.md |

Opcionalmente, gere o esqueleto inicial com a ferramenta determinística:

```bash
python3 marketing-skill/affiliate-blog-loop/scripts/article_scaffolder.py --tema "<tema>" --tipo <tipo>
```

## Fase 2: Passo 1 do loop — Criação do Artigo Completo

Escreva o artigo completo em PT-BR (1.800–2.500 palavras para listicles), altamente profissional, persuasivo e detalhado, com tom de guia completo e especializado:

- Título SEO (≤60 caracteres) e meta description (≤155 caracteres) no topo.
- Introdução persuasiva (problema → promessa → critérios).
- Aviso de transparência de afiliado logo após a introdução.
- Em listas (ex: Top 10), separe os produtos por nichos (custo-benefício, intermediário, premium, esportivo, gamer) e liste os benefícios claros de cada produto (✅ pontos fortes / ⚠️ pontos de atenção, "Ideal para:", faixa de preço).
- Tabela comparativa e seção "Como escolher".
- FAQ com perguntas de cauda longa (formato featured snippet).
- **Nunca** invente especificações técnicas nem preços exatos — use faixas de preço (ex: "R$ 150–250").

## Fase 3: Passo 2 do loop — Ganchos de Afiliado

Ao final da descrição de **cada** produto, adicione em linha própria o marcador visual exato:

```
[INSERIR CARTÃO DE PRODUTO MERCADO LIVRE AQUI]
```

Esse marcador indica onde o operador vai plugar o cartão de produto do plugin WordPress com o link de afiliado do Mercado Livre.

## Fase 4: Passo 3 do loop — Bloco de SEO

No final do artigo, crie a seção `## Bloco de SEO` com 10–15 palavras-chave de cauda longa altamente pesquisadas relacionadas ao tema. Você pode gerá-las com:

```bash
python3 marketing-skill/affiliate-blog-loop/scripts/seo_keyword_builder.py --produto "<produto>" --categoria <fones|celulares|smartwatches|ia|geral>
```

## Fase 5: Entrega e portões de qualidade

1. Salve o artigo como arquivo Markdown em `artigos/<slug-do-tema>.md` (crie a pasta se não existir; aceite caminho customizado se o usuário indicar) **e** apresente o artigo completo na conversa.
2. Antes de entregar, verifique os portões de qualidade:
   - [ ] Número de marcadores `[INSERIR CARTÃO DE PRODUTO MERCADO LIVRE AQUI]` == número de produtos.
   - [ ] Título ≤60 caracteres e meta description ≤155 caracteres.
   - [ ] Aviso de afiliado presente.
   - [ ] Nenhuma especificação inventada e nenhum preço exato (apenas faixas).
   - [ ] Bloco de SEO com 10–15 palavras-chave.
   - [ ] Tabela comparativa e FAQ presentes (para listicles e comparativos).

## Fase 6: Passo 4 do loop — Reiniciar o Loop

Após entregar o artigo e o Bloco de SEO, encerre perguntando **exatamente**:

> "Artigo finalizado! Qual será o próximo equipamento, comparativo ou notícia de IA que vamos analisar?"

E aguarde o próximo tema para repetir o processo.
