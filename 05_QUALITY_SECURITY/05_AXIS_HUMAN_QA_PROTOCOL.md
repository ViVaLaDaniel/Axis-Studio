# AXIS STUDIOS: HUMAN VISUAL QA CHECKLIST v2.3 (The "Vibe Check")

**PROTOCOL:** Before marking any task as "Done", the Human Operator must physically verify these 10 critical vectors.

**1. THE "FAT THUMB" TEST (Mobile UX)**
* [ ] Open the theme on a real phone (NOT browser dev tools).
* [ ] Try to click buttons with your thumb while holding the phone with one hand.
* [ ] **Pass:** No accidental clicks on neighboring elements. Touch targets are min 44x44px.

**2. THE "SAFARI NIGHTMARE" TEST (Cross-Browser)**
* [ ] Open the site on Safari (iOS or macOS).
* [ ] Check `100vh` sections and sticky bars.
* [ ] **Pass:** The browser's bottom navigation bar does NOT hide content. Sticky elements don't jitter.

**3. THE "KEYBOARD SHOCK" TEST (Input UX)**
* [ ] Click on a search input or email form on mobile.
* [ ] **Pass:** The virtual keyboard pushes the content up; the input field remains visible and focused.

**4. THE "EMPTY STATE" TEST (Data Resilience)**
* [ ] Create a Collection with 0 products.
* [ ] Create a Section but delete all text/images in settings.
* [ ] **Pass:** The theme doesn't crash. It shows a polite "No products found" message or hides the section gracefully.

**5. THE "GHOST SCROLL" TEST (Performance LCP)**
* [ ] Open DevTools (F12) -> Elements Tab.
* [ ] Select the main Hero Image.
* [ ] **Check:** Does the `<img>` tag contain `loading="eager"` AND `fetchpriority="high"`?
* [ ] **Pass:** Attributes are present. No white flashes on rapid scroll.

**6. THE "DATA SPAM" TEST (Layout Stability)**
* [ ] In the Theme Editor, enter a Product Title with 50 words.
* [ ] Upload a non-standard image ratio (e.g., very tall vertical).
* [ ] **Pass:** Layout uses `object-fit: cover` and `clamp()` text sizing. Nothing overlaps.

**7. THE "MERCHANT" TEST (Settings UX)**
* [ ] Open Theme Editor > Section Settings.
* [ ] **Pass:** NO pixel inputs found. Only "Small/Medium/Large" selects or Range Sliders are visible.

**8. THE "SOCIAL SHARE" TEST (Marketing)**
* [ ] Paste the preview link into Telegram/WhatsApp/Twitter validator.
* [ ] **Pass:** The correct "Social Sharing Image" and Description appear (OG Tags check).

**9. THE "STICKY ATC" TEST (Conversion)**
* [ ] Open a Product Page on Mobile.
* [ ] Scroll down past the "Add to Cart" button.
* [ ] **Pass:** A sticky bar appears at the bottom of the screen. It does NOT overlap with the chat widget or footer.

**10. THE "CHAT WIDGET" COLLISION TEST (Z-Index War)**
* [ ] Add a dummy chat widget (or imagine a button at bottom-right).
* [ ] Enable the Sticky ATC bar.
* [ ] **Pass:** The Sticky Bar stops short or has padding, allowing the Chat Widget to remain clickable. Z-index hierarchy is correct.

**11. THE "SCREENREADER" TEST (A11Y)**
* [ ] Navigate the site using only keyboard (Tab key).
* [ ] **Pass:** Focus is visible. Icon-only buttons announce their purpose (e.g., "Close menu").