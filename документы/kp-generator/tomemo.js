const { chromium } = require('playwright-core');
(async () => {
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const page = await browser.newPage();
  await page.goto('file://' + process.env.SC + '/kp/memo.html', { waitUntil: 'networkidle' });
  await page.waitForTimeout(600);
  console.log('высота:', await page.evaluate(() => document.body.scrollHeight), '(A4=1123)');
  await page.pdf({ path: process.env.SC + '/kp/Памятка-по-ценам.pdf', format: 'A4', printBackground: true });
  await browser.close();
})();
