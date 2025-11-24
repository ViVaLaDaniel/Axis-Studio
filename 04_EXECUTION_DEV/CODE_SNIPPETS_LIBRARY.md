# CODE_SNIPPETS_LIBRARY.md  
AXIS_ROOT v10.5 — Production Snippets Library  
(Reusable, Composable, Performance-Optimized Code Patterns)

Эта библиотека содержит стандартизированные, проверенные, производительные сниппеты Liquid/JS/CSS, используемые AXIS OS во всех секциях и шаблонах.

Каждый сниппет:
- чистый и атомарный,
- не содержит inline-логики,
- использует strict architecture patterns,
- оптимизирован под Core Web Vitals,
- соответствует Performance Budget,
- подключается через {% render %}.

────────────────────────────────────────
# 1. PRICE SNIPPET (price.liquid)
────────────────────────────────────────

**Паттерн:** Single Source Price Renderer  
**Правила:**  
- никакой логики в шаблонах,  
- форматирование через Intl.NumberFormat,  
- поддержка продажных цен.

```liquid
<span class="price">
  {% if product.compare_at_price > product.price %}
    <span class="price--old">{{ product.compare_at_price | money_without_trailing_zeros }}</span>
  {% endif %}
  <span class="price--current">{{ product.price | money_without_trailing_zeros }}</span>
</span>
```
```javascript
// JS Price Formatter (Используется в JS-компонентах)
export const formatPrice = (value, currency = 'USD') => {
  return new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency,
    minimumFractionDigits: 0
  }).format(value / 100);
};
```

────────────────────────────────────────
# 2. BADGES SNIPPET (badges.liquid)
────────────────────────────────────────

```liquid
{% if product.available == false %}
  <span class="badge badge--soldout">Sold Out</span>
{% elsif product.compare_at_price > product.price %}
  <span class="badge badge--sale">Sale</span>
{% endif %}
```
```css
/* CSS Tokens Integration */
.badge { 
  background: var(--color-energy-default);
  padding: var(--space-xs) var(--space-sm);
  font-size: var(--font-size-sm);
  border-radius: 4px;
}
```

────────────────────────────────────────
# 3. PRODUCT MEDIA SNIPPET (media.liquid)
────────────────────────────────────────

```liquid
<div class="product-media">
  {% for image in product.images %}
    <img 
      src="{{ image | image_url: width: 1200 }}" 
      alt="{{ image.alt | escape }}"
      loading="lazy"
      width="1200"
      height="auto"
    >
  {% endfor %}
</div>
```
```javascript
// JS: Gallery Interaction
const gallery = document.querySelector('.product-media');
gallery?.addEventListener('click', (e) => {
  if (e.target.tagName === 'IMG') {
    e.target.classList.toggle('zoomed');
  }
});
```

────────────────────────────────────────
# 4. VARIANT SELECTOR SNIPPET (variant-selector.liquid)
────────────────────────────────────────

```liquid
<div class="variant-selector" data-variants="{{ product.variants | json }}">
  {% for option in product.options_with_values %}
    <div class="variant-option">
      <span class="variant-option__name">{{ option.name }}</span>
      <div class="variant-option__values">
        {% for value in option.values %}
          <button 
            class="variant-btn" 
            data-option="{{ option.name }}" 
            data-value="{{ value }}"
          >
            {{ value }}
          </button>
        {% endfor %}
      </div>
    </div>
  {% endfor %}
</div>
```
```javascript
// JS Variant Engine (Vanilla JS)
export const VariantSelector = () => {
  const container = document.querySelector('.variant-selector');
  if (!container) return;

  const variants = JSON.parse(container.dataset.variants);
  const buttons = container.querySelectorAll('.variant-btn');

  buttons.forEach(btn => {
    btn.addEventListener('click', () => {
      btn.parentNode
        .querySelectorAll('.variant-btn')
        .forEach(b => b.classList.remove('active'));

      btn.classList.add('active');

      const selected = {};
      container.querySelectorAll('.variant-btn.active').forEach(active => {
        selected[active.dataset.option] = active.dataset.value;
      });

      const match = variants.find(v => {
        return Object.keys(selected)
          .every(k => v.options.includes(selected[k]));
      });

      document.dispatchEvent(new CustomEvent("variant:change", {
        detail: { variant: match }
      }));
    });
  });
};
```

────────────────────────────────────────
# 5. INTERSECTION OBSERVER PATTERN (reveal.js)
────────────────────────────────────────

```javascript
export const revealOnScroll = () => {
  const elements = document.querySelectorAll('[data-reveal]');
  const io = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('revealed');
        io.unobserve(entry.target);
      }
    });
  }, { threshold: 0.2 });

  elements.forEach(el => io.observe(el));
};
```
```css
/* CSS token-based reveal */
[data-reveal] {
  opacity: 0;
  transform: translateY(12px);
  transition: opacity var(--motion-primary), transform var(--motion-primary);
}

.revealed {
  opacity: 1;
  transform: translateY(0);
}
```

────────────────────────────────────────
# 6. STICKY ATC BAR (mobile)
────────────────────────────────────────

```liquid
<div id="sticky-atc" hidden>
  <button class="btn-primary">Add to cart</button>
</div>
```
```javascript
// JS:
export const stickyATC = () => {
  const atc = document.getElementById('sticky-atc');
  const target = document.querySelector('.product-form');

  const io = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      atc.hidden = entry.isIntersecting;
    });
  });

  io.observe(target);
};
```

────────────────────────────────────────
# 7. CART MICRO-INTERACTION (pulse)
────────────────────────────────────────

```javascript
export const cartPulse = () => {
  const el = document.querySelector('.cart-icon');
  if (!el) return;
  el.classList.add('pulse');
  setTimeout(() => el.classList.remove('pulse'), 300);
};
```

────────────────────────────────────────
# 8. SIGNALS INTEGRATION
────────────────────────────────────────

Каждый JS-модуль может отправлять сигналы AXIS:

```javascript
document.dispatchEvent(new CustomEvent("DEV.ERROR.CAUGHT", {
  detail: { message: "Variant mismatch", module: "variant-selector" }
}));
```

────────────────────────────────────────
# 9. ГЛАВНОЕ ПРАВИЛО AXIS CODE LIBRARY
────────────────────────────────────────

Clean components.  
No inline logic.  
Vanilla JS only.  
Maximum performance.  
Reuse everywhere.
