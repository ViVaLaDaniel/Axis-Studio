# AXIS OS: Product Playbook & User Manual

Welcome to AXIS OS, the world's first Constitutional AI Operating System for Shopify theme development. This document is your guide to understanding, using, and mastering the system.

---

## Chapter 1: What is AXIS OS?

AXIS OS is not an AI. It is a **strict, file-based operating system** that you install on your local machine. You then connect your own Large Language Model (LLM), such as Google's Gemini or OpenAI's GPT, to act as the "Executor" or "Hands" of the OS.

The core problem AXIS solves is **AI Hallucination and Inconsistency**. An unconstrained LLM can be creative but is also unpredictable and prone to making mistakes, breaking performance budgets, or ignoring security best practices.

AXIS OS solves this by wrapping the LLM in a "Constitution" of rules, protocols, and knowledge bases. The LLM is forced to read, understand, and **cite** these rules for every action it takes. It cannot write slow code, introduce security flaws, or deviate from the project's design system, because the OS forbids it.

---

## Chapter 2: The Value Proposition

Why choose AXIS OS over standard AI assistants or manual development?

### 1. **"Stop Hallucinations"**
- **Problem:** LLMs often "invent" code, use deprecated functions, or generate solutions that don't work.
- **AXIS Solution:** The OS forces the LLM to validate its own work against a strict set of rules (`AI_SECURITY_WALL.json`, `AXIS_GLOBAL_CONSTANTS.json`). The **Law of Citation** requires the LLM to state *which* rule justifies its code, making every output traceable and verifiable.

### 2. **"Enterprise Security, Guaranteed"**
- **Problem:** Manually reviewing code for security flaws (XSS, CSRF, data leaks) is slow and error-prone.
- **AXIS Solution:** Security is not an afterthought; it's a core function. `11_AXIS_SECURITY_SCANNER.json` provides rules that are automatically enforced on every piece of generated code, long before it ever reaches a staging environment.

### 3. **"Performance by Default"**
- **Problem:** It is easy to write code that feels fast on a developer's high-end machine but is slow for users on average mobile devices.
- **AXIS Solution:** The OS will refuse to generate code that violates the performance budgets defined in `15_AXIS_PERFORMANCE_BUDGET.json` and the device metrics in `05_QUALITY_SECURITY/DEVICE_BENCHMARKS.json`. If a feature is too "expensive," the `NEGOTIATION_PROTOCOL.json` forces a downgrade to a more performant alternative.

---

## Chapter 3: Getting Started - Quick Start

You can get AXIS OS running in three steps:

1.  **Clone the Repository:**
    - Clone the `Axis-Studio` repository to your local machine. This folder *is* the Operating System.

2.  **Install Your LLM Adapter:**
    - Choose your LLM "Executor." We recommend starting with Google's Gemini CLI.
    - Follow the setup instructions in `08_INTEGRATIONS/GEMINI_CLI_ADAPTER.md` to connect it to the AXIS OS folder.

3.  **Run the Boot Prompt:**
    - Open your chosen LLM's command-line interface.
    - Copy and paste the full boot prompt from `00_CORE_BRAIN/LLM_INTEGRATION_GUIDE.md`. This initializes the LLM, loading the core laws and making it ready for your first command.
    - The LLM should respond with: `AXIS OS Initialized. Awaiting directive.`

---

## Chapter 4: Your First Task (Example)

Once initialized, you can issue commands in plain language.

**Your Prompt:**
```
"Create a new Shopify section named 'testimonial-slider'. It should display a customer's quote, name, and a 5-star rating. The slider should be interactive and support touch gestures."
```

**The AI's Process (Simplified):**
1.  **ROLE SWITCH:** Switches to `LEAD_DEV` and `NEURO_DESIGNER` roles (`AI_ROLE_ENGINE.json`).
2.  **CONTEXT LOAD:** Reads `04_EXECUTION_DEV/CODE_SNIPPETS_LIBRARY.md` for slider patterns and `01_FOUNDATION_RULES/AXIS_MOTION_GUIDELINES.md` for animation rules.
3.  **VALIDATION:** Generates the Liquid and JavaScript code. It then internally checks this code against `15_AXIS_PERFORMANCE_BUDGET.json`.
4.  **NEGOTIATION:** If the generated slider JS is too large, it consults `NEGOTIATION_PROTOCOL.json` and may propose using a simpler, CSS-only slider to meet the performance budget.
5.  **OUTPUT & CITATION:** The AI provides the final code, along with a `Reasoning Trace`:
    - `[Reasoning Trace: Slider implementation uses IntersectionObserver for lazy-loading as per 00_TECH_SYSTEM §3.2. Animation easing curve 'cubic-bezier(0.4, 0, 0.2, 1)' is sourced from 01_MOTION_GUIDELINES §1.4]`

---

## Chapter 5: Understanding the AXIS "Mind"

The OS is organized like a company:

- **`00_CORE_BRAIN`**: The CEO and C-Suite. Makes decisions.
- **`01_FOUNDATION_RULES`**: The Legal Department. Sets the laws.
- **`02_STRATEGY_CREATIVE`**: R&D and Market Research.
- **`03_ARCHITECTURE`**: The Architects and City Planners.
- **`04_EXECUTION_DEV`**: The Engineers and Coders.
- **`05_QUALITY_SECURITY`**: The QA and Security Testing Team.
- **`06_CI_CD_RELEASE`**: The Release and Deployment Team.
- **`07_TEAM_DOCS`**: The Company's internal Wiki and HR department.
- **`08_INTEGRATIONS`**: The IT department, managing connections to external tools.
