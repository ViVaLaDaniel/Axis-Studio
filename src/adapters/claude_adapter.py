"""
Claude Provider using Anthropic SDK for AXIS Studio.
"""

import os
import logging
from typing import Optional
import anthropic

from src.adapters.llm_provider import LLMProvider, LLMProviderFactory

class ClaudeProvider(LLMProvider):
    """
    Claude Provider using the official Anthropic SDK.
    Requires ANTHROPIC_API_KEY environment variable.
    """

    def __init__(self, model_name: str = 'claude-3-opus-20240229'):
        super().__init__()
        self.model_name = model_name
        self.api_key = os.getenv('ANTHROPIC_API_KEY')
        self.client = None
        self._configure()

    def _configure(self):
        """Configure the Anthropic SDK."""
        if not self.api_key:
            self.logger.warning("ANTHROPIC_API_KEY not found in environment variables.")
            return

        self.client = anthropic.Anthropic(api_key=self.api_key)

    def generate(self, prompt: str, **kwargs) -> str:
        """
        Generate content using Claude.
        """
        if not self.is_available():
            raise RuntimeError("Claude API key not configured.")

        try:
            response = self.client.messages.create(
                model=self.model_name,
                max_tokens=kwargs.get('max_tokens', 4096),
                temperature=kwargs.get('temperature', 0.7),
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )

            return response.content[0].text

        except Exception as e:
            self.logger.error(f"Claude generation failed: {e}")
            raise

    def is_available(self) -> bool:
        """Check if API key is present."""
        return bool(self.client)

# Register with factory
LLMProviderFactory.register('claude', ClaudeProvider)
