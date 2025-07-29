import json
import os
import logging
from typing import Optional, Dict
from config import Config

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def save_state(task_id: str, state: Dict) -> None:
    """Save the state dictionary to a JSON file, ensuring directory exists."""
    try:
        os.makedirs(Config.PERSISTENT_DIR, exist_ok=True)
        file_path = os.path.join(Config.PERSISTENT_DIR, f"{task_id}_state.json")
        with open(file_path, "w") as f:
            json.dump(state, f, indent=2)
        logger.info(f"State saved for task_id '{task_id}' at '{file_path}'")
    except Exception as e:
        logger.error(f"Failed to save state for task_id '{task_id}': {e}")

def load_state(task_id: str) -> Optional[Dict]:
    """Load the state dictionary from JSON file. Returns default if not found."""
    file_path = os.path.join(Config.PERSISTENT_DIR, f"{task_id}_state.json")
    try:
        with open(file_path, "r") as f:
            state = json.load(f)
        logger.info(f"State loaded for task_id '{task_id}' from '{file_path}'")
        return state
    except FileNotFoundError:
        logger.warning(f"No saved state found for task_id '{task_id}'. Returning default state.")
        return {"task": task_id, "progress": []}
    except json.JSONDecodeError as e:
        logger.error(f"Corrupted state file for task_id '{task_id}': {e}. Returning default state.")
        return {"task": task_id, "progress": []}
    except Exception as e:
        logger.error(f"Unexpected error loading state for task_id '{task_id}': {e}. Returning default state.")
        return {"task": task_id, "progress": []}
