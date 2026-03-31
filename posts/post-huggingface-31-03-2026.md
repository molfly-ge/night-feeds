# huggingface — 31-03-2026

huggingface — 8 твитов. Важные релизы: llama.cpp 100K звёзд, Transformers.js v4, модель-лидер рейтингов и вектор на self-hosted AI.

## Модели

- **Qwen3.5-27B fine-tuned на Claude-4.6-Opus** (distilled data, обучена через Unsloth): 3 недели подряд #1 на HuggingFace. Превосходит Sonnet 4.5 на SWE-bench Verified. Работает локально на 16GB в 4-bit или 32GB в 8-bit. ([tweet](https://x.com/Hesamation/status/2038642306434150427))

## Инфраструктура

- **llama.cpp достиг 100K звёзд**: Georgi Gerganov отмечает, что local LLM-агенты стали реальностью после выхода gpt-oss летом прошлого года. Прогнозирует, что 90% AI-агентов будут работать локально с llama.cpp в течение 3-6 месяцев. 1500+ контрибьюторов. ([tweet](https://x.com/ggerganov/status/2038632534414680223))
- **Transformers.js v4**: WebGPU backend (браузер, Node.js, Bun, Deno), 200+ архитектур, полный рефактор кодовой базы, значительный прирост производительности. ([tweet](https://x.com/xenovacom/status/2038610331417608691))

## Разработка с агентами

- Niels Rogge использовал Codex для вклада **VidEoMT** (SOTA-модель для video segmentation) в библиотеку Transformers. Описывает лучшие практики работы с coding agents для портирования моделей. ([tweet](https://x.com/NielsRogge/status/2038654071054426595))
- Clement Delangue (HuggingFace CEO): с демократизацией разработки через Cursor/Lovable/Claude дифференциация компаний сместилась к обучению собственных моделей. "Будьте строителями AI, а не пользователями API." Анонс auto-research поверх HuggingFace hub. ([tweet](https://x.com/ClementDelangue/status/2038649731404927202))
- **Microsoft multilingual embedding models**: новые мультиязычные embedding-модели, хорошие результаты по мнению сообщества. ([tweet](https://x.com/victormustar/status/2038537420669337997))

## Источники

- [@Hesamation, 30-03-2026](https://x.com/Hesamation/status/2038642306434150427)
- [@ggerganov — llama.cpp 100K](https://x.com/ggerganov/status/2038632534414680223)
- [@xenovacom — Transformers.js v4](https://x.com/xenovacom/status/2038610331417608691)
