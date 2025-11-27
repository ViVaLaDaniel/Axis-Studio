# Gap Analysis Report

This report identifies the discrepancies between the projected "God Mode" system and the actual codebase.

## Priority 1: Critical Blockers (Must Fix Immediately)

### 1. Robust LLM API Adapters
*   **Gap:** Only `GeminiBrowserProvider` exists (Selenium-based).
*   **Impact:** System is unstable, slow, and reliant on UI layouts. Cannot run headless reliably in CI/CD.
*   **Fix:** Implement `OpenAIProvider` and `AnthropicProvider` using official SDKs.
*   **Effort:** Low (1-2 days).

### 2. Context Token Management
*   **Gap:** `AxisContext` loads files but doesn't measure token usage.
*   **Impact:** Complex prompts will fail or be truncated by LLMs.
*   **Fix:** Integrate `tiktoken` (for OpenAI) or character-count heuristics. Implement a "Context Packer" that selects only relevant brain modules for the specific task.
*   **Effort:** Medium (3-5 days).

### 3. Dynamic Execution Logic
*   **Gap:** `ThemeGenerator` uses hardcoded method calls (`_generate_file(...)`).
*   **Impact:** Adding new capabilities requires code changes, rendering the "Self-Updating Brain" partially ineffective.
*   **Fix:** Rewrite `generate_theme` to iterate over the `AI_THEME_BLUEPRINT` JSON structure dynamically.
    ```python
    # Proposed Logic
    for component in blueprint['components']:
        self.generate_component(component)
    ```
*   **Effort:** Medium (1 week).

## Priority 2: High Importance (Stability & Quality)

### 4. State Persistence
*   **Gap:** No `state.json` or database.
*   **Impact:** No resume capability. If generation fails at file 49/50, the process is lost.
*   **Fix:** Implement a `StateManager` that saves progress to disk after every step.
*   **Effort:** Low (2 days).

### 5. Automated Validation Loop (Auto-Fix)
*   **Gap:** `SecurityScanner` and `PerformanceGovernor` exist but are passive (reporting only).
*   **Impact:** Bad code is generated and saved. The user has to manually fix it.
*   **Fix:** Connect Scanner output to LLM input.
    *   *Loop:* Generate -> Scan -> Fail? -> Send Errors to LLM -> Re-Generate.
*   **Effort:** High (1-2 weeks).

## Priority 3: Medium Importance (Features)

### 6. Knowledge Syncer
*   **Gap:** `AXIS_KNOWLEDGE_SYNCER.json` describes scraping docs, but no scraper code exists.
*   **Impact:** Knowledge is static.
*   **Fix:** Implement `src/crawlers/shopify_docs.py` using `BeautifulSoup` or `Playwright`.
*   **Effort:** Medium (2 weeks).

### 7. Installation Scripts
*   **Gap:** No `install.sh` or `setup.py`.
*   **Impact:** High friction for new users.
*   **Fix:** Create standard setup scripts.
*   **Effort:** Low (1 day).

## Summary Table

| Gap | Priority | Complexity | Est. Effort |
| :--- | :--- | :--- | :--- |
| **API Adapters** | 🔴 Critical | Low | 2 Days |
| **Context/Tokens** | 🔴 Critical | Medium | 4 Days |
| **Dynamic Generator** | 🔴 Critical | Medium | 5 Days |
| **State Persistence** | 🟡 High | Low | 2 Days |
| **Auto-Fix Loop** | 🟡 High | High | 10 Days |
| **Knowledge Scraper** | 🟢 Medium | Medium | 10 Days |
