import os
import json
import time
import traceback
from typing import Dict, Any

import openai
from harpa_integration import HarpaExtension, HarpaUnavailableException
from state_manager import StateManager
from TASK_PROFILES import TASK_PROFILES
from config import Config

openai.api_key = Config.OPENAI_API_KEY


class OpenAIClient:
    def __init__(self):
        self.model = Config.AI_MODEL
        self.max_tokens = Config.MAX_TOKENS
        self.timeout = Config.REQUEST_TIMEOUT

    def chat(self, messages):
        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=messages,
                max_tokens=self.max_tokens,
                timeout=self.timeout,
            )
            return response['choices'][0]['message']['content']
        except Exception as e:
            print("OpenAI API error:", e)
            return None


class Orchestrator:
    def __init__(self):
        # Adjusted to match HarpaExtension constructor signature:
        self.harpa = HarpaExtension()
        self.openai_client = OpenAIClient()
        self.state = StateManager(Config.PERSISTENT_DIR)

    def ensure_harpa_ready(self):
        # Assuming HarpaExtension has is_running(), launch(), and check_connection() methods:
        if not getattr(self.harpa, 'is_running', lambda: False)():
            print("[INFO] Harpa is not running. Attempting to launch...")
            if hasattr(self.harpa, 'launch'):
                self.harpa.launch()
            for _ in range(10):
                if hasattr(self.harpa, 'check_connection') and self.harpa.check_connection():
                    print("[INFO] Harpa connected successfully.")
                    return True
                time.sleep(1)
            print("[ERROR] Failed to connect to Harpa after launching.")
            return False
        else:
            if hasattr(self.harpa, 'check_connection') and self.harpa.check_connection():
                return True
            else:
                print("[ERROR] Harpa appears to be running but not responding.")
                return False

    def execute_task(self, task_id: str, task_data: Dict[str, Any]):
        print(f"[INFO] Executing task: {task_id}")
        profile = TASK_PROFILES.get(task_id)

        if not profile:
            print(f"[ERROR] No profile found for task_id: {task_id}")
            return

        if not self.ensure_harpa_ready():
            print(f"[ERROR] Skipping task {task_id} due to Harpa being unavailable.")
            return

        try:
            context = profile['description']
            url = task_data.get('url')

            if not url:
                print(f"[WARNING] No URL provided for task {task_id}; skipping scraping.")
                scrape_data = ""
            else:
                scrape_data = self.harpa.scrape(url)

            messages = [
                {"role": "system", "content": context},
                {"role": "user", "content": scrape_data}
            ]

            reply = self.openai_client.chat(messages)
            if reply:
                print(f"[RESULT] Task {task_id} Output:\n{reply}\n")
                self.state.save_result(task_id, reply)
            else:
                print(f"[WARNING] No response from OpenAI for task {task_id}")
        except HarpaUnavailableException as he:
            print(f"[ERROR] Harpa became unavailable during task {task_id}: {he}")
        except Exception as e:
            print(f"[ERROR] Exception while executing task {task_id}: {e}")
            traceback.print_exc()

    def run(self):
        print("[INFO] Orchestrator started. Listening for tasks...")
        while True:
            task = self.state.fetch_next_task()
            if task:
                self.execute_task(task['id'], task['data'])
            else:
                print("[INFO] No new tasks. Sleeping...")
                time.sleep(5)


if __name__ == "__main__":
    orchestrator = Orchestrator()
    orchestrator.run()
