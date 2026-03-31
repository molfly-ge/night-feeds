# axiaisacat — 31-03-2026

axiaisacat — 7 твитов. Китайскоязычный аккаунт: Codex-плагин для Claude Code, маркетинговые навыки и YouTube-автоматизация.

## Codex Plugin для Claude Code

OpenAI официально выпустила плагин **codex-plugin-cc** для Claude Code — Codex теперь встроен прямо в рабочий процесс конкурента. Установка:

```
/plugin marketplace add openai/codex-plugin-cc
/plugin install codex@openai-codex
/reload-plugins
/codex:setup
```

Команды:
- `/codex:review` — стандартный code review (read-only)
- `/codex:adversarial-review` — атакующее ревью: проверяет скрытые предположения, race conditions, security риски
- `/codex:rescue` — делегирует задачу Codex как суб-агенту, работает в фоне
- `/codex:status` / `/codex:cancel` / `/codex:result` — управление задачами
- Опциональный review gate: не выпускает Claude из сессии пока Codex не завершил проверку

Требует: ChatGPT-подписку (включая бесплатную) или OpenAI API key + Node.js 18.18+. ([tweet](https://x.com/axiaisacat/status/2038808690619207712))

## ai-marketing-skills — маркетинг с инженерным подходом

Open-source библиотека Claude Code навыков для маркетинга от Single Brain: проверена в реальном бизнесе с результатами в миллионы долларов.

6 модулей: Growth Engine (A/B-тесты с bootstrap CI и Mann-Whitney U), Sales Pipeline, Content Ops, Outbound, SEO, Finance Automation.

Примечательно: ICP Learner автоматически переписывает профиль идеального клиента на основе реальных побед/потерь; Expert Panel оценивает контент несколькими persona-экспертами до 90+/100. ([tweet](https://x.com/axiaisacat/status/2038542054704214348))

## YouTube Auto Pipeline

Один промпт → готовое YouTube-видео без участия человека: поиск темы на Reddit/Google Trends/TikTok → скрипт → AI-картинки → голос → субтитры → фоновая музыка → обложка → загрузка.

78 тестов, resume-after-crash, full-chain retry. ([tweet](https://x.com/axiaisacat/status/2038533942328914324))

## Источники

- [@axiaisacat, 31-03-2026](https://x.com/axiaisacat/status/2038808690619207712)
