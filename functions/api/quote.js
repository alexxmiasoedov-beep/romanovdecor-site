import { json } from '../_lib.js';

export async function onRequestPost(context) {
  const { TG_BOT_TOKEN, TG_CHAT_ID } = context.env;
  if (!TG_BOT_TOKEN || !TG_CHAT_ID) {
    return json({ ok: false, error: 'Сервис заявок не настроен' }, 500);
  }

  let form;
  try {
    form = await context.request.formData();
  } catch (e) {
    return json({ ok: false, error: 'Неверный запрос' }, 400);
  }
  const pdf = form.get('pdf');
  let meta = {};
  try {
    meta = JSON.parse(form.get('meta') || '{}');
  } catch (e) {
    meta = {};
  }

  const lines = ['📄 Смета из калькулятора'];
  if (meta.name) lines.push('👤 Имя: ' + meta.name);
  if (meta.phone) lines.push('📞 Телефон: ' + meta.phone);
  if (meta.positions) lines.push('📋 Позиций: ' + meta.positions);
  if (meta.total) lines.push('💰 Итого: ' + Number(meta.total).toLocaleString('ru') + ' руб');
  if (meta.summary) lines.push('\n' + meta.summary);
  if (meta.message) lines.push('💬 Комментарий: ' + meta.message);
  if (meta.source) lines.push('📍 Откуда: ' + meta.source);
  // Telegram ограничивает caption 1024 символами
  const caption = lines.join('\n').slice(0, 1000);

  if (pdf && typeof pdf !== 'string') {
    const tgForm = new FormData();
    tgForm.append('chat_id', String(TG_CHAT_ID));
    tgForm.append('caption', caption);
    tgForm.append('document', pdf, 'romanov-decor-kp.pdf');
    const resp = await fetch('https://api.telegram.org/bot' + TG_BOT_TOKEN + '/sendDocument', {
      method: 'POST',
      body: tgForm,
    });
    if (!resp.ok) {
      return json({ ok: false, error: 'Не удалось отправить смету, позвоните нам' }, 502);
    }
    return json({ ok: true });
  }

  const resp = await fetch('https://api.telegram.org/bot' + TG_BOT_TOKEN + '/sendMessage', {
    method: 'POST',
    headers: { 'content-type': 'application/json' },
    body: JSON.stringify({ chat_id: TG_CHAT_ID, text: caption }),
  });
  if (!resp.ok) {
    return json({ ok: false, error: 'Не удалось отправить смету, позвоните нам' }, 502);
  }
  return json({ ok: true });
}
