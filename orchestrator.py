import os
from openai import OpenAI
from config import Config
from state_manager import save_state, load_state
from harpa_integration import execute_harpa

# Initialize OpenAI client
client = OpenAI(api_key=Config.OPENAI_API_KEY)

# Validate API key
if Config.OPENAI_API_KEY.startswith("sk-placeholder") or Config.OPENAI_API_KEY == "":
    print("\n⚠️ WARNING: Using placeholder API key")
    print("Please set your real OpenAI API key in .env file\n")
    exit(1)

def run_task(task_description: str, task_id: str = "default_task"):
    """
    Execute an AI-powered task using OpenAI and HARPA integration
    
    Args:
        task_description: Natural language description of the task
        task_id: Unique identifier for persisting task state
    """
    # Load previous state if exists
    state = load_state(task_id)
    
    # Initialize messages with system prompt
    messages = [
        {
            "role": "system", 
            "content": "You control HARPA AI. Format commands for browser automation."
        },
        {
            "role": "user", 
            "content": f"Task: {task_description}\n\nCurrent state: {state or 'No previous state'}"
        }
    ]
    
    while True:
        try:
            # Make API call to OpenAI with proper parameters
            response = client.chat.completions.create(
                model=Config.AI_MODEL,
                messages=messages,
                max_tokens=Config.MAX_TOKENS,
                timeout=Config.REQUEST_TIMEOUT
            )
            
            # Extract AI response
            ai_response = response.choices[0].message.content
            print(f"AI Response: {ai_response}")
            
            # Execute command through HARPA
            result = execute_harpa(ai_response)
            print(f"HARPA Result: {result}")
            
            # Update state and messages
            state = {"last_action": ai_response, "result": result}
            save_state(task_id, state)
            
            # Add AI response to message history
            messages.append({"role": "assistant", "content": ai_response})
            
            # Check for task completion
            if "[TASK COMPLETE]" in ai_response:
                print("Task completed successfully!")
                return result
                
        except Exception as e:
            print(f"Error: {str(e)}")
            return None

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='AI Task Orchestrator')
    parser.add_argument('--task', type=str, required=True, help='Task description')
    parser.add_argument('--task-id', type=str, default="default_task", help='Task identifier')
    
    args = parser.parse_args()
    
    print(f"Starting task: {args.task}")
    result = run_task(args.task, args.task_id)
    
    if result:
        print(f"Final Result: {result}")
    else:
        print("Task failed")
