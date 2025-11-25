# 08_INTEGRATIONS

## Role: LLM Adapters

This directory contains specific adapters for different Large Language Models (LLMs) or execution environments. The goal of AXIS OS is to be "LLM-agnostic," and this folder is the key to achieving that.

Each adapter describes how a specific LLM (like Gemini CLI, OpenAI's API, a local model, etc.) should be instructed to read, interpret, and execute the protocols and knowledge bases defined in the core AXIS OS directories (00-07).

### Contents:
- **`GEMINI_CLI_ADAPTER.md`**: Provides the specific bootstrapping prompts, commands, and workflow for operating AXIS OS with Google's Gemini CLI.
