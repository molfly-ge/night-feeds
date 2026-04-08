# CodexBar

macOS menubar-тулза для трекинга расходов на AI-кодинг от Peter Steinberger (steipete). 16 провайдеров в одном меню — Claude, Codex, Perplexity, OpenCode Go и др.

**В версии 0.20** (08-04-2026):
- Новые провайдеры: Perplexity и OpenCode Go
- Переключение Codex-аккаунтов без re-login
- Фикс инфляции claude token/cost из дублей
- Cost history мерджит session usage в provider history

**Базовая функциональность:**
- Multi-provider menu bar с per-provider toggles
- Session + weekly meters с reset countdowns
- Codex web dashboard enrichments (опционально): code review remaining, usage breakdown, credits history
- Local cost-usage scan для Codex+Claude (последние 30 дней)
- Provider status polling с incident-бейджами

## Ссылки

- [GitHub releases](https://github.com/steipete/CodexBar/releases)
- [Twitter — анонс 0.20](https://x.com/steipete/status/2041731875241066517)
