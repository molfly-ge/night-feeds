# ggerganov — 05-04-2026

2 твита за сутки.

**Prompt-based speculative decoding в llama.cpp** — Георги Гергanov показал демо спекулятивного декодирования через ngram-хэширование. Метод предлагает черновики до 64 токенов, отслеживая ngram'ы в наблюдаемых контекстах. Наиболее эффективен для задач программирования. [Твит](https://x.com/ggerganov/status/2040514840687514037)

**300 токенов/сек на Mac Studio M2 Ultra** — демонстрация запуска Gemma 4 26B A4B Q8_0 с полным качеством. Используется встроенный WebUI llama.cpp, поддержка MCP из коробки (веб-поиск, HuggingFace, GitHub) и prompt speculative decoding. Железо — Mac Studio M2 Ultra 2023 года. [Твит](https://x.com/ggerganov/status/2040514840687514037)

**PR с параметрами спекулятивного декодирования** — ссылка на pull request в репозитории llama.cpp, где описаны параметры, применявшиеся в демо. [Твит](https://x.com/ggerganov/status/2040514847696167259) · [PR llama.cpp #19164](https://github.com/ggml-org/llama.cpp/pull/19164)

## Источники

- [llama.cpp PR #19164 — prompt speculative decoding](https://github.com/ggml-org/llama.cpp/pull/19164)
- [@ggerganov, 04-04-2026](https://x.com/ggerganov/status/2040514840687514037)
- [@ggerganov, 04-04-2026](https://x.com/ggerganov/status/2040514847696167259)
