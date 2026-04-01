# dotey — 01-04-2026

22 твита — глубокий технический разбор утечки исходного кода Claude Code и обзор нового инструмента для поиска в видео.

**Утечка Claude Code: пошаговый разбор.** Не из-за bun — из-за ошибки разработчика (забытая строка в .npmignore). Dotey опубликовал трёхшаговый гайд по изучению кода:
1. Запустить утечку локально — код уже восстановлен сообществом [github.com/claude-code-best/claude-code](https://github.com/claude-code-best/claude-code) (910 лайков, 152 RT)
2. Анализировать функции: от входа до выхода, логировать API-запросы и ответы для понимания Agent Loop
3. Форкнуть и дорабатывать — лучший способ понять архитектуру [Твит](https://x.com/dotey/status/2039020301434909095)

**Три слоя anti-distillation в Claude Code.** Разбор от «утиного папы» из статьи на yage.ai:
- Слой 1: в API-ответы подмешиваются фиктивные tool calls. Обычных пользователей это не задевает — сервер фильтрует. Но тренировочные датасеты, собранные с API, получают загрязнённые данные.
- Слой 2: промежуточные рассуждения заменяются на краткое summary + криптографическую подпись. Полная цепочка мышления скрыта от внешних наблюдателей.
- Слой 3: отдельный JSON-протокол с версионным маркером, статистически изолированным от обычных API-запросов. Бонус — экономия ~4.5% output tokens.
[Статья yage.ai](https://yage.ai/share/claude-code-engineering-cost-20260331.html) [Твит](https://x.com/dotey/status/2039042306871906655)

**Почему Claude Code никогда не откроют.** Причины оставаться закрытыми: можно скрывать качество кода (один React-файл на несколько тысяч строк — норма, но открывать стыдно), добавлять скрытые фичи вроде anti-distillation, выпускать «новые» фичи которые уже готовы (например `/buddy` уже в коде, ждёт 1 апреля), быстро итерировать без code review. [Твит](https://x.com/dotey/status/2039151725680980209)

**axios@1.14.1 и axios@0.30.4 заражены.** Не первый такой случай с популярными npm-пакетами. Заражённые версии содержат Remote Access Trojan. [StepSecurity Blog](https://www.stepsecurity.io/blog/axios-compromised-on-npm-malicious-versions-drop-remote-access-trojan) [Твит](https://x.com/dotey/status/2038828715560534034)

**SentrySearch — поиск по видео естественным языком.** Опенсорс CLI: разрезает видео на перекрывающиеся фрагменты, кодирует их через Gemini Embedding API или локальный Qwen3-VL, хранит в ChromaDB. Поисковый запрос попадает в тот же векторный пространство — и сопоставляется с видеофрагментами напрямую, без OCR и описаний кадров. Стоимость индексации 1 часа: ~$2.84 через API или бесплатно на GPU с 24 GB VRAM. Специальная поддержка Tesla Dashcam: скорость, GPS, время на вырезанных клипах. [GitHub SentrySearch](https://github.com/xxxxxx) [Твит](https://x.com/dotey/status/2039147493355634989)

**Кодекс обучения по утечке:** смотреть изолированно от AI не стоит — лучше сразу форкать и реализовывать конкретные фичи, вроде `/buddy`. Это быстрее даёт понимание архитектуры. [Твит](https://x.com/dotey/status/2039173267018191155)

## Источники

- [claude-code-best (восстановленный код)](https://github.com/claude-code-best/claude-code)
- [yage.ai: три слоя anti-distillation](https://yage.ai/share/claude-code-engineering-cost-20260331.html)
- [StepSecurity: axios supply chain attack](https://www.stepsecurity.io/blog/axios-compromised-on-npm-malicious-versions-drop-remote-access-trojan)
- [@dotey, 01-04-2026 — шаг 1 разбора](https://x.com/dotey/status/2039020301434909095)
- [@dotey, 01-04-2026 — anti-distillation](https://x.com/dotey/status/2039042306871906655)
- [@dotey, 01-04-2026 — axios](https://x.com/dotey/status/2038828715560534034)
