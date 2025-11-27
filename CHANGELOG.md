# 📝 Changelog

All notable changes to **AXIS Studio** will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### Added
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
