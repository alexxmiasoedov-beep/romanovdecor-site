import { json } from '../_lib.js';

export async function onRequestPost(context) {
  let body;
  try {
    body = await context.request.json();
  } catch (e) {
    return json({ ok: false, error: 'Неверный запрос' }, 400);
  }
  const password = (body && body.password) || '';
  if (context.env.ADMIN_PASSWORD && password === context.env.ADMIN_PASSWORD) {
    return json({ ok: true });
  }
  return json({ ok: false, error: 'Неверный пароль' }, 401);
}
