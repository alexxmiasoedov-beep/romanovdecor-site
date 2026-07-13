export const CORS = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Headers': 'Content-Type, X-Admin-Password',
  'Access-Control-Allow-Methods': 'GET, POST, DELETE, PUT, OPTIONS',
};

export function json(data, status = 200, extra = {}) {
  return new Response(JSON.stringify(data), {
    status,
    headers: { 'content-type': 'application/json; charset=utf-8', ...CORS, ...extra },
  });
}

export function unauthorized() {
  return json({ ok: false, error: 'Нет доступа' }, 401);
}

export function isAuthed(context) {
  const pwd = context.request.headers.get('X-Admin-Password') || '';
  return Boolean(context.env.ADMIN_PASSWORD) && pwd === context.env.ADMIN_PASSWORD;
}

export function genId() {
  return Date.now().toString(36) + Math.random().toString(36).slice(2, 8);
}

export async function kvGetJson(env, key, fallback) {
  try {
    const raw = await env.KV.get(key);
    if (raw == null) return fallback;
    return JSON.parse(raw);
  } catch (e) {
    return fallback;
  }
}

export async function kvPutJson(env, key, value) {
  await env.KV.put(key, JSON.stringify(value));
}

// --- edge-кэш для публичных GET API ---
// Ключ канонизируется (без query), чтобы GET и инвалидация из POST совпадали.
export function apiCacheKey(context, pathname) {
  const url = new URL(context.request.url);
  if (pathname) url.pathname = pathname;
  url.search = '';
  url.searchParams.set('vv', '1');
  return new Request(url.toString());
}

export async function edgeJson(context, ttl, build) {
  const cache = caches.default;
  const key = apiCacheKey(context);
  const hit = await cache.match(key);
  if (hit) return hit;
  const data = await build();
  const resp = json(data, 200, { 'cache-control': 'public, max-age=0, s-maxage=' + ttl });
  context.waitUntil(cache.put(key, resp.clone()));
  return resp;
}

export async function purgeApiCache(context, pathname) {
  try {
    await caches.default.delete(apiCacheKey(context, pathname));
  } catch (e) {}
}
