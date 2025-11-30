# Implementation Guide

## 1. Setting Up the Development Environment

### Prerequisites
1.  **Python 3.10+**: Ensure `python --version` returns 3.10 or higher.
2.  **Chrome**: Install Google Chrome (for browser adapter).
3.  **Git**: Clone the repository.

### Step-by-Step Setup
```bash
# 1. Clone
git clone https://github.com/ViVaLaDaniel/Axis-Studio
cd Axis-Studio

# 2. Virtual Environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# 3. Install Dependencies
pip install -r requirements.txt

# 4. Environment Variables
cp .env.example .env
# Edit .env and add:
# GOOGLE_EMAIL=...
# GOOGLE_PASSWORD=... (If using browser)
# OPENAI_API_KEY=... (If using API)
```

## 2. Core Development Tasks

### Task A: Implementing a New LLM Adapter
Create `src/adapters/openai_adapter.py`:

```python
from src.adapters.llm_provider import LLMProvider, LLMProviderFactory
import openai

class OpenAIProvider(LLMProvider):
    def __init__(self, api_key=None, model="gpt-4"):
        self.client = openai.OpenAI(api_key=api_key)
        self.model = model

    def generate(self, prompt, **kwargs):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

LLMProviderFactory.register('openai', OpenAIProvider)
```

### Task B: Fixing the Generator Logic
Modify `src/core/generator.py` to be dynamic:

```python
def generate_theme(self, brief, theme_name):
    # Load blueprint
    blueprint = self.context.brain["AI_THEME_BLUEPRINT"]

    # Iterate phases
    for phase_name, phase_data in blueprint.items():
        if phase_name.startswith("phase_"):
            self.logger.info(f"Executing {phase_name}...")
            # Logic to interpret phase actions...
```

## 3. Testing Strategy

### Unit Tests
Run `pytest` to verify core logic:
```bash
pytest tests/
```
*Note: You need to write these tests. Focus on `Context` loading and `Orchestrator` logic.*

### Integration Tests
Run a "Dry Run" generation:
```bash
python src/cli/main.py generate "Test Brief" --provider mock
```
*Tip: Create a `MockProvider` that returns fixed strings to test the pipeline without spending money.*

## 4. Deployment

### Docker
Build the container for consistent execution:
```bash
docker build -t axis-studio .
docker run -it axis-studio status
```

### CI/CD
Use GitHub Actions to run the linter and unit tests on every push.
