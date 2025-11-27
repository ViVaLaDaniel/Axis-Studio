import json
import os
import logging
from typing import Dict, Any, Optional

class AxisContext:
    def __init__(self, config_path: str = "axis.config.json"):
        # Assuming this file is in src/core/, project root is ../../
        self.project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
        self.config_path = os.path.join(self.project_root, config_path)
        self.config: Dict[str, Any] = {}
        self.brain: Dict[str, Any] = {}
        self.logger = logging.getLogger("AxisContext")
        
        self.load_config()
        
    def load_config(self):
        """Loads the main axis.config.json"""
        if not os.path.exists(self.config_path):
            self.logger.error(f"Config file not found: {self.config_path}")
            raise FileNotFoundError(f"Config file not found: {self.config_path}")
            
        with open(self.config_path, 'r', encoding='utf-8') as f:
            try:
                self.config = json.load(f)
                self.logger.info(f"Loaded configuration from {self.config_path}")
            except json.JSONDecodeError as e:
                self.logger.error(f"Error decoding config JSON: {e}")
                raise

    def get_path(self, key: str) -> str:
        """Returns the absolute path for a given config key"""
        rel_path = self.config.get("paths", {}).get(key)
        if not rel_path:
            return None
        return os.path.join(self.project_root, rel_path)

    def load_brain(self):
        """Loads all JSON files from 00_CORE_BRAIN into memory"""
        brain_path = self.get_path("core_brain")
        if not brain_path or not os.path.exists(brain_path):
            self.logger.warning(f"Core Brain path not found or invalid: {brain_path}")
            return

        self.logger.info(f"Loading Brain from: {brain_path}")
        for filename in os.listdir(brain_path):
            if filename.endswith(".json"):
                file_path = os.path.join(brain_path, filename)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        key = filename.replace(".json", "")
                        self.brain[key] = data
                        self.logger.debug(f"Loaded brain module: {key}")
                except Exception as e:
                    self.logger.error(f"Failed to load brain module {filename}: {e}")
