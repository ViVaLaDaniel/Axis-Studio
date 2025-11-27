# Risk Register

## 1. Technical Risks

### TR-01: LLM Browser Automation Fragility
*   **Description:** The `GeminiBrowserProvider` relies on Selenium interacting with the DOM of `gemini.google.com`.
*   **Probability:** Very High (90%)
*   **Impact:** Critical (System stops working)
*   **Mitigation:**
    1.  **Immediate:** Implement `APIProvider` using official Gemini API (Vertex AI or AI Studio).
    2.  **Fallback:** Use browser automation only as a free tier fallback, with clear warnings.

### TR-02: Context Window Overflow
*   **Description:** The system loads many JSON files from `00_CORE_BRAIN`. As the brain grows, the combined text will exceed token limits (typically 32k-128k for current models, but costs rise).
*   **Probability:** High (80%)
*   **Impact:** High (Crashes or partial "forgetting" of instructions)
*   **Mitigation:** Implement RAG (Retrieval Augmented Generation) or a strict "Context Router" that only loads files relevant to the specific task (e.g., don't load `CRO_PATTERNS` when writing `settings_schema.json`).

### TR-03: Code Hallucination / Security Vulnerabilities
*   **Description:** LLMs may generate insecure code (XSS) or use deprecated Liquid tags.
*   **Probability:** Medium (40%)
*   **Impact:** High (Shopify Theme Store rejection)
*   **Mitigation:** The existing `SecurityScanner` is a good start. It must be made a **Blocking Gate**—if issues are found, the code is *never* written to disk, and the LLM is prompted to fix it.

## 2. Operational Risks

### OR-01: Google Account Bans
*   **Description:** Automated usage of personal Google accounts via Selenium violates ToS.
*   **Probability:** Medium
*   **Impact:** High (User loses account access)
*   **Mitigation:** Switch to paid API keys. Do not encourage mass automation via personal accounts in documentation.

### OR-02: Dependency on Shopify Ecosystem
*   **Description:** Shopify frequently updates APIs and Theme architectures.
*   **Probability:** Low (Yearly)
*   **Impact:** Medium
*   **Mitigation:** The "Knowledge Syncer" (planned) is crucial here to detect breaking changes in Shopify docs and update the Brain automatically.

## 3. Market Risks

### MR-01: Quality vs. Expectations
*   **Description:** Users expect "Agency Quality" (Score A) but receive "Template Quality" (Score C).
*   **Probability:** Medium
*   **Impact:** High (Reputation damage)
*   **Mitigation:** Focus on "Neuro-Design" rules. Ensure the `AI_THEME_BLUEPRINT` includes sophisticated CSS/JS interactions, not just static HTML.

## Risk Matrix

| ID | Risk | Prob. | Impact | Severity |
| :--- | :--- | :--- | :--- | :--- |
| **TR-01** | **Browser Automation** | 9 | 10 | **90 (Critical)** |
| **TR-02** | **Context Overflow** | 8 | 8 | **64 (High)** |
| **OR-01** | **Account Ban** | 5 | 9 | **45 (High)** |
| **TR-03** | **Security/XSS** | 4 | 8 | **32 (Medium)** |
| **MR-01** | **Quality Gap** | 5 | 6 | **30 (Medium)** |
