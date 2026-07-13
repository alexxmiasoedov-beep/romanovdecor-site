import { json, isAuthed, unauthorized, genId, kvGetJson, kvPutJson, edgeJson, purgeApiCache } from '../_lib.js';

const KEY = 'portfolio:list';

export async function onRequestGet(context) {
  return edgeJson(context, 120, async () => {
    const items = await kvGetJson(context.env, KEY, []);
    return { ok: true, items };
  });
}

export async function onRequestPost(context) {
  if (!isAuthed(context)) return unauthorized();
  let body;
  try {
    body = await context.request.json();
  } catch (e) {
    return json({ ok: false, error: 'Неверный запрос' }, 400);
  }
  const items = await kvGetJson(context.env, KEY, []);
  const item = Object.assign({}, body, { id: genId(), createdAt: Date.now() });
  items.unshift(item);
  await kvPutJson(context.env, KEY, items);
  await purgeApiCache(context);
  return json({ ok: true, item });
}
