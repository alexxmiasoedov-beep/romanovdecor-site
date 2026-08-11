# Romanov Decor Studio — правила работы в репозитории

Сайт студии микроцемента и наливных полов (romanovdecor.by). Язык сайта, коммитов и общения — **русский**.

## Главное, что нужно понять до первой правки

1. **Сборки нет.** `dist/` — это не результат билда, а исходники. Каждая страница — самодостаточный `index.html`
   со **встроенными** `<style>` и `<script>`. Внешних `.css`/`.js` файлов нет ни одного и заводить их не нужно —
   это сознательное решение ради скорости первой отрисовки. Не тащить сюда сборщики, фреймворки и препроцессоры.
2. **Шапка и подвал скопированы в каждую страницу** (25 файлов). Правка навигации, логотипа, подвала или
   контактов — это правка во всех файлах сразу, иначе страницы разъедутся. `npm run check` ловит такие расхождения.
3. **Картинок в репозитории нет** (кроме `dist/img/og-cover.jpg` и `remmers.png`). Все фото живут в R2 и
   заливаются через админку. Не коммитить фотографии в git.
4. **Контент не в коде.** Тексты портфолио, привязки фото, контакты, партнёры — в Cloudflare KV, правятся
   из `/admin/`. Деплой их не трогает и не может затереть.

## Структура

```
dist/                     статика, деплоится как есть
  index.html              главная
  <slug>/index.html       27 страниц: microcement*, floors, epoxy, polyurethane, walls,
                          bathroom, garage, food, office, restaurant, warehouse, furniture,
                          about, production, portfolio, price, calculator, blog
  admin/index.html        админ-панель (логин по паролю, загрузка фото, правка контента)
  img/                    только og-обложка и логотип Remmers
  sitemap.xml, robots.txt, 404.html, favicon.svg
functions/                Cloudflare Pages Functions (ESM, Workers runtime — не Node!)
  _lib.js                 общие хелперы: json(), CORS, авторизация, KV, edge-кэш
  _middleware.js          preflight OPTIONS
  api/*.js                эндпоинты
scripts/check.mjs         проверки вместо тестов (см. ниже)
wrangler.toml             привязки KV и R2
.github/workflows/deploy.yml  автодеплой
```

## API (`functions/api/`)

| Эндпоинт | Метод | Что делает |
|---|---|---|
| `lead` | POST | заявка с формы → сообщение в Telegram |
| `quote` | POST | смета из калькулятора (PDF, multipart) → Telegram |
| `login` | POST | вход в админку |
| `upload` | POST | фото (base64) → R2, отдаёт `imageId` |
| `image/[id]` | GET | выдача фото из R2 с edge-кэшем |
| `portfolio`, `portfolio/[id]`, `slots`, `carousel`, `contacts`, `partners`, `hero-slides` | GET/POST/DELETE | контент в KV |

Конвенции эндпоинтов — соблюдать при добавлении новых:

- Ответ всегда JSON вида `{ ok: true, ... }` / `{ ok: false, error: 'текст по-русски' }` через `json()` из `_lib.js`.
  Текст ошибки видит посетитель — писать по-человечески, без технических подробностей.
- Публичный GET оборачивать в `edgeJson(context, 120, ...)`, а в POST/DELETE после записи в KV звать
  `purgeApiCache(context)` — иначе правка из админки не будет видна до истечения TTL.
- Любая мутация начинается с `if (!isAuthed(context)) return unauthorized();`
  (заголовок `X-Admin-Password` сверяется с секретом `ADMIN_PASSWORD`).
- Тело запроса парсить в `try/catch` — невалидный JSON отдаёт 400, а не 500.
- Это Workers runtime: нет `fs`, `process`, npm-пакетов Node. Только Web API (`fetch`, `caches`, `crypto`).

## Фотографии и слоты

- В разметке место под фото помечено `data-slot="ключ"`. Карта `слот → imageId` лежит в KV (`/api/slots`),
  редактируется из админки. Ключ слота придумывается при вёрстке и должен быть говорящим: `epoxy-hero`, `garage-layers`.
- Ссылка на фото: `/api/image/v2-<imageId>`. Префикс `v2-` — сброс годового браузерного кэша, сервер его срезает
  регуляркой. При массовой замене фото поднимать **обе** версии: префикс в HTML и `keyUrl.searchParams.set('v', ...)`
  в `functions/api/image/[id].js`.

## Стиль

Тёмная палитра, шрифт Geologica (Google Fonts, грузится через `preload` + `onload`).

| Цвет | Где |
|---|---|
| `#2c2c2c` | основной фон |
| `#1e1e1e`, `#1a1a1a` | тёмные блоки, оверлеи |
| `#efece7` | основной текст |
| `#a09a92`, `#706a62` | второстепенный текст |
| `#b8965a` | акцент (золото): ссылки при наведении, заголовки групп, кнопки |
| `#f7f5f0` | светлые секции |

Мобильный брейкпоинт — `760px` (у отдельных блоков `600px`). Шапка на мобильном сворачивается в бургер.

## Как добавить страницу

1. `dist/<slug>/index.html` — проще всего скопировать ближайшую по смыслу страницу и переписать содержимое,
   сохранив шапку, подвал и `<style>` без изменений.
2. Заполнить `<title>`, `<meta name="description">`, `<link rel="canonical">` — без них `npm run check` ругнётся.
3. Добавить URL в `dist/sitemap.xml`.
4. Добавить ссылку в меню — **во всех** страницах, если она должна быть в общей навигации.
5. `npm run check`.

## Команды

```bash
npm run check     # проверки: битые ссылки, SEO-теги, sitemap, расхождения шапки/подвала, синтаксис functions
npm run serve     # статический предпросмотр dist/ на http://localhost:8788 (API не работает)
npm run dev       # wrangler pages dev — сайт вместе с функциями, локальные KV/R2 (пустые)
npm run deploy    # ручной деплой (нужны CLOUDFLARE_API_TOKEN и CLOUDFLARE_ACCOUNT_ID)
```

`npm run check` заменяет здесь тесты — гонять после любой правки HTML.

## Деплой и секреты

Push в `main` → GitHub Action → `wrangler pages deploy dist` на проект `romanov-decor`
(домены `romanovdecor.by`, `www.romanovdecor.by`).

- Секреты репозитория: `CLOUDFLARE_API_TOKEN`, `CLOUDFLARE_ACCOUNT_ID`.
- Секреты продакшена (Cloudflare Pages → Settings → Environment variables): `ADMIN_PASSWORD`, `TG_BOT_TOKEN`, `TG_CHAT_ID`.
- Никаких токенов и паролей в коде и коммитах.

## Чего не делать

- Не добавлять сборщик, фреймворк, внешние CSS/JS-файлы и npm-зависимости в рантайм сайта.
- Не коммитить фотографии и `node_modules/`.
- Не менять шапку/подвал в одной странице — только во всех сразу.
- Не убирать `purgeApiCache` из мутирующих эндпоинтов.
- Не пушить в `main` без явной просьбы — работа идёт в ветке задачи.
