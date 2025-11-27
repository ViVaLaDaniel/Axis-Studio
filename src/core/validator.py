import json
import os
import logging
from typing import Dict, Any, Optional
from jsonschema import validate, ValidationError, Draft7Validator


class AxisValidator:
    def __init__(self):
        self.logger = logging.getLogger("AxisValidator")
        self.schemas = self._load_schemas()

    def _load_schemas(self) -> Dict[str, Dict[str, Any]]:
        """Load predefined JSON schemas for common AXIS data structures."""
        return {
            "behavior_tree": {
                "type": "object",
                "required": ["version", "tasks"],
                "properties": {
                    "version": {"type": "string"},
                    "description": {"type": "string"},
                    "tasks": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "required": ["id", "name", "type"],
                            "properties": {
                                "id": {"type": "string"},
                                "name": {"type": "string"},
                                "type": {"type": "string", "enum": ["command", "file_create", "file_read"]},
                                "enabled": {"type": "boolean"},
                                "details": {"type": "object"}
                            }
                        }
                    }
                }
            },
            "axis_config": {
                "type": "object",
                "required": ["project_name", "version", "paths", "llm_config"],
                "properties": {
                    "project_name": {"type": "string"},
                    "version": {"type": "string"},
                    "paths": {
                        "type": "object",
                        "required": ["core_brain", "src_root"],
                        "properties": {
                            "core_brain": {"type": "string"},
                            "runtime_engine": {"type": "string"},
                            "reports": {"type": "string"},
                            "src_root": {"type": "string"}
                        }
                    },
                    "llm_config": {
                        "type": "object",
                        "required": ["default_provider", "providers"],
                        "properties": {
                            "default_provider": {"type": "string"},
                            "providers": {"type": "object"}
                        }
                    },
                    "development": {"type": "object"}
                }
            }
        }

    def validate_json(self, data: Dict[str, Any], schema: Optional[Dict[str, Any]] = None, schema_name: Optional[str] = None) -> bool:
        """
        Validates data against a JSON schema.
        
        Args:
            data: The data to validate
            schema: Custom schema dict (optional)
            schema_name: Name of predefined schema (optional, e.g., 'behavior_tree', 'axis_config')
            
        Returns:
            True if valid, False otherwise
        """
        # Determine which schema to use
        if schema_name and schema_name in self.schemas:
            schema_to_use = self.schemas[schema_name]
            self.logger.debug(f"Using predefined schema: {schema_name}")
        elif schema:
            schema_to_use = schema
            self.logger.debug("Using custom schema")
        else:
            self.logger.warning("No schema provided for validation. Skipping validation.")
            return True
        
        # Validate
        try:
            validate(instance=data, schema=schema_to_use)
            self.logger.info("JSON validation successful")
            return True
        except ValidationError as e:
            self.logger.error(f"JSON validation failed: {e.message}")
            self.logger.error(f"Failed at path: {' -> '.join(str(p) for p in e.path)}")
            return False
        except Exception as e:
            self.logger.error(f"Unexpected error during validation: {e}")
            return False

    def validate_file_exists(self, path: str) -> bool:
        """Validates that a file exists at the given path."""
        exists = os.path.exists(path)
        if not exists:
            self.logger.warning(f"Validation failed: File not found at {path}")
        return exists

    def validate_behavior_tree(self, tree: Dict[str, Any]) -> bool:
        """
        Convenience method to validate a behavior tree.
        
        Args:
            tree: Behavior tree data structure
            
        Returns:
            True if valid, False otherwise
        """
        return self.validate_json(tree, schema_name="behavior_tree")

    def validate_axis_config(self, config: Dict[str, Any]) -> bool:
        """
        Convenience method to validate axis.config.json.
        
        Args:
            config: Config data structure
            
        Returns:
            True if valid, False otherwise
        """
        return self.validate_json(config, schema_name="axis_config")
