#!/usr/bin/env python3
"""
article_scaffolder.py — Gera o esqueleto completo de um artigo do SISTEMA DE LOOP
do blog TecnoPulso (Programa de Afiliados do Mercado Livre).

Uso:
  python3 article_scaffolder.py --tema "Os 10 Melhores Smartwatches do Mercado Livre"
  python3 article_scaffolder.py --tema "Galaxy Buds vs Redmi Buds" --tipo comparativo
  python3 article_scaffolder.py --tema "Review do Fone XYZ" --tipo review --json
  python3 article_scaffolder.py --tema "Nova IA para o dia a dia" --tipo noticia-ia
  python3 article_scaffolder.py          # modo demonstração

Regras do loop codificadas no esqueleto:
  Passo 2 — após CADA produto, o marcador exato em linha própria:
            [INSERIR CARTÃO DE PRODUTO MERCADO LIVRE AQUI]
  Passo 3 — seção final "## Bloco de SEO" com palavras-chave de cauda longa
            (mesmas fórmulas do seo_keyword_builder.py).
  Passo 4 — lembrete da pergunta exata de reinício do loop.

100% determinístico: sem chamadas de rede, sem LLM.
"""

import argparse
import json
import os
import re
import sys

# Reutiliza as fórmulas de palavras-chave do mesmo pacote de skill.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import seo_keyword_builder as skb  # noqa: E402

# ---------------------------------------------------------------------------
# Constantes do loop
# ---------------------------------------------------------------------------

MARCADOR_CARTAO = "[INSERIR CARTÃO DE PRODUTO MERCADO LIVRE AQUI]"
PERGUNTA_LOOP = ("Artigo finalizado! Qual será o próximo equipamento, "
                 "comparativo ou notícia de IA que vamos analisar?")

TIPOS = ("top10", "comparativo", "noticia-ia", "review")

DEMO_TEMA = "Os 10 Melhores Fones de Ouvido Bluetooth do Mercado Livre"

QTDE_KEYWORDS_BLOCO_SEO = 12  # dentro da regra de 10 a 15 do Passo 3

STOPWORDS_INICIO = {
    "os", "as", "o", "a", "um", "uma", "top", "melhores", "melhor",
    "guia", "completo", "dos", "das", "de", "do", "da", "novos", "novas",
    "review", "análise", "analise",
}
STOPWORDS_FIM = {"em", "de", "do", "da", "dos", "das", "para", "no", "na"}
SUFIXOS_REMOVER = (
    " do mercado livre", " no mercado livre", " para comprar",
    " que valem a pena", " custo benefício", " custo-benefício",
)


# ---------------------------------------------------------------------------
# Derivação determinística do produto a partir do tema
# ---------------------------------------------------------------------------

def extrair_produto(tema: str) -> str:
    """Extrai o produto-base do tema para alimentar o Bloco de SEO.

    Ex.: "Os 10 Melhores Fones de Ouvido Bluetooth do Mercado Livre"
         -> "fones de ouvido bluetooth"
    """
    t = tema.lower()
    t = t.split(":")[0]                          # descarta subtítulo
    t = re.split(r"\bvs\.?\b|\bversus\b", t)[0]  # comparativos: fica o 1º produto
    t = re.sub(r"[?!\"“”]", " ", t)
    t = re.sub(r"\b(19|20)\d{2}\b", " ", t)      # anos
    t = re.sub(r"\btop\s*\d+\b", " ", t)         # "top 10"
    t = re.sub(r"\b\d+\b", " ", t)               # números soltos
    for sufixo in SUFIXOS_REMOVER:
        posicao = t.find(sufixo)
        if posicao > 0:
            t = t[:posicao]
    palavras = t.split()
    while palavras and palavras[0] in STOPWORDS_INICIO:
        palavras.pop(0)
    while palavras and palavras[-1] in STOPWORDS_FIM:
        palavras.pop()
    produto = " ".join(palavras).strip(" -–—:,.")
    return produto or " ".join(tema.lower().split())


# ---------------------------------------------------------------------------
# Blocos de markdown (esqueleto PT-BR)
# ---------------------------------------------------------------------------

def bloco_produto(numero: int, rotulo: str = "[NOME DO PRODUTO]") -> str:
    """Passo 2 do loop: cada produto termina com o marcador exato do cartão."""
    return f"""### {numero}. {rotulo}

**Análise:** [2–3 parágrafos: por que este produto merece a posição — desempenho real, qualidade de construção e diferenciais frente aos concorrentes. Seja específico e honesto; nunca invente especificações.]

**Ideal para:** [Perfil de comprador — ex.: quem treina todos os dias, quem trabalha em home office, quem busca o primeiro da categoria.]

**Pontos fortes:**
- [Benefício concreto 1 — ex.: bateria para o dia inteiro de uso]
- [Benefício concreto 2]
- [Benefício concreto 3]

**Pontos de atenção:**
- [Limitação honesta 1 — ex.: sem resistência à água]
- [Limitação honesta 2]

**Faixa de preço:** [Use sempre faixa, nunca valor exato — ex.: R$ 150–250]

{MARCADOR_CARTAO}
"""


def _cabecalho(tema: str, ano: int) -> list:
    return [
        f"<!-- TÍTULO SEO (até 60 caracteres): {tema} ({ano}) -->",
        "<!-- META DESCRIPTION (até 155 caracteres): [Resumo persuasivo com a "
        "palavra-chave principal e um convite claro à leitura.] -->",
        "",
        f"# {tema}",
        "",
        "*Atualizado em [DATA] · Por TecnoPulso — Análises e comparativos de "
        "tecnologia, sem enrolação.*",
        "",
        "[INTRODUÇÃO — 2 a 3 parágrafos: apresente o problema do leitor, prometa a "
        "solução deste artigo e explique por que ele pode confiar na análise do "
        "TecnoPulso. Use a palavra-chave principal no primeiro parágrafo.]",
        "",
    ]


def _linhas_tabela_top10(n: int) -> list:
    linhas = [
        "## Tabela comparativa",
        "",
        "| # | Produto | Ideal para | Faixa de preço | Destaque |",
        "|---|---------|------------|----------------|----------|",
    ]
    for i in range(1, n + 1):
        linhas.append(f"| {i} | [NOME DO PRODUTO {i}] | [perfil de uso] | "
                      "[R$ XXX–XXX] | [principal diferencial] |")
    linhas.append("")
    return linhas


def _corpo_top10(n: int, produto: str) -> list:
    linhas = [
        "## Como escolhemos (metodologia)",
        "",
        "[1 parágrafo + bullets com os critérios: custo benefício, avaliações de "
        "compradores no Mercado Livre, recursos que importam no dia a dia, "
        "durabilidade e reputação da marca.]",
        "",
        f"## Os {n} melhores em detalhes",
        "",
    ]
    for i in range(1, n + 1):
        linhas.append(bloco_produto(i))
    linhas += _linhas_tabela_top10(n)
    linhas += [
        "## Veredito: qual vale mais a pena?",
        "",
        f"[Feche com recomendações claras por perfil: melhor {produto} no geral, "
        "melhor custo benefício e melhor opção premium. Sem ficar em cima do muro.]",
        "",
    ]
    return linhas


def _corpo_comparativo(produto: str) -> list:
    return [
        "## Visão geral do comparativo",
        "",
        "[1 parágrafo: contexto do duelo e para quem cada produto tende a ser a "
        "melhor escolha.]",
        "",
        bloco_produto(1, "[NOME DO PRODUTO A]"),
        bloco_produto(2, "[NOME DO PRODUTO B]"),
        "## Tabela comparativa lado a lado",
        "",
        "| Critério | [PRODUTO A] | [PRODUTO B] |",
        "|----------|-------------|-------------|",
        "| Ideal para | [perfil] | [perfil] |",
        "| Bateria | [autonomia observada em uso real] | [autonomia observada em uso real] |",
        "| Qualidade de construção | [avaliação honesta] | [avaliação honesta] |",
        "| Recursos que importam | [lista curta] | [lista curta] |",
        "| Faixa de preço | [R$ XXX–XXX] | [R$ XXX–XXX] |",
        "",
        "## Veredito: qual escolher?",
        "",
        f"[Recomendação direta por perfil de uso de {produto} — deixe claro quem "
        "deve comprar cada um.]",
        "",
    ]


def _corpo_review(produto: str) -> list:
    return [
        "## Ficha resumida",
        "",
        "| Item | Detalhe |",
        "|------|---------|",
        "| Produto | [NOME DO PRODUTO] |",
        f"| Categoria | {produto} |",
        "| Ideal para | [perfil de comprador] |",
        "| Faixa de preço | [R$ XXX–XXX] |",
        "| Nota TecnoPulso | [x/10] |",
        "",
        "## Análise completa",
        "",
        bloco_produto(1),
        "## Experiência de uso no dia a dia",
        "",
        "[2–3 parágrafos: como o produto se comporta em uso real — conforto, "
        "aplicativo, o que surpreende e o que decepciona. Relate apenas o que "
        "puder ser verificado; nunca invente especificações.]",
        "",
        "## Para quem vale (e para quem não vale) a pena",
        "",
        "- **Vale a pena se:** [perfil/situação concreta]",
        "- **Vale a pena se:** [perfil/situação concreta]",
        "- **Não vale a pena se:** [perfil/situação concreta]",
        "",
    ]


def _corpo_noticia_ia() -> list:
    return [
        "## O que aconteceu",
        "",
        "[2 parágrafos: o fato, quem anunciou e quando. Cite a fonte oficial do "
        "anúncio.]",
        "",
        "## Por que isso importa",
        "",
        "[Análise: impacto para o mercado de tecnologia e para o consumidor "
        "brasileiro.]",
        "",
        "## Como isso afeta você no dia a dia",
        "",
        "[Exemplos práticos: trabalho, estudos, casa. Traduza o anúncio técnico em "
        "benefícios reais.]",
        "",
        "## Produto relacionado para aproveitar a novidade",
        "",
        "[1 parágrafo conectando a notícia a um produto disponível no Mercado "
        "Livre — ex.: um celular ou fone compatível com o novo recurso de IA.]",
        "",
        bloco_produto(1, "[NOME DO PRODUTO RELACIONADO]"),
    ]


def _faq(produto: str, ano: int, plural: bool) -> list:
    qual = "quais" if plural else "qual"
    original = "são originais" if plural else "é original"
    quanto = f"quanto custam bons {produto}" if plural else f"quanto custa um bom {produto}"
    return [
        "## Perguntas frequentes (FAQ)",
        "",
        f"### [Pergunta 1 — ex.: {qual} {produto} comprar em {ano}?]",
        "",
        "[Resposta direta em 2–4 frases, começando pela conclusão.]",
        "",
        f"### [Pergunta 2 — ex.: {produto} do Mercado Livre {original}?]",
        "",
        "[Explique como identificar lojas oficiais e vendedores bem avaliados.]",
        "",
        f"### [Pergunta 3 — ex.: {quanto}?]",
        "",
        "[Responda sempre com faixas de preço — ex.: R$ 150–250 —, nunca com "
        "valores exatos.]",
        "",
    ]


def _aviso_afiliado() -> list:
    return [
        "## Aviso de transparência",
        "",
        "> O TecnoPulso participa do Programa de Afiliados do Mercado Livre. Se "
        "você comprar pelos links desta página, podemos receber uma comissão — "
        "**sem nenhum custo adicional para você**. Isso financia nossos testes e "
        "análises e não influencia nossas opiniões.",
        "",
    ]


def _bloco_seo(keywords: list) -> list:
    linhas = ["## Bloco de SEO", ""]
    linhas += [f"- {kw}" for kw in keywords]
    return linhas


# ---------------------------------------------------------------------------
# Montagem do esqueleto
# ---------------------------------------------------------------------------

def montar_esqueleto(tema: str, tipo: str, produtos: int, ano: int) -> dict:
    produto = extrair_produto(tema)
    categoria = skb.detectar_categoria(tema)
    keywords = skb.gerar_keywords(produto, categoria, ano, QTDE_KEYWORDS_BLOCO_SEO)
    plural = skb._eh_plural(produto)

    linhas = _cabecalho(tema, ano)
    if tipo == "top10":
        linhas += _corpo_top10(produtos, produto)
    elif tipo == "comparativo":
        linhas += _corpo_comparativo(produto)
    elif tipo == "review":
        linhas += _corpo_review(produto)
    else:  # noticia-ia
        linhas += _corpo_noticia_ia()
    linhas += _faq(produto, ano, plural)
    linhas += _aviso_afiliado()
    linhas += _bloco_seo(keywords)

    markdown = "\n".join(linhas).rstrip() + "\n"
    return {
        "tema": tema,
        "tipo": tipo,
        "ano": ano,
        "produtos": produtos if tipo == "top10" else (2 if tipo == "comparativo" else 1),
        "categoria_detectada": categoria,
        "markdown": markdown,
        "keywords": keywords,
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description=("Gera o esqueleto completo (PT-BR) de um artigo do SISTEMA DE "
                     "LOOP do TecnoPulso: título SEO, blocos de produto com o "
                     "marcador do cartão Mercado Livre, tabela comparativa, FAQ, "
                     "aviso de afiliado e Bloco de SEO. Determinístico, sem rede "
                     "e sem LLM.")
    )
    parser.add_argument("--tema",
                        help='Tema do artigo, ex.: "Os 10 Melhores Smartwatches '
                             'do Mercado Livre"')
    parser.add_argument("--tipo", choices=TIPOS, default="top10",
                        help="Formato do artigo (padrão: top10)")
    parser.add_argument("--produtos", type=int, default=10,
                        help="Quantidade de produtos na lista — usado apenas no "
                             "tipo top10 (padrão: 10)")
    parser.add_argument("--ano", type=int, default=2026,
                        help="Ano de referência (padrão: 2026)")
    parser.add_argument("--json", action="store_true",
                        help="Saída em JSON (para automação)")
    args = parser.parse_args()

    if not 2000 <= args.ano <= 2100:
        parser.error("--ano deve estar entre 2000 e 2100")
    if args.tipo == "top10" and not 1 <= args.produtos <= 20:
        parser.error("--produtos deve estar entre 1 e 20 para o tipo top10")

    demo = args.tema is None
    tema = args.tema or DEMO_TEMA

    resultado = montar_esqueleto(tema, args.tipo, args.produtos, args.ano)

    if args.json:
        print(json.dumps(resultado, ensure_ascii=False, indent=2))
        return

    if demo:
        print("Nenhum tema informado — executando em modo demonstração.")
        print(f'Tema demo: "{DEMO_TEMA}" (tipo: {args.tipo})')
        print("─" * 72)
        print()

    print(resultado["markdown"])
    print("─" * 72)
    print("Passo 4 do loop — finalize a conversa SEMPRE com a pergunta exata:")
    print(f'"{PERGUNTA_LOOP}"')


if __name__ == "__main__":
    main()
