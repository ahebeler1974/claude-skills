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
│   ├── seo_keyword_builder.py                    # Gera candidatas de cauda longa p/ Bloco de SEO
│   └── wordpress_exporter.py                     # Exporta artigos como WXR p/ importar no WordPress
├── references/
│   ├── mercado-livre-afiliados.md                # Painel, links, comissões, fluxo no WordPress
│   ├── seo-cauda-longa.md                        # Intenções de busca e fórmulas de cauda longa
│   ├── design-do-blog.md                         # Layout e design impecável no WordPress
│   ├── naming-e-branding.md                      # Rebranding: ahebeler.shop → TecnoPulso
│   └── google-adsense.md                         # Ativação e aprovação do Google AdSense
├── assets/
│   ├── template-artigo-top10.md                  # Template de listicle Top 10
│   ├── template-comparativo.md                   # Template de comparativo X vs Y
│   ├── template-noticia-ia.md                    # Template de notícia de IA
│   ├── template-review.md                        # Template de review individual
│   ├── checklist-publicacao-wordpress.md         # Checklist operacional de publicação
│   ├── estilo-tecnopulso.css                     # CSS do blog v1 — tema claro
│   ├── estilo-tecnopulso-dark.css                # CSS do blog v2 — dark futurista (recomendado)
│   ├── home-tecnopulso.html                      # Página inicial futurista (blocos Gutenberg)
│   └── pauta-tecnopulso.md                       # Briefing anexável: da pauta ao artigo no ar
└── examples/
    ├── top-10-fones-bluetooth-mercado-livre-2026.md   # Exemplo pronto: Top 10
    ├── top-10-smartwatches-mercado-livre-2026.md      # Exemplo pronto: Top 10 (smartwatches)
    ├── comparativo-galaxy-s24-vs-iphone-15.md         # Exemplo pronto: comparativo
    ├── noticia-ia-celulares-2026.md                   # Exemplo pronto: notícia de IA
    └── tecnopulso-import.xml                          # Importação WordPress dos 4 exemplos
```

## Início rápido (3 passos)

1. **Carregue a skill:** leia [SKILL.md](SKILL.md) — é o conjunto de instruções que o agente segue para operar o blog.
2. **Dê a pauta:** informe tema/produto, tipo de artigo, público e palavra-chave alvo (ex: "Top 10 fones de ouvido bluetooth custo-benefício 2026").
3. **Receba o artigo e publique:** o agente entrega o artigo completo com marcadores de afiliado e Bloco de SEO; no WordPress, gere os links no painel Afiliados e Criadores do Mercado Livre (botão Compartilhar) e substitua cada marcador pelo cartão de produto.

Os scripts rodam sem instalação (Python 3, biblioteca padrão):

```bash
python3 scripts/article_scaffolder.py            # modo demo
python3 scripts/seo_keyword_builder.py --produto "smartwatch barato" --categoria smartwatches
python3 scripts/wordpress_exporter.py            # exporta examples/ como rascunhos p/ WordPress
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

## Exemplos prontos para publicar

Quatro artigos completos — cobrindo os 4 nichos do blog — demonstram o resultado esperado do loop:

- **Top 10 (fones):** [Os 10 Melhores Fones de Ouvido Bluetooth do Mercado Livre em 2026](examples/top-10-fones-bluetooth-mercado-livre-2026.md)
- **Top 10 (smartwatches):** [Os 10 Melhores Smartwatches do Mercado Livre em 2026](examples/top-10-smartwatches-mercado-livre-2026.md)
- **Comparativo (celulares):** [Galaxy S24 vs iPhone 15: qual vale mais a pena em 2026?](examples/comparativo-galaxy-s24-vs-iphone-15.md)
- **Notícia de IA:** [IA no celular em 2026: Galaxy AI, Apple Intelligence e Gemini na prática](examples/noticia-ia-celulares-2026.md)

Cada um já traz título SEO, meta description, aviso de transparência, marcadores de afiliado e Bloco de SEO — basta plugar os cartões do Mercado Livre e publicar.

**Publicação rápida:** o arquivo [examples/tecnopulso-import.xml](examples/tecnopulso-import.xml) já contém os 4 artigos como rascunhos do WordPress (gerado por `scripts/wordpress_exporter.py`). Importe em *Ferramentas > Importar > WordPress*, substitua cada bloco destacado pelo cartão de produto com o seu link de afiliado e cole o [CSS do blog](assets/estilo-tecnopulso.css) em *Aparência > Personalizar > CSS Adicional*.

## Documentação completa

Todas as instruções operacionais, estruturas por tipo de artigo, regras editoriais e o checklist de publicação no WordPress estão em [SKILL.md](SKILL.md).

---

**Versão:** 1.0.0 · **Categoria:** marketing · **Licença:** MIT
