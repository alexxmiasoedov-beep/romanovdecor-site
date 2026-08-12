import { json, isAuthed, unauthorized, CORS } from '../_lib.js';

// Список входящих сообщений бота: файлы, фото и текст.
// GET /api/tg-inbox            — последние сообщения
// GET /api/tg-inbox?offset=N   — подтвердить прочтение всего до N-1 и отдать остальное
export async function onRequestGet(context) {
  if (!isAuthed(context)) return unauthorized();
  const { TG_BOT_TOKEN } = context.env;
  if (!TG_BOT_TOKEN) return json({ ok: false, error: 'TG_BOT_TOKEN не задан' }, 500);

  const api = 'https://api.telegram.org/bot' + TG_BOT_TOKEN;
  const offset = new URL(context.request.url).searchParams.get('offset');
  const params = new URLSearchParams({ limit: '100', timeout: '0' });
  if (offset) params.set('offset', offset);

  const resp = await fetch(api + '/getUpdates?' + params.toString());
  const data = await resp.json();
  if (!data.ok) {
    // самая частая причина — на боте висит webhook, тогда getUpdates запрещён
    return json({ ok: false, error: data.description || 'Telegram отказал' }, 502);
  }

  const items = [];
  for (const up of data.result) {
    const msg = up.message || up.channel_post || up.edited_message;
    if (!msg) continue;
    const base = {
      update_id: up.update_id,
      date: msg.date,
      from: msg.from ? msg.from.username || msg.from.first_name : null,
      chat_id: msg.chat ? msg.chat.id : null,
      caption: msg.caption || msg.text || '',
    };
    if (msg.document) {
      items.push({ ...base, kind: 'document', file_id: msg.document.file_id,
        name: msg.document.file_name, size: msg.document.file_size, mime: msg.document.mime_type });
    } else if (msg.photo && msg.photo.length) {
      const p = msg.photo[msg.photo.length - 1];
      items.push({ ...base, kind: 'photo', file_id: p.file_id, name: 'photo.jpg', size: p.file_size });
    } else if (msg.video) {
      items.push({ ...base, kind: 'video', file_id: msg.video.file_id,
        name: msg.video.file_name || 'video.mp4', size: msg.video.file_size });
    } else if (msg.voice) {
      items.push({ ...base, kind: 'voice', file_id: msg.voice.file_id, name: 'voice.ogg', size: msg.voice.file_size });
    } else if (msg.text) {
      items.push({ ...base, kind: 'text' });
    }
  }

  const last = data.result.length ? data.result[data.result.length - 1].update_id : null;
  return json({ ok: true, count: items.length, last_update_id: last, items });
}

export function onRequestOptions() {
  return new Response(null, { headers: CORS });
}
