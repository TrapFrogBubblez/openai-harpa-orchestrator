import os
from openai import OpenAI
from config import Config
from state_manager import save_state, load_state
from harpa_integration import execute_harpa
if Config.OPENAI_API_KEY.startswith("sk-placeholder"):
    print("\n⚠️ WARNING: Using placeholder API key")
    print("Please set your real OpenAI API key in .env file\n")
    # Exit or continue with dummy logic
    exit(1)


client = OpenAI(api_key=Config.OPENAI_API_KEY)

def run_task(task_description: str, task_id: str = "default_task"):
    state = load_state(task_id)
    
    messages = [
        {"role": "system", "content": "You control HARPA AI. Format commands concisely as /scrape [URL] or /navigate [action]"},
        {"role": "user", "content": f"Task: {task_description}\n\nCurrent state: {str(state['progress'][-2:])}"}
    ]
    
    while True:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            temperature=0.1
        )
        gpt_instruction = response.choices[0].message.content
        
        if "TASK_COMPLETE" in gpt_instruction:
            return gpt_instruction
        
        print(f"\n>>> Executing: {gpt_instruction[:80]}...")
        harpa_result = execute_harpa(gpt_instruction)
        print(f"<<< HARPA Output ({len(harpa_result)} chars)")
        
        state['progress'].append({
            "step": len(state['progress']) + 1,
            "gpt_instruction": gpt_instruction,
            "harpa_result": harpa_result[:500] + "..." if len(harpa_result) > 500 else harpa_result
        })
        save_state(task_id, state)
        
        messages.append({"role": "assistant", "content": gpt_instruction})
        messages.append({"role": "user", "content": f"HARPA OUTPUT:\n{harpa_result}\n\nWhat next?"})

if __name__ == "__main__":
    result = run_task(
        task_description="Find return policy for Sony headphones on BestBuy.com",
        task_id="bestbuy_return_policy"
    )
    print("\n" + "="*50)
    print("TASK COMPLETE")
    print("="*50)
    print(result)
