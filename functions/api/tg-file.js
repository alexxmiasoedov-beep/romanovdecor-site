import { json, isAuthed, unauthorized, CORS } from '../_lib.js';

// Скачать файл из Телеграма по file_id (лимит Telegram — 20 МБ)
// GET /api/tg-file?id=<file_id>
export async function onRequestGet(context) {
  if (!isAuthed(context)) return unauthorized();
  const { TG_BOT_TOKEN } = context.env;
  if (!TG_BOT_TOKEN) return json({ ok: false, error: 'TG_BOT_TOKEN не задан' }, 500);

  const url = new URL(context.request.url);
  const id = url.searchParams.get('id');
  if (!id) return json({ ok: false, error: 'нужен параметр id' }, 400);

  const api = 'https://api.telegram.org/bot' + TG_BOT_TOKEN;
  const metaResp = await fetch(api + '/getFile?file_id=' + encodeURIComponent(id));
  const meta = await metaResp.json();
  if (!meta.ok) return json({ ok: false, error: meta.description || 'файл не найден' }, 502);

  const path = meta.result.file_path;
  const fileResp = await fetch('https://api.telegram.org/file/bot' + TG_BOT_TOKEN + '/' + path);
  if (!fileResp.ok) return json({ ok: false, error: 'не удалось скачать' }, 502);

  const name = url.searchParams.get('name') || path.split('/').pop();
  return new Response(fileResp.body, {
    headers: {
      'content-type': fileResp.headers.get('content-type') || 'application/octet-stream',
      'content-disposition': 'attachment; filename="' + name.replace(/"/g, '') + '"',
      ...CORS,
    },
  });
}

export function onRequestOptions() {
  return new Response(null, { headers: CORS });
}
