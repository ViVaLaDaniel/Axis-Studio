"""
Theme Generator Module for AXIS Studio.

This module handles the autonomous generation of Shopify themes.
It uses the LLM Provider to generate code based on the AI_THEME_BLUEPRINT.
"""

import os
import json
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Dict, Any, List

from src.core.context import AxisContext
from src.adapters.llm_provider import LLMProvider, LLMProviderFactory
from src.orchestrator import AxisOrchestrator

class ThemeGenerator:
    """
    Autonomous Theme Generator.
    
    Process:
    1. Load Blueprint (structure)
    2. Generate Plan (which files to create based on brief)
    3. Generate Code (iteratively or in parallel)
    4. Write to Disk
    """
    
    def __init__(self, provider_name: str = 'gemini'):
        self.logger = logging.getLogger("ThemeGenerator")
        self.context = AxisContext()
        self.context.load_brain()
        
        self.orchestrator = AxisOrchestrator()
        
        self.logger.info(f"Initializing LLM Provider: {provider_name}")
        self.provider = LLMProviderFactory.create(provider_name)
        
        # Load Blueprint
        self.blueprint = self.context.get_brain_module("AI_THEME_BLUEPRINT") or {}

    def generate_theme(self, brief: str, theme_name: str):
        """
        Generate a full theme based on the brief.
        """
        self.logger.info(f"🚀 Starting Theme Generation: '{theme_name}'")
        self.logger.info(f"📝 Brief: {brief}")
        
        # 1. Login if needed (Legacy support for browser provider)
        if hasattr(self.provider, 'login'):
            print("🔐 Logging in to LLM Provider...")
            self.provider.login()
            
        # 2. Create Theme Directory
        theme_root = os.path.join(self.context.project_root, "output", theme_name)
        self.logger.info(f"📂 Theme Root: {theme_root}")
        
        # Load checkpoint
        checkpoint = self._load_checkpoint(theme_root)
        
        # 3. Define files to generate
        files_to_generate = []
        
        # Try to parse from blueprint structure if available
        structure = self.blueprint.get("structure", {})
        if structure:
            for folder, content in structure.items():
                if isinstance(content, dict):
                    for filename, description in content.items():
                        files_to_generate.append((f"{folder}/{filename}", description))
        
        # Fallback if blueprint is empty
        if not files_to_generate:
            files_to_generate = [
                ("config/settings_schema.json", "Shopify settings_schema.json"),
                ("layout/theme.liquid", "Shopify theme.liquid layout file. Must include {{ content_for_header }} and {{ content_for_layout }}."),
                ("assets/base.css", "Main CSS file. Use CSS variables."),
                ("sections/hero.liquid", "Hero section with image and text settings."),
                ("templates/index.json", "JSON template for homepage including the hero section.")
            ]
        
        # 4. Generate Files (Parallel)
        with ThreadPoolExecutor(max_workers=3) as executor:
            future_to_file = {}
            for rel_path, context in files_to_generate:
                if rel_path in checkpoint.get("generated_files", []):
                    self.logger.info(f"  ⏭️ Skipping {rel_path} (already generated)")
                    continue

                future = executor.submit(self._generate_file, theme_root, rel_path, brief, context)
                future_to_file[future] = rel_path

            for future in as_completed(future_to_file):
                rel_path = future_to_file[future]
                try:
                    success = future.result()
                    if success:
                        self._update_checkpoint(theme_root, rel_path)
                except Exception as exc:
                    self.logger.error(f"File generation generated an exception: {rel_path} {exc}")

        self.logger.info(f"✅ Theme Generation Complete: {theme_root}")
        
        if hasattr(self.provider, 'close'):
            self.provider.close()

    def _generate_file(self, theme_root: str, relative_path: str, brief: str, context: str) -> bool:
        """Generate a single file using LLM."""
        full_path = os.path.join(theme_root, relative_path)
        self.logger.info(f"  👉 Generating: {relative_path}...")
        
        prompt = f"""
        ACT AS: Senior Shopify Developer.
        TASK: Write the code for the file '{relative_path}'.
        CONTEXT: {context}
        PROJECT BRIEF: {brief}
        
        STRICT RULES (SHOPIFY THEME STORE STANDARDS):
        1. Return ONLY the code. No markdown code blocks, no explanations.
        2. Valid syntax for the file type (Liquid, JSON, CSS, JS).
        3. SECURITY: ALL user-generated output must be escaped. Use `| escape` or `| json`.
        4. ACCESSIBILITY: Use semantic HTML (nav, button, header, footer). ARIA labels where needed.
        5. SCHEMA: settings_schema.json must be valid JSON.
        6. NO deprecated tags (e.g., use `image_url` instead of `img_url`).
        """
        
        try:
            code = self.provider.generate(prompt)
            
            # Clean up response (remove markdown if present)
            code = self._clean_response(code)
            
            # Write to file
            self.orchestrator.execute_task({
                "type": "file_create",
                "name": f"Create {relative_path}",
                "details": {
                    "path": full_path,
                    "content": code
                }
            })
            return True
            
        except Exception as e:
            self.logger.error(f"  ❌ Failed to generate {relative_path}: {e}")
            return False

    def _clean_response(self, text: str) -> str:
        """Remove markdown code blocks from LLM response."""
        text = text.strip()
        if text.startswith("```"):
            # Find first newline
            first_newline = text.find("\n")
            if first_newline != -1:
                text = text[first_newline+1:]
        
        if text.endswith("```"):
            text = text[:-3]
            
        return text.strip()

    def _load_checkpoint(self, theme_root: str) -> Dict[str, Any]:
        """Load checkpoint file."""
        checkpoint_path = os.path.join(theme_root, ".checkpoint.json")
        if os.path.exists(checkpoint_path):
            try:
                with open(checkpoint_path, 'r') as f:
                    return json.load(f)
            except Exception as e:
                self.logger.warning(f"Failed to load checkpoint: {e}")
        return {"generated_files": []}

    def _update_checkpoint(self, theme_root: str, relative_path: str):
        """Update checkpoint with newly generated file."""
        checkpoint_path = os.path.join(theme_root, ".checkpoint.json")
        data = self._load_checkpoint(theme_root)
        if relative_path not in data["generated_files"]:
            data["generated_files"].append(relative_path)

        try:
            with open(checkpoint_path, 'w') as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            self.logger.error(f"Failed to save checkpoint: {e}")
