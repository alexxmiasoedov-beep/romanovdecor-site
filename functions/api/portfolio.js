import { json, isAuthed, unauthorized, genId, kvGetJson, kvPutJson } from '../_lib.js';

const KEY = 'portfolio:list';

export async function onRequestGet(context) {
  const items = await kvGetJson(context.env, KEY, []);
  return json({ ok: true, items });
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
  return json({ ok: true, item });
}
