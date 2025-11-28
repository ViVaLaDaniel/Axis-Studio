"""
Gemini API Provider for AXIS Studio.

This module provides direct API access to Google Gemini
using the official google-generativeai library.
It relies on Application Default Credentials (ADC).
"""

import os
import logging
import time
from collections import deque
import google.generativeai as genai
from google.api_core import exceptions as google_exceptions

from src.adapters.llm_provider import LLMProvider, LLMProviderFactory

# Configure the Gemini API key from environment variables
# The library automatically looks for GOOGLE_API_KEY
if 'GOOGLE_API_KEY' in os.environ:
    genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

class GeminiApiProvider(LLMProvider):
    """
    LLM Provider for Google Gemini using the official API.
    Handles authentication via ADC (gcloud auth application-default login)
    or an API key (GOOGLE_API_KEY).
    Includes a client-side rate limiter.
    """

    def __init__(self, model_name: str = 'gemini-1.5-flash-latest', rpm_limit: int = 8):
        super().__init__()
        self.model_name = model_name
        self.model = None
        if self.is_available():
            self.model = genai.GenerativeModel(self.model_name)
        
        # Rate limiting
        self.rpm_limit = rpm_limit
        self.request_timestamps = deque()

    def _enforce_rate_limit(self):
        """Client-side rate limiter to avoid hitting API limits."""
        current_time = time.time()
        
        # Remove timestamps older than 60 seconds
        while self.request_timestamps and self.request_timestamps[0] <= current_time - 60:
            self.request_timestamps.popleft()
        
        if len(self.request_timestamps) >= self.rpm_limit:
            # Calculate wait time based on the oldest request in the window
            time_since_first_request = current_time - self.request_timestamps[0]
            time_to_wait = 60 - time_since_first_request
            
            self.logger.warning(
                f"Rate limit of {self.rpm_limit}/min reached. "
                f"Waiting for {time_to_wait:.1f} seconds."
            )
            if time_to_wait > 0:
                time.sleep(time_to_wait)
        
        self.request_timestamps.append(time.time())

    def is_available(self) -> bool:
        """
        Check if the provider is available and configured.
        It's available if the library is installed and either an API key
        is set or ADC are found.
        """
        try:
            # The library performs its own credential search.
            # We can check for a key, but the most reliable test
            # is to try a lightweight API call, like listing models.
            if os.getenv('GOOGLE_API_KEY'):
                return True
            
            # If no API key, ADC is the fallback. A simple way to check
            # without making a network call is to see if the gcloud
            # config directory exists, but this is not foolproof.
            # The best check is to let the library handle it.
            return True # Assume available and let it fail gracefully on generate
        except Exception as e:
            self.logger.error(f"Gemini API provider not available: {e}")
            return False

    def generate(self, prompt: str, **kwargs) -> str:
        """
        Generate a response from the Gemini API, respecting the rate limit.
        """
        if not self.model:
            raise RuntimeError("Gemini API model is not initialized. Check configuration.")

        # Enforce rate limit before making the call
        self._enforce_rate_limit()

        self.logger.info(f"Generating response with model '{self.model_name}'...")
        try:
            # Generate content
            response = self.model.generate_content(prompt)
            
            # Extract the text from the response
            if response.parts:
                return ''.join(part.text for part in response.parts if part.text)
            else:
                # Handle cases where the response might be blocked or empty
                self.logger.warning("Received an empty or blocked response from Gemini API.")
                return ""
                
        except google_exceptions.PermissionDenied as e:
            self.logger.error(
                "Gemini API permission denied. "
                "Ensure your API key is valid or you are logged in with "
                "'gcloud auth application-default login'."
            )
            raise RuntimeError("Gemini API permission denied.") from e
        except Exception as e:
            self.logger.error(f"An unexpected error occurred during Gemini API call: {e}")
            raise RuntimeError("Failed to generate content with Gemini API.") from e

# Register this provider with the factory
LLMProviderFactory.register('gemini_api', GeminiApiProvider)
