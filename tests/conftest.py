import pytest
from unittest.mock import MagicMock
import os
import sys

# Add src to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.adapters.llm_provider import LLMProvider

@pytest.fixture
def mock_llm_provider(mocker):
    """Mock the LLM provider to avoid real API calls."""
    mock = mocker.Mock(spec=LLMProvider)
    mock.generate.return_value = "Mocked Code Content"
    mock.is_available.return_value = True
    return mock
