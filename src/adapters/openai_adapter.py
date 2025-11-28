"""
OpenAI Provider for AXIS Studio.
"""

import os
import logging
from typing import Optional
from openai import OpenAI

from src.adapters.llm_provider import LLMProvider, LLMProviderFactory

class OpenAIProvider(LLMProvider):
    """
    OpenAI Provider using the official OpenAI SDK.
    Requires OPENAI_API_KEY environment variable.
    """

    def __init__(self, model_name: str = 'gpt-4o'):
        super().__init__()
        self.model_name = model_name
        self.api_key = os.getenv('OPENAI_API_KEY')
        self.client = None
        self._configure()

    def _configure(self):
        """Configure the OpenAI SDK."""
        if not self.api_key:
            self.logger.warning("OPENAI_API_KEY not found in environment variables.")
            return

        self.client = OpenAI(api_key=self.api_key)

    def generate(self, prompt: str, **kwargs) -> str:
        """
        Generate content using OpenAI.
        """
        if not self.is_available():
            raise RuntimeError("OpenAI API key not configured.")

        try:
            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=[
                    {"role": "user", "content": prompt}
                ],
                temperature=kwargs.get('temperature', 0.7),
                max_tokens=kwargs.get('max_tokens', 4096)
            )

            return response.choices[0].message.content

        except Exception as e:
            self.logger.error(f"OpenAI generation failed: {e}")
            raise

    def is_available(self) -> bool:
        """Check if API key is present."""
        return bool(self.client)

# Register with factory
LLMProviderFactory.register('openai', OpenAIProvider)
