# Dependency Manifest

## System Requirements
- **OS:** Windows, macOS, or Linux
- **Python:** 3.10+ (Required for type hinting and modern features)
- **Browser:** Google Chrome (Required for `gemini_browser` adapter)

## Python Dependencies (`requirements.txt`)

Based on the code analysis, the following packages are required:

```text
# Core
pydantic>=2.0.0          # Data validation (Architecture)
python-dotenv>=1.0.0     # Environment variable management

# LLM & Browser Automation
selenium>=4.15.0         # Required for GeminiBrowserProvider
webdriver-manager>=4.0.0 # Auto-manage Chrome drivers
# openai>=1.0.0          # Recommended for future API support
# anthropic>=0.3.0       # Recommended for future API support

# Utilities
requests>=2.31.0         # For future API calls / scrapers
jsonschema>=4.0.0        # Validating Brain JSONs against schemas
tiktoken>=0.5.0          # Token counting (Recommended)

# CLI & Formatting
rich>=13.0.0             # (Recommended) For beautiful CLI output
colorama>=0.4.6          # Basic terminal colors

# Testing
pytest>=7.0.0            # Unit testing
```

## External Tools (Optional but Integration Ready)
- **Shopify CLI:** Required for `shopify theme push` and `shopify theme dev`.
- **Lighthouse:** Required for `PerformanceGovernor` advanced audits (Node.js).
- **Node.js 18+:** Required if running Shopify CLI or Lighthouse locally.

## Dockerfile Recommendation

To standardize the environment and avoid Selenium/Chrome version mismatches:

```dockerfile
FROM python:3.11-slim

# Install Chrome for Selenium
RUN apt-get update && apt-get install -y chromium chromium-driver

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Set env for headless chrome
ENV CHROME_BIN=/usr/bin/chromium
ENV CHROMEDRIVER_PATH=/usr/bin/chromedriver

ENTRYPOINT ["python", "src/cli/main.py"]
```
