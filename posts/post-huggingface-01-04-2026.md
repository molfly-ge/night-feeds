# huggingface — 01-04-2026

2 твита — модель уровня Claude Opus на 16 GB VRAM и выход TRL v1.0.

**27B-модель бьёт Claude Sonnet 4.5 на SWE-bench, помещается в 16 GB VRAM.** TQ3_1S (TurboQuant) — новый формат квантизации, изначально разработанный Google для KV cache compression. Сообщество обнаружило, что он работает и на весах модели: 27B в 12.9 GB против 14.4 GB у Q4_0, разница 0.19% по PPL. Это 1.5 GB, которые решают, помещается модель на карту или нет. На 16 GB RTX 5060 Ti: рассуждение уровня Claude 4 Opus, v2 урезает chain-of-thought bloat на 24% при 96.91% HumanEval. [Твит](https://x.com/huggingface/status/2038917359260623229)

**TRL v1.0 вышел.** Стабильные API, широкие интеграции, архитектура, рассчитанная на будущие изменения в области. [Блог HF](http://hf.co/blog/trl-v1) [Твит](https://x.com/huggingface/status/2039000031949165005)

## Источники

- [TRL v1.0 — блог HuggingFace](http://hf.co/blog/trl-v1)
- [@huggingface, 01-04-2026 — TQ3_1S/27B модель](https://x.com/huggingface/status/2038917359260623229)
- [@huggingface, 01-04-2026 — TRL v1.0](https://x.com/huggingface/status/2039000031949165005)
