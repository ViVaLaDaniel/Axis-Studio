import os
import json
import pytest
from unittest.mock import patch, MagicMock

from src.core.generator import ThemeGenerator

class TestIntegration:

    @patch('src.core.generator.LLMProviderFactory')
    @patch('src.core.generator.AxisContext')
    def test_full_theme_generation(self, mock_ctx_cls, mock_factory, tmp_path):
        """
        Simulate a full theme generation run.
        """
        # Setup Mocks
        mock_provider = MagicMock()
        mock_provider.generate.return_value = "{% comment %} Mocked Code {% endcomment %}"
        mock_factory.create.return_value = mock_provider

        mock_ctx = mock_ctx_cls.return_value
        mock_ctx.project_root = str(tmp_path)
        mock_ctx.get_path.return_value = str(tmp_path / "00_CORE_BRAIN")

        # Create fake brain
        brain_dir = tmp_path / "00_CORE_BRAIN"
        brain_dir.mkdir(parents=True)
        with open(brain_dir / "AI_THEME_BLUEPRINT.json", "w") as f:
            json.dump({"structure": {}}, f)

        # Run Generator
        gen = ThemeGenerator()
        gen.generate_theme("Test Brief", "integration_test_theme")

        # Verify Directory Structure
        theme_root = tmp_path / "output" / "integration_test_theme"
        assert theme_root.exists()
        assert (theme_root / "config/settings_schema.json").exists()
        assert (theme_root / "layout/theme.liquid").exists()
        assert (theme_root / ".checkpoint.json").exists()

        # Verify Checkpoint Content
        with open(theme_root / ".checkpoint.json", "r") as f:
            checkpoint = json.load(f)
            assert "config/settings_schema.json" in checkpoint["generated_files"]
