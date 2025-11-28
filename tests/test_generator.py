import os
import json
import pytest
from unittest.mock import MagicMock, patch

from src.core.generator import ThemeGenerator
from src.core.context import AxisContext
from src.adapters.llm_provider import LLMProviderFactory

class TestThemeGenerator:

    @pytest.fixture
    def mock_context(self, mocker, tmp_path):
        """Mock AxisContext to use a temporary directory."""
        mock = mocker.MagicMock(spec=AxisContext)
        mock.project_root = str(tmp_path)
        mock.get_path.return_value = str(tmp_path / "brain")
        # Mock brain load
        mock.brain = {"AI_THEME_BLUEPRINT": {"structure": {}}}
        return mock

    @patch('src.core.generator.AxisContext')
    @patch('src.core.generator.LLMProviderFactory')
    def test_init(self, mock_factory, mock_context_cls, mock_llm_provider):
        """Test generator initialization."""
        mock_factory.create.return_value = mock_llm_provider

        gen = ThemeGenerator(provider_name='test_provider')

        assert gen.provider == mock_llm_provider
        mock_factory.create.assert_called_with('test_provider')

    @patch('src.core.generator.AxisContext')
    @patch('src.core.generator.LLMProviderFactory')
    def test_generate_file_success(self, mock_factory, mock_context_cls, mock_llm_provider, tmp_path):
        """Test single file generation."""
        mock_factory.create.return_value = mock_llm_provider

        # Setup mock context
        mock_ctx = mock_context_cls.return_value
        mock_ctx.project_root = str(tmp_path)
        mock_ctx.get_path.return_value = None # Disable brain loading for this test

        gen = ThemeGenerator()
        theme_root = str(tmp_path / "output" / "test_theme")
        os.makedirs(theme_root, exist_ok=True)

        # Mock LLM response
        mock_llm_provider.generate.return_value = "Liquid Code"

        success = gen._generate_file(theme_root, "layout/theme.liquid", "Brief", "Context")

        assert success is True
        assert os.path.exists(os.path.join(theme_root, "layout/theme.liquid"))
        with open(os.path.join(theme_root, "layout/theme.liquid"), 'r') as f:
            assert f.read() == "Liquid Code"

    @patch('src.core.generator.AxisContext')
    @patch('src.core.generator.LLMProviderFactory')
    def test_clean_response(self, mock_factory, mock_context_cls):
        """Test markdown cleaning."""
        gen = ThemeGenerator()

        raw = "```liquid\n{{ content }}\n```"
        clean = gen._clean_response(raw)
        assert clean == "{{ content }}"

        raw_no_lang = "```\n{{ content }}\n```"
        clean = gen._clean_response(raw_no_lang)
        assert clean == "{{ content }}"
