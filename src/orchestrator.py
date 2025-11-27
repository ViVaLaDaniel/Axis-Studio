import json
import os
import subprocess
import logging

# --- Настройка логирования ---
LOG_FILE = "engine.log"
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)

# --- Constants ---
CORE_BRAIN_PATH = "00_CORE_BRAIN"
BEHAVIOR_TREE_FILE = "AI_BEHAVIOR_TREE.json"

def load_behavior_tree():
    """Loads the behavior tree from the JSON file."""
    tree_path = os.path.join(CORE_BRAIN_PATH, BEHAVIOR_TREE_FILE)
    logging.info(f"--- Loading behavior tree from: {tree_path} ---")
    
    if not os.path.exists(tree_path):
        logging.error(f"Behavior tree not found at {tree_path}")
        return None
        
    with open(tree_path, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError as e:
            logging.error(f"Error decoding JSON: {e}")
            return None

def execute_engine(tree):
    """Executes tasks from the behavior tree."""
    if not tree or 'tasks' not in tree:
        logging.warning("--- Invalid or empty behavior tree. Nothing to execute. ---")
        return

    logging.info(f"--- Found {len(tree['tasks'])} tasks in the behavior tree. ---")
    
    for task in tree['tasks']:
        if task.get("enabled", False):
            logging.info(f"[EXECUTING TASK]: {task.get('name', 'Unnamed Task')}")
            task_type = task.get("type")
            
            if task_type == "command":
                details = task.get("details", {})
                command = details.get("command")
                logging.info(f"  - Type: Command")
                logging.info(f"  - Action: Running command -> {command}")
                
                try:
                    result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
                    stdout = result.stdout.strip()
                    if stdout:
                        logging.info(f"  - STDOUT: {stdout}")
                    stderr = result.stderr.strip()
                    if stderr:
                        logging.warning(f"  - STDERR: {stderr}")
                except subprocess.CalledProcessError as e:
                    logging.error(f"  - ERROR: Command failed with exit code {e.returncode}")
                    logging.error(f"  - STDERR: {e.stderr.strip()}")
                except FileNotFoundError:
                    logging.error(f"  - ERROR: Command not found. Is the program in your PATH?")
                
            else:
                logging.warning(f"  - Type: {task_type} (Not implemented yet)")
        else:
            logging.info(f"[SKIPPING TASK]: {task.get('name', 'Unnamed Task')} (disabled)")
            
    logging.info("--- Engine execution finished. ---")


if __name__ == "__main__":
    logging.info("--- AXIS AI Execution Engine v0.3 ---")
    behavior_tree = load_behavior_tree()
    if behavior_tree:
        execute_engine(behavior_tree)
