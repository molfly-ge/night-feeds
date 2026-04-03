# huggingface — 03-04-2026

25 твитов за сутки.

Главная тема дня — **выход Gemma 4 от Google**. Практически все твиты посвящены этому событию:

**Gemma 4 — Apache 2.0 и локальный запуск.** Google выпустила Gemma 4 — самые мощные открытые модели на базе технологий Gemini 3. Ключевое изменение: переход на лицензию Apache 2.0 вместо проприетарной лицензии Google. Модели мультимодальные (текст, изображения, аудио), поддерживают 140 языков. [Анонс GoogleAI](https://x.com/GoogleAI/status/2039735543068504476) | [Обзор от osanseviero](https://x.com/osanseviero/status/2039736377181434329)

**Локальный запуск — центральный нарратив.** CEO Hugging Face Clement Delangue активно продвигает идею «future is local»: Gemma 4 работает на трёхлетнем Mac — бесплатно, безопасно, быстро. [Демо в браузере через WebGPU](https://huggingface.co/spaces/webml-community/Gemma-4-WebGPU) от @xenovacom — полностью приватно и бесплатно. [Твит](https://x.com/ClementDelangue/status/2039782910996148508)

**Интеграции и инструменты.** Day-0 поддержка в llama.cpp: команда `llama-server -hf ggml-org/gemma-4-26B-A4B-it-GGUF:Q4_K_M` для мгновенного запуска. [ggerganov показал работу](https://x.com/ggerganov/status/2039752638384709661) на Mac Studio M2 Ultra с MCP-поддержкой. Также доступна [GGUF-версия от Unsloth](https://huggingface.co/unsloth/gemma-4-31B-it-GGUF) (18.3 GB Q4KM). Поддержка в TRL для мультимодальных агентов. [Твит](https://x.com/ggerganov/status/2039744468899811419)

**Qwopus 27B v3** — третья итерация популярного файнтюна Qwen3.5-27B, дистиллированного из Claude 4.6 Opus. [Анонс](https://x.com/KyleHessling1/status/2039685136221118861)

Отдельно Clement Delangue высказался о **неправильности абстракции Git для ML-данных** — чекпоинты, состояния оптимизатора и логи тренировок не нуждаются в контроле версий, а нуждаются в быстром и дешёвом хранилище. [Твит](https://x.com/ClementDelangue/status/2039695447506210905)

## Источники

- [Gemma-4-WebGPU demo](https://huggingface.co/spaces/webml-community/Gemma-4-WebGPU)
- [gemma-4-31B-it (HF)](https://huggingface.co/google/gemma-4-31B-it)
- [gemma-4-31B-it-GGUF (Unsloth)](https://huggingface.co/unsloth/gemma-4-31B-it-GGUF)
- [@GoogleAI — анонс Gemma 4](https://x.com/GoogleAI/status/2039735543068504476)
- [@ClementDelangue — local is the future](https://x.com/ClementDelangue/status/2039749537250558337)
- [@ggerganov — llama.cpp demo](https://x.com/ggerganov/status/2039752638384709661)
- [@xenovacom — Gemma 4 in browser](https://x.com/xenovacom/status/2039741226337935430)
- [@natolambert — Apache 2.0 adoption](https://x.com/natolambert/status/2039736104052486326)
- [@ClementDelangue — Git for ML data](https://x.com/ClementDelangue/status/2039695447506210905)
