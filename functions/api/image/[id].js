import { CORS, json } from '../../_lib.js';

export async function onRequestGet(context) {
  const id = context.params.id;
  if (!id) return json({ ok: false, error: 'Не указан ID' }, 400);
  const obj = await context.env.R2.get(id);
  if (!obj) return json({ ok: false, error: 'Не найдено' }, 404);
  const headers = {
    'content-type': (obj.httpMetadata && obj.httpMetadata.contentType) || 'image/jpeg',
    'cache-control': 'public, max-age=31536000, immutable',
    etag: obj.httpEtag,
    ...CORS,
  };
  return new Response(obj.body, { headers });
}
