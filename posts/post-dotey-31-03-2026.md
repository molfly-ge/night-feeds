# dotey — 31-03-2026

dotey — 13 твитов. Китайскоязычный аккаунт: глубокие разборы Codex-плагина, computer use в Claude Code, Feishu CLI и 15 функций Claude Code от Boris Cherny.

## OpenAI Codex-плагин для Claude Code

OpenAI официально вошла в экосистему конкурента. Плагин **codex-plugin-cc** превращает Codex в «второе мнение» прямо внутри Claude Code.

Три ключевые команды:
- `/codex:review` — read-only стандартный ревью
- `/codex:adversarial-review` — атакует скрытые предположения: миграции, auth-изменения, инфраструктурные скрипты
- `/codex:rescue` — передаёт задачу Codex-агенту при зависании потока

Все работают в фоне. Опциональный review gate блокирует Claude до завершения проверки, но может вызвать цикл двух агентов и сжечь квоту. Техническая реализация: через локальный Codex CLI и app server, переиспользует существующую auth и MCP-настройку. ([tweet](https://x.com/dotey/status/2038682622180634793))

## Computer Use в Claude Code

Anthropic добавила управление Mac-десктопом в Claude Code CLI. Цикл: написать Swift/Electron-код → скомпилировать → запустить → кликать кнопки → скриншот-верификация → исправить → повторить.

Режим включается через `/mcp` → computer-use сервер. Безопасность: каждое приложение требует отдельной авторизации, терминальные окна не скриншотятся, Esc прерывает, только одна сессия управляет экраном одновременно. Пока: только macOS, Pro/Max, не работает с `-p`. ([tweet](https://x.com/dotey/status/2038671395631108220))

## Feishu (Lark) CLI — AI-агентам в корпоративную среду

Feishu (аналог Notion/Slack) открыла **lark-cli**: AI-агент говорит одну фразу → выполняет цепочку корпоративных задач. Сообщение на собрание → создать задачи → разослать итоги.

Почему CLI, а не MCP: CLI самодокументируется (`--help`), поддерживает `--dry-run`, возвращает структурированный JSON, не занимает контекст постоянно. MCP — для сред без доступа к терминалу.

Установка: `npm install -g @larksuite/cli`. Ключевая идея для дизайнеров AI CLI: help как единственная документация, dry-run как безопасная сеть, ошибки с инструкцией следующего шага. ([tweet](https://x.com/dotey/status/2038406683865624800))

## review-swarm: 4 параллельных read-only агента

Skill от Thomas Ricouard (iOS/macOS разработчик, перешёл в OpenAI Codex): 4 специализированных агента запускаются параллельно по git diff:
1. Intent & Regression: неожиданный behavioral drift?
2. Security & Privacy: auth, injection, утечки данных
3. Performance & Reliability: горячие пути, race conditions, resource leaks
4. Contract & Coverage: API совместимость, тестовое покрытие

Вывод — приоритизированный список: "fix now / fix soon / optional". ([tweet](https://x.com/dotey/status/2038431616125530447) / источник)

## 15 недооценённых функций Claude Code (Boris Cherny)

Разбор от создателя Claude Code: мобильный Claude Code на iOS, `/teleport` (перенос сессии из терминала в облако), `/loop 5m /babysit` (автоматическое сопровождение PR к мержу), `/schedule` (задачи на неделю), Hooks (SessionStart, PreToolUse, Stop), `/btw` (вопрос без прерывания задачи), git worktrees (десятки параллельных агентов), `/batch` (тысячи параллельных воркфлоу), `--bare` (10× ускорение запуска SDK), `--add-dir` (работа с несколькими репозиториями), `/voice` (большинство кода Cherny пишет голосом). ([tweet](https://x.com/dotey/status/2038481514732691940))

## Источники

- [@dotey, 31-03-2026](https://x.com/dotey/status/2038808815883047340)
- [lark-cli (Feishu)](https://x.com/dotey/status/2038406683865624800)
