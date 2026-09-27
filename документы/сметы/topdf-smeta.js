// Печать многостраничной сметы: SC=<папка с kp/smeta.html> NODE_PATH=/opt/node22/lib/node_modules node topdf-smeta.js
const { chromium } = require('playwright');
const SC = process.env.SC;
(async () => {
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const page = await browser.newPage({ viewport: { width: 794, height: 1123 }, deviceScaleFactor: 2 });
  await page.goto(`file://${SC}/kp/smeta.html`, { waitUntil: 'networkidle' });
  await page.waitForTimeout(1200);
  const hs = await page.evaluate(() => [...document.querySelectorAll('body > div')].map(d => [d.offsetHeight, d.scrollHeight]));
  console.log('pages (height, content):', JSON.stringify(hs));
  await page.screenshot({ path: `${SC}/smeta-prev.png`, fullPage: true });
  await page.pdf({ path: `${SC}/kp/smeta.pdf`, format: 'A4', printBackground: true });
  await browser.close();
})();
