# SPEC_LIVING_STYLEGUIDE.md  
AXIS_ROOT v10.5 — Living Styleguide Specification  
(Автоматически обновляемый визуальный стандарт AXIS OS)

Этот документ является «живым» styleguide, который обновляется Knowledge Syncer и использует все модули AXIS:  
цветовую систему, нейро-дизайн, поведенческие паттерны, motion, UX-текст и токены.

Его цель:  
создавать предсказуемый, научно обоснованный, быстрый и конверсионный UI.

────────────────────────────────────────
# 1. ОСНОВА LIVING STYLEGUIDE
────────────────────────────────────────

## 1.1 Почему он называется «Living»?
Потому что каждый модуль AXIS может обновлять его:

- AXIS_COLOR_PSYCHOLOGY.json → обновляет цветовые токены  
- AXIS_NEURO_DESIGN_LIBRARY.json → обновляет UX-принципы  
- AXIS_MOTION_GUIDELINES.md → обновляет анимации  
- AXIS_TEXT_GUIDELINES.md → обновляет текстовые паттерны  
- AXIS_BEHAVIORAL_PATTERNS.json → корректирует UX-потоки  
- AXIS_KNOWLEDGE_SYNCER.json → обновляет структуру и версии  

Это не статичный документ, это — **организм**.

────────────────────────────────────────
# 2. ДИЗАЙН-ТОКЕНЫ
────────────────────────────────────────

Токены — основа всей визуальной системы.

## 2.1 Color Tokens
Источник: AXIS_COLOR_PSYCHOLOGY.json  
Формат токена:

```
color.<emotion>.<state>
```

Примеры:
- color.trust.default  
- color.energy.hover  
- color.luxury.dark  
- color.calm.background  

## 2.2 Typography Tokens

```
font.family.primary
font.size.xl
font.size.body
font.weight.bold
line.height.sm
```

## 2.3 Spacing Tokens

```
space.xs = 4px
space.sm = 8px
space.md = 16px
space.lg = 24px
space.xl = 40px
```

## 2.4 Motion Tokens
Источник: AXIS_MOTION_GUIDELINES.md  

```
motion.duration.primary = 180ms
motion.duration.micro = 90ms
motion.curve.standard = cubic-bezier(0.22, 1, 0.36, 1)
```

────────────────────────────────────────
# 3. КОМПОНЕНТНАЯ СИСТЕМА AXIS
────────────────────────────────────────

## 3.1 Buttons
### Primary Button
- high-contrast  
- color = color.energy.default (или color.trust.default)  
- radius = 6–8px  
- micro-motion = enabled  
- accessibility contrast ≥ 4.5  

### Secondary Button
- color = neutral / low chroma  
- no strong shadows  

### CTA Behavior
- attention appears within 150–250ms  
- supports sticky/mobile-friendly states  

---

## 3.2 Form Elements
- labels above inputs  
- inline validation  
- touch targets ≥ 44px  
- avoid floating labels  

---

## 3.3 Cards
### Product Card Rules:
- media-first  
- price group must follow Gestalt proximity  
- variant preview minimal  
- hover micro-interaction enabled  
- badge layer supports contrast tokens  

---

## 3.4 Navigation
- max 7 top-level items  
- sticky nav on scroll  
- predictable layout (Jacob’s Law)  
- mobile nav prioritized for thumb reach  

────────────────────────────────────────
# 4. GRID SYSTEM & LAYOUT
────────────────────────────────────────

## 4.1 Grid Rules
- base grid: 4px / 8px  
- container max-width: 1440px  
- gutter: 24px (desktop), 16px (tablet), 12px (mobile)

<h2>4.2 Section Vertical Rhythm
Spacing rules:

```
section_spacing_top = space.xl
section_spacing_bottom = space.xl
```

## 4.3 Content Hierarchy
Следует F-pattern или Z-pattern (из Neuro Design):

- headline  
- subheadline  
- key benefits  
- media  
- CTA  

────────────────────────────────────────
# 5. ACCESSIBILITY (WCAG 2.1 AA)
────────────────────────────────────────

### Основные правила:
- контраст ≥ 4.5:1  
- интерактивные элементы ≥ 44px  
- фокус-состояния всегда видимы  
- motion режим reduce-motion поддерживается  

### Запрещено:
- красный текст на цветных фонах  
- жёлтый текст на белом  
- быстрые flashing animations  

────────────────────────────────────────
# 6. LIVING CONTENT RULES
────────────────────────────────────────

Стиль-гайд автоматически обновляется на основе:

1) UX-исследований (UX_RESEARCH_LIBRARY.json)  
2) CRO-паттернов  
3) поведенческих паттернов  
4) нейро-дизайна  
5) конкурентных трендов  
6) Core Web Vitals  
7) Shopify.changelog  

Если появляются:
- новые UX findings → обновление токенов, сеток, правил  
- новые CRO паттерны → обновление CTA и карточек  
- новые archetypes → обновление текстов, motion, цветов  
- новые performance требования → обновление layout правил  

────────────────────────────────────────
# 7. UX FLOW PATTERNS
────────────────────────────────────────

### PDP Flow
1. Gallery-first  
2. Price + Benefits  
3. CTA  
4. Variants  
5. Social proof  
6. Product info (accordion)

<h3>Cart Flow
- sticky checkout CTA  
- shipping info visible  
- upsell unobtrusive  

<h3>Checkout Flow
- multi-step  
- inline validation  
- progress indicator  

────────────────────────────────────────
# 8. DARK PATTERN RESTRICTIONS
────────────────────────────────────────

Запрещено:
- fake urgency  
- auto-adding items  
- hidden fees  
- confusing CTAs  
- deceptive pricing  

────────────────────────────────────────
# 9. ИНТЕГРАЦИЯ С AXIS
────────────────────────────────────────

<h3>Читает из:
- AXIS_NEURO_DESIGN_LIBRARY.json  
- AXIS_CRO_PATTERNS.json  
- AXIS_COLOR_PSYCHOLOGY.json  
- AXIS_BEHAVIORAL_PATTERNS.json  
- AXIS_ECOMMERCE_ARCHETYPES.json  

<h3>Пишет в:
- design_tokens.json  
- 03_AXIS_MASTER_SYSTEM_v6.2.json  
- 20_AXIS_VISUALIZER.md  

────────────────────────────────────────
# 10. ГЛАВНОЕ ПРАВИЛО LIVING STYLEGUIDE
────────────────────────────────────────

```
Design must be alive, scientific and predictable.
```
