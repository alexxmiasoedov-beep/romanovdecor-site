import { json, isAuthed, unauthorized, kvGetJson, kvPutJson, purgeApiCache } from '../../_lib.js';

const KEY = 'portfolio:list';

export async function onRequestPut(context) {
  if (!isAuthed(context)) return unauthorized();
  const id = context.params.id;
  let body;
  try {
    body = await context.request.json();
  } catch (e) {
    return json({ ok: false, error: 'Неверный запрос' }, 400);
  }
  const items = await kvGetJson(context.env, KEY, []);
  const idx = items.findIndex((it) => it.id === id);
  if (idx === -1) return json({ ok: false, error: 'Проект не найден' }, 404);
  items[idx] = Object.assign({}, items[idx], body, {
    id: items[idx].id,
    createdAt: items[idx].createdAt,
  });
  await kvPutJson(context.env, KEY, items);
  await purgeApiCache(context, '/api/portfolio');
  return json({ ok: true, item: items[idx] });
}

export async function onRequestDelete(context) {
  if (!isAuthed(context)) return unauthorized();
  const id = context.params.id;
  const items = await kvGetJson(context.env, KEY, []);
  const next = items.filter((it) => it.id !== id);
  if (next.length === items.length) return json({ ok: false, error: 'Проект не найден' }, 404);
  await kvPutJson(context.env, KEY, next);
  await purgeApiCache(context, '/api/portfolio');
  return json({ ok: true });
}
