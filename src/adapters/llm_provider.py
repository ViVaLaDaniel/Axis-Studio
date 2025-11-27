"""
LLM Provider Base Interface for AXIS Studio.

This module provides an abstract interface for LLM providers.
Supports multiple backends: API-based and browser-based.
"""

import logging
from abc import ABC, abstractmethod
from typing import Dict, Any, Optional

class LLMProvider(ABC):
    """Abstract base class for LLM providers."""
    
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
    
    @abstractmethod
    def generate(self, prompt: str, **kwargs) -> str:
        """
        Generate a response from the LLM.
        
        Args:
            prompt: The input prompt
            **kwargs: Additional provider-specific parameters
            
        Returns:
            Generated text response
        """
        pass
    
    @abstractmethod
    def is_available(self) -> bool:
        """Check if the provider is available and configured."""
        pass


class LLMProviderFactory:
    """Factory for creating LLM provider instances."""
    
    _providers = {}
    
    @classmethod
    def register(cls, name: str, provider_class):
        """Register a new provider."""
        cls._providers[name] = provider_class
    
    @classmethod
    def create(cls, name: str, **config) -> LLMProvider:
        """Create a provider instance by name."""
        if name not in cls._providers:
            raise ValueError(f"Unknown provider: {name}")
        return cls._providers[name](**config)
    
    @classmethod
    def list_providers(cls):
        """List all registered providers."""
        return list(cls._providers.keys())

# Import adapters to ensure registration
# Note: In a real app, this might be dynamic or in __init__.py
try:
    import src.adapters.gemini_adapter
    import src.adapters.claude_adapter
    import src.adapters.openai_adapter
except ImportError:
    pass
