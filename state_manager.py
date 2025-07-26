import json
import os
from config import Config

def save_state(task_id: str, state: dict):
    os.makedirs(Config.PERSISTENT_DIR, exist_ok=True)
    with open(f"{Config.PERSISTENT_DIR}/{task_id}_state.json", "w") as f:
        json.dump(state, f, indent=2)

def load_state(task_id: str) -> dict:
    try:
        with open(f"{Config.PERSISTENT_DIR}/{task_id}_state.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"task": task_id, "progress": []}
