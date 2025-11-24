# ARCH_PATTERNS.md  
AXIS_ROOT v10.5 — Architectural Patterns of Shopify OS Themes

Этот документ — фундаментальная библиотека архитектурных паттернов для AXIS OS.  
Он определяет правила инженерии Shopify-тем, структуру секций, шаблонов, данных, зависимостей и жизненный цикл композиции интерфейса.

AXIS использует эти паттерны для:
- проектирования тем с нуля,
- анализа проблем архитектуры,
- генерации секций,
- построения UX-потоков,
- предотвращения "тяжёлых" и неуправляемых шаблонов,
- интеграции Best Practices Shopify OS 2.0.

────────────────────────────────────────
# 1. ГЛАВНЫЕ ПРИНЦИПЫ АРХИТЕКТУРЫ AXIS OS
────────────────────────────────────────

## 1.1 Основа: Модульность
Каждый блок темы — автономный модуль:
- Section  
- Snippet  
- ASSET (style/js)  
- Template  
- JSON Template Schema  

Модуль не должен зависеть от конкретного места в дереве.

## 1.2 Чистота шаблонов


Templates must contain ZERO business logic.

Весь функционал → в sections/snippets.

## 1.3 Одно Ответственное Место
Каждый модуль имеет смысл и задачу.  
Никаких дублирований.  
Каждая сущность = один источник истины.

## 1.4 Вертикальная и Горизонтальная Композиция
- Vertical: hero → content → CTA → grid → footer  
- Horizontal: multi-column, multi-card patterns  

## 1.5 Reusability First (повторное использование)
Компоненты проектируются так, чтобы использоваться в разных секциях.

## 1.6 Multi-level Theming
Цвет, motion, spacing, typography → через design_tokens.json.  
Тема никогда не жёстко меняется в CSS.

## 1.7 Performance Budget  
Любой шаблон должен соблюдать:
- ≤ 30KB JS  
- ≤ 80KB CSS  
- LCP ≤ 2.5s  

────────────────────────────────────────
# 2. ПАТТЕРНЫ СЕКЦИЙ (SECTION PATTERNS)
────────────────────────────────────────

## 2.1 Hero Patterns
### A) Visual-first Hero
- large imagery  
- minimal text  
- one clear CTA  
- recommended for: fashion, beauty, lifestyle

### B) Benefit-first Hero
- structured bullets  
- attention flow  
- recommended for: tech, fitness, supplements

### C) Split Hero (50/50)
- product left  
- text right  
- ideal for: SaaS, DTC with complex offers

---

## 2.2 Grid Patterns
### A) Standard 3/4 Grid
- ideal for catalogs with ≤ 100 products  
- balanced cognition  

### B) Masonry Grid (UX constraint!)
- only for visual niches (home decor, art)  
- NEVER for large inventories

### C) Cards with Hover Micro-motion
- pre-attentive motion  
- higher CTR  

---

## 2.3 PDP (Product Page) Patterns
### A) Gallery-first
- based on Baymard: visual dominance improves decision speed

### B) Info-first
- for analytical buyers (tech, gear)

### C) Accordion Data Layout
- reduces cognitive load (Hick’s Law)

---

## 2.4 Collection Page Patterns
### A) Left Filters + Grid  
### B) Horizontal Filters + Sticky Top Bar  
### C) Quick-add Enabled Cards  

---

## 2.5 CTA Placement Patterns
### A) Single Primary CTA  
### B) Dual CTA (Primary + Secondary)  
### C) Peek CTA (appears based on scroll depth)  

────────────────────────────────────────
# 3. ПАТТЕРНЫ ДАННЫХ (DATA PATTERNS)
────────────────────────────────────────

## 3.1 Single Source Pattern
Все данные товара должны поступать из единого объекта product.

## 3.2 Schema-Driven UI
Каждая секция имеет JSON schema:
- settings  
- blocks  
- presets  
- conditional elements  

## 3.3 Content Projection Pattern
Секция должна поддерживать диаграмму контента:
- main content  
- optional areas  
- override areas  

────────────────────────────────────────
# 4. ПАТТЕРНЫ ШАБЛОНОВ (TEMPLATE PATTERNS)
────────────────────────────────────────

## 4.1 Thin Template Pattern
Правило Shopify OS:


Templates should remain nearly empty.

Шаблон вызывает секции → секции управляют логикой.

## 4.2 Template Split Pattern  
Если файл > 20 секций → split using 16_TEMPLATE_SPLITTER_TOOL.md.

## 4.3 View Composition Pattern  
Каждый шаблон описывает только:
- какие секции  
- порядок секций  
- параметры секций  

────────────────────────────────────────
# 5. ПАТТЕРНЫ SNIPPETS
────────────────────────────────────────

## 5.1 Functional Snippets  
Функции:
- price  
- variant selector  
- breadcrumbs  
- badges  

## 5.2 Reusable Snippets
Должны использоваться во многих секциях:
- media  
- badges system  
- rating stars  
- buttons  

## 5.3 High-frequency Snippets  
Кандидаты на inline optimization:
- price  
- inventory  
- rating  

────────────────────────────────────────
# 6. ПАТТЕРНЫ JS / INTERACTION LAYER
────────────────────────────────────────

## 6.1 Intersection Observer Patterns
- lazy loading  
- reveal animations  
- sticky components lifecycle  

## 6.2 Micro-interaction Pattern
- add-to-cart  
- wishlist  
- gallery zoom  
- variant hover  

## 6.3 Event-Driven Pattern (via TECH_AXIS_SIGNALS)
Каждый JS-модуль → реагирует на сигналы AXIS OS:


ARCH.CHANGE
PERFORMANCE.WARNING
KNOWLEDGE.UPDATE


────────────────────────────────────────
# 7. ARCHITECTURAL ANTI-PATTERNS (ЧТО ЗАПРЕЩЕНО)
────────────────────────────────────────

### ❌ Fat templates  
### ❌ Inline styles  
### ❌ Hardcoded values  
### ❌ Business logic in templates  
### ❌ Six-level nested HTML  
### ❌ Sections with > 300 lines  
### ❌ Snippets duplicated across sections  

────────────────────────────────────────
# 8. АРХИТЕКТУРНЫЙ PIPELINE AXIS
────────────────────────────────────────

## Step 1 — Strategy (02_STRATEGY_CREATIVE)
UX, CRO, Neuro решают паттерны.

<h2>Step 2 — Architect (03_ARCHITECTURE)
Архитектор собирает структуру и зависимости.

<h2>Step 3 — Execution Dev (04_EXECUTION_DEV)
Создаётся код секций, snippets.

<h2>Step 4 — QA (05_QUALITY_SECURITY)
Performance + security + accessibility.

<h2>Step 5 — Release (06_CI_CD_RELEASE)
Pack → preview store → compliance check.

────────────────────────────────────────
# 9. ИНТЕГРАЦИЯ С AXIS OS
────────────────────────────────────────

### Читает:
- AXIS_NEURO_DESIGN_LIBRARY.json  
- AXIS_CRO_PATTERNS.json  
- AXIS_BEHAVIORAL_PATTERNS.json  

### Пишет:
- DATA_FLOWS.md  
- SPEC_LIVING_STYLEGUIDE.md  
- 03_AXIS_MASTER_SYSTEM_v6.2.json  

────────────────────────────────────────
# 10. ГЛАВНОЕ ПРАВИЛО:
────────────────────────────────────────


Architecture should simplify, never complicate.
