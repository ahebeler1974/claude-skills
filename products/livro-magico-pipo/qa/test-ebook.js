const { chromium } = require('playwright-core');
const path = require('path');

const EBOOK = 'file://' + require('path').resolve(__dirname, '../produto/livro-magico-pipo.html');
const OUT = './shots';

(async () => {
  const browser = await chromium.launch({ executablePath: process.env.CHROMIUM_PATH || '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
  const page = await browser.newPage({ viewport: { width: 390, height: 780 }, hasTouch: true });
  const erros = [];
  page.on('console', m => { if (m.type() === 'error') erros.push('CONSOLE: ' + m.text()); });
  page.on('pageerror', e => erros.push('PAGEERROR: ' + e.message));

  await page.goto(EBOOK);
  await page.waitForTimeout(800);
  await page.screenshot({ path: `${OUT}/00-capa.png` });

  // capa -> começar
  await page.tap('#btn-comecar', { force: true });
  await page.waitForTimeout(1200);
  await page.screenshot({ path: `${OUT}/01-ovos.png` });

  // quebrar os 3 ovos (2 toques cada)
  const ovos = await page.$$('.ovo-slot');
  for (const ovo of ovos) { await ovo.tap({ force: true }); await page.waitForTimeout(250); await ovo.tap({ force: true }); await page.waitForTimeout(350); }
  await page.waitForTimeout(1200);
  await page.screenshot({ path: `${OUT}/01-ovos-abertos.png` });

  // pintar
  await page.tap('#seta-prox', { force: true });
  await page.waitForTimeout(700);
  const dots = await page.$$('.dot-pintavel');
  console.log('bolinhas encontradas:', dots.length);
  for (const d of dots) { await d.tap({ force: true }); await page.waitForTimeout(120); }
  await page.waitForTimeout(900);
  await page.screenshot({ path: `${OUT}/02-pintar.png` });

  // piano
  await page.tap('#seta-prox', { force: true });
  await page.waitForTimeout(700);
  await page.screenshot({ path: `${OUT}/03-piano.png` });
  for (const t of await page.$$('.tecla')) { await t.tap({ force: true }); await page.waitForTimeout(150); }

  // circular o gato — desenha um círculo em volta do gato (canto inf. direito)
  await page.tap('#seta-prox', { force: true });
  await page.waitForTimeout(700);
  await page.screenshot({ path: `${OUT}/04-circular.png` });
  const q = await page.$('#quadro-circular');
  const bb = await q.boundingBox();
  const cx = bb.x + bb.width * 0.79, cy = bb.y + bb.height * 0.76, R = Math.min(bb.width, bb.height) * 0.18;
  await page.mouse.move(cx + R, cy);
  await page.mouse.down();
  for (let a = 0; a <= 380; a += 12) {
    const rad = a * Math.PI / 180;
    await page.mouse.move(cx + R * Math.cos(rad), cy + R * Math.sin(rad));
    await page.waitForTimeout(8);
  }
  await page.mouse.up();
  await page.waitForTimeout(1200);
  await page.screenshot({ path: `${OUT}/04-circular-feito.png` });

  // contar (3 rodadas: 2,3,5)
  await page.tap('#seta-prox', { force: true });
  await page.waitForTimeout(700);
  await page.screenshot({ path: `${OUT}/05-contar.png` });
  for (const rodada of [2, 3, 5]) {
    for (let i = 0; i < rodada; i++) {
      const alvo = await page.$(`.pintinho-contavel:not(.contado)`);
      if (alvo) { await alvo.tap({ force: true }); await page.waitForTimeout(300); }
    }
    await page.waitForTimeout(2600);
  }
  await page.screenshot({ path: `${OUT}/05-contar-fim.png` });

  // formas — arrastar cada peça pro slot
  await page.tap('#seta-prox', { force: true });
  await page.waitForTimeout(700);
  await page.screenshot({ path: `${OUT}/06-formas.png` });
  for (const tipo of ['circulo', 'quadrado', 'triangulo']) {
    const peca = await page.$(`.forma-peca[data-tipo="${tipo}"]`);
    const slot = await page.$(`.encaixe[data-tipo="${tipo}"]`);
    const bp = await peca.boundingBox(), bs = await slot.boundingBox();
    await page.mouse.move(bp.x + bp.width / 2, bp.y + bp.height / 2);
    await page.mouse.down();
    await page.mouse.move(bs.x + bs.width / 2, bs.y + bs.height / 2, { steps: 12 });
    await page.mouse.up();
    await page.waitForTimeout(400);
  }
  await page.waitForTimeout(900);
  await page.screenshot({ path: `${OUT}/06-formas-feito.png` });

  // música
  await page.tap('#seta-prox', { force: true });
  await page.waitForTimeout(700);
  await page.tap('#btn-cantar', { force: true });
  await page.waitForTimeout(4000);
  await page.screenshot({ path: `${OUT}/07-musica.png` });
  await page.waitForTimeout(22000); // deixa a música acabar

  // desenhar
  await page.tap('#seta-prox', { force: true });
  await page.waitForTimeout(700);
  const qd = await page.$('#quadro-desenho');
  const bd = await qd.boundingBox();
  await page.mouse.move(bd.x + 40, bd.y + 60);
  await page.mouse.down();
  for (let i = 0; i < 160; i++) {
    await page.mouse.move(
      bd.x + 40 + (i * 1.7) % (bd.width - 80),
      bd.y + 60 + Math.sin(i / 8) * 60 + i * 0.5
    );
  }
  await page.mouse.up();
  await page.waitForTimeout(1200);
  await page.screenshot({ path: `${OUT}/08-desenhar.png` });

  // diploma
  await page.tap('#seta-prox', { force: true });
  await page.waitForTimeout(700);
  await page.fill('#campo-nome', 'Helena');
  await page.tap('#btn-criar-diploma', { force: true });
  await page.waitForTimeout(1500);
  await page.screenshot({ path: `${OUT}/09-diploma.png` });

  const estrelas = await page.textContent('#conta-estrelas');
  console.log('ESTRELAS FINAIS:', estrelas, '(esperado: 9)');
  console.log('ERROS:', erros.length ? erros.join('\n') : 'nenhum');
  console.log('DETALHE:', await page.evaluate(() => JSON.stringify(S.estrelas)));
  await browser.close();
})().catch(e => { console.error('FALHA:', e.message); process.exit(1); });
