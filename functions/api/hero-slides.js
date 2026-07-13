import { json, isAuthed, unauthorized, kvGetJson, kvPutJson } from '../_lib.js';

const KEY = 'hero:slides';

export async function onRequestGet(context) {
  const slides = await kvGetJson(context.env, KEY, []);
  return json({ ok: true, slides });
}

export async function onRequestPost(context) {
  if (!isAuthed(context)) return unauthorized();
  let body;
  try {
    body = await context.request.json();
  } catch (e) {
    return json({ ok: false, error: 'Неверный запрос' }, 400);
  }
  const slides = Array.isArray(body && body.slides) ? body.slides : [];
  await kvPutJson(context.env, KEY, slides);
  return json({ ok: true, slides });
}
