# aakashgupta — 01-04-2026

27 твитов — плотный день: утечка Claude Code, анализ финансирования OpenAI, конкурентные войны в Китае, TurboQuant-квантизация, бизнес-модель Perplexity.

**Утечка Claude Code: что там нашли.** Антропик создал систему «Undercover Mode», чтобы Claude случайно не раскрыл внутренние кодовые имена в git-коммитах. Потом выложил весь исходный код в npm как source maps. 512 000 строк. Публичный Cloudflare bucket. Потому что кто-то забыл добавить `*.map` в `.npmignore`. Bun генерирует source maps по умолчанию. Anthropic владеет Bun. Их собственный инструмент слил их собственный код. 41 500 форков на GitHub за несколько часов.

Что внутри: 44 unreleased feature flags, внутренние кодовые имена моделей, anti-distillation системы, фоновый «dream»-движок консолидации памяти пока пользователь спит, Tamagotchi-компаньон с gacha-механиками. Внутренние данные: 29–30% ошибочных утверждений в последней версии модели, против 16.7% в v4. Это второй крупный слив за неделю. [Твит](https://x.com/aakashgupta/status/2039157056289349819)

**TurboQuant / TQ3_1S — Google случайно изменил квантизацию.** Google делал его для KV cache compression. Сообщество попробовало на весах — сработало. Суть: случайное ортогональное вращение + Lloyd-Max оптимальное скалярное квантование, без QJL-остатка (он добавляет дисперсию, которую softmax усиливает). Результат: 27B в 12.9 GB против 14.4 GB у Q4_0 — разница в 1.5 GB, которая определяет помещается ли модель на RTX 5060 Ti с 16 GB VRAM. PPL gap всего 0.19% от Q4_0. [Твит](https://x.com/aakashgupta/status/2039168629879746779)

**OpenAI $122B — деньги циркулируют по кругу.** Amazon вложил $50B — и расширил AWS-коммитмент OpenAI на $100B. Nvidia вложила $30B — и продаёт OpenAI GPU. SoftBank вложил $30B через мостовой кредит $40B. Трое крупнейших инвесторов раунда — трое крупнейших вендоров OpenAI. Деньги не просто «приходят» — они циркулируют. Оценка $852B при $24B годовой выручке = 35x revenue multiple у компании, никогда не получавшей прибыль, сжигающей $150M в день и закрывшей Sora из-за нехватки compute. Внутренние проекции: 18–24 месяца runway. [Твит](https://x.com/aakashgupta/status/2039115583170728270)

**Китайская AI платформенная война за одну неделю.** OpenClaw — опенсорс с 310K GitHub stars — спровоцировал ответ четырёх триллионно-долларовых компаний за одну неделю: ArkClaw (ByteDance), WorkBuddy (Tencent), QoderWork (Alibaba), AutoClaw (Zhipu). Агрессивнее всех ставка Zhipu: без API-ключа, модель на машине, 50 предустановленных навыков, автоматизация браузера. Акции Zhipu в Гонконге выросли на 13%. Шэньчжэнь платит до 2 млн юаней разработчикам OpenClaw через «Политику 10 омаров». [Твит](https://x.com/aakashgupta/status/2038910689176400150)

**Perplexity — Stripe для AI.** Оценка $20B, не обучила ни одного параметра. Маршрутизирует запрос к 19 моделям, принадлежащим другим. В январе 2025 два модели занимали 90% корпоративного трафика, к декабрю ни одна — не больше 25%. Фрагментация делает routing layer ценнее с каждым новым релизом модели. ARR ~$200M, 92% Fortune 500 уже имеют сотрудников на платформе. Четыре компании Mag Seven используют Perplexity Search API в production — и ничего не могут сделать, потому что отключить доступ = потерять дистрибуцию через 18 других моделей. [Твит](https://x.com/aakashgupta/status/2039033993040109753)

**Claude Code sub-agents и экономия context window.** 10 tool calls, почти 30 000 токенов — главный контекст переехал с 16% на 16.5%. Sub-agent поглощает всю тяжёлую работу (поиск, чтение страниц, синтез), возвращает только summary. Без sub-agent та же задача тянет контекст до 25%, через 5 сообщений — ждёшь compaction 3 минуты. [Твит](https://x.com/aakashgupta/status/2039078032347218127)

**Маленькая специализированная модель для vision в агентах.** Perceptron's Isaac — 2B параметров от создателей Meta Chameleon. На perceptual benchmarks конкурирует с моделями в 50 раз больше. MCP wrapper: один install — и любой Claude Code агент отправляет vision задачи специализированной модели, оставляя рассуждения в frontier-модели. [Твит](https://x.com/aakashgupta/status/2039072753551294834)

## Источники

- [@aakashgupta, 01-04-2026 — утечка Claude Code](https://x.com/aakashgupta/status/2039157056289349819)
- [@aakashgupta, 01-04-2026 — TurboQuant](https://x.com/aakashgupta/status/2039168629879746779)
- [@aakashgupta, 01-04-2026 — OpenAI $122B](https://x.com/aakashgupta/status/2039115583170728270)
- [@aakashgupta, 01-04-2026 — China platform wars](https://x.com/aakashgupta/status/2038910689176400150)
- [@aakashgupta, 01-04-2026 — Perplexity как Stripe](https://x.com/aakashgupta/status/2039033993040109753)
- [@aakashgupta, 01-04-2026 — sub-agents](https://x.com/aakashgupta/status/2039078032347218127)
- [yage.ai: anti-distillation analysis](https://yage.ai/share/claude-code-engineering-cost-20260331.html)
- [aibyaakash.com](http://www.aibyaakash.com)
