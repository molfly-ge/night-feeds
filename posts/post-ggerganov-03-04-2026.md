# ggerganov — 03-04-2026

10 твитов за сутки.

## Gemma 4 — day-0 поддержка в llama.cpp

**Релиз Gemma 4** — Google выпустила Gemma 4, и llama.cpp получил поддержку модели с первого дня. Георгий называет её «лучшей open-source моделью, которую можно запустить локально». Квантизированные GGUF-версии уже доступны на Hugging Face. [Твит](https://x.com/ggerganov/status/2039744468899811419) | [Модели на HF](https://huggingface.co/collections/ggml-org/gemma-4)

**Демо: 300 токенов/с на Mac Studio M2 Ultra** — Gemma 4 26B A4B Q8_0 с prompt-based speculative decoding выдаёт 300 т/с на трёхлетнем Mac Studio. Встроенный WebUI, MCP-поддержка (web-search, HF, GitHub) из коробки. [Твит](https://x.com/ggerganov/status/2039752638384709661) Уточнение: скорость объясняется тем, что модель пересказывает контент из промпта — спекулятивное декодирование особенно эффективно в таком случае. [Твит](https://x.com/ggerganov/status/2039753496317059270)

**NVIDIA оптимизировала Gemma 4** — партнёры из NVIDIA AI PC помогли с оптимизациями и бенчмарками для запуска Gemma 4 во всей экосистеме NVIDIA. [Твит](https://x.com/ggerganov/status/2039797628116881567) | [Блог NVIDIA](https://blogs.nvidia.com/blog/rtx-ai-garage-open-models-google-gemma-4/)

## llama.cpp как локальный агент

**WebUI + MCP = самодостаточный агент** — llama.cpp со встроенным WebUI позиционируется как самый легковесный локальный агент с поддержкой MCP-серверов (Hugging Face, поиск и др.). [Твит](https://x.com/ggerganov/status/2039786276765782518)

**Tailscale для мобильного инференса** — совет: связать Mac и телефон через Tailscale для быстрого приватного инференса на ходу. Демо Gemma 4 на iPhone через Mac Studio. [Твит](https://x.com/ggerganov/status/2039804601810001921)

**Установка одной командой** — ретвит @julien_c: `brew install llama.cpp --HEAD`, затем `llama-server -hf ggml-org/gemma-4-26B-A4B-it-GGUF:Q4_K_M`. [Ретвит](https://x.com/julien_c/status/2039746054355067002)

## Источники

- [Gemma 4 GGUF на Hugging Face](https://huggingface.co/collections/ggml-org/gemma-4)
- [NVIDIA RTX AI Garage — Gemma 4](https://blogs.nvidia.com/blog/rtx-ai-garage-open-models-google-gemma-4/)
- [@ggerganov, 03-04-2026](https://x.com/ggerganov/status/2039744468899811419)
- [@ggerganov, 03-04-2026](https://x.com/ggerganov/status/2039752638384709661)
- [@ggerganov, 03-04-2026](https://x.com/ggerganov/status/2039797628116881567)
- [@ggerganov, 03-04-2026](https://x.com/ggerganov/status/2039804601810001921)
- [@ggerganov, 03-04-2026](https://x.com/ggerganov/status/2039786276765782518)
- [@julien_c (ретвит), 03-04-2026](https://x.com/julien_c/status/2039746054355067002)
