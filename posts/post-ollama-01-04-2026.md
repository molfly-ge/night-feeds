# ollama — 01-04-2026

11 твитов — крупный релиз Ollama с поддержкой MLX на Apple Silicon.

**Ollama + MLX: большое обновление.** Теперь Ollama может использовать MLX как бэкенд на Mac — это прямой прирост производительности на всём Apple Silicon. На M5/M5 Pro/M5 Max задействуются новые GPU Neural Accelerators для ускорения и TTFT (time to first token), и скорости генерации. Тест на Qwen3.5-35B-A3B: NVFP4 против Q4_K_M предыдущей версии. [Блог Ollama](https://ollama.com/blog/mlx) [Твит анонса](https://x.com/ollama/status/2038871514003513501)

**Стартовая модель — Qwen3.5-35B-A3B-nvfp4.** Нужно больше 32 GB unified memory. Работает с Claude Code и OpenClaw:
```
ollama launch claude --model qwen3.5:35b-a3b-coding-nvfp4
ollama launch openclaw --model qwen3.5:35b-a3b-coding-nvfp4
```
[Твит](https://x.com/ollama/status/2038835457358958652)

**NVFP4: точность производственного уровня.** Новый формат NVIDIA уменьшает требования к памяти и bandwidth, сохраняя качество. Ollama теперь даёт те же результаты, что и production-инфраструктура у крупных провайдеров. [Твит](https://x.com/ollama/status/2038835453265367271)

**Умное кэширование.** Ollama переиспользует кэш между разговорами, снижая потребление памяти. Интеллектуальные контрольные точки по всему промпту ускоряют ответы при разветвлённых сессиях (как в Claude Code с общим system prompt). [Твит](https://x.com/ollama/status/2038835455777763762)

**Пользователи уже тестируют.** Qwen3.5:36b через MLX ускорился в 2.2x на первом же апгрейде. Qwen3.5:4b-nvfp4 на M1 Max — 38% быстрее предыдущей версии в реальном агентном use case. [Твит](https://x.com/ollama/status/2039014724071719405)

**Поддержка кастомных моделей.** Команда работает над расширением списка архитектур и упрощённым импортом fine-tuned моделей. [Твит](https://x.com/ollama/status/2038835458969686091)

## Источники

- [Ollama Blog: MLX backend](https://ollama.com/blog/mlx)
- [@ollama, 01-04-2026 — анонс MLX](https://x.com/ollama/status/2038871514003513501)
- [@ollama, 01-04-2026 — старт с Qwen3.5](https://x.com/ollama/status/2038835457358958652)
- [@ollama, 01-04-2026 — NVFP4](https://x.com/ollama/status/2038835453265367271)
- [@ollama, 01-04-2026 — кэширование](https://x.com/ollama/status/2038835455777763762)
