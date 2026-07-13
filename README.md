# Romanov Decor Studio — romanovdecor.by

Сайт компании Romanov Decor Studio: микроцемент собственного производства и наливные полы в Минске.

## Структура

- `index.html` — главная страница
- Остальные страницы: `microcement.html`, `floors.html`, `walls.html`, `bathroom.html`, `price.html`, `portfolio.html`, `calculator.html`, `blog.html`, `about.html` и т.д.
- `img/` — изображения
- `favicon.svg` — иконка сайта

Все стили и скрипты встроены прямо в HTML-страницы, шрифты подгружаются с Google Fonts. Сборка не требуется — это полностью статический сайт.

## Деплой

Сайт публикуется через Cloudflare Pages, подключённый к этому репозиторию: каждый пуш в ветку `main` автоматически выкладывается на [romanovdecor.by](https://romanovdecor.by/) за ~1 минуту.

Ссылки на сайте используют «чистые» адреса без расширения (`/microcement`, `/price`) — Cloudflare Pages автоматически сопоставляет их с файлами `.html`.
