# 🔗 Regra dos Links de Afiliado — Guia Casa Inteligente (VALIDADO em 26/06/2026)

> Documento definitivo pra **não errar mais** na hora de montar os links de afiliado do Mercado Livre.
> As duas formas abaixo foram **testadas ao vivo**: uma cai na vitrine (errada), a outra cai no
> produto (certa). Etiqueta de afiliado em uso: **`alexandrehebeler`**.

---

## ✅ O JEITO CERTO (use sempre este)

**Fórmula:**

```
URL da página do produto  +  ?matt_word=alexandrehebeler
```

**Passo a passo:**

1. No Mercado Livre (logado como afiliado), abra a **página do produto**.
2. Copie a URL **até o `/p/MLBxxxxxxxx`**. Pode apagar tudo que vier depois do `#` (lixo de
   rastreamento de navegação).
3. Cole no final: **`?matt_word=alexandrehebeler`**

**Exemplo real (validado — abriu direto no produto):**

```
https://www.mercadolivre.com.br/xiaomi-robot-vacuum-s40c-5000pa-navegaco-a-laser-lds-de-360-aspirado-e-lavado-wi-fi-alexagoogle/p/MLB51669529?matt_word=alexandrehebeler
```

✔️ Cai **direto na página do produto**.
✔️ Rastreia sua comissão (a etiqueta `matt_word=alexandrehebeler`).
✔️ É o mesmo formato dos posts **01 e 02** que já estão no ar.

> Se a URL do produto já tiver um `?` (com outros parâmetros), use **`&matt_word=alexandrehebeler`**
> em vez de `?`.

---

## ❌ O JEITO ERRADO (NUNCA usar nos botões de compra)

**1. Link curto `meli.la` do botão "Compartilhar" / "Gerar link"**

- Testado: `https://meli.la/2nwiJU6` → **redirecionou para a VITRINE**
  `https://www.mercadolivre.com.br/social/alexandrehebeler...` ("ALEXANDREHEBELER | Perfil Social").
- O leitor cai numa lista do seu perfil e precisa clicar de novo em "Ir para produto" → **converte muito menos.**

**2. "Gerador de produtos recomendados"** (`/afiliados/linkbuilder`)

- O próprio subtítulo avisa: *"as pessoas... podem encontrar o produto recomendado no seu **perfil social**."*
- Também gera link de **vitrine**. Evitar para reviews.

> ⚠️ Resumindo: qualquer link que contenha **`/social/`** está ERRADO para os botões de compra.

---

## 🧪 Como conferir um link em 5 segundos

1. Cole o link numa aba anônima (ou me mande aqui que eu testo).
2. Veja onde ele **para** depois de redirecionar:
   - URL com **`/p/MLB...`** e a página do produto aberta → ✅ **certo**.
   - URL com **`/social/`** e título "Perfil Social" → ❌ **errado** (vitrine).

---

## 📋 No WordPress (ao colar o link no botão)

1. Selecione o texto do botão "Ver preço no Mercado Livre" → **Ctrl+K** → cole o link `…?matt_word=alexandrehebeler`.
2. Ative **abrir em nova aba**.
3. Confirme **`rel="nofollow sponsored"`** (Opções do bloco → Editar como HTML).
4. Apague o destaque amarelo de lembrete.

---

## ℹ️ Observações

- A comissão **varia por produto** (o robô Xiaomi S40C, por ex., mostrou **GANHOS 5%** na barra Afiliados).
  O % aparece na barra preta "Afiliados" quando você abre o produto logado.
- **Cookie de 30 dias:** quem clica no seu link e compra qualquer coisa no ML em até 30 dias gera
  comissão (último clique).
- A barra preta **"Afiliados"** no topo (com "GANHOS X%" e "Compartilhar") confirma que você está
  navegando logado como afiliado — mas, de novo: **não use o `meli.la` dela nos botões**; monte a URL
  do produto com `?matt_word=alexandrehebeler`.
