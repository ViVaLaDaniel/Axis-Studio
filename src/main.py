import os
import sys

# Добавляем корневую директорию проекта в sys.path, чтобы Python мог находить модули
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.orchestrator import execute_engine, load_behavior_tree
# from src.core import some_core_function  # Пример импорта из core
# from src.adapters import some_adapter_function # Пример импорта из adapters
# from src.cli import main_cli_interface # Пример импорта из cli
# from src.utils import some_utility_function # Пример импорта из utils

if __name__ == "__main__":
    print("--- AXIS AI Runtime Engine - Main Entry Point ---")
    
    # Здесь будет логика загрузки конфигурации из axis.config.json
    # и инициализации оркестратора
    
    # Временный запуск оркестратора напрямую
    behavior_tree = load_behavior_tree()
    if behavior_tree:
        execute_engine(behavior_tree)