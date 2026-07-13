import { json } from '../_lib.js';

export async function onRequestPost(context) {
  let body;
  try {
    body = await context.request.json();
  } catch (e) {
    return json({ ok: false, error: 'Неверный запрос' }, 400);
  }
  const name = String((body && body.name) || '').trim();
  const phone = String((body && body.phone) || '').trim();
  const message = String((body && body.message) || '').trim();
  const source = String((body && body.source) || '').trim();

  if (!phone && !name) {
    return json({ ok: false, error: 'Укажите имя и телефон' }, 400);
  }

  const { TG_BOT_TOKEN, TG_CHAT_ID } = context.env;
  if (!TG_BOT_TOKEN || !TG_CHAT_ID) {
    return json({ ok: false, error: 'Сервис заявок не настроен' }, 500);
  }

  const lines = ['🔔 Новая заявка с сайта'];
  if (name) lines.push('👤 Имя: ' + name);
  if (phone) lines.push('📞 Телефон: ' + phone);
  if (message) lines.push('💬 Сообщение: ' + message);
  if (source) lines.push('📍 Откуда: ' + source);

  const resp = await fetch('https://api.telegram.org/bot' + TG_BOT_TOKEN + '/sendMessage', {
    method: 'POST',
    headers: { 'content-type': 'application/json' },
    body: JSON.stringify({ chat_id: TG_CHAT_ID, text: lines.join('\n') }),
  });
  if (!resp.ok) {
    return json({ ok: false, error: 'Не удалось отправить заявку, позвоните нам' }, 502);
  }
  return json({ ok: true });
}
