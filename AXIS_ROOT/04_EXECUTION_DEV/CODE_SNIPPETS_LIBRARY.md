# CODE_SNIPPETS_LIBRARY.md
AXIS_ROOT v10.5 — Code Snippets Library

Эта библиотека содержит переиспользуемые сниппеты кода, соответствующие стандартам AXIS OS для Liquid, JavaScript и CSS.

---

## Liquid Snippets

### 1. Проверка наличия объекта и его свойства

```liquid
{%- liquid
  assign object_exists = false
  if product and product.title != blank
    assign object_exists = true
  endif
%}
{%- if object_exists -%}
  <p>{{ product.title }}</p>
{%- endif -%}
```

### 2. Форматирование цены

```liquid
{%- capture formatted_price -%}
  {{ product.price | money }}
{%- endcapture -%}
<span class="product-price">{{ formatted_price }}</span>
```

---

## JavaScript Snippets

### 1. Dispatch AXIS Signal

```javascript
document.dispatchEvent(new CustomEvent("AXIS.DATA.UPDATED", {
  detail: {
    module: "cart",
    data: {
      items: /* updated cart items */
    }
  }
}));
```

### 2. Использование IntersectionObserver для Lazy Load

```javascript
const lazyLoadObserver = new IntersectionObserver((entries, observer) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const img = entry.target;
      const src = img.getAttribute('data-src');
      if (src) {
        img.src = src;
        img.removeAttribute('data-src');
        observer.unobserve(img);
      }
    }
  });
});

document.querySelectorAll('img[data-src]').forEach(img => {
  lazyLoadObserver.observe(img);
});
```

---

## CSS Snippets

### 1. Использование Design Tokens

```css
.button-primary {
  background-color: var(--color-trust-default);
  color: var(--color-neutral-white);
  padding: var(--spacing-md) var(--spacing-lg);
  border-radius: var(--borderRadius-md);
  transition: background-color var(--motion-duration-normal) var(--motion-easing-ease-in-out);
}

.button-primary:hover {
  background-color: var(--color-trust-dark);
}
```

### 2. Mobile-first медиа-запрос

```css
.container {
  padding: var(--spacing-md); /* Mobile default */
}

@media screen and (min-width: 768px) {
  .container {
    padding: var(--spacing-lg); /* Tablet and up */
  }
}
```
