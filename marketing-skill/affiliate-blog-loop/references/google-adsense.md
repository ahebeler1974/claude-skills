# Google AdSense no TecnoPulso — guia completo de ativação e aprovação

O AdSense é a **segunda fonte de renda** do blog: enquanto os links do Mercado Livre
pagam por venda, o AdSense paga por impressão/clique nos anúncios — dinheiro entrando
com o blog "vivo", 24h por dia, mesmo quando ninguém compra. Este guia leva do zero
à aprovação e ao primeiro pagamento.

**Importante:** AdSense e afiliados do Mercado Livre **podem conviver no mesmo blog**
sem violar nenhuma política, desde que o conteúdo seja original e os anúncios não
enganem o leitor.

---

## ETAPA 0 — Deixe o blog "aprovável" ANTES de se inscrever

O Google recusa sites que não parecem "negócios reais". O TecnoPulso já tem conteúdo
original e design profissional — falta o kit institucional. Crie estas 2 páginas
(Páginas → Adicionar nova) e coloque no rodapé/menu:

### 1. Política de Privacidade (obrigatória)

Conteúdo mínimo (pode usar como base):

> Esta página descreve como o TecnoPulso trata dados de visitantes. Utilizamos
> cookies para melhorar a experiência de navegação e veicular anúncios.
> **Google AdSense:** este site exibe anúncios fornecidos pelo Google. O Google
> utiliza cookies (incluindo o cookie DART) para exibir anúncios com base em visitas
> anteriores. Você pode desativar a publicidade personalizada em
> adssettings.google.com. **Afiliados:** participamos do Programa de Afiliados do
> Mercado Livre e podemos receber comissão por compras feitas através de nossos
> links, sem custo adicional para você. **Contato:** [seu e-mail]. Em conformidade
> com a LGPD (Lei 13.709/2018), você pode solicitar a exclusão de seus dados pelo
> e-mail acima.

### 2. Contato

Uma página simples com seu e-mail de contato (pode ser um formulário do plugin, mas
e-mail em texto já basta).

### Checklist de elegibilidade antes de aplicar

- [ ] **Search Console verificado e sitemap enviado** (pendência conhecida — faça antes!)
- [ ] Páginas Sobre, Contato e Política de Privacidade publicadas e no rodapé/menu
- [ ] **Mínimo recomendado: 15–20 artigos publicados** (hoje são 4 + antigos de casa
      inteligente — rode o loop por 3–4 semanas antes de aplicar; sites com pouco
      conteúdo são a causa nº 1 de recusa por "conteúdo de baixo valor")
- [ ] Domínio com HTTPS ativo (cadeado no navegador)
- [ ] Você tem 18+ anos e conta Google própria

---

## ETAPA 1 — Inscrição no AdSense (10 min)

1. Acesse **adsense.google.com** logado na sua conta Google e clique em **Começar**.
2. Site: `https://ahebeler.shop` · País: **Brasil** · aceite os termos.
3. Preencha o **endereço de pagamento** com seus dados reais (nome idêntico ao do
   banco — depois não dá para mudar a titularidade).

## ETAPA 2 — Conectar o site ao AdSense (15 min)

O jeito mais fácil no WordPress é o plugin oficial do Google:

1. **Plugins → Adicionar novo** → busque **"Site Kit by Google"** → Instalar → Ativar.
2. Siga o assistente do Site Kit: conecte sua conta Google → ele verifica o Search
   Console automaticamente → em seguida ative o módulo **AdSense** dentro do Site Kit.
3. O Site Kit insere o código do AdSense em todas as páginas sozinho (sem mexer em
   tema). Volte ao painel do AdSense e clique em **"Verificar"** / **"Solicitar revisão"**.

**Alternativa sem plugin:** copie a tag `<script>` que o AdSense fornece e cole em
GeneratePress: **Aparência → Personalizar → (ou plugin "WPCode") → cabeçalho `<head>`**.

## ETAPA 3 — ads.txt (5 min — evita perder receita)

O AdSense vai pedir um arquivo `ads.txt`. Com o Site Kit, ative em
**Site Kit → Configurações → AdSense → ads.txt** (automático). Manualmente: crie o
arquivo com a linha que o AdSense mostrar, no formato:

```
google.com, pub-XXXXXXXXXXXXXXXX, DIRECT, f08c47fec0942fa0
```

e envie para a raiz do site (a Hostinger tem gerenciador de arquivos no hPanel).

## ETAPA 4 — Espera da revisão (2 dias a 4 semanas)

- O status fica **"Preparando..."** — normal demorar. Não fique reenviando.
- **Continue publicando artigos durante a espera** — sites ativos aprovam mais.
- Se for **recusado**: o e-mail diz o motivo (quase sempre "conteúdo de baixo
  valor"). Publique mais 10 artigos originais e reaplique após 2 semanas — pode
  reaplicar quantas vezes precisar.

## ETAPA 5 — Aprovado! Configurando os anúncios do jeito certo

1. No AdSense: **Anúncios → Por site → ahebeler.shop → Anúncios automáticos: ATIVAR**.
   Deixe o Google posicionar sozinho no começo.
2. **Ajuste a carga de anúncios para ~50–60%** (controle deslizante) — blog novo com
   excesso de anúncio espanta leitor e derruba o SEO.
3. Desative formatos intrusivos se incomodarem: âncora no topo e "vinheta"
   (tela cheia entre páginas) são os que mais irritam no celular.
4. Depois de 2–3 semanas, veja no relatório quais posições rendem e crie blocos
   manuais nos pontos quentes: **após a introdução**, **no meio do artigo** e
   **antes do FAQ** (Site Kit ou bloco "Anúncio" do WordPress).

## ETAPA 6 — Pagamento

- **Limiar: US$ 100** (pago em R$ via transferência bancária no Brasil).
- Com ~US$ 10 acumulados o Google envia um **PIN por carta** para confirmar seu
  endereço (chega em 2–4 semanas) — digite-o em Pagamentos → Verificação.
- Cadastre a conta bancária em **Pagamentos → Formas de pagamento**.

---

## Regras de ouro (quem quebra, perde a conta — sem recurso)

1. **NUNCA clique nos próprios anúncios** nem peça cliques ("clique ali para apoiar").
2. Não recarregue a página para inflar impressões, nem use tráfego comprado/bots.
3. Não coloque anúncio em pop-up, nem sobreposto a botão (o leitor não pode clicar
   "sem querer").
4. Conteúdo sempre original — cópia de outros sites derruba a conta e o SEO juntos.
5. Mantenha a Política de Privacidade citando cookies e anúncios (LGPD + exigência
   do Google).

## Expectativa realista (nicho tech no Brasil)

- RPM (receita por 1.000 visualizações) típico: **R$ 2–15** — tecnologia paga acima
  da média porque anunciantes de eletrônicos disputam o espaço.
- Tradução: AdSense vira renda relevante com **dezenas de milhares de visitas/mês**.
  No começo, o Mercado Livre paga mais; o AdSense cresce junto com o tráfego.
- O combo vencedor continua o mesmo: **2–3 artigos/semana pelo loop + TikTok/Reels
  apontando para o blog** → tráfego → comissões + AdSense.

## Resumo em 1 linha

> Search Console ✔ → Sobre/Contato/Privacidade ✔ → 15–20 artigos ✔ → Site Kit →
> solicitar revisão → ads.txt → aguardar → ativar anúncios automáticos a 50% →
> nunca clicar no próprio anúncio → PIN por carta → US$ 100 → 💰
