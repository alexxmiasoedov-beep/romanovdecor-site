import { json, isAuthed, unauthorized, kvGetJson, kvPutJson, edgeJson, purgeApiCache } from '../_lib.js';

const KEY = 'carousel:slides';

export async function onRequestGet(context) {
  return edgeJson(context, 120, async () => {
    const slides = await kvGetJson(context.env, KEY, []);
    return { ok: true, slides };
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
  const slides = Array.isArray(body && body.slides) ? body.slides : [];
  await kvPutJson(context.env, KEY, slides);
  await purgeApiCache(context);
  return json({ ok: true, slides });
}
