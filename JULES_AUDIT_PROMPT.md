# AXIS Studio - Complete System Audit Request

**Project:** AXIS Studio - Autonomous Shopify Theme Factory  
**Language:** Python 3.x  
**Framework:** Shopify Liquid + Custom AI Generator  

---

## 🎯 AUDIT OBJECTIVES

Please perform a comprehensive code review and dependency analysis of this Shopify theme generation system. Focus on:

1. **Python dependencies validation** (all imports functional)
2. **Code quality & best practices** (PEP 8, type hints, error handling)
3. **Architecture soundness** (separation of concerns, modularity)
4. **Security vulnerabilities** (XSS, CSRF, injection risks)
5. **Performance bottlenecks** (file I/O, JSON parsing, LLM calls)
6. **Knowledge base integrity** (18 JSON databases consistency)

---

## 📁 PROJECT STRUCTURE

```
AXIS Studio/
├── src/
│   ├── core/
│   │   ├── generator.py          # Main theme generator (CRITICAL)
│   │   ├── context.py             # Knowledge base loader
│   │   └── __init__.py
│   ├── adapters/
│   │   ├── llm_provider.py        # LLM abstraction layer
│   │   ├── gemini_browser.py      # Selenium-based Gemini adapter (TO BE REPLACED)
│   │   ├── claude_adapter.py      # Empty stub (NEEDS IMPLEMENTATION)
│   │   └── openai_adapter.py      # Empty stub (NEEDS IMPLEMENTATION)
│   └── orchestrator.py            # Task execution orchestrator
│
├── 00_CORE_BRAIN/                 # Knowledge databases (18 JSON files)
│   ├── PSYCHOLOGY_DB.json         # Conversion psychology patterns
│   ├── COMPONENT_LIBRARY.json     # 11 ready-made Liquid components
│   ├── SHOPIFY_LIQUID_DB.json     # Shopify Liquid reference
│   ├── SHOPIFY_API_DB.json        # Shopify APIs documentation
│   ├── THEME_DB_*.json            # 7 theme decompositions (Dawn, Impact, etc.)
│   └── ... (14 more)
│
├── test_generator.py              # System validation script
└── requirements.txt               # Python dependencies (if exists)
```

---

## 🔍 SPECIFIC AUDIT CHECKS

### 1. **Dependencies Validation**

**Check:**
- Are all Python imports resolvable? (`jsonschema`, `pydantic`, `selenium`, etc.)
- Does `requirements.txt` exist and cover all imports?
- Are version pins appropriate? (avoid `package==*`, prefer `package>=X.Y`)

**Expected Imports:**
```python
# From src/core/generator.py
import json, os, logging
from typing import Dict, Any, List, Optional
from src.core.context import AxisContext
from src.adapters.llm_provider import LLMProvider, LLMProviderFactory
```

**Action Required:**
- Generate missing `requirements.txt` if absent
- Flag any unresolved imports
- Recommend stable versions for critical packages

---

### 2. **Code Quality - `src/core/generator.py`**

**Critical Checks:**

✅ **Syntax Validation:**
- Python 3.8+ compatible?
- No syntax errors (indentation, unclosed strings, brackets)?
- Type hints used consistently?

✅ **Error Handling:**
- Are try/except blocks properly scoped?
- Does error handling prevent data loss? (e.g., partially generated themes)
- Are errors logged with sufficient context?

✅ **Security:**
- File path traversal prevention? (use `os.path.join`, validate user inputs)
- No hardcoded credentials?
- Liquid code outputs properly escaped to prevent XSS?

**Code Snippet to Review:**
```python
# Line ~287-350: _generate_file method
# Line ~355-420: _select_component_from_library method
```

---

### 3. **Architecture Issues**

**Known Problems (from previous audit):**

🚨 **CRITICAL - Selenium Dependency:**
```python
# src/adapters/gemini_browser.py
# Currently uses Selenium to interact with Gemini web UI
# ISSUE: Fragile, slow, violates Google ToS
```
**Recommendation:**  
Replace with `google-generativeai` SDK:
```python
import google.generativeai as genai
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
model = genai.GenerativeModel('gemini-pro')
response = model.generate_content(prompt)
```

🚨 **MISSING - State Persistence:**
```python
# No checkpointing system for theme generation
# If generation fails at file 15/20, user loses all progress
```
**Recommendation:**  
Implement state snapshots:
```python
def save_checkpoint(theme_root, progress_data):
    checkpoint = {
        'files_generated': [...],
        'current_step': 'sections',
        'timestamp': datetime.now().isoformat()
    }
    with open(f'{theme_root}/.checkpoint.json', 'w') as f:
        json.dump(checkpoint, f)
```

🚨 **MISSING - Context Overflow Protection:**
```python
# context.py loads ALL 18 databases (~2MB JSON) into memory
# Can exceed LLM token limits (128k for Gemini 1.5)
```
**Recommendation:**  
Implement lazy loading:
```python
def _build_knowledge_context(self, file_path: str, niche: str):
    # Load ONLY relevant databases for this file type
    if 'hero' in file_path:
        return self.design_patterns_schema + self.copywriting_db
    elif 'product' in file_path:
        return self.psychology_db + self.pricing_db
    # etc.
```

---

### 4. **Knowledge Base Integrity**

**Validate JSON Files:**

```bash
# Check all 18 files in 00_CORE_BRAIN/
for file in 00_CORE_BRAIN/*.json; do
    python -m json.tool "$file" > /dev/null && echo "✅ $file" || echo "❌ $file BROKEN"
done
```

**Known Issues:**
- ❌ `axis_brain_v10.0_GOD_MODE.json` - UTF-8 BOM encoding (FIXED, verify)
- ✅ `COMPONENT_LIBRARY.json` - Should contain 11 components with keys:
  - PRODUCT_CARD, CART_DRAWER, PREDICTIVE_SEARCH, SIZE_GUIDE_MODAL
  - MEGA_MENU, COLLECTION_FILTERS, QUICK_SHOP, STICKY_HEADER
  - NEWSLETTER, RECOMMENDATIONS, ANNOUNCEMENT

**Validation Script:**
```python
import json
brain_files = [
    'PSYCHOLOGY_DB.json',
    'COMPONENT_LIBRARY.json',
    'SHOPIFY_LIQUID_DB.json',
    # ... 15 more
]

for file in brain_files:
    with open(f'00_CORE_BRAIN/{file}', 'r', encoding='utf-8') as f:
        data = json.load(f)
        print(f"✅ {file}: {len(data)} top-level keys")
```

---

### 5. **Performance Bottlenecks**

**Profile These Functions:**

```python
# generator.py:_generate_shopify_theme (line ~250)
# - Generates 15-20 files sequentially
# - Each file = 1 LLM call (~5-15 seconds)
# - Total time: 2-5 minutes per theme
```

**Optimization Opportunities:**
1. **Parallel file generation** (use `asyncio` or `ThreadPoolExecutor`)
2. **LLM response caching** (same prompt = reuse response)
3. **Component library first** (avoid LLM for common components)

**Benchmark Target:**
- Theme generation: **< 2 minutes** (currently ~5 minutes)
- Knowledge loading: **< 1 second** (currently ~2 seconds)

---

### 6. **Testing Coverage**

**Current Test Suite:**
```python
# test_generator.py - 5 tests
# ✅ Syntax validation
# ✅ Knowledge loading (18 DBs)
# ✅ Component library (11 components)
# ✅ Generator initialization
# ✅ File structure validation
```

**Missing Tests:**
- ❌ End-to-end theme generation (create full theme, validate OS 2.0 structure)
- ❌ LLM provider switching (Gemini → Claude → OpenAI fallback)
- ❌ Error recovery (simulate file write failure, verify rollback)
- ❌ Performance benchmarks (time generation, memory usage)

**Recommended:**
```python
def test_full_theme_generation():
    gen = ThemeGenerator()
    theme_root = gen.generate_theme(
        brief="Luxury watch store",
        theme_name="test_luxury"
    )
    
    # Validate structure
    assert os.path.exists(f"{theme_root}/layout/theme.liquid")
    assert os.path.exists(f"{theme_root}/sections/header.liquid")
    assert os.path.exists(f"{theme_root}/config/settings_schema.json")
    
    # Validate no security issues
    with open(f"{theme_root}/sections/product.liquid") as f:
        code = f.read()
        assert "{{ product.title | escape }}" in code  # XSS prevention
```

---

## 🎯 CRITICAL QUESTIONS FOR JULES

1. **Can this system run without Selenium?**  
   → Check if native API adapters (`claude_adapter.py`, `openai_adapter.py`) are functional

2. **Is the architecture production-ready?**  
   → Evaluate error handling, state management, scalability

3. **What are the TOP 3 security risks?**  
   → XSS in generated Liquid code? Unvalidated file paths? API key exposure?

4. **What dependencies are missing from `requirements.txt`?**  
   → Auto-generate complete dependency list

5. **How can we reduce theme generation time by 50%?**  
   → Identify parallelization opportunities, caching strategies

---

## 📊 EXPECTED DELIVERABLES

1. **Dependency Report:**
   - List all required packages with recommended versions
   - Flag any security vulnerabilities (use `pip-audit` or similar)

2. **Code Quality Score:**
   - PEP 8 compliance %
   - Type coverage %
   - Test coverage %

3. **Architecture Recommendations:**
   - Top 5 refactoring priorities
   - Migration plan from Selenium to native APIs

4. **Security Audit:**
   - List of vulnerabilities (HIGH/MEDIUM/LOW)
   - Remediation steps for each

5. **Performance Report:**
   - Current bottlenecks (with line numbers)
   - Estimated speedup from recommended optimizations

---

## 🚀 CONTEXT FOR JULES

**This is a production system that:**
- Generates complete Shopify themes (~20 files) from a single brief
- Uses 18 knowledge databases (CRO patterns, design systems, theme decompositions)
- Targets Shopify Theme Store submission (must pass strict quality checks)
- Currently uses Selenium (BAD) but needs to migrate to proper APIs (GOOD)

**Success Criteria:**
- ✅ All tests pass (`python test_generator.py` = 5/5)
- ✅ No critical security issues
- ✅ Theme generation < 2 minutes
- ✅ Production-ready architecture (no Selenium, proper error handling, state persistence)

**Budget:**
- Development time: Immediate fixes needed
- User: Solo developer (Даня)
- Stakes: High (targeting $24k revenue Year 1)

---

## 📝 NOTES

- This system passed **5/5 tests** as of 2025-11-28
- Component Library: **11/11 components** functional
- Knowledge bases: **15/18** loading correctly (3 CRO bases integrated into GOD_MODE file)
- Main blocker: **Selenium dependency** (violates Google ToS, unreliable)

**Run the audit and provide actionable next steps to make this production-ready! 🚀**
