import json
import os
import subprocess
import logging
from typing import Dict, Any, Optional

from src.core.context import AxisContext
from src.core.validator import AxisValidator

class AxisOrchestrator:
    def __init__(self):
        # Configure logging if not already configured
        if not logging.getLogger().handlers:
            logging.basicConfig(
                level=logging.INFO,
                format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
        self.logger = logging.getLogger("AxisOrchestrator")
        
        self.logger.info("Initializing Axis Orchestrator...")
        self.context = AxisContext()
        self.validator = AxisValidator()
        
        # Load the brain on init
        self.context.load_brain()

    def load_behavior_tree(self) -> Optional[Dict[str, Any]]:
        """Loads the behavior tree from the Brain or file system."""
        # Try to get from loaded brain first
        tree = self.context.brain.get("AI_BEHAVIOR_TREE")
        if tree:
            self.logger.info("Loaded Behavior Tree from Memory (Brain).")
            return tree
            
        # Fallback to file system if not in memory (legacy support)
        brain_path = self.context.get_path("core_brain")
        if brain_path:
            tree_path = os.path.join(brain_path, "AI_BEHAVIOR_TREE.json")
            if os.path.exists(tree_path):
                self.logger.info(f"Loading Behavior Tree from file: {tree_path}")
                with open(tree_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
        
        self.logger.error("Behavior Tree not found.")
        return None

    def execute_task(self, task: Dict[str, Any]):
        """Executes a single task."""
        task_name = task.get("name", "Unnamed Task")
        task_type = task.get("type")
        details = task.get("details", {})
        
        self.logger.info(f"[EXECUTING]: {task_name} (Type: {task_type})")
        
        if task_type == "command":
            self._execute_command(details)
        elif task_type == "file_create":
            self._execute_file_create(details)
        elif task_type == "file_read":
            self._execute_file_read(details)
        else:
            self.logger.warning(f"Unknown task type: {task_type}")

    def _execute_command(self, details: Dict[str, Any]):
        command = details.get("command")
        if not command:
            self.logger.error("Command details missing 'command' field.")
            return
            
        self.logger.info(f"  -> Running Shell Command: {command}")
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
            if result.stdout:
                self.logger.info(f"  STDOUT: {result.stdout.strip()}")
            if result.stderr:
                self.logger.warning(f"  STDERR: {result.stderr.strip()}")
        except subprocess.CalledProcessError as e:
            self.logger.error(f"  Command failed: {e}")

    def _execute_file_create(self, details: Dict[str, Any]):
        path = details.get("path")
        content = details.get("content", "")
        
        if not path:
            self.logger.error("file_create missing 'path'")
            return
            
        # Resolve path relative to project root if not absolute
        if not os.path.isabs(path):
            path = os.path.join(self.context.project_root, path)
            
        self.logger.info(f"  -> Creating File: {path}")
        try:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
            self.logger.info("  File created successfully.")
        except Exception as e:
            self.logger.error(f"  Failed to create file: {e}")

    def _execute_file_read(self, details: Dict[str, Any]):
        path = details.get("path")
        if not path:
            self.logger.error("file_read missing 'path'")
            return
            
        if not os.path.isabs(path):
            path = os.path.join(self.context.project_root, path)
            
        self.logger.info(f"  -> Reading File: {path}")
        if self.validator.validate_file_exists(path):
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    self.logger.info(f"  Content ({len(content)} bytes) read.")
            except Exception as e:
                self.logger.error(f"  Failed to read file: {e}")

    def run(self):
        """Main execution loop."""
        tree = self.load_behavior_tree()
        if not tree or 'tasks' not in tree:
            self.logger.warning("No tasks to execute.")
            return

        self.logger.info(f"--- Starting Execution of {len(tree['tasks'])} tasks ---")
        for task in tree['tasks']:
            if task.get("enabled", True):
                self.execute_task(task)
            else:
                self.logger.info(f"[SKIPPING]: {task.get('name')} (Disabled)")
        self.logger.info("--- Execution Finished ---")

# Standalone execution for backward compatibility
def execute_engine(tree=None):
    orchestrator = AxisOrchestrator()
    orchestrator.run()

if __name__ == "__main__":
    orchestrator = AxisOrchestrator()
    orchestrator.run()
