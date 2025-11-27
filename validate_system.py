"""
AXIS Studio — System Validation Script
Проверяет совместимость всех баз знаний и интеграцию с генератором
"""

import json
import os
import sys

def validate_json_files():
    """Проверка валидности всех JSON баз данных"""
    print("\n🔍 Проверка JSON файлов...\n")
    
    files = [
        '00_CORE_BRAIN/DESIGN_PATTERNS_SCHEMA.json',
        '00_CORE_BRAIN/DESIGN_PATTERNS_DB_DAWN.json',
        '00_CORE_BRAIN/DESIGN_PATTERNS_DB_IMPACT.json',
        '00_CORE_BRAIN/PSYCHOLOGY_DB.json',
        '00_CORE_BRAIN/RETENTION_DB.json',
        '00_CORE_BRAIN/COPYWRITING_DB.json',
        '00_CORE_BRAIN/MICRO_INTERACTIONS_DB.json',
        '00_CORE_BRAIN/PRICING_PSYCHOLOGY_DB.json',
        '00_CORE_BRAIN/TRUST_SIGNALS_DB.json',
        '00_CORE_BRAIN/THEME_DB_DAWN.json',
        '00_CORE_BRAIN/THEME_DB_IMPACT.json'
    ]
    
    valid = 0
    errors = []
    
    for file_path in files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            print(f"  ✅ {file_path}")
            valid += 1
        except json.JSONDecodeError as e:
            print(f"  ❌ {file_path}: {e}")
            errors.append((file_path, str(e)))
        except FileNotFoundError:
            print(f"  ⚠️  {file_path}: File not found")
            errors.append((file_path, "File not found"))
    
    print(f"\n✅ Валидных файлов: {valid}/{len(files)}")
    return len(errors) == 0, errors

def test_context_loader():
    """Проверка загрузки контекста"""
    print("\n🧠 Проверка Context Loader...\n")
    
    try:
        from src.core.context import AxisContext
        
        ctx = AxisContext()
        ctx.load_brain()
        
        print(f"  ✅ Context загружен")
        print(f"  📊 Всего модулей: {len(ctx.brain)}")
        
        # Проверка ключевых баз
        key_dbs = [
            'DESIGN_PATTERNS_SCHEMA',
            'DESIGN_PATTERNS_DB_DAWN', 
            'DESIGN_PATTERNS_DB_IMPACT',
            'PSYCHOLOGY_DB',
            'RETENTION_DB',
            'COPYWRITING_DB',
            'MICRO_INTERACTIONS_DB',
            'PRICING_PSYCHOLOGY_DB',
            'TRUST_SIGNALS_DB'
        ]
        
        print("\n  Ключевые базы данных:")
        loaded = 0
        for db in key_dbs:
            if db in ctx.brain:
                print(f"    ✅ {db}")
                loaded += 1
            else:
                print(f"    ❌ {db} - НЕ ЗАГРУЖЕНА")
        
        print(f"\n  ✅ Загружено: {loaded}/{len(key_dbs)}")
        return loaded == len(key_dbs)
        
    except Exception as e:
        print(f"  ❌ Ошибка: {e}")
        return False

def test_generator():
    """Проверка генератора тем"""
    print("\n🏭 Проверка Theme Generator...\n")
    
    try:
        from src.core.generator import ThemeGenerator
        
        gen = ThemeGenerator('gemini_browser')
        
        print(f"  ✅ Generator инициализирован")
        
        # Проверка загруженных баз
        attrs = [
            'design_patterns_schema',
            'psychology_db',
            'retention_db',
            'copywriting_db',
            'theme_db_dawn',
            'theme_db_impact'
        ]
        
        print("\n  Загруженные базы в генераторе:")
        loaded = 0
        for attr in attrs:
            if hasattr(gen, attr) and getattr(gen, attr):
                size = len(str(getattr(gen, attr)))
                print(f"    ✅ {attr} ({size} chars)")
                loaded += 1
            else:
                print(f"    ❌ {attr} - НЕ ЗАГРУЖЕНА")
        
        print(f"\n  ✅ Загружено: {loaded}/{len(attrs)}")
        
        # Проверка методов
        methods = ['_extract_niche_from_context', '_build_knowledge_context']
        print("\n  Критические методы:")
        for method in methods:
            if hasattr(gen, method):
                print(f"    ✅ {method}")
            else:
                print(f"    ❌ {method} - ОТСУТСТВУЕТ")
        
        return loaded == len(attrs)
        
    except Exception as e:
        print(f"  ❌ Ошибка: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Главная функция"""
    print("=" * 80)
    print("AXIS Studio — System Validation")
    print("=" * 80)
    
    # Тест 1: JSON валидация
    json_valid, json_errors = validate_json_files()
    
    # Тест 2: Context Loader
    context_ok = test_context_loader()
    
    # Тест 3: Generator
    generator_ok = test_generator()
    
    # Итоги
    print("\n" + "=" * 80)
    print("📊 ИТОГИ ПРОВЕРКИ")
    print("=" * 80)
    print(f"  JSON файлы:      {'✅ OK' if json_valid else '❌ ОШИБКИ'}")
    print(f"  Context Loader:  {'✅ OK' if context_ok else '❌ ОШИБКИ'}")
    print(f"  Theme Generator: {'✅ OK' if generator_ok else '❌ ОШИБКИ'}")
    
    if json_valid and context_ok and generator_ok:
        print("\n🎉 ВСЕ ПРОВЕРКИ ПРОЙДЕНЫ — СИСТЕМА ГОТОВА К РАБОТЕ!")
        return 0
    else:
        print("\n⚠️  ОБНАРУЖЕНЫ ПРОБЛЕМЫ — ТРЕБУЕТСЯ ИСПРАВЛЕНИЕ")
        if json_errors:
            print("\nОшибки JSON:")
            for file, error in json_errors:
                print(f"  - {file}: {error}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
