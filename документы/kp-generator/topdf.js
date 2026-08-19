// Печать HTML в PDF. Один скрипт на все документы.
//
//   npm i playwright-core
//   export SC=/путь/к/рабочей/папке
//   python3 build_memo_manager.py
//   node topdf.js memo-manager "Прайс-под-ключ"
//
// Первый аргумент — имя html без расширения в $SC/kp/,
// второй — имя pdf без расширения там же.
// Третий аргумент --shot дополнительно кладёт рядом png для проверки вёрстки.
const { chromium } = require('playwright-core');

const SC = process.env.SC || '/tmp/kp';
const src = process.argv[2] || 'memo-manager';
const out = process.argv[3] || src;
const shot = process.argv.includes('--shot');

(async () => {
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const page = await browser.newPage({
    viewport: { width: 794, height: 1123 },   // A4 в CSS-пикселях
    deviceScaleFactor: 2,
  });
  await page.goto(`file://${SC}/kp/${src}.html`, { waitUntil: 'networkidle' });
  await page.waitForTimeout(800);             // ждём подгрузку Geologica

  const h = await page.evaluate(() => document.body.scrollHeight);
  console.log(`высота: ${h} (A4 = 1123)${h === 1123 ? '' : '  ← вёрстка не сходится'}`);

  if (shot) await page.screenshot({ path: `${SC}/${src}-prev.png`, fullPage: true });
  await page.pdf({ path: `${SC}/kp/${out}.pdf`, format: 'A4', printBackground: true });
  await browser.close();
})();
