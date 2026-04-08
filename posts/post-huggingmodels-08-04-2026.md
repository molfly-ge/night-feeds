# huggingmodels — 08-04-2026

50 твитов за сутки. Бот публикует серии из 3-4 твитов на каждую модель: краткое описание + ссылка. Это лента релизов и переупаковок моделей с HF — за окно прошло около 17 моделей.

**Gemma-4-E4B (Google) — any-to-any**. Multimodal трансформер: принимает любую комбинацию текста и изображений на вход, выдаёт любой текстовый вывод. Apache 2.0, safetensors, 22k+ скачиваний. [Модель](https://huggingface.co/google/gemma-4-E4B) · [Твит](https://x.com/HuggingModels/status/2041755444264452402)

**Gemma-4-E2B-it-GGUF (unsloth) — квантованная vision-language**. Multimodal Gemma-4 с понижением ресурсных требований через GGUF. 280K+ скачиваний. [Модель](https://huggingface.co/unsloth/gemma-4-E2B-it-GGUF) · [Твит](https://x.com/HuggingModels/status/2041720956079763708)

**gemma-4-21b-a4b-it-REAP (0xSero)** — pruned-версия Gemma-4 21B с REAP, мультимодал, ~660 скачиваний. [Модель](https://huggingface.co/0xSero/gemma-4-21b-a4b-it-REAP) · [Твит](https://x.com/HuggingModels/status/2041728500437262494)

**gemma4-31b-Opus-4.6-reasoning (kai-os)** — fine-tuned reasoning-специалист на Gemma-4 31B. [Модель](https://huggingface.co/kai-os/gemma4-31b-Opus-4.6-reasoning) · [Твит](https://x.com/HuggingModels/status/2041747629223375254)

**Bonsai-8B-mlx-1bit (prism-ml)** — 8B-параметрическая модель в 1-бит квантизации, заточенная под Apple Silicon (MLX). 28k+ скачиваний. [Модель](https://huggingface.co/prism-ml/Bonsai-8B-mlx-1bit) · [Твит](https://x.com/HuggingModels/status/2041762997488755150)

**Qwopus3.5-27B-v3 (Jackrong)** — vision-language reasoning, тег competitive-programming, 10k+ скачиваний. [Модель](https://huggingface.co/Jackrong/Qwopus3.5-27B-v3) · [Твит](https://x.com/HuggingModels/status/2041762728323527091)

**Qwen3.5-35B-A3B-APEX-GGUF (mudler)** — 35B MoE с advanced mixed-precision квантизацией, llama.cpp-friendly, 47k+ скачиваний. [Модель](https://huggingface.co/mudler/Qwen3.5-35B-A3B-APEX-GGUF) · [Твит](https://x.com/HuggingModels/status/2041720954498511274)

**Trinity-Large-Thinking (arcee-ai)** — AFMoE-архитектура (Adaptive Fast Mixture of Experts), заточена под reasoning + tool-use. [Модель](https://huggingface.co/arcee-ai/Trinity-Large-Thinking) · [Твит](https://x.com/HuggingModels/status/2041755179100598719)

**Voxtral-4B-TTS-2603 (mistralai)** — multilingual TTS на 7 языков, ~6k скачиваний. [Модель](https://huggingface.co/mistralai/Voxtral-4B-TTS-2603) · [Твит](https://x.com/HuggingModels/status/2041747894865424563)

**Nemotron-OCR-V2 (nvidia)** — OCR с пониманием layout, multilingual (включая English+Chinese), распознавание объектов в контексте текста. [Модель](https://huggingface.co/nvidia/nemotron-ocr-v2) · [Твит](https://x.com/HuggingModels/status/2041736051581186547)

**Falcon-Perception (tiiuae)** — vision-language, open-vocabulary segmentation: указываешь словами «red car» / «person wearing a hat» — модель строит pixel-perfect маску. [Модель](https://huggingface.co/tiiuae/Falcon-Perception) · [Твит](https://x.com/HuggingModels/status/2041736051862147216)

**JoyAI-Image-Edit (jdopensource)** — модель для редактирования изображений, 72 community likes. [Модель](https://huggingface.co/jdopensource/JoyAI-Image-Edit) · [Твит](https://x.com/HuggingModels/status/2041728505080377558)

**wav2vec2-large-xlsr-53-russian (jonatasgrosman)** — ASR для русского, 6.7M скачиваний, бенчмарк Robust Speech Event. [Модель](https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-russian) · [Твит](https://x.com/HuggingModels/status/2041773805857866058)

## Источники

- [google/gemma-4-E4B](https://huggingface.co/google/gemma-4-E4B)
- [unsloth/gemma-4-E2B-it-GGUF](https://huggingface.co/unsloth/gemma-4-E2B-it-GGUF)
- [0xSero/gemma-4-21b-a4b-it-REAP](https://huggingface.co/0xSero/gemma-4-21b-a4b-it-REAP)
- [kai-os/gemma4-31b-Opus-4.6-reasoning](https://huggingface.co/kai-os/gemma4-31b-Opus-4.6-reasoning)
- [prism-ml/Bonsai-8B-mlx-1bit](https://huggingface.co/prism-ml/Bonsai-8B-mlx-1bit)
- [Jackrong/Qwopus3.5-27B-v3](https://huggingface.co/Jackrong/Qwopus3.5-27B-v3)
- [mudler/Qwen3.5-35B-A3B-APEX-GGUF](https://huggingface.co/mudler/Qwen3.5-35B-A3B-APEX-GGUF)
- [arcee-ai/Trinity-Large-Thinking](https://huggingface.co/arcee-ai/Trinity-Large-Thinking)
- [mistralai/Voxtral-4B-TTS-2603](https://huggingface.co/mistralai/Voxtral-4B-TTS-2603)
- [nvidia/nemotron-ocr-v2](https://huggingface.co/nvidia/nemotron-ocr-v2)
- [tiiuae/Falcon-Perception](https://huggingface.co/tiiuae/Falcon-Perception)
- [jdopensource/JoyAI-Image-Edit](https://huggingface.co/jdopensource/JoyAI-Image-Edit)
- [jonatasgrosman/wav2vec2-large-xlsr-53-russian](https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-russian)
