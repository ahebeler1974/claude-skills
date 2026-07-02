#!/usr/bin/env python3
"""
Exportador WordPress (WXR) do TecnoPulso.

Converte artigos Markdown do SISTEMA DE LOOP em um arquivo WXR
(WordPress eXtended RSS) pronto para importar em Ferramentas > Importar >
WordPress. Cada artigo vira um post (rascunho por padrão) com título,
slug, resumo (meta description), categoria e conteúdo em HTML — com os
marcadores [INSERIR CARTÃO DE PRODUTO MERCADO LIVRE AQUI] destacados para
você plugar os cartões de afiliado antes de publicar.

Determinístico, sem rede e sem LLM. Apenas biblioteca padrão.

Uso:
  python3 wordpress_exporter.py artigo1.md artigo2.md --saida import.xml
  python3 wordpress_exporter.py                # modo demo (usa ../examples)
"""

import argparse
import html
import json
import re
import sys
import unicodedata
from datetime import datetime, timedelta
from pathlib import Path

MARCADOR = "[INSERIR CARTÃO DE PRODUTO MERCADO LIVRE AQUI]"

MARCADOR_HTML = (
    '<p style="border:2px dashed #d97706;background:#fffbeb;color:#92400e;'
    'padding:12px 16px;border-radius:8px;font-weight:bold;text-align:center;">'
    "&#128295; [INSERIR CARTÃO DE PRODUTO MERCADO LIVRE AQUI] &#128295;<br/>"
    '<span style="font-weight:normal;font-size:14px;">Substitua este bloco pelo '
    "cartão de produto do plugin com o SEU link de afiliado do Mercado Livre.</span></p>"
)

# Ordem importa: padrões mais específicos primeiro.
CATEGORIAS_POR_ARQUIVO = [
    (r"fone", "Fones de Ouvido"),
    (r"smartwatch|relogio|watch", "Smartwatches"),
    (r"noticia-ia|-ia-|\bia\b", "Inteligência Artificial"),
    (r"celular|iphone|galaxy|comparativo|smartphone", "Celulares"),
]
CATEGORIA_PADRAO = "Reviews"


def slugify(texto):
    """Converte texto em slug de URL (sem acentos, minúsculas, hífens)."""
    norm = unicodedata.normalize("NFKD", texto)
    sem_acentos = norm.encode("ascii", "ignore").decode("ascii")
    slug = re.sub(r"[^a-z0-9]+", "-", sem_acentos.lower()).strip("-")
    return slug or "post"


def detectar_categoria(nome_arquivo):
    nome = nome_arquivo.lower()
    for padrao, categoria in CATEGORIAS_POR_ARQUIVO:
        if re.search(padrao, nome):
            return categoria
    return CATEGORIA_PADRAO


def _inline(texto):
    """Aplica formatação inline: escapes, links, negrito, itálico, código."""
    texto = html.escape(texto, quote=False)
    texto = re.sub(r"\[([^\]]+)\]\((https?://[^)\s]+)\)", r'<a href="\2">\1</a>', texto)
    texto = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", texto)
    texto = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"<em>\1</em>", texto)
    texto = re.sub(r"`([^`]+)`", r"<code>\1</code>", texto)
    return texto


def _fechar_paragrafo(buffer, saida):
    if buffer:
        saida.append("<p>" + _inline(" ".join(buffer)) + "</p>")
        buffer.clear()


def _tabela_html(linhas):
    """Converte linhas '| a | b |' em <table> (2ª linha é o separador)."""
    def celulas(linha):
        return [c.strip() for c in linha.strip().strip("|").split("|")]

    corpo = [l for i, l in enumerate(linhas) if i != 1]
    if not corpo:
        return ""
    partes = ['<table class="tp-tabela"><thead><tr>']
    partes += [f"<th>{_inline(c)}</th>" for c in celulas(corpo[0])]
    partes.append("</tr></thead><tbody>")
    for linha in corpo[1:]:
        partes.append("<tr>" + "".join(f"<td>{_inline(c)}</td>" for c in celulas(linha)) + "</tr>")
    partes.append("</tbody></table>")
    return "".join(partes)


def markdown_para_html(markdown):
    """Converte o subconjunto de Markdown usado nos artigos do loop em HTML."""
    saida, paragrafo, lista, citacao, tabela = [], [], [], [], []
    for linha in markdown.split("\n") + [""]:
        texto = linha.rstrip()
        eh_lista = texto.startswith("- ")
        eh_citacao = texto.startswith(">")
        eh_tabela = texto.startswith("|")

        if lista and not eh_lista:
            saida.append("<ul>" + "".join(f"<li>{_inline(i)}</li>" for i in lista) + "</ul>")
            lista = []
        if citacao and not eh_citacao:
            saida.append("<blockquote><p>" + _inline(" ".join(citacao)) + "</p></blockquote>")
            citacao = []
        if tabela and not eh_tabela:
            saida.append(_tabela_html(tabela))
            tabela = []

        if not texto:
            _fechar_paragrafo(paragrafo, saida)
        elif texto == MARCADOR:
            _fechar_paragrafo(paragrafo, saida)
            saida.append(MARCADOR_HTML)
        elif re.match(r"#{1,6} ", texto):
            _fechar_paragrafo(paragrafo, saida)
            nivel = len(texto) - len(texto.lstrip("#"))
            saida.append(f"<h{nivel}>{_inline(texto[nivel + 1:])}</h{nivel}>")
        elif texto in ("---", "***"):
            _fechar_paragrafo(paragrafo, saida)
            saida.append("<hr/>")
        elif eh_lista:
            _fechar_paragrafo(paragrafo, saida)
            lista.append(texto[2:])
        elif eh_citacao:
            _fechar_paragrafo(paragrafo, saida)
            citacao.append(texto.lstrip("> "))
        elif eh_tabela:
            _fechar_paragrafo(paragrafo, saida)
            tabela.append(texto)
        else:
            paragrafo.append(texto)
    return "\n".join(saida)


def extrair_artigo(caminho):
    """Lê um artigo do loop e separa título, meta description e corpo."""
    texto = Path(caminho).read_text(encoding="utf-8")
    titulo_seo = re.search(r"\*\*Título SEO:\*\*\s*(.+)", texto)
    meta = re.search(r"\*\*Meta description:\*\*\s*(.+)", texto)
    h1 = re.search(r"^# (.+)$", texto, re.M)

    titulo = (titulo_seo.group(1) if titulo_seo else h1.group(1) if h1 else Path(caminho).stem).strip()
    resumo = meta.group(1).strip() if meta else ""

    corpo = texto
    if h1:
        corpo = corpo[h1.end():]  # título vira o título do post; H1 sai do corpo
    corpo = re.sub(r"\*\*(Título SEO|Meta description):\*\*.*", "", corpo)
    return {
        "titulo": titulo,
        "resumo": resumo,
        "slug": slugify(Path(caminho).stem),
        "categoria": detectar_categoria(Path(caminho).name),
        "html": markdown_para_html(corpo.strip()),
    }


def _cdata(texto):
    return "<![CDATA[" + texto.replace("]]>", "]]]]><![CDATA[>") + "]]>"


def gerar_wxr(posts, site, autor, status, data_base):
    itens = []
    for i, p in enumerate(posts, start=1):
        data_post = data_base + timedelta(minutes=i)
        data_str = data_post.strftime("%Y-%m-%d %H:%M:%S")
        pub_date = data_post.strftime("%a, %d %b %Y %H:%M:%S +0000")
        cat_slug = slugify(p["categoria"])
        itens.append(f"""    <item>
      <title>{html.escape(p['titulo'])}</title>
      <link>{site}/{p['slug']}/</link>
      <pubDate>{pub_date}</pubDate>
      <dc:creator>{_cdata(autor)}</dc:creator>
      <guid isPermaLink="false">{site}/?p={1000 + i}</guid>
      <description></description>
      <content:encoded>{_cdata(p['html'])}</content:encoded>
      <excerpt:encoded>{_cdata(p['resumo'])}</excerpt:encoded>
      <wp:post_id>{1000 + i}</wp:post_id>
      <wp:post_date>{_cdata(data_str)}</wp:post_date>
      <wp:post_date_gmt>{_cdata(data_str)}</wp:post_date_gmt>
      <wp:comment_status>{_cdata('open')}</wp:comment_status>
      <wp:ping_status>{_cdata('open')}</wp:ping_status>
      <wp:post_name>{_cdata(p['slug'])}</wp:post_name>
      <wp:status>{_cdata(status)}</wp:status>
      <wp:post_parent>0</wp:post_parent>
      <wp:menu_order>0</wp:menu_order>
      <wp:post_type>{_cdata('post')}</wp:post_type>
      <wp:post_password>{_cdata('')}</wp:post_password>
      <wp:is_sticky>0</wp:is_sticky>
      <category domain="category" nicename="{cat_slug}">{_cdata(p['categoria'])}</category>
    </item>""")

    return f"""<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0"
  xmlns:excerpt="http://wordpress.org/export/1.2/excerpt/"
  xmlns:content="http://purl.org/rss/1.0/modules/content/"
  xmlns:wfw="http://wellformedweb.org/CommentAPI/"
  xmlns:dc="http://purl.org/dc/elements/1.1/"
  xmlns:wp="http://wordpress.org/export/1.2/">
  <channel>
    <title>TecnoPulso</title>
    <link>{site}</link>
    <description>Análises e comparativos de tecnologia, sem enrolação.</description>
    <language>pt-BR</language>
    <wp:wxr_version>1.2</wp:wxr_version>
    <wp:base_site_url>{site}</wp:base_site_url>
    <wp:base_blog_url>{site}</wp:base_blog_url>
    <wp:author>
      <wp:author_id>1</wp:author_id>
      <wp:author_login>{_cdata(slugify(autor))}</wp:author_login>
      <wp:author_email>{_cdata('')}</wp:author_email>
      <wp:author_display_name>{_cdata(autor)}</wp:author_display_name>
      <wp:author_first_name>{_cdata('')}</wp:author_first_name>
      <wp:author_last_name>{_cdata('')}</wp:author_last_name>
    </wp:author>
{chr(10).join(itens)}
  </channel>
</rss>
"""


def main():
    parser = argparse.ArgumentParser(
        description=(
            "Converte artigos Markdown do SISTEMA DE LOOP do TecnoPulso em um arquivo "
            "WXR para importar no WordPress (Ferramentas > Importar > WordPress). "
            "Os posts entram como rascunho para você plugar os cartões de afiliado "
            "do Mercado Livre antes de publicar. Determinístico, sem rede e sem LLM."
        )
    )
    parser.add_argument("arquivos", nargs="*", help="Artigos .md do loop (sem argumentos: modo demo com examples/)")
    parser.add_argument("--saida", default="tecnopulso-import.xml", help="Arquivo WXR de saída (padrão: tecnopulso-import.xml)")
    parser.add_argument("--site", default="https://tecnopulso.com.br", help="URL do blog (padrão: https://tecnopulso.com.br)")
    parser.add_argument("--autor", default="TecnoPulso", help="Nome do autor dos posts (padrão: TecnoPulso)")
    parser.add_argument("--status", choices=["draft", "publish"], default="draft", help="Status dos posts importados (padrão: draft)")
    parser.add_argument("--data", default=None, help="Data base dos posts em AAAA-MM-DD (padrão: hoje)")
    parser.add_argument("--categoria", default=None, help="Força uma categoria única para todos os artigos")
    parser.add_argument("--json", action="store_true", help="Imprime resumo em JSON")
    args = parser.parse_args()

    arquivos = [Path(a) for a in args.arquivos]
    demo = not arquivos
    if demo:
        pasta_exemplos = Path(__file__).resolve().parent.parent / "examples"
        arquivos = sorted(pasta_exemplos.glob("*.md"))
        if not arquivos:
            print("Modo demo: nenhuma pasta examples/ encontrada e nenhum arquivo informado.", file=sys.stderr)
            sys.exit(1)

    faltando = [str(a) for a in arquivos if not a.is_file()]
    if faltando:
        print(f"Arquivo(s) não encontrado(s): {', '.join(faltando)}", file=sys.stderr)
        sys.exit(1)

    data_base = datetime.strptime(args.data, "%Y-%m-%d") if args.data else datetime.now().replace(microsecond=0)

    posts = []
    for arquivo in arquivos:
        post = extrair_artigo(arquivo)
        if args.categoria:
            post["categoria"] = args.categoria
        posts.append(post)

    Path(args.saida).write_text(gerar_wxr(posts, args.site.rstrip("/"), args.autor, args.status, data_base), encoding="utf-8")

    if args.json:
        print(json.dumps({
            "saida": str(args.saida),
            "status": args.status,
            "posts": [{"titulo": p["titulo"], "slug": p["slug"], "categoria": p["categoria"]} for p in posts],
        }, ensure_ascii=False, indent=2))
    else:
        if demo:
            print("Nenhum arquivo informado — executando em modo demonstração com a pasta examples/.\n")
        print(f"✅ Arquivo WXR gerado: {args.saida} ({len(posts)} post(s), status: {args.status})\n")
        for p in posts:
            print(f"  • {p['titulo']}  [{p['categoria']}]  → /{p['slug']}/")
        print("\nComo importar no WordPress:")
        print("  1. Painel > Ferramentas > Importar > WordPress (instale o importador se pedido)")
        print("  2. Envie este arquivo e atribua os posts ao seu usuário")
        print(f"  3. Os artigos entram como {'rascunho' if args.status == 'draft' else 'publicados'} — " )
        print("     substitua cada bloco destacado pelo cartão de produto com o SEU link de afiliado")


if __name__ == "__main__":
    main()
