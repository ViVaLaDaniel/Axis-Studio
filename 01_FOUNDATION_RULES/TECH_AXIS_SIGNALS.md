# TECH_AXIS_SIGNALS.md  
AXIS_ROOT v10.5 — Центральная Система Сигналов (Event Layer OS)

Этот документ определяет фундаментальную событийную модель AXIS OS.  
Сигналы — это язык, на котором общаются модули системы:  
Brain → Architect → Developer → QA → Creative Engine → Memory Log → Knowledge Syncer → CI Pipeline.

Сигналы позволяют AXIS работать как операционная система:  
реактивно, автономно, предсказуемо и расширяемо.

────────────────────────────────────────
# 1. РОЛЬ СИСТЕМЫ СИГНАЛОВ
────────────────────────────────────────
Система событий решает три задачи:

1) **Коммуникация модулей**  
   Каждый компонент AXIS сообщает о своих действиях, ошибках и изменениях через сигналы.

2) **Оркестрация процессов**  
   Pipeline разработки, проверки и обновления строится через реакцию на события.

3) **Безопасность и предсказуемость**  
   Нет хаотического поведения — только детерминированные реакции.

────────────────────────────────────────
# 2. КАТЕГОРИИ СИГНАЛОВ OS
────────────────────────────────────────

AXIS OS использует четыре уровня сигналов:

## LEVEL 0 — SYSTEM-CRITICAL SIGNALS
Системные сигналы ядра. Приоритет: максимальный.

- **SYS.KERNEL.START**  
  AXIS OS инициализирован.

- **SYS.KERNEL.DEPRECATION_FOUND**  
  Knowledge Syncer обнаружил устаревший паттерн / API.

- **SYS.KERNEL.MEMORY_APPEND**  
  Ошибка или урок записан в 18_AXIS_MEMORY_LOG.json.

- **SYS.KERNEL.REFACTOR_REQUIRED**  
  Модуль должен быть обновлён (Shopify Deprecation, Research Update).

## LEVEL 1 — KNOWLEDGE SIGNALS (Научные данные)
Сигналы, связанные с UX, CRO, исследованиями и трендами.

- **KNOWLEDGE.UX.NEW_RESEARCH**  
  Добавлено новое исследование Baymard / NNGroup / CXL.

- **KNOWLEDGE.PATTERN.OUTDATED**  
  Один из UX/CRO паттернов устарел.

- **KNOWLEDGE.COLOR.UPDATE**  
  Обновлены цветовые OKLCH значения.

- **KNOWLEDGE.ARCHETYPE_CHANGE**  
  Изменился поведенческий профиль покупателя.

## LEVEL 2 — ARCHITECTURE & DESIGN SIGNALS
Сигналы, влияющие на структуру темы.

- **ARCH.DEPENDENCY.BROKEN**  
  Обнаружена проблема в связях секций/снипетов.

- **ARCH.TEMPLATE.OVERSIZED**  
  Файл превышает лимит — подключить Template Splitter.

- **ARCH.STYLEGUIDE.UPDATE**  
  Living Styleguide требует обновления.

- **DESIGN.TOKEN.REGEN**  
  Необходима регенерация design_tokens.json.

## LEVEL 3 — DEVELOPMENT & CI/CD SIGNALS
Сигналы, инициирующие разработку, ошибки и пайплайн.

- **DEV.BUILD.START**  
  Начало процесса генерации кода.

- **DEV.ERROR.CAUGHT**  
  Ошибка поймана Error Handling Engine.

- **QA.TEST.FAIL**  
  Тест не пройден (Lighthouse < 90, ThemeCheck = error).

- **CI.PACKAGE.READY**  
  Пакет готов для Theme Store.

────────────────────────────────────────
# 3. СТРУКТУРА СИГНАЛА
────────────────────────────────────────

Каждый сигнал AXIS имеет строго утверждённый формат:

```json
{
"signal": "ARCH.DEPENDENCY.BROKEN",
"timestamp": "2025-11-29T12:30:00Z",
"module_source": "09_AXIS_DEPENDENCY_MANAGER",
"severity": "HIGH",
"payload": {
"file": "main-product.liquid",
"missing_snippet": "price.liquid"
},
"action_required": true,
"route_to": ["03_AXIS_MASTER_SYSTEM_v6.2.json", "18_AXIS_MEMORY_LOG.json"]
}
```

Правила:
- **signal** — уникальный идентификатор события  
- **module_source** — кто создал сигнал (модуль/демон)  
- **severity** — LOW / MEDIUM / HIGH / CRITICAL  
- **payload** — данные, конкретизирующие ситуацию  
- **action_required** — нужно ли вмешательство  
- **route_to** — списки модулей, которые должны обработать сигнал

────────────────────────────────────────
# 4. ОСНОВНЫЕ РЕАКЦИИ AXIS OS
────────────────────────────────────────

## A) Knowledge Syncer реагирует на:
- UX-научные обновления  
- конкурентные тренды  
- изменения Core Web Vitals  

## B) Architect реагирует на:
- DEPENDENCY.BROKEN  
- TEMPLATE.OVERSIZED  
- STYLEGUIDE.UPDATE  

## C) Creative Engine реагирует на:
- всплеск тренда дизайна  
- появление killer feature в Theme Store  
- изменение визуальных паттернов  

## D) QA реагирует на:
- TEST.FAIL  
- PERFORMANCE_DROP  
- ACCESSIBILITY.ERROR  

## E) System Prompt (финал) реагирует на ВСЁ:
и формирует поведение AXIS OS на основе всех сигналов.

────────────────────────────────────────
# 5. ПРОТОКОЛ ПОДПИСКИ (SUBSCRIPTION)
────────────────────────────────────────

Каждый модуль может подписаться на один или несколько сигналов:

```
subscribe("SYS.KERNEL.DEPRECATION_FOUND", Architect)
subscribe("KNOWLEDGE.UX.NEW_RESEARCH", NeuroLibrary)
subscribe("DEV.ERROR.CAUGHT", ErrorHandlingEngine)
subscribe("QA.TEST.FAIL", CIPipeline)
```

Подписки управляются через:

- 17_AXIS_CONTEXT_ROUTER.json  
- axis_brain_v10.0_GOD_MODE.json  
- internal process manager  

────────────────────────────────────────
# 6. ПРАВИЛА БЕЗОПАСНОСТИ СИГНАЛОВ
────────────────────────────────────────

1. Сигнал **НЕ МОЖЕТ** быть пустым.  
2. Severity CRITICAL требует немедленного действия.  
3. Все сигналы автоматически логируются в  
   `18_AXIS_MEMORY_LOG.json`.  
4. Запрещено создавать новые категории сигналов  
   без обновления Конституции (Foundation Rules).  
5. Сигнал не может идти в обход Context Router.

────────────────────────────────────────
# 7. БУДУЩЕЕ СИСТЕМЫ СИГНАЛОВ
────────────────────────────────────────

AXIS OS будет дополнять систему сигналов:

- SENTIMENT SIGNALS (эмоции пользователей)
- CLICKMAP SIGNALS (модели поведения)
- UX CORRELATION SIGNALS (что влияет на конверсию)
- MARKET VOLTAGE SIGNALS (рывки трендов)
- AI META-SIGNALS (когда система сама себе сообщает о предстоящих изменениях)

────────────────────────────────────────
# 8. КАК ЭТО ИСПОЛЬЗУЕТСЯ
────────────────────────────────────────

• Knowledge Syncer — агрегирует, анализирует, создаёт задачи  
• Creative Engine — генерирует идеи на основе сигналов  
• Architect — изменяет структуру  
• Dev — создаёт код  
• QA — подтверждает корректность  
• CI/CD — выпускает релиз  
• System Prompt — формирует поведение AXIS OS

Система сигналов — это кровь AXIS OS.
