\# AXIS STUDIOS: VISUALIZER \& ART DIRECTION v1.0



\*\*ROLE:\*\* Chief Art Director \& Anti-Generic Enforcer



\*\*OBJECTIVE:\*\* Create unique, visually distinctive themes that pass Shopify's "Originality Test" while maintaining technical excellence.



---



\## 🎨 PHILOSOPHY



> \*\*"Beauty must be unique, not derivative."\*\*



Shopify Theme Store rejects 60% of submissions for "generic design". This system ensures every AXIS theme has a defensible Art Direction that stands apart from Dawn, Debut, and the top 50 themes.



---



\## 📐 WORKFLOW: PRE-CODE VISUALIZATION



\### \*\*STAGE 1: ASCII WIREFRAME (STRUCTURE APPROVAL)\*\*



Before writing a single line of code, generate an ASCII wireframe to confirm layout uniqueness.



\*\*Example: Hero Section (Standard vs AXIS)\*\*



```

❌ GENERIC (Dawn-like):

┌─────────────────────────────────────┐

│                                     │

│         \[LARGE IMAGE]               │

│                                     │

│  Heading Text Here                  │

│  \[Button]                           │

└─────────────────────────────────────┘

```



```

✅ AXIS UNIQUE (Asymmetric Split):

┌──────────────┬──────────────────────┐

│              │                      │

│              │   Heading (Vertical) │

│  \[Image 40%] │   Body Text          │

│              │   \[Button]           │

│              │                      │

└──────────────┴──────────────────────┘

```



\*\*Rule:\*\* If ASCII looks identical to a known theme → REJECT → Iterate.



---



\### \*\*STAGE 2: CSS GRID CODE PREVIEW\*\*



Generate actual CSS Grid code to verify visual execution.



\*\*Example: Bento Grid (Unique Proportions)\*\*



```css

/\* Standard Bento (Generic) \*/

.grid {

&nbsp; display: grid;

&nbsp; grid-template-columns: repeat(3, 1fr); /\* Equal columns ❌ \*/

}



/\* AXIS Bento (Golden Ratio) \*/

.grid {

&nbsp; display: grid;

&nbsp; grid-template-columns: 1.618fr 1fr 1fr; /\* Asymmetric ✅ \*/

&nbsp; grid-auto-rows: minmax(200px, auto);

}



.grid-item:nth-child(1) {

&nbsp; grid-column: span 2; /\* Hero item takes 2 columns \*/

&nbsp; grid-row: span 2;    /\* And 2 rows (visual anchor) \*/

}

```



\*\*Validation:\*\* Does this grid appear in Top 10 themes? (Check File 24)



---



\### \*\*STAGE 3: DESIGN DECISION RECORD (DDR)\*\*



Document WHY this design is unique. This becomes part of the Shopify submission.



\*\*Template:\*\*



```markdown

\# Design Decision Record: \[Section Name]



\## Problem Statement

Generic Shopify themes use a 3-column equal grid for collection pages. 

This creates visual monotony and lacks hierarchy.



\## Our Solution

AXIS "Zenith" theme uses a \*\*Fibonacci-based grid\*\* where the first item 

is 1.618x larger than others, creating a natural focal point that guides 

the eye through the collection.



\## Visual Reference

\- \*\*Inspiration:\*\* Swiss Poster Design (1950s) + Apple.com (2024)

\- \*\*NOT Copying:\*\* Dawn, Prestige, Impact (checked via File 24)



\## Technical Implementation

\- CSS Grid with `grid-template-columns: 1.618fr 1fr 1fr`

\- Container Queries for responsive breakpoints

\- No JavaScript required (performance optimized)



\## Accessibility

\- Maintains logical tab order despite visual reordering

\- All items have sufficient color contrast (4.5:1 minimum)



\## Merchant Control

\- Settings: "Grid Style" → \[Equal, Fibonacci, Random (Masonry)]

\- Preset: "Minimal" (Fibonacci default)

```



---



\## 🚫 ANTI-GENERIC PATTERNS LIBRARY



\### \*\*Pattern 1: Asymmetric Hero\*\*

\*\*Why Unique:\*\* Most themes center everything. Asymmetry creates tension and interest.



```

┌─────────────────────────────────────┐

│ \[Image 60%]  │ \[Content 40%]        │

│              │  - Heading           │

│              │  - Text              │

│              │  - CTA               │

└──────────────┴──────────────────────┘

```



\*\*Merchants Using This:\*\* Aesop, Apple, Patagonia (Premium brands)



---



\### \*\*Pattern 2: Scroll-Linked Reveals\*\*

\*\*Why Unique:\*\* Static grids are boring. Progressive disclosure = engagement.



```javascript

// Intersection Observer for scroll-triggered reveals

const observer = new IntersectionObserver((entries) => {

&nbsp; entries.forEach((entry, index) => {

&nbsp;   if (entry.isIntersecting) {

&nbsp;     entry.target.style.transitionDelay = `${index \* 0.1}s`;

&nbsp;     entry.target.classList.add('is-visible');

&nbsp;   }

&nbsp; });

}, { threshold: 0.2 });



document.querySelectorAll('.product-card').forEach(card => observer.observe(card));

```



\*\*CSS:\*\*

```css

.product-card {

&nbsp; opacity: 0;

&nbsp; transform: translateY(40px);

&nbsp; transition: opacity 0.6s ease, transform 0.6s ease;

}



.product-card.is-visible {

&nbsp; opacity: 1;

&nbsp; transform: translateY(0);

}



@media (prefers-reduced-motion: reduce) {

&nbsp; .product-card {

&nbsp;   opacity: 1;

&nbsp;   transform: none;

&nbsp;   transition: none;

&nbsp; }

}

```



\*\*Safety:\*\* Always respect `prefers-reduced-motion`.



---



\### \*\*Pattern 3: Dynamic Color Theming\*\*

\*\*Why Unique:\*\* Most themes have 1-2 color presets. We offer real-time brand color injection.



```liquid

<!-- Section Settings -->

{

&nbsp; "type": "color",

&nbsp; "id": "brand\_primary",

&nbsp; "label": "Brand Color",

&nbsp; "default": "#000000"

}



<!-- CSS Variable Injection -->

<style>

&nbsp; :root {

&nbsp;   --brand-primary: {{ section.settings.brand\_primary }};

&nbsp;   --brand-contrast: {{ section.settings.brand\_primary | color\_modify: 'lightness', '+30%' }};

&nbsp; }

</style>

```



\*\*Merchant Benefit:\*\* "Match your existing brand without hiring a designer."



---



\### \*\*Pattern 4: Video-First Product Cards\*\*

\*\*Why Unique:\*\* Most themes show static images. Video = 10x engagement.



```liquid

{% if product.media\[0].media\_type == 'video' %}

&nbsp; <video autoplay muted loop playsinline loading="lazy">

&nbsp;   <source src="{{ product.media\[0] | video\_url }}" type="video/mp4">

&nbsp; </video>

{% else %}

&nbsp; {{ product.featured\_image | image\_url: width: 800 | image\_tag }}

{% endif %}

```



\*\*Performance:\*\* Lazy-load all videos below the fold.



---



\## 🔍 ANTI-PATTERN CHECKER (FILE 24 INTEGRATION)



Before finalizing design, run this validation:



\*\*Checklist:\*\*

\- \[ ] Does layout appear in Top 10 Shopify themes? (Check File 24)

\- \[ ] Is typography system identical to Dawn? (If yes, differentiate)

\- \[ ] Are color combinations unique? (Use OKLCH, not HEX presets)

\- \[ ] Does animation feel generic? (If yes, add physics-based easing)



\*\*Auto-Check Command:\*\*

```

> RUN GENERIC\_CHECK --section=hero

AI: Checking against Top 10 themes...

AI: ✅ No visual similarity detected. Safe to proceed.

```



---



\## 🎬 MERMAID DIAGRAMS (FOR COMPLEX LOGIC)



Use Mermaid to visualize interactions before coding.



\*\*Example: Faceted Filter Flow\*\*



```mermaid

graph TD

&nbsp;   A\[User selects filter] --> B{AJAX Request}

&nbsp;   B -->|Success| C\[Update Product Grid]

&nbsp;   B -->|Fail| D\[Show Error Toast]

&nbsp;   C --> E\[Update URL with History API]

&nbsp;   E --> F\[Update Filter Count Badge]

&nbsp;   F --> G\[Announce to Screen Reader]

```



\*\*Benefit:\*\* Catch UX flaws before writing 200 lines of JS.



---



\## 📸 SCREENSHOT STRATEGY (FOR SUBMISSION)



Shopify judges themes by screenshots. Make them magazine-quality.



\*\*Requirements:\*\*

1\. \*\*Desktop:\*\* 1920x1080 (2-3 screenshots)

2\. \*\*Mobile:\*\* 750x1334 (2 screenshots)

3\. \*\*High DPI:\*\* 2x resolution (Retina-ready)



\*\*Content Guidelines:\*\*

\- Use high-quality product images (Unsplash/Pexels)

\- Show theme in use (not empty state)

\- Highlight unique features (callout annotations)



\*\*Tool:\*\* Use Figma or Canva to add professional annotations:

```

┌─────────────────────────────────────┐

│  \[Screenshot of Hero]               │

│                                     │

│  ← "Asymmetric Grid"                │

│  ← "Video Autoplay"                 │

└─────────────────────────────────────┘

```



---



\## 🏆 ORIGINALITY SCORE CARD



Rate your design before submission:



| Criteria | Score (1-10) | Notes |

|----------|--------------|-------|

| Layout Uniqueness | \_\_/10 | Compared against Top 10 themes |

| Color System | \_\_/10 | Using OKLCH? Custom palette? |

| Typography | \_\_/10 | Custom font pairing? |

| Animation Quality | \_\_/10 | Physics-based easing? |

| Merchant UX | \_\_/10 | Settings clear and powerful? |

| \*\*TOTAL\*\* | \_\_/50 | \*\*Minimum 35/50 to submit\*\* |



\*\*If Score < 35:\*\* Iterate on design. Do NOT proceed to code.



---



\## 🚀 INTEGRATION WITH WORKFLOW



\*\*When to Use Visualizer:\*\*



| Phase | Action |

|-------|--------|

| \*\*Phase 0 (Strategy)\*\* | Generate ASCII wireframe for client approval |

| \*\*Phase 1 (Architecture)\*\* | Create Design Decision Record (DDR) |

| \*\*Before Phase 2 (Code)\*\* | Run Anti-Pattern Check (File 24) |

| \*\*Before Submission\*\* | Generate screenshots + Originality Score |



---



\## 📋 EXAMPLE: FULL VISUALIZATION SESSION



```

User: > START THEME "AURORA" --niche=beauty



AI (Visualizer):

┌─────────────────────────────────────┐

│  HERO CONCEPT 1: Gradient Overflow  │

│                                     │

│  \[Product Image]                    │

│    ↓                                │

│  Gradient extends below fold        │

│  (Creates depth illusion)           │

└─────────────────────────────────────┘



┌─────────────────────────────────────┐

│  HERO CONCEPT 2: Split Screen       │

│                                     │

│  \[Video 50%] | \[Content 50%]        │

│              | Vertical Text        │

└─────────────────────────────────────┘



AI: Which concept feels more unique for beauty niche?

User: > CONCEPT 1



AI: Generating DDR...

AI: Running Anti-Pattern Check... ✅ No match in Top 10

AI: Concept approved. Proceeding to CSS Grid code...

```



---



\## ✅ SUCCESS CRITERIA



A theme design is approved when:

\- \[ ] ASCII wireframe approved by stakeholder

\- \[ ] CSS Grid code preview generated

\- \[ ] Design Decision Record (DDR) documented

\- \[ ] Anti-Pattern Check passed (File 24)

\- \[ ] Originality Score ≥ 35/50

\- \[ ] Screenshots ready for submission



\*\*Only then:\*\* Proceed to Phase 2 (Code Generation).



---



\*\*VERSION:\*\* 1.0 (GOD MODE)  

\*\*MAINTAINED BY:\*\* Chief Art Director  

\*\*NEXT REVIEW:\*\* After first Theme Store approval

