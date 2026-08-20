import { json } from '../_lib.js';

// Номер КП: дата ДДММГГ + порядковая буква за день (210826A, 210826B, …).
// Счётчик хранится в KV по ключу дня, чтобы номера не повторялись у разных
// посетителей. После Z идут AA, AB и так далее.
export async function onRequestPost(context) {
  const minsk = new Date(Date.now() + 3 * 3600 * 1000); // Минск = UTC+3
  const dd = String(minsk.getUTCDate()).padStart(2, '0');
  const mm = String(minsk.getUTCMonth() + 1).padStart(2, '0');
  const yy = String(minsk.getUTCFullYear() % 100).padStart(2, '0');
  const day = dd + mm + yy;

  const key = 'kpseq:' + day;
  let n = parseInt(await context.env.KV.get(key), 10) || 0;
  n += 1;
  await context.env.KV.put(key, String(n), { expirationTtl: 172800 });

  let letters = '';
  let v = n;
  while (v > 0) {
    v -= 1;
    letters = String.fromCharCode(65 + (v % 26)) + letters;
    v = Math.floor(v / 26);
  }
  return json({ ok: true, number: day + letters });
}
