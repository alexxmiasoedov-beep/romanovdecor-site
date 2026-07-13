import { json, isAuthed, unauthorized, kvGetJson, kvPutJson } from '../_lib.js';

const KEY = 'slots:map';

export async function onRequestGet(context) {
  const slots = await kvGetJson(context.env, KEY, {});
  return json({ ok: true, slots });
}

export async function onRequestPost(context) {
  if (!isAuthed(context)) return unauthorized();
  let body;
  try {
    body = await context.request.json();
  } catch (e) {
    return json({ ok: false, error: 'Неверный запрос' }, 400);
  }
  const key = body && body.key;
  if (!key) return json({ ok: false, error: 'Не указан ключ слота' }, 400);
  const value = (body && body.imageId) != null ? String(body.imageId) : '';
  const slots = await kvGetJson(context.env, KEY, {});
  if (value === '') {
    delete slots[key];
  } else {
    slots[key] = value;
  }
  await kvPutJson(context.env, KEY, slots);
  return json({ ok: true, slots });
}
