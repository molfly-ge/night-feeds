# llama.cpp

Высокопроизводительный C/C++ фреймворк для инференса LLM. Поддерживает широкий спектр моделей (LLaMA, Gemma, Mistral и др.), квантизацию, встроенный WebUI и MCP из коробки. Работает на CPU, Apple Silicon (Metal), CUDA и других бэкендах.

Демонстрация: Gemma 4 26B A4B Q8_0 на Mac Studio M2 Ultra даёт 300 токенов/сек с prompt speculative decoding (ngram-хэширование, черновики до 64 токенов).

**Ссылки:**
- GitHub: https://github.com/ggml-org/llama.cpp
- PR #19164 (prompt speculative decoding): https://github.com/ggml-org/llama.cpp/pull/19164
- Twitter: https://x.com/ggerganov

**Источник:** [@ggerganov, 04-04-2026](https://x.com/ggerganov/status/2040514840687514037)
