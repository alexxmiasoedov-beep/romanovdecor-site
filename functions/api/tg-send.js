import { json, isAuthed, unauthorized, CORS } from '../_lib.js';

// Отправить файл или текст в рабочий чат Телеграма, с сохранением имени файла.
// POST /api/tg-send   multipart: file=<файл>, name=<имя.pdf>, caption=<текст>
// POST /api/tg-send   multipart: caption=<текст>            — просто сообщение
export async function onRequestPost(context) {
  if (!isAuthed(context)) return unauthorized();
  const { TG_BOT_TOKEN, TG_CHAT_ID } = context.env;
  if (!TG_BOT_TOKEN || !TG_CHAT_ID) return json({ ok: false, error: 'Телеграм не настроен' }, 500);

  let form;
  try {
    form = await context.request.formData();
  } catch (e) {
    return json({ ok: false, error: 'Неверный запрос' }, 400);
  }

  const api = 'https://api.telegram.org/bot' + TG_BOT_TOKEN;
  const caption = (form.get('caption') || '').toString().slice(0, 1000);
  const file = form.get('file');

  if (file && typeof file !== 'string') {
    const name = (form.get('name') || file.name || 'file').toString();
    const tg = new FormData();
    tg.append('chat_id', String(TG_CHAT_ID));
    if (caption) tg.append('caption', caption);
    tg.append('document', file, name);
    const resp = await fetch(api + '/sendDocument', { method: 'POST', body: tg });
    const data = await resp.json();
    if (!data.ok) return json({ ok: false, error: data.description || 'ошибка отправки' }, 502);
    return json({ ok: true, sent: name });
  }

  if (!caption) return json({ ok: false, error: 'нечего отправлять' }, 400);
  const resp = await fetch(api + '/sendMessage', {
    method: 'POST',
    headers: { 'content-type': 'application/json' },
    body: JSON.stringify({ chat_id: TG_CHAT_ID, text: caption }),
  });
  const data = await resp.json();
  if (!data.ok) return json({ ok: false, error: data.description || 'ошибка отправки' }, 502);
  return json({ ok: true });
}

export function onRequestOptions() {
  return new Response(null, { headers: CORS });
}
