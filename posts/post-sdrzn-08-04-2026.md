# sdrzn — 08-04-2026

3 твита за сутки. Серия про vendor lock-in в inference-провайдерах: 41% всего кода сегодня — AI-assisted, и значит провайдер модели — это уже не tool, а инфраструктура.

**Vendor lock-in в AI-стеке**. sdrzn (создатель Cline): «Ты оптимизировал под скорость, твой вендор — под lock-in. Один из вас получил, что хотел. Если для смены inference-провайдера нужно трогать что-то кроме конфига — у тебя уже накоплен долг». [Твит](https://x.com/sdrzn/status/2041563576452960334)

**Деградация модели в середине спринта поднимает цену**. Обоснование: при 41% AI-assisted кода провайдер становится инфраструктурой, и деградировавшая модель «отравляет колодец» — падает качество code review, тесты упускают edge cases, документация дрейфует. [Твит](https://x.com/sdrzn/status/2041563581079290007)

**Решение — model-agnostic архитектура**. Принцип тот же, что и с DB-connection: абстрагируй, не вшивай. Смена провайдера = изменение конфига, не переписывание. Полный пост: [Architects or tenants — modern AI stacks are being built on rented foundations](https://cline.bot/blog/architects-or-tenants-modern-ai-stacks-are-being-built-on-rented-foundations). [Твит](https://x.com/sdrzn/status/2041563582316605932)

## Источники

- [Cline blog — Architects or tenants](https://cline.bot/blog/architects-or-tenants-modern-ai-stacks-are-being-built-on-rented-foundations)
