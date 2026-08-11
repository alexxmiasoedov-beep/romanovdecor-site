#!/usr/bin/env node
// Проверки сайта Romanov Decor Studio — заменяют тесты, которых у статики нет.
// Запуск: npm run check   (без зависимостей, только Node)
//
// Что проверяется:
//   1. внутренние ссылки ведут на существующие страницы и файлы
//   2. у каждой страницы есть title / description / canonical, canonical совпадает с адресом
//   3. sitemap.xml соответствует набору страниц
//   4. шапка и подвал не разъехались между страницами
//   5. functions/*.js синтаксически валидны
//   6. телефон одинаковый везде, где он зашит в разметку

import { readFileSync, readdirSync, statSync, existsSync } from 'node:fs';
import { execFileSync } from 'node:child_process';
import { join, relative, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = join(dirname(fileURLToPath(import.meta.url)), '..');
const DIST = join(ROOT, 'dist');
const FUNCTIONS = join(ROOT, 'functions');
const SITE = 'https://romanovdecor.by';

// Страницы, которых нет в навигации и которые не должны попадать в sitemap.
const SITEMAP_EXCLUDE = new Set(['/admin']);

// Страницы с намеренно своей вёрсткой шапки/подвала — не сравниваются с остальными.
// /calculator — отдельный инструмент с минимальной шапкой и ссылкой «← на сайт», подвала нет.
const LAYOUT_EXCLUDE = new Set(['/admin', '/calculator']);

const errors = [];
const warnings = [];
const fail = (check, msg) => errors.push({ check, msg });
const warn = (check, msg) => warnings.push({ check, msg });

// ---------- сбор файлов ----------

function walk(dir) {
  const out = [];
  for (const name of readdirSync(dir)) {
    const full = join(dir, name);
    if (statSync(full).isDirectory()) out.push(...walk(full));
    else out.push(full);
  }
  return out;
}

const allFiles = walk(DIST);
const pages = allFiles
  .filter((f) => f.endsWith('index.html'))
  .map((f) => ({
    file: f,
    rel: relative(ROOT, f),
    // '/'; '/about'; '/admin'
    url: '/' + relative(DIST, dirname(f)).split('\\').join('/'),
    html: readFileSync(f, 'utf8'),
  }))
  .map((p) => ({ ...p, url: p.url === '/.' ? '/' : p.url }))
  .sort((a, b) => a.url.localeCompare(b.url));

const publicPages = pages.filter((p) => !SITEMAP_EXCLUDE.has(p.url));

// ---------- 1. внутренние ссылки ----------

function linkTargets(html) {
  const out = new Set();
  const re = /(?:href|src)\s*=\s*"([^"]+)"/g;
  let m;
  while ((m = re.exec(html))) out.add(m[1]);
  return out;
}

function resolves(target) {
  const path = target.split('#')[0].split('?')[0];
  if (path === '' || path === '/') return true;
  const asFile = join(DIST, path);
  if (existsSync(asFile) && statSync(asFile).isFile()) return true;
  const asDir = join(DIST, path, 'index.html');
  return existsSync(asDir);
}

for (const page of pages) {
  for (const target of linkTargets(page.html)) {
    if (!target.startsWith('/')) continue; // внешние, mailto:, tel:, относительные data-url
    if (target.startsWith('/api/')) continue; // отдаётся функциями, файла нет
    if (target.startsWith('//')) continue; // протокол-относительные внешние
    if (!resolves(target)) fail('ссылки', `${page.rel}: битая ссылка ${target}`);
  }
}

// ---------- 2. SEO-теги ----------

const pick = (html, re) => {
  const m = html.match(re);
  return m ? m[1].trim() : '';
};

for (const page of publicPages) {
  const title = pick(page.html, /<title>([^<]*)<\/title>/i);
  const desc = pick(page.html, /<meta\s+name="description"\s+content="([^"]*)"/i);
  const canonical = pick(page.html, /<link\s+rel="canonical"\s+href="([^"]*)"/i);

  if (!title) fail('seo', `${page.rel}: нет <title>`);
  else if (title.length > 65) warn('seo', `${page.rel}: title длиннее 65 символов (${title.length})`);

  if (!desc) fail('seo', `${page.rel}: нет meta description`);
  else if (desc.length > 165) warn('seo', `${page.rel}: description длиннее 165 символов (${desc.length})`);

  if (!canonical) {
    fail('seo', `${page.rel}: нет canonical`);
  } else {
    const expected = page.url === '/' ? SITE + '/' : SITE + page.url;
    const norm = (u) => u.replace(/\/$/, '');
    if (norm(canonical) !== norm(expected)) {
      fail('seo', `${page.rel}: canonical ${canonical}, ожидался ${expected}`);
    }
  }
}

// дубли title и description между страницами — поисковики этого не любят
for (const [field, re] of [
  ['title', /<title>([^<]*)<\/title>/i],
  ['description', /<meta\s+name="description"\s+content="([^"]*)"/i],
]) {
  const seen = new Map();
  for (const page of publicPages) {
    const value = pick(page.html, re);
    if (!value) continue;
    if (!seen.has(value)) seen.set(value, []);
    seen.get(value).push(page.url);
  }
  for (const [value, urls] of seen) {
    if (urls.length > 1) warn('seo', `одинаковый ${field} на ${urls.join(', ')}: «${value.slice(0, 60)}…»`);
  }
}

// ---------- 3. sitemap.xml ----------

const sitemapPath = join(DIST, 'sitemap.xml');
if (!existsSync(sitemapPath)) {
  fail('sitemap', 'нет dist/sitemap.xml');
} else {
  const xml = readFileSync(sitemapPath, 'utf8');
  const listed = new Set(
    [...xml.matchAll(/<loc>([^<]+)<\/loc>/g)].map((m) => {
      const path = m[1].trim().replace(SITE, '');
      return path === '' || path === '/' ? '/' : path.replace(/\/$/, '');
    }),
  );
  const actual = new Set(publicPages.map((p) => p.url));

  for (const url of actual) if (!listed.has(url)) fail('sitemap', `страница ${url} не указана в sitemap.xml`);
  for (const url of listed) if (!actual.has(url)) fail('sitemap', `в sitemap.xml есть ${url}, но такой страницы нет`);
}

// ---------- 4. расхождения шапки и подвала ----------

function block(html, tag) {
  const m = html.match(new RegExp(`<${tag}[^>]*>[\\s\\S]*?<\\/${tag}>`, 'i'));
  return m ? m[0] : null;
}

// Пометка текущего пункта меню (class="act") законно отличается от страницы к странице.
const normalize = (s) =>
  s
    .replace(/\s+/g, ' ')
    .replace(/\s*class="([^"]*)"/g, (all, cls) => {
      const rest = cls
        .split(/\s+/)
        .filter((c) => c && c !== 'act' && c !== 'active')
        .join(' ');
      return rest ? ` class="${rest}"` : '';
    })
    .replace(/\s*aria-current="[^"]*"/g, '')
    .trim();

for (const [tag, label] of [
  ['header', 'шапка'],
  ['footer', 'подвал'],
]) {
  const variants = new Map();
  for (const page of pages) {
    if (LAYOUT_EXCLUDE.has(page.url)) continue;
    const b = block(page.html, tag);
    if (!b) {
      fail('разметка', `${page.rel}: нет <${tag}>`);
      continue;
    }
    const key = normalize(b);
    if (!variants.has(key)) variants.set(key, []);
    variants.get(key).push(page.url);
  }
  if (variants.size > 1) {
    const sorted = [...variants.entries()].sort((a, b) => b[1].length - a[1].length);
    const [majorityHtml, majorityUrls] = sorted[0];
    const hrefs = (s) => [...s.matchAll(/href="([^"]+)"/g)].map((m) => m[1]);
    const majorityHrefs = hrefs(majorityHtml);

    for (const [html, urls] of sorted.slice(1)) {
      const own = hrefs(html);
      const missing = majorityHrefs.filter((h) => !own.includes(h));
      const extra = own.filter((h) => !majorityHrefs.includes(h));
      const detail = [
        missing.length ? `нет ссылок: ${missing.join(', ')}` : '',
        extra.length ? `лишние ссылки: ${extra.join(', ')}` : '',
        !missing.length && !extra.length ? 'ссылки те же, отличается разметка' : '',
      ]
        .filter(Boolean)
        .join('; ');
      fail(
        'разметка',
        `${label} отличается от остальных ${majorityUrls.length} страниц на ${urls.join(', ')} — ${detail}`,
      );
    }
  }
}

// ---------- 5. синтаксис functions ----------

if (existsSync(FUNCTIONS)) {
  for (const file of walk(FUNCTIONS).filter((f) => f.endsWith('.js'))) {
    try {
      execFileSync(process.execPath, ['--check', file], { stdio: 'pipe' });
    } catch (e) {
      fail('functions', `${relative(ROOT, file)}: ${String(e.stderr || e).split('\n').slice(0, 3).join(' ')}`);
    }
  }
}

// ---------- 6. телефон ----------

const phones = new Map();
for (const page of pages) {
  for (const m of page.html.matchAll(/(?:tel:|"telephone":")(\+?[\d\s()-]{9,})/g)) {
    const digits = m[1].replace(/\D/g, '');
    if (!digits) continue;
    if (!phones.has(digits)) phones.set(digits, new Set());
    phones.get(digits).add(page.url);
  }
}
if (phones.size > 1) {
  warn(
    'контакты',
    'в разметке зашиты разные телефоны: ' +
      [...phones.entries()].map(([d, urls]) => `+${d} (${[...urls].join(', ')})`).join('; '),
  );
}

// ---------- отчёт ----------

const CHECKS = ['ссылки', 'seo', 'sitemap', 'разметка', 'functions', 'контакты'];
const byCheck = (list, name) => list.filter((i) => i.check === name);

console.log(`\nПроверка сайта: ${pages.length} страниц, ${walk(FUNCTIONS).length} файлов функций\n`);

for (const check of CHECKS) {
  const e = byCheck(errors, check);
  const w = byCheck(warnings, check);
  const icon = e.length ? '✗' : w.length ? '!' : '✓';
  console.log(`${icon} ${check}`);
  for (const { msg } of e) console.log(`    ошибка:  ${msg}`);
  for (const { msg } of w) console.log(`    замечание: ${msg}`);
}

console.log('');
if (errors.length) {
  console.log(`Ошибок: ${errors.length}, замечаний: ${warnings.length}\n`);
  process.exit(1);
}
console.log(`Ошибок нет, замечаний: ${warnings.length}\n`);
