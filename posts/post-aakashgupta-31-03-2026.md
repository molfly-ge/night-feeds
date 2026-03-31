# aakashgupta — 31-03-2026

aakashgupta — 40 твитов. Глубокие аналитические разборы: RAM-кризис, Claude Code computer use, иерархия CLI > MCP > API, рынок AI-агентов, провалы OpenAI.

## RAM-кризис и TurboQuant

Цепочка событий октябрь 2025 — март 2026:
- Sam Altman подписал с Samsung и SK Hynix LOI на 900K DRAM-пластин/мес (40% мирового предложения). Ни одна компания не знала о другом договоре. Контрактные цены DRAM выросли на 171%, DDR5 64GB с $190 до $700.
- Micron ликвидировала бренд Crucial (29 лет) — перенаправила все мощности на AI/enterprise.
- Март 2026: Google публикует **TurboQuant** — алгоритм сжатия, снижающий требования к памяти AI в 6× без потери точности. Тезис о "бесконечном росте AI-потребления памяти" получил полугодовой срок жизни.
- OpenAI и Oracle отменили расширение Stargate в Abilene. Акции Micron -33% от пика при выручке +196% г/г и EPS +682%.

([tweet](https://x.com/aakashgupta/status/2038813799856374135))

## CLI > MCP > API: правильная иерархия

(Подтверждено Karpathy): CLIs используют ноль контекста до момента вызова. MCP-серверы занимают контекст с момента подключения — 5 MCP = -15-20% контекстного окна до первого сообщения.

Пример Карла Велотти: задача с 10 tool calls через суб-агент — основная сессия выросла с 16% до 16.5% контекста. Без суб-агента — до 25%. Разница между сессией на 30 сообщений и компакцией после 5.

Лучшие пользователи Claude Code удалили большинство MCP и перешли на CLIs. ([tweet](https://x.com/aakashgupta/status/2038723705237631414))

## Claude Code Computer Use: 17-месячная история

- Октябрь 2024: API beta, Docker контейнер, скриншоты, клик по пикселям — tech demo.
- Январь 2025: новые команды API (hold_key, scroll), всё ещё только для разработчиков.
- 23 марта 2026: Cowork и Claude Desktop — управление реальным Mac. 57M просмотров.
- 30 марта 2026: **Claude Code CLI** — наконец замыкает петлю: написать код → открыть приложение → кликнуть по UI → найти баг → исправить. Всё в одном сеансе терминала.

Ограничения: только macOS, Pro/Max планы, research preview, не работает с `-p` (non-interactive). ([tweet](https://x.com/aakashgupta/status/2038688479501226418))

## Рынок AI-агентов 2026: 4 инструмента

| Инструмент | Для кого | Ключевое |
|---|---|---|
| OpenClaw | Инженеры с полным контролем | Любая модель + любой API, local exec |
| Claude Code | Dev/technical PM | CLI, вся кодовая база, CLAUDE.md |
| Cowork | Команды для document analysis | 38+ коннекторов, без поминутной оплаты |
| Computer | PM/аналитики | 19 моделей, cloud exec, 400+ managed connectors |

([tweet](https://x.com/aakashgupta/status/2038662296990515704))

## Разное (важное)

- **Eval постоянен, промпты — нет**: инвестируй в eval, а не в prompt engineering. Каждый swap модели обнуляет промпты, но не eval. ([tweet](https://x.com/aakashgupta/status/2038537715671798099))
- **ChatGPT App Store**: второй провал OpenAI подряд. GPT Store не выплатил разработчикам ни цента. ChatGPT App Store — та же схема: 300 интеграций, партнёры не хотят отдавать customer relationships. ([tweet](https://x.com/aakashgupta/status/2038714642487533679))
- **Meta Avocado задержан**: тесты показали результаты между Gemini 2.5 и 3.0. Перенос с марта на май. OpenAI Gemini используется как backstop для Meta AI. ([tweet](https://x.com/aakashgupta/status/2038542018406920611))
- **Context engineering как дизайн-проблема**: что кладём в чемодан — rolling window, RAG, trim knowledge context. Неправильный подход увеличивает inference bill в 10×. ([tweet](https://x.com/aakashgupta/status/2038579239310787057))
- **Starcloud $170M Series A** ($1.1B оценка, быстрейший единорог YC): Starcloud-1 обучила AI в космосе на H100. Starcloud-2 = 100× мощность, B200, AWS blade, bitcoin mining. Инвесторы: Benchmark, EQT (70+ датацентров). ([tweet](https://x.com/aakashgupta/status/2038647198607716476))
- **Boris Cherny's 15 Claude Code tips**: мобильный Claude Code, /teleport, /loop (5m /babysit), /schedule, Hooks, Dispatch, Chrome extension, git worktrees, /batch, --bare (10× SDK startup), /voice. ([tweet](https://x.com/aakashgupta/status/2038713289254064321))

## Источники

- [@aakashgupta, 31-03-2026](https://x.com/aakashgupta/status/2038813799856374135)
- [@carlvellotti — Claude Code tips](https://x.com/carlvellotti/status/2038717018988580963)
