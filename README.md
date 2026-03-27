# night-feeds

Ежедневный автоматический дайджест Twitter-аккаунтов. Запускается каждую ночь в 06:00 по Екатеринбургу через Claude Code Remote Trigger.

## Что делает

Для каждого аккаунта из `list.txt`:
1. Забирает твиты за последние 24 часа через [twitter-cli](https://github.com/public-clis/twitter-cli)
2. Пишет саммари на русском (ясно, без жаргона) → `posts/post-{account}-{DD-MM-YYYY}.md`
3. Если нашёл упоминание инструмента/сервиса/API — создаёт карточку → `tools/{tool-name}.md`

После обхода всех аккаунтов:
4. Собирает агрегированный дайджест с топ-идеями и пересечениями тем → `digests/digest-{DD-MM-YYYY}.md`
5. Обновляет реестр всех дайджестов → `index.md`
6. Делает `git commit` и `git push`

## Структура

```
posts/    — саммари по каждому аккаунту
tools/    — карточки обнаруженных инструментов (не перезаписываются)
digests/  — агрегированный дайджест дня
index.md  — реестр всех дайджестов
list.txt  — список Twitter-аккаунтов (по одному URL на строку)
```

## Запуск

**Автоматически:** Remote Trigger `trig_01KwrzPAVMtqbe5Db4FbmQPk` — каждый день в 01:00 UTC (06:00 Екб).

**Вручную:** открыть репозиторий в Claude Code и написать: _"запусти pipeline из CLAUDE.md"_.

## Зависимости

- [twitter-cli](https://github.com/public-clis/twitter-cli) — `uv tool install twitter-cli`
- [ljg-skills](https://github.com/lijigang/ljg-skills/) — навыки `ljg-plain`, `ljg-card`
