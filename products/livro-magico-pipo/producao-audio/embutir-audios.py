#!/usr/bin/env python3
"""
Embute os áudios profissionais (MP3) dentro do Livro Mágico do Pipo.

USO:
    python3 embutir-audios.py PASTA_COM_MP3S [saida.html]

- PASTA_COM_MP3S: pasta com os arquivos nomeados conforme o
  ROTEIRO-DE-GRAVACAO.md (ex.: tema.mp3, musica-pipo.mp3, voz-parabens.mp3...)
- O script lê produto/livro-magico-pipo.html, injeta os áudios em base64
  e grava livro-magico-pipo-com-audio.html (ou o nome que você passar).

O arquivo final continua sendo UM único HTML offline — só que agora com
voz natural e músicas de verdade. Arquivos ausentes não são problema:
o livro usa os sons sintetizados como reserva para o que faltar.
"""
import sys, os, base64, re

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    pasta = sys.argv[1]
    raiz = os.path.dirname(os.path.abspath(__file__))
    origem = os.path.join(raiz, '..', 'produto', 'livro-magico-pipo.html')
    destino = sys.argv[2] if len(sys.argv) > 2 else os.path.join(
        raiz, '..', 'produto', 'livro-magico-pipo-com-audio.html')

    html = open(origem, encoding='utf-8').read()
    MARCA = '/*__AUDIOS_EMBUTIDOS__*/'
    if MARCA not in html:
        print('ERRO: marcador de áudio não encontrado no HTML.')
        sys.exit(1)

    linhas, total = [], 0
    for nome in sorted(os.listdir(pasta)):
        if not nome.lower().endswith(('.mp3', '.m4a', '.ogg')):
            continue
        audio_id = os.path.splitext(nome)[0]
        if not re.fullmatch(r'[a-z0-9-]+', audio_id):
            print(f'  AVISO: "{nome}" ignorado (use só letras minúsculas, números e hífen)')
            continue
        dados = open(os.path.join(pasta, nome), 'rb').read()
        mime = {'mp3': 'audio/mpeg', 'm4a': 'audio/mp4', 'ogg': 'audio/ogg'}[nome.rsplit('.', 1)[1].lower()]
        b64 = base64.b64encode(dados).decode()
        linhas.append(f'AUDIO["{audio_id}"]="data:{mime};base64,{b64}";')
        total += len(dados)
        print(f'  ✔ {audio_id} ({len(dados)//1024} KB)')

    if not linhas:
        print('Nenhum áudio encontrado na pasta.')
        sys.exit(1)

    html = html.replace(MARCA, MARCA + '\n' + '\n'.join(linhas))
    open(destino, 'w', encoding='utf-8').write(html)
    print(f'\n✅ {len(linhas)} áudios embutidos ({total//1024} KB) → {os.path.abspath(destino)}')
    print('Teste o arquivo no celular e use-o como produto final no lugar do original.')

if __name__ == '__main__':
    main()
