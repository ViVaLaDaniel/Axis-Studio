# 📝 Changelog

All notable changes to **AXIS Studio** will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### 🛡️ Security (CRITICAL FIXES - 2025-11-27)
- **FIXED CRITICAL:** Shell injection vulnerability in `src/orchestrator.py`
  - Removed dangerous `shell=True` from subprocess.run
  - Implemented command whitelist (echo, mkdir, ls, cat, pwd, cd, etc.)
  - Added argument count validation
  - Added 30-second timeout for all commands
  - Enhanced error handling (timeout, file not found, etc.)
- **FIXED:** Implemented full JSON schema validation in `src/core/validator.py`
  - Uses `jsonschema` library for validation
  - Added predefined schemas for `behavior_tree` and `axis_config`
  - Added convenience methods: `validate_behavior_tree()`, `validate_axis_config()`
- **FIXED:** Syntax error in `requirements.txt` (line 2: comment merged with dependency)
- **ADDED:** `.env.example` template for API keys and configuration

### Added
- `requirements.txt`: Added `google-generativeai>=0.3.0` and `openai>=1.3.0` for LLM SDK support
- `src/orchestrator.py`: Behavior tree validation before execution (SECURITY layer)
- `02_STRATEGY_CREATIVE/25_AXIS_CRO_SCIENTIST.json`: Complete CRO agent with niche analysis, pattern selection decision trees
- `src/core/generator.py`: **AUTONOMOUS THEME FACTORY**
  - Niche detection from brief via LLM
  - Competitor intelligence integration (analyzes top 10 Shopify themes)
  - CRO pattern selection by archetype (luxury/fashion/wellness/B2B)
  - Interactive path selection dialog (Desktop/Custom/Project output)
  - Full Shopify OS 2.0 structure generation (15+ files: sections, templates, snippets, assets)
  - Automatic CRO optimization report

### 🏭 Autonomous Factory (Phase 4 - COMPLETED)
**Готово к использованию:** `python src/cli/main.py create-theme "VIP theme for luxury watches"`

Система теперь:
1. Анализирует нишу из brief
2. Загружает best practices из топ-тем (Impact, Prestige, Impulse и др.)
3. Выбирает CRO паттерны под архетип
4. Спрашивает где создать тему (Desktop/Custom/Project output)
5. Генерирует полную Shopify тему (15+ файлов)
6. Создаёт CRO отчёт с рекомендациями

### 🔬 Theme Knowledge Base (Phase 4.5 - NEW)
**Инструмент для автоматизации:** `src/utils/theme_analyzer.py`

База знаний топовых Shopify тем:
- `THEME_DECOMPOSITION_SCHEMA.json` — шаблон для декомпозиции
- `THEME_DB_DAWN.json` — полная разборка Dawn (800+ строк)
- `THEME_DB_IMPACT.json` — разборка Impact (premium фичи)
- Analyzer tool для автоматического анализа любой темы

**Зачем:** LLM генерирует на основе РЕАЛЬНЫХ рабочих примеров из топ-тем, а не "из воздуха"

**Использование:**
```bash
python src/utils/theme_analyzer.py --theme dawn --github https://github.com/Shopify/dawn
```
- `src/core/context.py`: Context Loader module for reading configuration and Brain files.
- `src/core/validator.py`: Validator module for JSON schema validation.
- `src/cli/main.py`: CLI interface with `run`, `init`, `status`, and `generate` commands.
- `src/utils/security_scanner.py`: Security Scanner for Liquid, JS, and CSS files (XSS detection, dangerous functions).
- `src/utils/performance.py`: Performance Governor for enforcing file size budgets.
- `src/adapters/llm_provider.py`: Base LLM Provider interface with factory pattern.
- `src/adapters/gemini_browser.py`: Browser-based Gemini provider using Selenium.
- `src/core/generator.py`: Theme Generator module for autonomous theme creation.
- `00_CORE_BRAIN/AXIS_SYSTEM_PROMPT_v10.json`: Complete system prompt definition for LLM initialization.
- `00_CORE_BRAIN/AI_THEME_BLUEPRINT.json`: JSON definition of Shopify OS 2.0 theme structure.
- `TESTING_GUIDE.md`: Manual testing instructions for Runtime Engine verification.
- `output/hello.txt`: Demo file created by Runtime Engine.
- `requirements.txt`: Added selenium dependency.

### Changed
- `src/orchestrator.py`: Refactored to class-based architecture with native file operations (`file_create`, `file_read`).
- `src/utils/performance.py`: Synced CSS budget to 100 KB (was 50 KB) to match `15_PERFORMANCE_BUDGET.json`.
- `src/` directory structure (core, adapters, cli, utils).
- `axis.config.json`: Configuration file for the runtime.
- New documentation structure (`README.md`, `ROADMAP.md`, `VERSION.md`, `LICENSE`).

### Changed
- Refactored project structure to separate "Brain" (JSON) from "Body" (Python).
- Moved `engine.py` from `09_ENGINE` to `src/orchestrator.py`.

---

## [10.5.0] - 2025-11-27
### Added
- **Scientific Edition** architecture.
- `00_CORE_BRAIN` updated with `AXIS_KNOWLEDGE_SYNCER`.
- `02_STRATEGY_CREATIVE` populated with Neuro-Design libraries.

### Fixed
- File encoding issues in `01_FOUNDATION_RULES`.
- Indentation errors in legacy scripts.

---

## [10.0.0] - 2025-11-01
### Added
- Initial "God Mode" architecture.
- Complete set of JSON configuration files.
