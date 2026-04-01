# roundtablespace — 01-04-2026

Центральная история дня — утечка исходного кода Claude Code. 29 твитов, и примерно половина так или иначе касается этого события и вокруг него.

**Утечка Claude Code.** Исходник появился через source maps в npm-пакете — 512 000 строк, публичный Cloudflare bucket. [Интерактивный обзор кода](https://claude-code-info.vercel.app/) позволяет ходить по нему как по продукту. Внутри обнаружили 44 нереализованных feature flag: фоновые агенты 24/7, один Claude-оркестратор с несколькими worker-агентами, cron-расписание, голосовое управление, управление браузером через Playwright, «сон» агентов с само-возобновлением, персистентная память между сессиями. [Твит с описанием скрытых фич](https://x.com/roundtablespace/status/2038960753458438156)

**Ollama + MLX.** Ollama заработал на Apple Silicon через MLX — локальные агенты Claude Code, OpenClaw, Codex ускорились на Mac. [Твит](https://x.com/roundtablespace/status/2039119297771941904)

**GLM 5.1 — 744B модель без пейволла.** Zhipu убрали ограничение с 744B агентной модели, что делает её доступной в инструментах вроде Claude Code и Kilo Code. [Твит](https://x.com/roundtablespace/status/2039134397136535772)

**AutoClaw — локальный OpenClaw.** Инструмент запускает OpenClaw на собственной машине без API-ключа, данные не покидают устройство. [Твит](https://x.com/roundtablespace/status/2039126847259091001)

**GLM OCR — 0.9B модель #1 на OmniDocBench.** Zhipu выложили в опенсорс лучшую на данный момент OCR-модель: 94.62 балла, меньше гигабайта параметров, работает на edge-устройствах, понимает таблицы, формулы, печати. [Твит](https://x.com/roundtablespace/status/2039043800317001815)

**Polymarket + Claude.** Сразу несколько постов о случаях, когда Claude-бот торговал на Polymarket: $62 → $721 000, $1 000 → $23 100 за 48 часов. OpenClaw при этом слился в ноль. [Твит](https://x.com/roundtablespace/status/2039157046520479915)

**OpenAI поднял $122B.** Крупнейший венчурный раунд в истории при оценке $852B. [Твит](https://x.com/roundtablespace/status/2039104198294241736)

**Skill Seekers — слой данных для ИИ.** Один командой превращает документацию, репо, PDF или видео в структурированную базу знаний для экспорта в 16 платформ (Claude, Cursor, LangChain, Pinecone и др.). 12K GitHub stars, #3 в трендах. [GitHub](https://github.com/yusufkaraaslan/Skill_Seekers)

**AtomicChat — опенсорс альтернатива ChatGPT.** Локальные LLM + облачные модели + полный контроль над данными. [GitHub](https://github.com/AtomicBot-ai/Atomic-Chat)

**Claude логирует агрессию пользователей.** Когда злишься на Claude и пишешь об этом — он это фиксирует в аналитике как негативный сигнал. Не меняет поведения, просто записывает. [Твит](https://x.com/roundtablespace/status/2039111747936690483)

**Public API для агентов с доступом к рынку.** Регулятор открыл доступ для агентов, умеющих следить за рынком, управлять деньгами и совершать сделки. [Твит](https://x.com/roundtablespace/status/2039172145985589478)

**Oumi — сборка кастомной модели за часы, не месяцы.** Предлагает ускоренный путь к fine-tuning под конкретные задачи. [Твит](https://x.com/roundtablespace/status/2039164596049637661)

## Источники

- [claude-code-info.vercel.app](https://claude-code-info.vercel.app/)
- [Skill Seekers на GitHub](https://github.com/yusufkaraaslan/Skill_Seekers)
- [AtomicChat на GitHub](https://github.com/AtomicBot-ai/Atomic-Chat)
- [@roundtablespace, 01-04-2026 — утечка Claude Code](https://x.com/roundtablespace/status/2038960753458438156)
- [@roundtablespace, 01-04-2026 — скрытые фичи](https://x.com/roundtablespace/status/2038968303092220291)
- [@roundtablespace, 01-04-2026 — Ollama+MLX](https://x.com/roundtablespace/status/2039119297771941904)
- [@roundtablespace, 01-04-2026 — GLM 5.1](https://x.com/roundtablespace/status/2039134397136535772)
- [@roundtablespace, 01-04-2026 — AutoClaw](https://x.com/roundtablespace/status/2039126847259091001)
