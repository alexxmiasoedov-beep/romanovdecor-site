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
