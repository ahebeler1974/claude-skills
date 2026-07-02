# Affiliate Blog Loop — TecnoPulso

Sistema operacional completo ("Sistema de Loop") para rodar um blog profissional de análises de tecnologia no Brasil — o **TecnoPulso** — monetizado exclusivamente pelo **Programa de Afiliados do Mercado Livre**.

**Tagline do blog:** "Análises e comparativos de tecnologia, sem enrolação."
**Nichos:** celulares, relógios inteligentes (smartwatches), fones de ouvido e novidades de IA.
**Domínios sugeridos:** tecnopulso.com.br e tecnopulso.shop.

## O que esta skill faz

Transforma qualquer pedido de pauta em um artigo pronto para publicar, seguindo um loop de 4 passos:

1. **Criação do Artigo Completo** — guia profissional, persuasivo e detalhado, com benefícios claros de cada produto
2. **Ganchos de Afiliado** — marcador `[INSERIR CARTÃO DE PRODUTO MERCADO LIVRE AQUI]` após cada produto
3. **Bloco de SEO** — 10 a 15 palavras-chave de cauda longa no final do artigo
4. **Reiniciar o Loop** — o artigo termina perguntando qual será a próxima pauta

Inclui 4 tipos de artigo (Top 10, comparativo X vs Y, notícia de IA e review individual), regras editoriais E-E-A-T, aviso de transparência de afiliado obrigatório e checklist de qualidade antes da entrega.

## Estrutura da pasta

```
affiliate-blog-loop/
├── SKILL.md                                      # Instruções mestras do sistema de loop
├── README.md                                     # Este arquivo
├── scripts/
│   ├── article_scaffolder.py                     # Gera esqueleto do artigo por tipo
│   └── seo_keyword_builder.py                    # Gera candidatas de cauda longa p/ Bloco de SEO
├── references/
│   ├── programa-afiliados-mercado-livre.md       # Painel, links, comissões, regras do programa
│   ├── seo-cauda-longa-brasil.md                 # Padrões de busca do consumidor brasileiro
│   ├── copywriting-review-tech.md                # Copy persuasiva para reviews e listas
│   └── transparencia-e-compliance.md             # Obrigações de transparência (CDC, CONAR)
└── assets/
    ├── template-top10.md                         # Template de listicle Top 10
    ├── template-comparativo.md                   # Template de comparativo X vs Y
    ├── template-noticia-ia.md                    # Template de notícia de IA
    └── template-review.md                        # Template de review individual
```

## Início rápido (3 passos)

1. **Carregue a skill:** leia [SKILL.md](SKILL.md) — é o conjunto de instruções que o agente segue para operar o blog.
2. **Dê a pauta:** informe tema/produto, tipo de artigo, público e palavra-chave alvo (ex: "Top 10 fones de ouvido bluetooth custo-benefício 2026").
3. **Receba o artigo e publique:** o agente entrega o artigo completo com marcadores de afiliado e Bloco de SEO; no WordPress, gere os links no painel Afiliados e Criadores do Mercado Livre (botão Compartilhar) e substitua cada marcador pelo cartão de produto.

Os scripts rodam sem instalação (Python 3, biblioteca padrão):

```bash
python3 scripts/article_scaffolder.py            # modo demo
python3 scripts/seo_keyword_builder.py --tema "smartwatch barato" --nicho smartwatches
```

## Exemplo de uma iteração do loop

**Você:** "Vamos fazer um Top 10 de smartwatches até R$ 500."

**O agente:**
1. Confirma público e palavra-chave alvo ("melhor smartwatch até 500 reais 2026")
2. Entrega o artigo completo: título ≤ 60 caracteres, meta description ≤ 155, aviso de transparência de afiliado, tabela comparativa, 10 produtos com benefícios e faixas de preço (nunca valores exatos), FAQ para featured snippets
3. Após **cada** produto, em linha própria: `[INSERIR CARTÃO DE PRODUTO MERCADO LIVRE AQUI]`
4. Fecha com a seção `## Bloco de SEO` (10-15 palavras-chave de cauda longa)
5. Termina com: **"Artigo finalizado! Qual será o próximo equipamento, comparativo ou notícia de IA que vamos analisar?"**

**Você:** responde com a próxima pauta — e o loop recomeça.

## Documentação completa

Todas as instruções operacionais, estruturas por tipo de artigo, regras editoriais e o checklist de publicação no WordPress estão em [SKILL.md](SKILL.md).

---

**Versão:** 1.0.0 · **Categoria:** marketing · **Licença:** MIT
