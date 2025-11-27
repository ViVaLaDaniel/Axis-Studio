# 🧪 AXIS Studio Testing Guide

**Цель:** Проверить, что Runtime Engine работает корректно.

---

## Шаг 1: Проверка структуры

Убедись, что у тебя есть следующие файлы:

```
src/
├── core/
│   ├── context.py
│   └── validator.py
├── cli/
│   └── main.py
├── orchestrator.py
└── main.py

00_CORE_BRAIN/
└── AI_BEHAVIOR_TREE.json
```

---

## Шаг 2: Запуск через Orchestrator

Открой терминал в корне проекта и выполни:

```bash
python src/orchestrator.py
```

**Ожидаемый результат:**

```
2025-11-27 20:15:00 - AxisOrchestrator - INFO - Initializing Axis Orchestrator...
2025-11-27 20:15:00 - AxisContext - INFO - Loaded configuration from axis.config.json
2025-11-27 20:15:00 - AxisContext - INFO - Loading Brain from: 00_CORE_BRAIN
2025-11-27 20:15:00 - AxisOrchestrator - INFO - Loaded Behavior Tree from Memory (Brain).
2025-11-27 20:15:00 - AxisOrchestrator - INFO - --- Starting Execution of 2 tasks ---
2025-11-27 20:15:00 - AxisOrchestrator - INFO - [EXECUTING]: Initialize Project (Type: command)
2025-11-27 20:15:00 - AxisOrchestrator - INFO -   -> Running Shell Command: echo 'AI Engine Started. Initializing project...'
2025-11-27 20:15:00 - AxisOrchestrator - INFO -   STDOUT: AI Engine Started. Initializing project...
2025-11-27 20:15:00 - AxisOrchestrator - INFO - [EXECUTING]: Create Hello World File (Type: file_create)
2025-11-27 20:15:00 - AxisOrchestrator - INFO -   -> Creating File: C:\Users\wiwal\GIT\Axis Studio\output\hello.txt
2025-11-27 20:15:00 - AxisOrchestrator - INFO -   File created successfully.
2025-11-27 20:15:00 - AxisOrchestrator - INFO - --- Execution Finished ---
```

**Проверка:**

Должна появиться папка `output/` с файлом `hello.txt` внутри.

---

## Шаг 3: Запуск через CLI

```bash
python src/cli/main.py run
```

Это должно дать тот же результат, что и Шаг 2.

---

## Шаг 4: Проверка статуса

```bash
python src/cli/main.py status
```

**Ожидаемый вывод:**

```
✅ AXIS Studio v10.5 - Scientific Edition
📂 Project Root: C:\Users\wiwal\GIT\Axis Studio
🧠 Brain: 00_CORE_BRAIN
⚙️ Runtime: src/
```

---

## Troubleshooting

### Ошибка: `ModuleNotFoundError: No module named 'src'`

**Решение:** Убедись, что ты запускаешь команды из корня проекта (`C:\Users\wiwal\GIT\Axis Studio`).

### Ошибка: `FileNotFoundError: axis.config.json`

**Решение:** Проверь, что файл `axis.config.json` находится в корне проекта.

---

## Следующие шаги

После успешного прохождения тестов:

1. Переходи к **Phase 3: Quality & Security** (см. `ROADMAP.md`).
2. Начинай разработку **Security Scanner** и **Performance Governor**.
