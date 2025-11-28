"""
Gemini Provider using Google Generative AI SDK for AXIS Studio.
"""

import os
import logging
from typing import Optional
import google.generativeai as genai
from google.api_core import retry

from src.adapters.llm_provider import LLMProvider, LLMProviderFactory

class GeminiProvider(LLMProvider):
    """
    Gemini Provider using the official Google Generative AI SDK.
    Requires GEMINI_API_KEY environment variable.
    """

    def __init__(self, model_name: str = 'gemini-1.5-flash'):
        super().__init__()
        self.model_name = model_name
        self.api_key = os.getenv('GEMINI_API_KEY')
        self._configure()

    def _configure(self):
        """Configure the GenAI SDK."""
        if not self.api_key:
            self.logger.warning("GEMINI_API_KEY not found in environment variables.")
            return

        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel(self.model_name)

    def generate(self, prompt: str, **kwargs) -> str:
        """
        Generate content using Gemini.

        Args:
            prompt: The input prompt
            **kwargs: Additional parameters (temperature, etc.)

        Returns:
            Generated text
        """
        if not self.is_available():
            raise RuntimeError("Gemini API key not configured.")

        try:
            # Set generation config
            generation_config = genai.types.GenerationConfig(
                temperature=kwargs.get('temperature', 0.7),
                max_output_tokens=kwargs.get('max_tokens', 8192),
            )

            # Generate content with retry logic
            response = self.model.generate_content(
                prompt,
                generation_config=generation_config
            )

            if response.text:
                return response.text
            else:
                self.logger.warning("Gemini returned empty response.")
                return ""

        except Exception as e:
            self.logger.error(f"Gemini generation failed: {e}")
            raise

    def is_available(self) -> bool:
        """Check if API key is present."""
        return bool(self.api_key)

# Register with factory
LLMProviderFactory.register('gemini', GeminiProvider)
