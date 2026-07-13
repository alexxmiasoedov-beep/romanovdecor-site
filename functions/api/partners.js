import { json, isAuthed, unauthorized, kvGetJson, kvPutJson } from '../_lib.js';

const KEY = 'partners:list';

export async function onRequestGet(context) {
  const partners = await kvGetJson(context.env, KEY, []);
  return json({ ok: true, partners });
}

export async function onRequestPost(context) {
  if (!isAuthed(context)) return unauthorized();
  let body;
  try {
    body = await context.request.json();
  } catch (e) {
    return json({ ok: false, error: 'Неверный запрос' }, 400);
  }
  const partners = Array.isArray(body && body.partners) ? body.partners : [];
  await kvPutJson(context.env, KEY, partners);
  return json({ ok: true, partners });
}
