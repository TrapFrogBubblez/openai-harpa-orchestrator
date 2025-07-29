import os
import json
import time
import traceback
from typing import Dict, Any

import openai
from harpa_integration import HarpaExtension
from state_manage import StateManager
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
        self.harpa = HarpaExtension(Config.HARPA_EXTENSION_PATH, Config.HARPA_EXTENSION_ID)
        self.openai_client = OpenAIClient()
        self.state = StateManager(Config.PERSISTENT_DIR)

    def execute_task(self, task_id: str, task_data: Dict[str, Any]):
        print(f"[INFO] Executing task: {task_id}")
        profile = TASK_PROFILES.get(task_id)

        if not profile:
            print(f"[ERROR] No profile found for task_id: {task_id}")
            return

        try:
            context = profile['context']
            url = task_data.get('url')
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
        except Exception as e:
            print(f"[ERROR] Exception while executing task {task_id}:", e)
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
