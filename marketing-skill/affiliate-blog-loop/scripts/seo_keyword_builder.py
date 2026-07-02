#!/usr/bin/env python3
"""
seo_keyword_builder.py — Gera o "Bloco de SEO" com palavras-chave de cauda longa
para artigos do blog TecnoPulso (Programa de Afiliados do Mercado Livre).

Uso:
  python3 seo_keyword_builder.py --produto "fones de ouvido bluetooth" --categoria fones
  python3 seo_keyword_builder.py --produto "smartwatch" --categoria smartwatches --quantidade 12
  python3 seo_keyword_builder.py --produto "celulares" --categoria celulares --json
  python3 seo_keyword_builder.py          # modo demonstração

100% determinístico: sem chamadas de rede, sem LLM — apenas templates combinatórios.
"""

import argparse
import json
import re

# ---------------------------------------------------------------------------
# Configuração
# ---------------------------------------------------------------------------

CATEGORIAS = ("fones", "celulares", "smartwatches", "ia", "geral")

DEMO_PRODUTO = "fones de ouvido bluetooth"

# Templates de alta intenção de compra — sempre entram primeiro.
# Placeholders: {p} produto, {ano} ano, {melhor}/{qual}/{bom_barato} concordância.
TEMPLATES_PRIORITARIOS = [
    "{melhor} {p} custo benefício {ano}",
    "{qual} {p} comprar em {ano}",
    "{p} vale a pena",
    "{p} {bom_barato}",
]

# Templates genéricos — funcionam para qualquer nicho do blog.
TEMPLATES_GERAIS = [
    "{melhor} {p} até 200 reais",
    "{p} para trabalhar",
    "{p} para estudar",
    "{p} para treinar",
    "como escolher {p}",
    "{p} com melhor bateria",
    "{p} no mercado livre vale a pena",
    "comparativo de {p} {ano}",
    "onde comprar {p} com desconto",
    "{p} barato com boa qualidade",
]

# Templates específicos por nicho do TecnoPulso.
TEMPLATES_POR_CATEGORIA = {
    "fones": [
        "{p} com cancelamento de ruído",
        "{p} para academia",
        "{p} sem fio para celular",
        "{p} com graves fortes",
        "{melhor} {p} para chamadas e reuniões",
    ],
    "celulares": [
        "{p} com câmera boa",
        "{p} com bateria que dura o dia todo",
        "{p} intermediário custo benefício {ano}",
        "{p} para jogos sem travar",
        "{p} com boa tela para vídeos",
    ],
    "smartwatches": [
        "{p} com monitor de sono",
        "{p} para corrida",
        "{p} com gps integrado",
        "{p} compatível com android e iphone",
        "{p} para acompanhar treinos e saúde",
    ],
    "ia": [
        "o que é {p}",
        "como usar {p}",
        "{p} no dia a dia",
        "{p} gratuito vale a pena",
        "{melhor} ferramenta de {p} {ano}",
    ],
    "geral": [],
}


# ---------------------------------------------------------------------------
# Núcleo determinístico
# ---------------------------------------------------------------------------

def _normalizar(texto: str) -> str:
    """Minúsculas + espaços simples (padrão de palavra-chave de cauda longa)."""
    return " ".join(texto.lower().split())


def _eh_plural(produto: str) -> bool:
    """Heurística simples: primeira palavra terminada em 's' => plural.

    Ex.: 'fones de ouvido' -> plural; 'smartwatch' -> singular.
    """
    palavras = produto.split()
    if not palavras:
        return False
    primeira = palavras[0]
    return len(primeira) > 3 and primeira.endswith("s")


def detectar_categoria(texto: str) -> str:
    """Detecta o nicho do TecnoPulso a partir de um tema/produto (determinístico)."""
    t = _normalizar(texto)
    if any(s in t for s in ("fone", "headphone", "headset", "earbud", "tws")):
        return "fones"
    if any(s in t for s in ("smartwatch", "relógio inteligente", "relogio inteligente",
                            "smartband", "pulseira inteligente")):
        return "smartwatches"
    if any(s in t for s in ("celular", "smartphone", "iphone", "telefone")):
        return "celulares"
    if ("inteligência artificial" in t or "inteligencia artificial" in t
            or "chatgpt" in t or re.search(r"\bia\b", t)):
        return "ia"
    return "geral"


def gerar_keywords(produto: str, categoria: str = "geral",
                   ano: int = 2026, quantidade: int = 14) -> list:
    """Gera a lista de palavras-chave de cauda longa (deduplicada, ordem estável)."""
    p = _normalizar(produto)
    plural = _eh_plural(p)
    campos = {
        "p": p,
        "ano": ano,
        "melhor": "melhores" if plural else "melhor",
        "qual": "quais" if plural else "qual",
        "bom_barato": "bons e baratos" if plural else "bom e barato",
    }
    templates = (
        TEMPLATES_PRIORITARIOS
        + TEMPLATES_POR_CATEGORIA.get(categoria, [])
        + TEMPLATES_GERAIS
    )
    vistos = set()
    keywords = []
    for template in templates:
        kw = " ".join(template.format(**campos).split())
        if kw not in vistos:
            vistos.add(kw)
            keywords.append(kw)
        if len(keywords) >= quantidade:
            break
    return keywords


# ---------------------------------------------------------------------------
# Saída
# ---------------------------------------------------------------------------

def imprimir_bloco_seo(keywords: list):
    print("## Bloco de SEO")
    print()
    for kw in keywords:
        print(f"- {kw}")
    print()
    print(f"{len(keywords)} palavras-chave de cauda longa geradas "
          "(recomendado: 10 a 15 por artigo).")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description=("Gera o 'Bloco de SEO' com palavras-chave de cauda longa em PT-BR "
                     "para artigos do TecnoPulso (determinístico, sem rede e sem LLM).")
    )
    parser.add_argument("--produto",
                        help='Produto ou assunto base, ex.: "fones de ouvido bluetooth"')
    parser.add_argument("--categoria", choices=CATEGORIAS, default=None,
                        help="Nicho do blog (padrão: geral)")
    parser.add_argument("--ano", type=int, default=2026,
                        help="Ano de referência para as palavras-chave (padrão: 2026)")
    parser.add_argument("--quantidade", type=int, default=14,
                        help="Quantidade máxima de palavras-chave (padrão: 14)")
    parser.add_argument("--json", action="store_true",
                        help="Saída em JSON (para automação)")
    args = parser.parse_args()

    if args.quantidade < 1:
        parser.error("--quantidade deve ser maior ou igual a 1")
    if not 2000 <= args.ano <= 2100:
        parser.error("--ano deve estar entre 2000 e 2100")

    demo = args.produto is None
    produto = _normalizar(args.produto or DEMO_PRODUTO)
    categoria = args.categoria or ("fones" if demo else "geral")

    keywords = gerar_keywords(produto, categoria, args.ano, args.quantidade)

    if args.json:
        print(json.dumps({
            "produto": produto,
            "categoria": categoria,
            "ano": args.ano,
            "keywords": keywords,
        }, ensure_ascii=False, indent=2))
        return

    if demo:
        print("Nenhum produto informado — executando em modo demonstração.")
        print(f'Produto demo: "{DEMO_PRODUTO}" (categoria: {categoria})')
        print()

    imprimir_bloco_seo(keywords)


if __name__ == "__main__":
    main()
