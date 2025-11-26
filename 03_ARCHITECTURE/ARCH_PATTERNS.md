# ARCH_PATTERNS.md  
AXIS_ROOT v10.5 â€” Architectural Patterns of Shopify OS Themes

Ð­Ñ‚Ð¾Ñ‚ Ð´Ð¾ÐºÑƒÐ¼ÐµÐ½Ñ‚ â€” Ñ„ÑƒÐ½Ð´Ð°Ð¼ÐµÐ½Ñ‚Ð°Ð»ÑŒÐ½Ð°Ñ Ð±Ð¸Ð±Ð»Ð¸Ð¾Ñ‚ÐµÐºÐ° Ð°Ñ€Ñ…Ð¸Ñ‚ÐµÐºÑ‚ÑƒÑ€Ð½Ñ‹Ñ… Ð¿Ð°Ñ‚Ñ‚ÐµÑ€Ð½Ð¾Ð² Ð´Ð»Ñ AXIS OS.  
ÐžÐ½ Ð¾Ð¿Ñ€ÐµÐ´ÐµÐ»ÑÐµÑ‚ Ð¿Ñ€Ð°Ð²Ð¸Ð»Ð° Ð¸Ð½Ð¶ÐµÐ½ÐµÑ€Ð¸Ð¸ Shopify-Ñ‚ÐµÐ¼, ÑÑ‚Ñ€ÑƒÐºÑ‚ÑƒÑ€Ñƒ ÑÐµÐºÑ†Ð¸Ð¹, ÑˆÐ°Ð±Ð»Ð¾Ð½Ð¾Ð², Ð´Ð°Ð½Ð½Ñ‹Ñ…, Ð·Ð°Ð²Ð¸ÑÐ¸Ð¼Ð¾ÑÑ‚ÐµÐ¹ Ð¸ Ð¶Ð¸Ð·Ð½ÐµÐ½Ð½Ñ‹Ð¹ Ñ†Ð¸ÐºÐ» ÐºÐ¾Ð¼Ð¿Ð¾Ð·Ð¸Ñ†Ð¸Ð¸ Ð¸Ð½Ñ‚ÐµÑ€Ñ„ÐµÐ¹ÑÐ°.

AXIS Ð¸ÑÐ¿Ð¾Ð»ÑŒÐ·ÑƒÐµÑ‚ ÑÑ‚Ð¸ Ð¿Ð°Ñ‚Ñ‚ÐµÑ€Ð½Ñ‹ Ð´Ð»Ñ:
- Ð¿Ñ€Ð¾ÐµÐºÑ‚Ð¸Ñ€Ð¾Ð²Ð°Ð½Ð¸Ñ Ñ‚ÐµÐ¼ Ñ Ð½ÑƒÐ»Ñ,
- Ð°Ð½Ð°Ð»Ð¸Ð·Ð° Ð¿Ñ€Ð¾Ð±Ð»ÐµÐ¼ Ð°Ñ€Ñ…Ð¸Ñ‚ÐµÐºÑ‚ÑƒÑ€Ñ‹,
- Ð³ÐµÐ½ÐµÑ€Ð°Ñ†Ð¸Ð¸ ÑÐµÐºÑ†Ð¸Ð¹,
- Ð¿Ð¾ÑÑ‚Ñ€Ð¾ÐµÐ½Ð¸Ñ UX-Ð¿Ð¾Ñ‚Ð¾ÐºÐ¾Ð²,
- Ð¿Ñ€ÐµÐ´Ð¾Ñ‚Ð²Ñ€Ð°Ñ‰ÐµÐ½Ð¸Ñ "Ñ‚ÑÐ¶Ñ‘Ð»Ñ‹Ñ…" Ð¸ Ð½ÐµÑƒÐ¿Ñ€Ð°Ð²Ð»ÑÐµÐ¼Ñ‹Ñ… ÑˆÐ°Ð±Ð»Ð¾Ð½Ð¾Ð²,
- Ð¸Ð½Ñ‚ÐµÐ³Ñ€Ð°Ñ†Ð¸Ð¸ Best Practices Shopify OS 2.0.

â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
# 1. Ð“Ð›ÐÐ’ÐÐ«Ð• ÐŸÐ Ð˜ÐÐ¦Ð˜ÐŸÐ« ÐÐ Ð¥Ð˜Ð¢Ð•ÐšÐ¢Ð£Ð Ð« AXIS OS
â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€

## 1.1 ÐžÑÐ½Ð¾Ð²Ð°: ÐœÐ¾Ð´ÑƒÐ»ÑŒÐ½Ð¾ÑÑ‚ÑŒ
ÐšÐ°Ð¶Ð´Ñ‹Ð¹ Ð±Ð»Ð¾Ðº Ñ‚ÐµÐ¼Ñ‹ â€” Ð°Ð²Ñ‚Ð¾Ð½Ð¾Ð¼Ð½Ñ‹Ð¹ Ð¼Ð¾Ð´ÑƒÐ»ÑŒ:
- Section  
- Snippet  
- ASSET (style/js)  
- Template  
- JSON Template Schema  

ÐœÐ¾Ð´ÑƒÐ»ÑŒ Ð½Ðµ Ð´Ð¾Ð»Ð¶ÐµÐ½ Ð·Ð°Ð²Ð¸ÑÐµÑ‚ÑŒ Ð¾Ñ‚ ÐºÐ¾Ð½ÐºÑ€ÐµÑ‚Ð½Ð¾Ð³Ð¾ Ð¼ÐµÑÑ‚Ð° Ð² Ð´ÐµÑ€ÐµÐ²Ðµ.

## 1.2 Ð§Ð¸ÑÑ‚Ð¾Ñ‚Ð° ÑˆÐ°Ð±Ð»Ð¾Ð½Ð¾Ð²


Templates must contain ZERO business logic.

Ð’ÐµÑÑŒ Ñ„ÑƒÐ½ÐºÑ†Ð¸Ð¾Ð½Ð°Ð» â†’ Ð² sections/snippets.

## 1.3 ÐžÐ´Ð½Ð¾ ÐžÑ‚Ð²ÐµÑ‚ÑÑ‚Ð²ÐµÐ½Ð½Ð¾Ðµ ÐœÐµÑÑ‚Ð¾
ÐšÐ°Ð¶Ð´Ñ‹Ð¹ Ð¼Ð¾Ð´ÑƒÐ»ÑŒ Ð¸Ð¼ÐµÐµÑ‚ ÑÐ¼Ñ‹ÑÐ» Ð¸ Ð·Ð°Ð´Ð°Ñ‡Ñƒ.  
ÐÐ¸ÐºÐ°ÐºÐ¸Ñ… Ð´ÑƒÐ±Ð»Ð¸Ñ€Ð¾Ð²Ð°Ð½Ð¸Ð¹.  
ÐšÐ°Ð¶Ð´Ð°Ñ ÑÑƒÑ‰Ð½Ð¾ÑÑ‚ÑŒ = Ð¾Ð´Ð¸Ð½ Ð¸ÑÑ‚Ð¾Ñ‡Ð½Ð¸Ðº Ð¸ÑÑ‚Ð¸Ð½Ñ‹.

## 1.4 Ð’ÐµÑ€Ñ‚Ð¸ÐºÐ°Ð»ÑŒÐ½Ð°Ñ Ð¸ Ð“Ð¾Ñ€Ð¸Ð·Ð¾Ð½Ñ‚Ð°Ð»ÑŒÐ½Ð°Ñ ÐšÐ¾Ð¼Ð¿Ð¾Ð·Ð¸Ñ†Ð¸Ñ
- Vertical: hero â†’ content â†’ CTA â†’ grid â†’ footer  
- Horizontal: multi-column, multi-card patterns  

## 1.5 Reusability First (Ð¿Ð¾Ð²Ñ‚Ð¾Ñ€Ð½Ð¾Ðµ Ð¸ÑÐ¿Ð¾Ð»ÑŒÐ·Ð¾Ð²Ð°Ð½Ð¸Ðµ)
ÐšÐ¾Ð¼Ð¿Ð¾Ð½ÐµÐ½Ñ‚Ñ‹ Ð¿Ñ€Ð¾ÐµÐºÑ‚Ð¸Ñ€ÑƒÑŽÑ‚ÑÑ Ñ‚Ð°Ðº, Ñ‡Ñ‚Ð¾Ð±Ñ‹ Ð¸ÑÐ¿Ð¾Ð»ÑŒÐ·Ð¾Ð²Ð°Ñ‚ÑŒÑÑ Ð² Ñ€Ð°Ð·Ð½Ñ‹Ñ… ÑÐµÐºÑ†Ð¸ÑÑ….

## 1.6 Multi-level Theming
Ð¦Ð²ÐµÑ‚, motion, spacing, typography â†’ Ñ‡ÐµÑ€ÐµÐ· design_tokens.json.  
Ð¢ÐµÐ¼Ð° Ð½Ð¸ÐºÐ¾Ð³Ð´Ð° Ð½Ðµ Ð¶Ñ‘ÑÑ‚ÐºÐ¾ Ð¼ÐµÐ½ÑÐµÑ‚ÑÑ Ð² CSS.

## 1.7 Performance Budget  
Ð›ÑŽÐ±Ð¾Ð¹ ÑˆÐ°Ð±Ð»Ð¾Ð½ Ð´Ð¾Ð»Ð¶ÐµÐ½ ÑÐ¾Ð±Ð»ÑŽÐ´Ð°Ñ‚ÑŒ:
- â‰¤ 30KB JS  
- â‰¤ 80KB CSS  
- LCP â‰¤ 2.5s  

â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
# 2. ÐŸÐÐ¢Ð¢Ð•Ð ÐÐ« Ð¡Ð•ÐšÐ¦Ð˜Ð™ (SECTION PATTERNS)
â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€

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
- ideal for catalogs with â‰¤ 100 products  
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
- reduces cognitive load (Hickâ€™s Law)

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

â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
# 3. ÐŸÐÐ¢Ð¢Ð•Ð ÐÐ« Ð”ÐÐÐÐ«Ð¥ (DATA PATTERNS)
â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€

## 3.1 Single Source Pattern
Ð’ÑÐµ Ð´Ð°Ð½Ð½Ñ‹Ðµ Ñ‚Ð¾Ð²Ð°Ñ€Ð° Ð´Ð¾Ð»Ð¶Ð½Ñ‹ Ð¿Ð¾ÑÑ‚ÑƒÐ¿Ð°Ñ‚ÑŒ Ð¸Ð· ÐµÐ´Ð¸Ð½Ð¾Ð³Ð¾ Ð¾Ð±ÑŠÐµÐºÑ‚Ð° product.

## 3.2 Schema-Driven UI
ÐšÐ°Ð¶Ð´Ð°Ñ ÑÐµÐºÑ†Ð¸Ñ Ð¸Ð¼ÐµÐµÑ‚ JSON schema:
- settings  
- blocks  
- presets  
- conditional elements  

## 3.3 Content Projection Pattern
Ð¡ÐµÐºÑ†Ð¸Ñ Ð´Ð¾Ð»Ð¶Ð½Ð° Ð¿Ð¾Ð´Ð´ÐµÑ€Ð¶Ð¸Ð²Ð°Ñ‚ÑŒ Ð´Ð¸Ð°Ð³Ñ€Ð°Ð¼Ð¼Ñƒ ÐºÐ¾Ð½Ñ‚ÐµÐ½Ñ‚Ð°:
- main content  
- optional areas  
- override areas  

â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
# 4. ÐŸÐÐ¢Ð¢Ð•Ð ÐÐ« Ð¨ÐÐ‘Ð›ÐžÐÐžÐ’ (TEMPLATE PATTERNS)
â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€

## 4.1 Thin Template Pattern
ÐŸÑ€Ð°Ð²Ð¸Ð»Ð¾ Shopify OS:


Templates should remain nearly empty.

Ð¨Ð°Ð±Ð»Ð¾Ð½ Ð²Ñ‹Ð·Ñ‹Ð²Ð°ÐµÑ‚ ÑÐµÐºÑ†Ð¸Ð¸ â†’ ÑÐµÐºÑ†Ð¸Ð¸ ÑƒÐ¿Ñ€Ð°Ð²Ð»ÑÑŽÑ‚ Ð»Ð¾Ð³Ð¸ÐºÐ¾Ð¹.

## 4.2 Template Split Pattern  
Ð•ÑÐ»Ð¸ Ñ„Ð°Ð¹Ð» > 20 ÑÐµÐºÑ†Ð¸Ð¹ â†’ split using 16_TEMPLATE_SPLITTER_TOOL.md.

## 4.3 View Composition Pattern  
ÐšÐ°Ð¶Ð´Ñ‹Ð¹ ÑˆÐ°Ð±Ð»Ð¾Ð½ Ð¾Ð¿Ð¸ÑÑ‹Ð²Ð°ÐµÑ‚ Ñ‚Ð¾Ð»ÑŒÐºÐ¾:
- ÐºÐ°ÐºÐ¸Ðµ ÑÐµÐºÑ†Ð¸Ð¸  
- Ð¿Ð¾Ñ€ÑÐ´Ð¾Ðº ÑÐµÐºÑ†Ð¸Ð¹  
- Ð¿Ð°Ñ€Ð°Ð¼ÐµÑ‚Ñ€Ñ‹ ÑÐµÐºÑ†Ð¸Ð¹  

â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
# 5. ÐŸÐÐ¢Ð¢Ð•Ð ÐÐ« SNIPPETS
â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€

## 5.1 Functional Snippets  
Ð¤ÑƒÐ½ÐºÑ†Ð¸Ð¸:
- price  
- variant selector  
- breadcrumbs  
- badges  

## 5.2 Reusable Snippets
Ð”Ð¾Ð»Ð¶Ð½Ñ‹ Ð¸ÑÐ¿Ð¾Ð»ÑŒÐ·Ð¾Ð²Ð°Ñ‚ÑŒÑÑ Ð²Ð¾ Ð¼Ð½Ð¾Ð³Ð¸Ñ… ÑÐµÐºÑ†Ð¸ÑÑ…:
- media  
- badges system  
- rating stars  
- buttons  

## 5.3 High-frequency Snippets  
ÐšÐ°Ð½Ð´Ð¸Ð´Ð°Ñ‚Ñ‹ Ð½Ð° inline optimization:
- price  
- inventory  
- rating  

â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
# 6. ÐŸÐÐ¢Ð¢Ð•Ð ÐÐ« JS / INTERACTION LAYER
â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€

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
ÐšÐ°Ð¶Ð´Ñ‹Ð¹ JS-Ð¼Ð¾Ð´ÑƒÐ»ÑŒ â†’ Ñ€ÐµÐ°Ð³Ð¸Ñ€ÑƒÐµÑ‚ Ð½Ð° ÑÐ¸Ð³Ð½Ð°Ð»Ñ‹ AXIS OS:


ARCH.CHANGE
PERFORMANCE.WARNING
KNOWLEDGE.UPDATE


â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
# 7. ARCHITECTURAL ANTI-PATTERNS (Ð§Ð¢Ðž Ð—ÐÐŸÐ Ð•Ð©Ð•ÐÐž)
â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€

### âŒ Fat templates  
### âŒ Inline styles  
### âŒ Hardcoded values  
### âŒ Business logic in templates  
### âŒ Six-level nested HTML  
### âŒ Sections with > 300 lines  
### âŒ Snippets duplicated across sections  

â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
# 8. ÐÐ Ð¥Ð˜Ð¢Ð•ÐšÐ¢Ð£Ð ÐÐ«Ð™ PIPELINE AXIS
â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€

## Step 1 â€” Strategy (02_STRATEGY_CREATIVE)
UX, CRO, Neuro Ñ€ÐµÑˆÐ°ÑŽÑ‚ Ð¿Ð°Ñ‚Ñ‚ÐµÑ€Ð½Ñ‹.

<h2>Step 2 â€” Architect (03_ARCHITECTURE)
ÐÑ€Ñ…Ð¸Ñ‚ÐµÐºÑ‚Ð¾Ñ€ ÑÐ¾Ð±Ð¸Ñ€Ð°ÐµÑ‚ ÑÑ‚Ñ€ÑƒÐºÑ‚ÑƒÑ€Ñƒ Ð¸ Ð·Ð°Ð²Ð¸ÑÐ¸Ð¼Ð¾ÑÑ‚Ð¸.

<h2>Step 3 â€” Execution Dev (04_EXECUTION_DEV)
Ð¡Ð¾Ð·Ð´Ð°Ñ‘Ñ‚ÑÑ ÐºÐ¾Ð´ ÑÐµÐºÑ†Ð¸Ð¹, snippets.

<h2>Step 4 â€” QA (05_QUALITY_SECURITY)
Performance + security + accessibility.

<h2>Step 5 â€” Release (06_CI_CD_RELEASE)
Pack â†’ preview store â†’ compliance check.

â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
# 9. Ð˜ÐÐ¢Ð•Ð“Ð ÐÐ¦Ð˜Ð¯ Ð¡ AXIS OS
â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€

### Ð§Ð¸Ñ‚Ð°ÐµÑ‚:
- AXIS_NEURO_DESIGN_LIBRARY.json  
- AXIS_CRO_PATTERNS.json  
- AXIS_BEHAVIORAL_PATTERNS.json  

### ÐŸÐ¸ÑˆÐµÑ‚:
- DATA_FLOWS.md  
- SPEC_LIVING_STYLEGUIDE.md  
- 03_AXIS_MASTER_SYSTEM_v6.2.json  

â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
# 10. Ð“Ð›ÐÐ’ÐÐžÐ• ÐŸÐ ÐÐ’Ð˜Ð›Ðž:
â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€


Architecture should simplify, never complicate.

