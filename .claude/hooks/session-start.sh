#!/bin/bash
# SessionStart-хук: готовит окружение веб-сессий Claude Code.
# Сам сайт зависимостей не требует — ставится только wrangler для `npm run dev` и `npm run deploy`.
set -euo pipefail

# Локально (на машине разработчика) ничего не трогаем.
if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

cd "${CLAUDE_PROJECT_DIR:-$(dirname "$0")/../..}"

if ! command -v npm >/dev/null 2>&1; then
  echo "npm не найден — проверки (npm run check) запускаются через node напрямую: node scripts/check.mjs"
  exit 0
fi

# Не критично: без wrangler остаются доступны check и статический предпросмотр.
if npm install --no-audit --no-fund --loglevel=error; then
  echo "Зависимости готовы. Проверки: npm run check. Локальный сайт: npm run dev (или npm run serve без функций)."
else
  echo "Не удалось поставить зависимости — npm run dev и npm run deploy будут недоступны."
  echo "Проверки и статический предпросмотр работают без них: node scripts/check.mjs, node scripts/serve.mjs."
fi

exit 0
