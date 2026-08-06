const { chromium } = require('playwright-core');
(async () => {
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const page = await browser.newPage();
  await page.goto('file://' + process.env.SC + '/kp/kp-evgeniy5.html', { waitUntil: 'networkidle' });
  await page.waitForTimeout(800);
  const h = await page.evaluate(() => document.body.scrollHeight);
  console.log('высота:', h, '(A4=1123)');
  await page.pdf({ path: process.env.SC + '/kp/КП-Евгений-микроцемент.pdf', format: 'A4', printBackground: true });
  await browser.close();
})();
