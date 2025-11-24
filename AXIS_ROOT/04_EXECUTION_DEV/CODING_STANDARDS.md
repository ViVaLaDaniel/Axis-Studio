# CODING_STANDARDS.md  
AXIS_ROOT v10.5 — Coding Standards & Engineering Constitution  
(Единая техническая конституция для Liquid, JS, CSS и архитектуры AXIS OS)

Цель документа — формировать предсказуемый, производительный, безопасный и гибкий код, который соответствует требованиям Shopify OS 2.0 и архитектуре AXIS OS.

────────────────────────────────────────
# 1. ОБЩИЕ ПРИНЦИПЫ AXIS OS
────────────────────────────────────────

1) **Simple > Clever**  
Код должен быть понятен без пояснений.

2) **Predictable Architecture**  
Поведение секций, шаблонов и JS всегда детерминировано.

3) **Performance First**  
Каждая строка кода должна уважать Performance Budget.

4) **Design Tokens Only**  
Никаких жёстко зашитых цветов, отступов, тени, шрифтов.

5) **No Redundancy**  
Повторяющаяся логика → в snippets.

6) **Security Always Active**  
Никаких inline-скриптов, eval, data injection без escape.

7) **Accessibility = Core**  
Любой компонент должен соответствовать WCAG 2.1 AA.

────────────────────────────────────────
# 2. LIQUID STANDARDS
────────────────────────────────────────

## 2.1 Запрещено:
- ❌ логика бизнес-правил в шаблонах  
- ❌ вложенные условия более чем на 2 уровня  
- ❌ цикл for с > 3 действиями внутри  
- ❌ использование `img_url` (устарело)  
- ❌ inline CSS  
- ❌ огромные Liquid-файлы > 300 строк  

## 2.2 Правила разметки

### 1. Templates should be empty


{% section 'hero' %}
{% section 'product-grid' %}


### 2. Sections = logic + layout  
Внутри секции:
- настройки  
- blocks  
- Liquid-структура  
- минимум логики  
- максимальная читаемость  

### 3. Snippets = функциональные компоненты  
Цены, бейджи, медиа, рейтинг, скидки → только snippets.

### 4. Комментарии формата:


{%- comment -%} AXIS: describes purpose of block {%- endcomment -%} 


---

# 3. JAVASCRIPT STANDARDS (ES6+)
────────────────────────────────────────

## 3.1 Запрещено:
- ❌ jQuery  
- ❌ Lodash  
- ❌ inline скрипты  
- ❌ манипуляции DOM без проверки существования  
- ❌ таймеры без реальной необходимости  
- ❌ анимации через JS (если не требуется)  

## 3.2 Обязательные стандарты

### 1. Strict Modules
Каждый модуль должен быть замкнутым: 


export const Gallery = () => { ... };


### 2. Использовать IntersectionObserver  
Для:
- lazy load  
- reveal  
- sticky  
- наблюдения поведения  

### 3. Dispatch AXIS Signals
Пример: 


document.dispatchEvent(new CustomEvent("DEV.ERROR.CAUGHT", {
detail: { module: "variant", error: "invalid mapping" }
}));


### 4. Data-first архитектура
JS работает только с:
- `data-*`
- JSON payload  
- signals  

### 5. Никакого дублирования логики
Если JS повторяется → выносится в global-utils.js.

---

# 4. CSS / SCSS СТАНДАРТЫ
────────────────────────────────────────

## 4.1 Запрещено:
- ❌ фиксированные цвета  
- ❌ фиксированные отступы  
- ❌ жёсткие px если есть токен  
- ❌ inline-styles  
- ❌ @.cargo\registry\src\index.crates.io-6f17d22bba15001f\pin-project-1.1.8\tests\ui\pin_project\import_unnamed.rs (использовать @AppData\Local\Packages\Microsoft.WindowsNotepad_8wekyb3d8bbwe\SystemAppData\Helium\User.dat)  

## 4.2 Обязательные правила

### 1. Использовать Design Tokens 


color: var(--color-trust-default);
padding: var(--space-md);
transition: var(--motion-primary);


### 2. Mobile-first  
Стили начинаются с мобильного.

### 3. Utility-first (ограничено)
Только критические классы:
- .hidden  
- .visually-hidden  

### 4. Components Anatomy
Компонент =  
- root  
- sub-element  
- modifiers  

Пример: 


.card {}
.card__media {}
.card--featured {}


---

# 5. NAMING RULES
────────────────────────────────────────

## 5.1 Liquid Naming 


section: hero.liquid
snippet: price.liquid
template: product.json


## 5.2 CSS Naming — BEM 


btn
btn--primary
btn__icon


## 5.3 JS Naming 


VariantSelector
CartDrawer
StickyATC


## 5.4 Token Naming 


color.energy.default
font.size.lg
space.md
motion.duration.primary


---

# 6. ACCESSIBILITY STANDARDS
────────────────────────────────────────

- контраст ≥ 4.5:1  
- интерактивные области ≥ 44px  
- видимые focus states  
- поддержка prefers-reduced-motion  
- aria-labels для всех значимых элементов  
- semantic HTML обязательный  
- avoid div soup  

---

# 7. SECURITY STANDARDS
────────────────────────────────────────

- никогда не рендерить user input без escape  
- избегать inline JS  
- запрещён `{{ content_for_header }}` без фильтрации  
- проверять внешние скрипты (CSP-ready)  
- event listeners — только безопасные узлы  

---

# 8. PERFORMANCE BUDGET STANDARDS
────────────────────────────────────────

### JS:
- ≤ 30KB на страницу  
- динамические импорты для тяжёлых фич  

### CSS:
- ≤ 80KB  
- критические стили — inline only для LCP  

### Liquid:
- минимизация циклов  
- минимизация условий  

### Media:
- WebP  
- lazy load  
- responsive sizes  

---

# 9. COMPONENT ARCHITECTURE RULES
────────────────────────────────────────

## 9.1 Компонент должен быть:
- атомарным  
- тестируемым  
- изолированным  
- управляемым токенами  
- без побочных эффектов  

## 9.2 Component contract:
- входные данные  
- внутреннее состояние  
- визуальное состояние  

## 9.3 Запрещено:
- изменять DOM без проверки  
- менять глобальные состояния напрямую  
- использовать JS вместо CSS transition  

---

# 10. AXIS SIGNALS COMPLIANCE
────────────────────────────────────────

Любой компонент должен:

### 1) Получать сигналы


document.addEventListener("ARCH.UPDATE", ...)


### 2) Отправлять сигналы


document.dispatchEvent(...)


### 3) Логировать критические ошибки в Memory Log  

---

# 11. ФАЙЛОВАЯ АРХИТЕКТУРА
────────────────────────────────────────



/sections
/snippets
/assets/js/components
/assets/js/utils
/assets/css/components
/templates


---

# 12. ГЛАВНОЕ ПРАВИЛО AXIS CODING OS
────────────────────────────────────────



Код должен быть чистым, быстрым, предсказуемым и научно обоснованным.
