"""
Theme Generator Module for AXIS Studio.

This module handles the autonomous generation of Shopify themes.
It uses the LLM Provider to generate code based on the AI_THEME_BLUEPRINT.
"""

import os
import json
import logging
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
    3. Generate Code (iteratively for each file)
    4. Write to Disk
    """
    
    def __init__(self, provider_name: str = 'gemini_browser'):
        self.logger = logging.getLogger("ThemeGenerator")
        self.context = AxisContext()
        self.context.load_brain()
        
        self.orchestrator = AxisOrchestrator()
        
        self.logger.info(f"Initializing LLM Provider: {provider_name}")
        self.provider = LLMProviderFactory.create(provider_name)
        
        # Load Blueprint
        blueprint_path = os.path.join(self.context.brain_path, "AI_THEME_BLUEPRINT.json")
        with open(blueprint_path, 'r', encoding='utf-8') as f:
            self.blueprint = json.load(f)
            
    def generate_theme(self, brief: str, theme_name: str):
        """
        Generate a full theme based on the brief.
        """
        self.logger.info(f"🚀 Starting Theme Generation: '{theme_name}'")
        self.logger.info(f"📝 Brief: {brief}")
        
        # 1. Login if needed
        if hasattr(self.provider, 'login'):
            print("🔐 Logging in to LLM Provider...")
            self.provider.login()
            
        # 2. Create Theme Directory
        theme_root = os.path.join(self.context.project_root, "output", theme_name)
        self.logger.info(f"📂 Theme Root: {theme_root}")
        
        # 3. Generate Core Files (Iterative)
        # We start with the essentials defined in blueprint
        
        # A. Config
        self._generate_file(theme_root, "config/settings_schema.json", brief, "Shopify settings_schema.json")
        
        # B. Layout
        self._generate_file(theme_root, "layout/theme.liquid", brief, "Shopify theme.liquid layout file. Must include {{ content_for_header }} and {{ content_for_layout }}.")
        
        # C. Assets
        self._generate_file(theme_root, "assets/base.css", brief, "Main CSS file. Use CSS variables.")
        
        # D. Sections (Hero)
        self._generate_file(theme_root, "sections/hero.liquid", brief, "Hero section with image and text settings.")
        
        # E. Templates (Index)
        self._generate_file(theme_root, "templates/index.json", brief, "JSON template for homepage including the hero section.")
        
        self.logger.info(f"✅ Theme Generation Complete: {theme_root}")
        
        if hasattr(self.provider, 'close'):
            self.provider.close()

    def _generate_file(self, theme_root: str, relative_path: str, brief: str, context: str):
        """Generate a single file using LLM."""
        full_path = os.path.join(theme_root, relative_path)
        self.logger.info(f"  👉 Generating: {relative_path}...")
        
        prompt = f"""
        ACT AS: Senior Shopify Developer.
        TASK: Write the code for the file '{relative_path}'.
        CONTEXT: {context}
        PROJECT BRIEF: {brief}
        
        RULES:
        - Return ONLY the code. No markdown code blocks, no explanations.
        - Valid syntax for the file type.
        - Use standard Shopify Liquid tags.
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
            
        except Exception as e:
            self.logger.error(f"  ❌ Failed to generate {relative_path}: {e}")

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
