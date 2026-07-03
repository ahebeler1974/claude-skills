# QA — Teste end-to-end do Livro Mágico

Percorre as 10 páginas como uma criança faria (toques, círculo desenhado, arrastar de formas)
e verifica que as 9 estrelas são conquistáveis sem erros de console.

```bash
npm install playwright-core
mkdir -p shots
CHROMIUM_PATH=/caminho/para/chrome node test-ebook.js
# esperado: "ESTRELAS FINAIS: 9" e "ERROS: nenhum"
```
