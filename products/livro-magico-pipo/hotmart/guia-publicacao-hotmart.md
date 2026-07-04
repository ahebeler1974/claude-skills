# Guia de Publicação no Hotmart — passo a passo do zero ao primeiro anúncio

Siga na ordem. Cada etapa diz exatamente onde clicar e o que escrever. Tempo total estimado: 2-3 horas.

---

## Etapa 0 — Preparar o pacote de entrega

1. No repositório, rode `bash products/livro-magico-pipo/hotmart/montar-pacote.sh` — ele gera `livro-magico-pipo-v1.zip` com:
   - `livro-magico-pipo.html` (o produto)
   - `bonus/atividades-para-imprimir.html` (Bônus 1)
   - `bonus/guia-dos-pais.md` (Bônus 2 — converta para PDF antes de subir: abra no navegador/editor e "Imprimir → Salvar como PDF")
   - `LEIA-ME-PRIMEIRO.txt` (instruções para o comprador — texto pronto abaixo)
2. **Teste o zip você mesmo** em: um Android (abrir o .html pelo gerenciador de arquivos/Chrome), um iPhone/iPad (abrir pelo app Arquivos/Safari) e um computador. O som deve ligar após o primeiro toque em "Começar a magia".

**Texto pronto do LEIA-ME-PRIMEIRO.txt** (o script já o inclui):

```
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

🎁 BÔNUS:
- "atividades-para-imprimir.html": abra e imprima (menu →
  Imprimir). São 8 atividades de papel e lápis.
- "guia-dos-pais.pdf": a ciência por trás de cada página
  e como brincar junto.

👨‍👩‍👧 CANTINHO DOS PAIS: dentro do livro, segure o botão
   "Pais" por 3 segundos (canto superior direito).

Precisa de ajuda? Responda o e-mail da sua compra.
Divirtam-se! Piu piu! 🐤
```

## Etapa 1 — Cadastro do produto no Hotmart

1. Crie/acesse sua conta em `app.hotmart.com` → **Produtos → Cadastrar produto**.
2. Campo a campo:
   - **Tipo:** Curso online/Conteúdo digital → formato **Área de membros da Hotmart (Hotmart Club)** ← recomendado (ver Etapa 2 por quê).
   - **Nome:** `O Livro Mágico do Pipo — Ebook Interativo (2 a 6 anos)`
   - **Categoria:** Educação → Infantil (ou "Maternidade e Família", teste qual converte melhor na busca do marketplace).
   - **Idioma/Moeda/País:** Português / BRL / Brasil.
   - **Descrição (cole e ajuste):**
     > Ebook interativo para crianças de 2 a 6 anos que transforma tempo de tela passivo em tempo de tela ativo. São 10 páginas mágicas com som, voz em português, músicas originais e atividades de tocar, pintar, circular, contar, encaixar, cantar e desenhar — terminando em um diploma com o nome da criança. Funciona em qualquer celular, tablet ou computador, direto no navegador, sem instalar aplicativo e sem internet depois de baixar. Sem anúncios e sem coleta de dados da criança. Inclui 2 bônus: Caderno de Atividades para imprimir e Guia dos Pais. Produto dirigido a pais e responsáveis. Baseado em princípios de neurociência do desenvolvimento infantil — estimula e convida, sem promessas de resultado. Garantia incondicional de 7 dias.
   - **Imagem do produto:** 600×600px. Use a arte da capa (Pipo em fundo azul estrelado + título). Gere a partir do screenshot `vendas/screenshots/00-capa.png` recortado em quadrado, ou recrie no Canva com os mesmos elementos.
3. **Página de vendas:** informe a URL onde você hospedou `vendas/pagina-de-vendas.html` (Etapa 5).

## Etapa 2 — Formato de entrega: Hotmart Club com 4 módulos

Por que Club e não "arquivo direto": (a) você pode atualizar o produto sem reenviar nada (antipirataria e roadmap v1.1+); (b) módulos deixam a entrega parecendo maior; (c) o Club tem app próprio, o comprador não perde o acesso.

Estrutura de módulos:

| Módulo | Conteúdo | Upload |
|---|---|---|
| 1. 🐤 O Livro Mágico | `livro-magico-pipo-v1.zip` + vídeo curto seu (1-2 min) mostrando como abrir no celular | zip + vídeo |
| 2. 🎁 Bônus: Caderno de Atividades | `atividades-para-imprimir.html` + versão PDF | arquivos |
| 3. 📖 Bônus: Guia dos Pais | `guia-dos-pais.pdf` | PDF |
| 4. 🔄 Atualizações | Página "Novidades da versão" — cada update vira conteúdo novo aqui | texto |

Marque todos como liberação imediata (sem drip — segurar conteúdo além dos 7 dias de garantia viola o CDC e gera Reclame Aqui).

## Etapa 3 — Preço, garantia e checkout

1. **Preço:** R$ 49,90 · parcelamento em até 5x (parcela mínima ~R$ 10) · Pix e boleto ativos.
2. **Garantia:** 7 dias (mínimo legal). Considere 15 dias como quebra de objeção — custo marginal zero.
3. **Order bump** (Ferramentas → Order bump): produto secundário "Pacote Festa do Pipo" (crie como produto separado de R$ 12,90) com a chamada: *"🎁 Leve também o Pacote Festa do Pipo (diploma emoldurável + colorir gigante + convites) por só R$ 12,90 — só nesta tela."*
4. **Pixel:** Ferramentas → Pixel de rastreamento → adicionar Pixel do Meta (eventos InitiateCheckout e Purchase automáticos).
5. **E-mail transacional:** personalize o e-mail de entrega com o texto do "E-mail 1 pós-compra" de `vendas/sequencia-emails.md`.

## Etapa 4 — Checklist de aprovação (evita reprovação na análise)

- [ ] Página de vendas descreve exatamente o que é entregue (10 páginas + 2 bônus + formato HTML offline)
- [ ] Nenhuma promessa de resultado pedagógico/médico ("vai aprender a ler", "desenvolve o cérebro")
- [ ] Nenhuma menção a marcas de terceiros
- [ ] Depoimentos: apenas reais e autorizados (na v1, a seção está com placeholders — ou preencha com relatos reais ou oculte a seção antes de submeter)
- [ ] Garantia de 7 dias visível
- [ ] Dados de contato/suporte válidos
- [ ] Comunicação 100% dirigida a adultos

## Etapa 5 — Hospedar a página de vendas (grátis)

Opção mais simples — **Netlify Drop:**
1. Acesse `app.netlify.com/drop` (crie conta grátis).
2. Renomeie `pagina-de-vendas.html` para `index.html`, coloque numa pasta e arraste a pasta para a página do Netlify.
3. Ele devolve uma URL (ex.: `pipo-livro-magico.netlify.app`). Você pode plugar um domínio próprio depois (ex.: `livromagicodopipo.com.br`, ~R$ 40/ano no Registro.br).
4. **Antes de subir:** troque TODOS os `#LINK-CHECKOUT-HOTMART` pelo link real do checkout (Hotmart → seu produto → Links → Página de pagamento). Busque e substitua no arquivo (são 5 ocorrências).

Alternativas equivalentes: Vercel (`vercel.com`, arraste igual) ou GitHub Pages (suba o arquivo num repositório e ative Pages em Settings).

## Etapa 6 — Afiliação

1. Produto → Afiliação → **Ativar**.
2. Comissão: **60% nos primeiros 90 dias** (estratégia de lançamento), depois 50%. Duração de cookie: 60 dias. Atribuição: último clique.
3. Aprovação de afiliados: **manual** no início (protege a marca de afiliado que promete demais e derruba seu produto).
4. Materiais para afiliados (suba no Club ou Drive): vídeos de tela do produto, 12 copies de `vendas/copy-anuncios.md`, regras de compliance (1 página): falar com pais, sem marcas de terceiros, sem promessa de resultado, sem segmentar menores.

## Etapa 7 — Checklist pré-lançamento (20 itens)

**Produto:** [ ] zip testado em Android [ ] testado em iPhone/iPad [ ] testado em computador [ ] som ok após 1º toque [ ] diploma imprime [ ] bônus abrem e imprimem
**Hotmart:** [ ] produto aprovado [ ] preço/parcelas ok [ ] garantia configurada [ ] order bump ativo [ ] e-mail de entrega personalizado [ ] compra-teste feita por você (modo sandbox ou compra real reembolsada)
**Página:** [ ] hospedada [ ] links de checkout reais [ ] abre bem no celular [ ] pixel disparando (teste com Meta Pixel Helper)
**Marketing:** [ ] perfil Instagram criado [ ] 5+ Reels prontos [ ] sequência de e-mails carregada [ ] 3 UGCs com autorização assinada
**Jurídico:** [ ] dossiê de originalidade arquivado (datas, repositório, autoria) [ ] pedido de marca no INPI iniciado (opcional, recomendado)

## Etapa 8 — Pós-venda

1. **Responda compradores em até 24h** (e-mail de suporte da Hotmart). 90% das dúvidas serão "como abro o arquivo?" — mande o LEIA-ME e um vídeo de 30s.
2. **Peça avaliação no dia 7** (e-mail 3 pós-compra). Avaliações no Hotmart alimentam o marketplace — vendas orgânicas de graça.
3. **Reembolso:** aprove sem discutir dentro dos 7 dias (é lei e é reputação). Monitore o motivo: se passar de 5%, o problema está na expectativa criada pelo anúncio, não no produto.
4. **Atualizações:** a cada versão (v1.1, v1.2...), poste no Módulo 4 e dispare e-mail — reativa a base e prepara o upsell.
