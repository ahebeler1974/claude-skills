# Google Ads — O Livro Mágico do Pipo

Campanhas prontas para colar. **Comprador = mãe/pai** (nunca anunciar para crianças — política Google + CONAR). Link final: sua página de vendas hospedada (com UTM: `?utm_source=google&utm_medium=cpc&utm_campaign=pipo-search`).

**Nota de realismo:** para produto low ticket de R$ 49,90, o Google Search converte melhor em **demanda existente** ("atividades interativas para crianças", "jogo educativo 3 anos") — volume menor e CPC maior que Meta. Comece com Meta (demanda latente) e use Google para: (1) capturar quem pesquisa a categoria; (2) remarketing via YouTube; (3) proteger a marca "Pipo" quando ela crescer. Orçamento sugerido: 70% Meta / 30% Google no início.

---

## 1. Campanha Search — Grupo "Atividades interativas" (RSA)

**Títulos (máx. 30 caracteres cada — use 12-15):**
1. `Ebook Interativo Infantil`
2. `Tela Ativa Para Seu Filho`
3. `Atividades Com Som e Música`
4. `Para Crianças de 2 a 6 Anos`
5. `Sem App e Sem Internet`
6. `Toque, Cante, Pinte, Conte`
7. `Livro Que Responde ao Toque`
8. `Chega de Tela Passiva`
9. `R$49,90 · Pagamento Único`
10. `Acesso Imediato no Celular`
11. `10 Atividades Interativas`
12. `Sem Anúncios e Sem Cadastro`
13. `Garantia de 7 Dias`
14. `Diploma Com o Nome do Filho`
15. `Aprovado Pelas Mães`*

*use o 15 apenas depois de ter avaliações reais.

**Descrições (máx. 90 caracteres — use as 4):**
1. `Seu filho toca e a tela responde: sons, músicas e atividades educativas. Sem instalar app.`
2. `10 páginas mágicas: pintar, contar, circular, cantar e desenhar. Funciona offline no celular.`
3. `Transforme o tempo de tela em aprendizado ativo. R$49,90, acesso imediato e 7 dias de garantia.`
4. `Baseado em princípios de neurociência do desenvolvimento. Bônus: caderno para imprimir.`

**Palavras-chave (correspondência de frase):**
```
"atividades interativas para crianças"
"jogo educativo infantil celular"
"atividades educativas 3 anos"
"atividades educativas 4 anos"
"brincadeiras educativas para crianças"
"livro interativo infantil"
"jogos educativos 2 anos"
"aplicativo educativo infantil"
"atividades para crianças no tablet"
"ebook infantil interativo"
```

**Negativas (obrigatórias):**
```
grátis, gratuito, baixar grátis, pdf grátis, online grátis,
para imprimir grátis, youtube, desenho animado, vagas, curso de,
como fazer, apk, play store
```

## 2. Campanha Search — Grupo "Dor da tela" (RSA)

**Títulos:**
1. `Filho Viciado em Telinha?`
2. `Troque o Vídeo Por Atividade`
3. `Tela Útil Existe. Veja Como`
4. `Menos YouTube, Mais Aprender`
5. `Tempo de Tela de Qualidade`
6. `A Tela Que Ensina de Verdade`
7. `Para Pais de Crianças 2-6`
8. `Ebook Interativo R$49,90`
9. `Sem Mensalidade · Sem App`
10. `Comece em 2 Minutos`

**Descrições:**
1. `Em vez de assistir parado, seu filho toca, canta, conta e desenha. A tela responde na hora.`
2. `O mesmo celular, um uso melhor: 10 atividades com som e voz em português. Offline.`
3. `Sessões curtas com começo, meio e fim — dentro da recomendação da SBP. Garantia de 7 dias.`
4. `Pagou uma vez, é seu. Acesso imediato por e-mail + caderno de atividades de bônus.`

**Palavras-chave (frase):**
```
"tempo de tela criança"
"como diminuir tela do filho"
"filho viciado em celular o que fazer"
"tela para criança faz mal"
"alternativa ao youtube para crianças"
"como tirar criança do celular"
```
⚠️ Neste grupo o anúncio NÃO pode prometer "tirar do vício" (alegação de saúde). O ângulo é sempre "troque a qualidade da tela".

## 3. YouTube (VAC — Video Action Campaign) e Remarketing

- **Criativo:** os mesmos vídeos UGC do Meta (roteiros em `roteiros-videos.md`), versão 15-20s com o toque-resposta nos 3 primeiros segundos e legenda queimada.
- **Segmentação:** públicos "Pais de filhos pequenos (0-6)" + interesses "Educação infantil" + remarketing de visitantes da página (7-30 dias) — sempre 25-54 anos.
- **Frequência:** cap de 3/semana no remarketing (nicho pequeno satura rápido).
- **Lance inicial:** tCPA R$ 30-35, depois otimizar para ≤ R$ 25.

## 4. Performance Max (só depois da conversão estar rastreada)

Ative quando tiver 30+ conversões/mês registradas. Assets: 5 títulos e 5 descrições dos grupos acima, 3 vídeos UGC, logos do Pipo, imagens dos screenshots reais (`vendas/screenshots/`). Sinal de público: lista de compradores (e-mails do Hotmart via zapier/planilha) + visitantes da página.

## 5. Rastreamento (obrigatório antes de ligar qualquer campanha)

1. Google Ads → Conversões → nova conversão de site "Compra".
2. Na Hotmart: Ferramentas → Pixel de rastreamento → adicionar o Google Ads (ID de conversão + rótulo) — a Hotmart dispara a conversão na página de obrigado.
3. Na página de vendas: instalar a tag global (gtag.js) e o evento `begin_checkout` no clique dos botões CTA.
4. Vincular Google Ads ↔ Google Analytics 4 para ver o funil completo.

## 6. Compliance Google Ads para produto infantil

- Anúncio dirigido ao ADULTO comprador; segmentação sempre 25+ (Google proíbe segmentar menores; conteúdo "made for kids" não recebe anúncio personalizado).
- Sem promessas de resultado pedagógico/terapêutico ("seu filho vai aprender a ler", "trata atraso de fala") — reprovação por "alegações não comprovadas".
- Sem marcas de terceiros em keywords, títulos ou descrições (nem como palavra-chave de concorrente de marca registrada infantil).
- Página de destino deve entregar o que o anúncio promete (Google verifica consistência) — a nossa entrega: formato, preço e garantia idênticos ao anúncio.

## 7. Orçamento e metas (primeiros 60 dias)

| Canal | Orçamento/dia | Meta CPA | Papel |
|---|---|---|---|
| Meta Ads | R$ 70 | ≤ R$ 25 | Motor principal (demanda latente) |
| Google Search | R$ 20 | ≤ R$ 30 | Capturar demanda ativa da categoria |
| YouTube remarketing | R$ 10 | ≤ R$ 20 | Recuperar visitantes da página |

Regra de decisão: canal 2 semanas acima do CPA máximo (R$ 35) → pausa e realoca para o vencedor.
