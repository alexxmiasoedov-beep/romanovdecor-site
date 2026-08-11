#!/usr/bin/env node
// Статический предпросмотр dist/ без wrangler: node scripts/serve.mjs [порт]
// Отдаёт страницы как Cloudflare Pages: /about → dist/about/index.html.
// Запросы к /api/* здесь не работают — для них нужен `npm run dev`.

import { createServer } from 'node:http';
import { readFile, stat } from 'node:fs/promises';
import { join, extname, dirname, normalize } from 'node:path';
import { fileURLToPath } from 'node:url';

const DIST = join(dirname(fileURLToPath(import.meta.url)), '..', 'dist');
const PORT = Number(process.argv[2] || process.env.PORT || 8788);

const TYPES = {
  '.html': 'text/html; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.js': 'text/javascript; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.xml': 'application/xml; charset=utf-8',
  '.txt': 'text/plain; charset=utf-8',
  '.svg': 'image/svg+xml',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.png': 'image/png',
  '.webp': 'image/webp',
  '.ico': 'image/x-icon',
};

async function readIfFile(path) {
  try {
    if (!(await stat(path)).isFile()) return null;
    return await readFile(path);
  } catch {
    return null;
  }
}

createServer(async (req, res) => {
  const path = decodeURIComponent(new URL(req.url, 'http://localhost').pathname);
  // не выпускаем запрос за пределы dist/
  const safe = normalize(path).replace(/^(\.\.[/\\])+/, '');

  if (safe.startsWith('/api/')) {
    res.writeHead(501, { 'content-type': 'application/json; charset=utf-8' });
    res.end(JSON.stringify({ ok: false, error: 'Функции здесь не работают — запустите npm run dev' }));
    return;
  }

  const candidates = [join(DIST, safe), join(DIST, safe, 'index.html')];
  for (const candidate of candidates) {
    const body = await readIfFile(candidate);
    if (body) {
      res.writeHead(200, { 'content-type': TYPES[extname(candidate)] || 'application/octet-stream' });
      res.end(body);
      return;
    }
  }

  const notFound = await readIfFile(join(DIST, '404.html'));
  res.writeHead(404, { 'content-type': 'text/html; charset=utf-8' });
  res.end(notFound || 'Не найдено');
}).listen(PORT, () => {
  console.log(`Предпросмотр dist/ — http://localhost:${PORT}  (Ctrl+C чтобы остановить)`);
});
