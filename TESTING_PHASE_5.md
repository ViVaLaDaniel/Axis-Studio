# 🏭 Phase 5: Autonomous Factory - Verification Guide

**Date:** 2025-11-27  
**Status:** Ready for Testing

---

## 🚀 What We Built

We have enabled the **Theme Generator**. This module allows you to create a complete Shopify theme structure from a single text brief.

### Key Components:
1.  **`src/core/generator.py`**: The brain that orchestrates the creation of files.
2.  **`00_CORE_BRAIN/AI_THEME_BLUEPRINT.json`**: The skeleton defining what files to create.
3.  **`axis create-theme`**: The CLI command to trigger the process.

---

## 🧪 How to Test

### Prerequisites
1.  **Chrome Browser** installed.
2.  **Google Account** credentials (for Gemini).
3.  **Dependencies** installed (`pip install -r requirements.txt`).

### Step 1: Set Environment Variables
Open your terminal (PowerShell) and set your Google credentials. These are used by Selenium to log you in.

```powershell
$env:GOOGLE_EMAIL = "your_email@gmail.com"
$env:GOOGLE_PASSWORD = "your_password"
```

> **Note:** If you prefer not to put your password in the terminal, the script will pause and ask you to login manually if it fails.

### Step 2: Run the Generator
Run the following command to create a test theme.

```powershell
python src/cli/main.py create-theme "A minimalist fashion store with black and white aesthetics" --name test-theme-1
```

### Step 3: Watch the Magic
1.  A Chrome window will open.
2.  It will navigate to Gemini.
3.  **Action Required:** If it doesn't log in automatically, log in manually and press Enter in the terminal.
4.  The system will start generating files one by one:
    - `config/settings_schema.json`
    - `layout/theme.liquid`
    - `assets/base.css`
    - `sections/hero.liquid`
    - `templates/index.json`

### Step 4: Verify Output
Check the `output/test-theme-1` directory. You should see a valid Shopify theme structure.

---

## ⚠️ Troubleshooting

-   **Browser closes too fast?** The script closes the browser after completion. Check the logs in the terminal.
-   **Login failed?** The automated login is basic. Manual login is the most reliable fallback.
-   **"Element not found"?** Gemini's UI might have changed. We may need to update the CSS selectors in `src/adapters/gemini_browser.py`.

---

**Ready to launch?** 🚀
