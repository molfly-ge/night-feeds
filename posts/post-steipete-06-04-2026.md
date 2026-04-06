# steipete — 06-04-2026

40 твитов за сутки. Питер Штайнбергер (создатель OpenClaw) активно обсуждает блокировку со стороны Anthropic, работает над улучшением KV-кэширования и переключается на GPT как основную модель для OpenClaw.

**Anthropic блокирует OpenClaw через first-party harness** — главный твит дня (4200+ лайков, 1M+ просмотров): Anthropic теперь блокирует даже использование собственного CLI `claude -p` с упоминанием OpenClaw в system prompt. Ответ 400: «Third-party apps now draw from your extra usage, not your plan limits». Питер констатирует: «bring your own coin». [Твит](https://x.com/steipete/status/2040811558427648357)

**Отказ от фичи Claude-подписки в OpenClaw** — подтвердил, что Anthropic целенаправленно блокирует именно OpenClaw, хотя по документации first-party harness должен быть разрешён. Фичу пришлось убрать. [Твит](https://x.com/steipete/status/2040925717144252694)

**Переход на GPT** — «I made GPT really good today and switched. Opus is still funnier, but got close and GPT is more reliable.» OpenClaw теперь хорошо работает с GPT, Opus пока смешнее, но GPT стабильнее. Упоминает GPT 5.4 как рекомендацию вместо старых Codex-моделей. [Твит](https://x.com/steipete/status/2040918087881441336)

**Улучшение KV-кэширования** — следующее обновление OpenClaw значительно улучшит KV caching, что прямо отвечает на критику перерасхода токенов. [Твит](https://x.com/steipete/status/2040991162828292230)

**Мультимодельная поддержка** — OpenClaw работает с MiniMax, Kimi, GLM, Xiaomi и другими. «Pretty much all except Anthropic do» — все провайдеры, кроме Anthropic, поддерживают сторонние harness-ы. [Твит](https://x.com/steipete/status/2040977742376689867)

**AI-тестирование вместо e2e** — «Brainstormed with codex and it... just works. Way better than old-school e2e tests.» Построил систему тестирования за 6 часов с помощью Codex, результат лучше классических e2e-тестов. [Твит](https://x.com/steipete/status/2040894356106747912)

**Эмоции в GPT** — «It took a hammer, but I managed to beat emotions into GPT.» Доработал системный промпт для эмоционального поведения модели, пользователи отмечают «old claude vibes». [Твит](https://x.com/steipete/status/2040982273193869671)

**Грядущие фичи** — видео и аудио возможности для OpenClaw пока отсутствуют, но интеграция с Runway упоминается как «coming rn». Следующий системный промпт будет значительно лучше. [Твит](https://x.com/steipete/status/2040827914350997606)

## Источники

- [@steipete о блокировке Claude](https://x.com/steipete/status/2040811558427648357)
- [Отказ от фичи Claude-подписки](https://x.com/steipete/status/2040925717144252694)
- [Переход на GPT](https://x.com/steipete/status/2040918087881441336)
- [Улучшение KV-кэширования](https://x.com/steipete/status/2040991162828292230)
- [Мультимодельная поддержка](https://x.com/steipete/status/2040977742376689867)
- [AI-тестирование](https://x.com/steipete/status/2040894356106747912)
- [Эмоции в GPT](https://x.com/steipete/status/2040982273193869671)
