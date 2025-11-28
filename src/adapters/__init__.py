# This file makes the 'adapters' directory a Python package
# and ensures that all provider modules are loaded and registered.

from . import gemini_browser
from . import gemini_api_provider
# To add more providers, just import them here, e.g.:
# from . import openai_provider
