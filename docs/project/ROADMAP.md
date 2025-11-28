# 🗺️ AXIS Studio Roadmap

**Current Version:** v10.5 (Scientific Edition)
**Target:** v11.0 (Autonomous Agent)

---

## 🏁 Phase 1: The Kernel (Completed)
**Goal:** Define the "Brain" and Architecture.
- [x] **Core Brain:** Role definitions, System Prompts, Context Router.
- [x] **Foundation Rules:** Design System, Performance Budget, Zero Trust Protocol.
- [x] **Architecture:** Shopify OS 2.0 structure, JSON Templates, Section Clusters.
- [x] **Strategy:** CRO Patterns, Neuro-Design Library.

---

## 🚀 Phase 2: The Runtime Engine (Completed ✅)
**Goal:** Awaken the "Body" (Python) to execute the "Brain".
- [x] **Orchestrator v1.0:**
    - [x] Native file operations (create, read, write).
    - [x] Context loading from `00_CORE_BRAIN`.
- [x] **CLI Interface:**
    - [x] `axis run` (via `python src/cli/main.py run`)
    - [x] `axis status`
- [ ] **LLM Adapter:** Connect to Gemini/OpenAI APIs via `src/adapters`.

---

## 🛡️ Phase 3: Quality & Security (Current Focus)
**Goal:** Automated enforcement of laws.
- [x] **Security Scanner:** Python script to check for XSS/Injection in Liquid/JS.
- [x] **Performance Governor:** Auto-check file sizes against budget (<150KB JS, <50KB CSS).
- [ ] **A11y Checker:** Automated accessibility audit.
- [ ] **Integration:** Connect scanners to Orchestrator workflow.

---

## 🤖 Phase 4: Autonomous Factory
**Goal:** Full automation.
- [ ] **Theme Generator:** `axis create-theme "brief"` -> Full Shopify Theme.
- [ ] **Auto-Fix:** Engine detects errors and self-corrects.
- [ ] **Market Deployment:** Auto-package for Theme Store submission.

---

## 📚 Phase 5: Documentation & Infrastructure
**Goal:** Create a comprehensive and easily navigable documentation portal.
- [x] **docs/ structure:**
    - [x] `docs/architecture/`
    - [x] `docs/setup/`
    - [x] `docs/modules/`
    - [x] `docs/internals/`