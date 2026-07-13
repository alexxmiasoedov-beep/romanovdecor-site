import { CORS, json } from '../../_lib.js';

export async function onRequestGet(context) {
  let id = context.params.id;
  if (!id) return json({ ok: false, error: 'Не указан ID' }, 400);
  // версионный префикс в пути (v2-...) — сброс годового браузерного кэша при массовой замене картинок
  id = id.replace(/^v\d+-/, '');

  // Кэш на границе Cloudflare: картинки неизменяемые, origin дёргаем один раз
  const cache = caches.default;
  const keyUrl = new URL(context.request.url);
  keyUrl.searchParams.set('v', '3'); // версия кэша: поднять при массовой замене картинок
  const cacheKey = new Request(keyUrl.toString());
  const cached = await cache.match(cacheKey);
  if (cached) return cached;

  const obj = await context.env.R2.get(id);
  if (!obj) return json({ ok: false, error: 'Не найдено' }, 404);
  const headers = {
    'content-type': (obj.httpMetadata && obj.httpMetadata.contentType) || 'image/jpeg',
    'cache-control': 'public, max-age=31536000, immutable',
    etag: obj.httpEtag,
    ...CORS,
  };
  const resp = new Response(await obj.arrayBuffer(), { headers });
  context.waitUntil(cache.put(cacheKey, resp.clone()));
  return resp;
}
