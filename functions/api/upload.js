import { json, isAuthed, unauthorized, genId } from '../_lib.js';

export async function onRequestPost(context) {
  if (!isAuthed(context)) return unauthorized();
  let body;
  try {
    body = await context.request.json();
  } catch (e) {
    return json({ ok: false, error: 'Неверный запрос' }, 400);
  }
  const data = body && body.data;
  const mime = (body && body.mime) || 'image/jpeg';
  if (!data) return json({ ok: false, error: 'Нет данных файла' }, 400);

  let bytes;
  try {
    const bin = atob(data);
    bytes = new Uint8Array(bin.length);
    for (let i = 0; i < bin.length; i++) bytes[i] = bin.charCodeAt(i);
  } catch (e) {
    return json({ ok: false, error: 'Не удалось декодировать файл' }, 400);
  }

  const imageId = genId();
  await context.env.R2.put(imageId, bytes, { httpMetadata: { contentType: mime } });
  return json({ ok: true, imageId });
}
