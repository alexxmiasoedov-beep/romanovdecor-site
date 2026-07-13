import { json, isAuthed, unauthorized, kvGetJson, kvPutJson } from '../_lib.js';

const KEY = 'contacts:data';
const FIELDS = ['phone', 'email', 'address', 'hours', 'telegram', 'viber', 'instagram'];

export async function onRequestGet(context) {
  const def = {};
  FIELDS.forEach((f) => (def[f] = ''));
  const contacts = await kvGetJson(context.env, KEY, def);
  return json({ ok: true, contacts });
}

export async function onRequestPost(context) {
  if (!isAuthed(context)) return unauthorized();
  let body;
  try {
    body = await context.request.json();
  } catch (e) {
    return json({ ok: false, error: 'Неверный запрос' }, 400);
  }
  const contacts = {};
  FIELDS.forEach((f) => (contacts[f] = String((body && body[f]) || '')));
  await kvPutJson(context.env, KEY, contacts);
  return json({ ok: true, contacts });
}
