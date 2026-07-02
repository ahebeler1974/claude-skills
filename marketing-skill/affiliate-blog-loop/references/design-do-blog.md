# Design e Layout do Blog TecnoPulso no WordPress

Guia de design para um blog de reviews com aparência impecável e profissional. Objetivo duplo: (1) o leitor confia no conteúdo à primeira vista e (2) nada atrapalha o caminho até o botão "Ver oferta no Mercado Livre". Design de blog de afiliados é design de conversão com credibilidade editorial.

## Escolha do tema WordPress

Critérios obrigatórios (nesta ordem):

1. **Velocidade:** tema leve (< 100 KB de CSS/JS base). Cada segundo de carregamento a mais derruba conversão e ranqueamento.
2. **Mobile-first:** a maioria do tráfego de reviews tech no Brasil vem do celular. Teste o tema primeiro no celular, depois no desktop.
3. **Suporte a blocos (Gutenberg/FSE):** cartões de produto, tabelas e caixas de prós/contras são blocos — o tema precisa estilizá-los bem sem page builder.
4. **Tipografia e espaçamento decentes por padrão:** menos CSS custom para manter.
5. **Atualizações ativas e boa avaliação** no diretório do WordPress.

Temas recomendados para blog de reviews:

| Tema | Ponto forte | Observação |
|---|---|---|
| **GeneratePress** | Extremamente leve e rápido; padrão da indústria para afiliados | Visual sóbrio; personalize cores para não ficar genérico |
| **Kadence** | Blocos avançados nativos (tabelas, cards, CTA) | Ótimo equilíbrio entre recursos e performance |
| **News Crunch** | Visual de portal de notícias tech pronto | Bom para home estilo "revista"; verifique o peso das páginas |

Recomendação prática: GeneratePress ou Kadence como base + blocos nativos + plugin de cartões de afiliado. Evite temas "multipurpose" gigantes com sliders e animações.

## Identidade visual do TecnoPulso

**Paleta — 1 cor primária + neutras:**

- **Primária:** um azul-elétrico ou verde-tecnologia (ex.: azul `#0B5FFF` ou similar) usada APENAS em links, botões de CTA e detalhes de destaque. Se tudo é colorido, nada se destaca.
- **Neutras:** fundo branco `#FFFFFF` ou off-white `#FAFAFA`; texto quase-preto `#1A1A1A` (nunca preto puro sobre branco puro em blocos longos); cinzas `#6B7280` para metadados (data, autor) e `#E5E7EB` para bordas.
- **Cor de alerta/CTA secundária opcional** (ex.: laranja) exclusiva para botões "Ver oferta" — botão de compra em cor única e consistente em TODO o site cria reconhecimento imediato.
- Contraste mínimo WCAG AA (4.5:1) para texto de corpo — teste primária sobre branco antes de adotar.

**Tipografia:**

- Uma família para títulos (pode ter personalidade: Inter, Sora, Manrope) e uma para corpo (legibilidade máxima: Inter, Source Sans, system fonts).
- **Corpo com no mínimo 17px** (ideal 17–19px) e line-height 1.6–1.7. Texto pequeno é o erro nº 1 de blogs amadores.
- Largura de linha do conteúdo: 65–75 caracteres (~700–760px de coluna). Linhas quilométricas cansam.
- Máximo 2 famílias tipográficas no site inteiro.

## Anatomia do artigo de review perfeito

Ordem dos elementos, do topo ao rodapé:

1. **H1 + linha de metadados:** autor com foto, data de publicação E data de atualização visível ("Atualizado em 02/07/2026").
2. **Disclosure de afiliado** (caixa discreta mas legível) — antes de qualquer link de produto.
3. **Imagem de destaque** relevante e otimizada (WebP, com o produto/tema real, não banco de imagens genérico).
4. **Parágrafo de abertura** que responde em 2–3 frases o que o leitor vai descobrir.
5. **Sumário/índice clicável** (bloco de índice ou plugin leve) — essencial em top 10; leitores pulam direto para o produto que interessa e o Google gera sitelinks.
6. **Seção "Como escolhemos"** curta: critérios de avaliação (credibilidade + conformidade com o Product Reviews Update).
7. **Blocos de produto** (um por item do ranking):
   - H2 com posição e nome ("1. {Produto} — melhor custo-benefício geral")
   - 80–150 palavras de análise com benefícios concretos
   - **Caixa de prós/contras** (duas colunas ou duas listas com títulos "Prós" e "Contras")
   - Faixa de preço ("na faixa de R$ 150–250")
   - **Cartão de produto** com link de afiliado (substitui o marcador `[INSERIR CARTÃO DE PRODUTO MERCADO LIVRE AQUI]`)
8. **Tabela comparativa responsiva** com todos os produtos (nome, destaque, faixa de preço, "melhor para") — antes ou depois da lista; no mobile, com scroll horizontal ou colunas empilhadas.
9. **Veredito final:** qual comprar em 1 parágrafo por perfil de leitor ("se você quer o mais barato...", "se bateria é prioridade...").
10. **FAQ** (3–5 perguntas) em H3.
11. **Bloco de SEO** (lista de 10–15 keywords).
12. **Links internos** para 2–4 artigos relacionados ("Leia também").

## Design do cartão de produto

Hierarquia visual do cartão (de cima para baixo / mais forte para mais fraco):

1. **Foto do produto** — fundo limpo, boa resolução, proporção consistente entre todos os cartões.
2. **Nome do produto** — negrito, tamanho de subtítulo.
3. **Benefício-chave em 1 linha** — não spec, benefício: "Bateria para o dia inteiro com tela sempre ligada".
4. **2–4 bullets de benefícios** (opcional, quando o plugin permitir).
5. **Botão CTA: "Ver oferta no Mercado Livre"** — cor de CTA do site, largura confortável para o dedão (mínimo 44px de altura), texto que informa o destino (transparência + expectativa correta). Evite "Comprar" seco: o leitor vai VER a oferta, o preço atual está lá.

Regras do cartão:

- Cartão com borda ou fundo levemente destacado do texto — visível, não gritante.
- Um único CTA por cartão. Dois botões dividem o clique.
- O link do botão é SEMPRE o link de afiliado gerado (ver guia do Mercado Livre).
- Nunca exiba preço exato "congelado" no cartão se o plugin não atualizar automaticamente — preço desatualizado destrói confiança.

## Performance e Core Web Vitals

Metas: LCP < 2,5s, CLS < 0,1, INP < 200ms. Como chegar lá:

1. **Imagens em WebP comprimidas** (qualidade 75–85), redimensionadas para o tamanho real de exibição (nada de foto 4000px numa coluna de 760px). Plugin de conversão/compressão automática.
2. **Lazy loading** para toda imagem abaixo da dobra (nativo do WordPress: manter ativo); a imagem de destaque acima da dobra NÃO deve ter lazy load (piora o LCP).
3. **Cache de página** (plugin de cache) + cache do navegador + CDN se disponível no host.
4. **Evitar page builders pesados** (Elementor/Divi carregam CSS/JS massivos). Blocos nativos + tema leve entregam o mesmo visual com fração do peso.
5. **Fontes:** hospedar localmente, `font-display: swap`, máximo 2 famílias e 3–4 pesos no total.
6. **Dimensões explícitas** (width/height) em todas as imagens e embeds para zerar CLS.
7. **Plugins no mínimo:** cada plugin é peso e risco. Auditoria trimestral: desativar o que não é essencial.
8. Medir com PageSpeed Insights (aba mobile primeiro) a cada mudança de tema ou plugin.

## Elementos de confiança

Blog de afiliado vive de credibilidade. Itens obrigatórios:

- **Página "Sobre"** contando quem faz o TecnoPulso, o método de análise e a promessa editorial ("Análises e comparativos de tecnologia, sem enrolação").
- **Autor com bio e foto** em cada artigo (caixa de autor no rodapé do post) — sinal de E-E-A-T para o Google e para o leitor.
- **Política de Afiliados** como página permanente, linkada no rodapé, explicando a relação com o Mercado Livre.
- **Data de atualização visível** no topo dos artigos — review tech "sem data" é review morto.
- **Página de Contato** funcional.
- **Política de Privacidade** (obrigação com a LGPD se houver analytics/comentários/newsletter).
- Design consistente: mesmo formato de cartão, mesma cor de CTA, mesma estrutura de artigo em todo o site.

## Checklist de design antes de publicar

- [ ] Testado no celular real (não só no preview do editor)
- [ ] Corpo do texto >= 17px, linhas com respiro (line-height >= 1.6)
- [ ] Imagem de destaque em WebP, sem lazy load; demais imagens com lazy load
- [ ] Todas as imagens com alt text descritivo em PT-BR
- [ ] Sumário clicável funcionando (âncoras corretas)
- [ ] Disclosure de afiliado visível antes do primeiro cartão
- [ ] Todos os cartões com foto + benefício + botão "Ver oferta no Mercado Livre"
- [ ] Todos os botões testados em aba anônima (abrem o produto certo com link de afiliado)
- [ ] Tabela comparativa legível no mobile
- [ ] Caixas de prós/contras presentes em cada produto
- [ ] Nenhum preço exato no texto — apenas faixas de preço
- [ ] Data de atualização visível
- [ ] 2–4 links internos com âncoras descritivas
- [ ] PageSpeed mobile sem regressão (LCP < 2,5s)
- [ ] Zero erros de layout shift ao rolar a página (CLS)
