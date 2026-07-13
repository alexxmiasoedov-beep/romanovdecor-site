# Romanov Decor Studio — romanovdecor.by

Сайт студии микроцемента и наливных полов. Хостится на **Cloudflare Pages** (проект `romanov-decor`, домены `romanovdecor.by`, `www.romanovdecor.by`, `romanov-decor.pages.dev`).

## Структура

- `dist/` — статические страницы сайта (каждая страница — папка со своим `index.html`)
- `dist/admin/` — админ-панель (портфолио, фото-слоты, карусель, контакты, партнёры)
- `functions/` — серверные функции Cloudflare Pages Functions:
  - `api/lead` — заявки с форм → Telegram
  - `api/quote` — сметы из калькулятора (PDF) → Telegram
  - `api/login`, `api/upload`, `api/image/*` — вход в админку и загрузка/выдача фото (хранятся в R2)
  - `api/portfolio`, `api/slots`, `api/carousel`, `api/contacts`, `api/partners`, `api/hero-slides` — контент, редактируемый из админки (хранится в KV)
- `wrangler.toml` — конфигурация деплоя (привязки KV и R2)
- `.github/workflows/deploy.yml` — автодеплой: каждый push в `main` выкладывает сайт на Cloudflare

## Автодеплой

Workflow использует два секрета репозитория (Settings → Secrets and variables → Actions):

- `CLOUDFLARE_API_TOKEN` — API-токен Cloudflare с правом «Cloudflare Pages — Edit»
- `CLOUDFLARE_ACCOUNT_ID` — ID аккаунта Cloudflare

## Данные

Контент (тексты портфолио, привязки фото, контакты) живёт в Cloudflare KV, фотографии — в R2-бакете `romanov-decor-images`. Деплой кода их не затрагивает.

Секреты окружения продакшена (задаются в Cloudflare Pages → Settings → Environment variables): `ADMIN_PASSWORD`, `TG_BOT_TOKEN`, `TG_CHAT_ID`.

## Локальный деплой вручную

```bash
export CLOUDFLARE_API_TOKEN=...
export CLOUDFLARE_ACCOUNT_ID=...
npx wrangler pages deploy dist --project-name=romanov-decor --branch=main
```
