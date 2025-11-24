# DATA_FLOWS.md  
AXIS_ROOT v10.5 — Data Flow Architecture for Shopify OS Themes (AXIS OS)

Этот документ описывает, как данные проходят через всю систему AXIS:  
от Shopify → к Liquid → к Sections → к Snippets → к JS → к UI → к Signals → к Memory Log.

AXIS OS использует эти правила, чтобы создавать темы, которые:
- быстрые,
- масштабируемые,
- прозрачные,
- предсказуемые,
- легко дебажатся,
- не ломаются от обновлений Shopify.

────────────────────────────────────────
# 1. ФИЛОСОФИЯ ПОТОКОВ ДАННЫХ AXIS OS
────────────────────────────────────────

## 1.1 Everything is data-driven
Никакая секция не содержит жёстко зашитую логику.  
Все данные → из Shopify или схемы.

## 1.2 Zero Redundancy
Каждый фрагмент информации существует только в одном месте.

## 1.3 Predictable Flows
Откуда пришли данные — всегда ясно.  
Что с ними делает UI — детерминировано.

## 1.4 Schema→Content→UI Pipeline
Секция — это результат 3 уровней:
1. JSON Schema  
2. Section Liquid  
3. Section UI (HTML/CSS/JS)

────────────────────────────────────────
# 2. ГЛАВНАЯ КАРТА ПОТОКОВ ДАННЫХ
────────────────────────────────────────

```
Shopify Platform
│
▼
Liquid Layer (Templates & Sections)
│
├── pulls → product, collection, cart, settings
│
▼
Section Schema (settings + blocks)
│
▼
Section Runtime Context (liquid/JSON)
│
▼
Snippet Injection (reusable UI logic)
│
▼
JS Interaction Layer (state, events, signals)
│
▼
UI Rendering (final component)
│
▼
AXIS Signals (UX, errors, performance)
│
▼
18_AXIS_MEMORY_LOG.json (long-term learning)
```

────────────────────────────────────────
# 3. LIQUID → SECTION FLOW (STRUCTURAL LAYER)
────────────────────────────────────────

## 3.1 Template → Section Flow
Templates НЕ должны содержать логику.  
Templates — только список секций.

```
template → { section A, B, C }
section → schema + content + UI
```

## 3.2 Section Schema as Source of Truth
Каждая секция имеет:
- settings  
- blocks  
- types  
- conditions  
- presets  

Секция получает один объект:

```
section.settings
section.blocks
```

## 3.3 Section Liquid (Execution Layer)
Liquid генерирует HTML, контент и структуру.

Правила:
- no loops > 3  
- no nested logic > 2 levels  
- no inline styles  
- no business logic  

────────────────────────────────────────
# 4. SECTION → SNIPPET FLOW (DECOMPOSITION LAYER)
────────────────────────────────────────

Сложная логика всегда выносится в snippets.

Примеры:
- price  
- rating  
- inventory  
- variant selector  
- badges  
- buttons  
- media  

**Все snippets должны быть чистыми и независимыми.**

Они работают как компоненты.

────────────────────────────────────────
# 5. SNIPPET → JS FLOW (INTERACTION LAYER)
────────────────────────────────────────

JS должен получать только:

- data-* attributes
- json payload
- intersection events
- signals


JS не должен парсить HTML.  
JS должен работать с данными, не с макетом.

────────────────────────────────────────
# 6. JS → UI FLOW (RENDER LAYER)
────────────────────────────────────────

JS создаёт:
- state  
- transitions  
- micro-interactions  
- events  

UI компонент читает:
- state  
- props  
- signals  
- timers (ethically)  
- user input  

UI никогда не изменяет данные.  
UI только отображает.

────────────────────────────────────────
# 7. UI → AXIS SIGNALS FLOW (SYSTEM EVENT LAYER)
────────────────────────────────────────

Когда UI взаимодействует с пользователем:

- add to cart  
- variant change  
- error  
- scroll depth  
- search interaction  
- form mistake  
- performance drop  

UI отправляет сигнал:

```
UI.SIGNAL.TYPE
payload: {...}
```

Эти сигналы попадают в:
- TECH_AXIS_SIGNALS.md  
- 18_AXIS_MEMORY_LOG.json  
- Architect  
- CRO Scientist  
- Creative Engine  

────────────────────────────────────────
# 8. KNOWLEDGE FLOW (LEARNING LAYER)
────────────────────────────────────────

Все данные, сигналы, UX-следы → идут в:

```
18_AXIS_MEMORY_LOG.json
```

А затем Knowledge Syncer решает:

- устарели ли паттерны  
- нужно ли обновить UX-настройки  
- нужно ли переписать секцию  
- нужно ли изменить motion или color  
- изменился ли рынок  
- какой archetype активен  

Knowledge Syncer → обновляет библиотеки.

────────────────────────────────────────
# 9. DATA OUT: HOW AXIS USES THIS
────────────────────────────────────────

## 9.1 Creative Engine
- генерирует новые секции на основе Data Flows  
- видит, где bottlenecks  
- понимает UX-навигацию

## 9.2 CRO Scientist
- анализирует поведение  
- corrects friction  
- вводит новый паттерн

## 9.3 Architect
- переписывает структуру  
- управляет зависимостями  
- оптимизирует Liquid

## 9.4 Developer
- пишет JS/HTML/CSS на основе Data Architecture

## 9.5 QA & Performance
- тестируют каждый поток

────────────────────────────────────────
# 10. ГЛАВНОЕ ПРАВИЛО:
────────────────────────────────────────

```
Data must flow one-way.
Logic must be centralized.
UI must always be predictable.
```
