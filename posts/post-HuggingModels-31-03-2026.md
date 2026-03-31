# HuggingModels — 31-03-2026

HuggingModels — 20 твитов. Новые модели на HuggingFace и переход от промпт-запросов к самоподдерживающимся AI-системам.

## CreaoAI: AI как инфраструктура, а не инструмент

Ключевая идея: AI перестал останавливаться на ответах — теперь строит системы, которые продолжают работать. Пример: мониторинг HuggingFace-модели → при новой версии: лог в Google Sheets + пинг в Slack. AI построил scraper, подключил оба инструмента и зафиксировал как App. Инфраструктура работает в фоне без повторных промптов. ([tweet](https://x.com/HuggingModels/status/2038644179300126756))

## Новые модели

- **Qwen3.5-35B-A3B-GPTQ-Int4**: мультимодальная vision-language модель, 4-bit квантизация, Apache 2.0, ~300K загрузок, совместима с Azure. ([tweet](https://x.com/HuggingModels/status/2038639926494065081))
- **Qwen3.5-397B-A17B-GPTQ-Int4**: 397B параметров, MoE архитектура, 4-bit (4× меньше памяти с сохранением качества). Apache 2.0. ([tweet](https://x.com/HuggingModels/status/2038413423399334231))
- **Qwen3.5-27B-GPTQ-Int4**: VLM, endpoint compatible, Azure-ready. ([tweet](https://x.com/HuggingModels/status/2038420978775257287))
- **Uncensored 20B GGUF code model**: без цензуры, для кодогенерации, работает локально на потребительском железе, 60K+ загрузок. ([tweet](https://x.com/HuggingModels/status/2038405894384566448))

## Источники

- [@HuggingModels, 30-03-2026](https://x.com/HuggingModels/status/2038644179300126756)
