import os
from openai import OpenAI
from config import Config
from state_manager import save_state, load_state
from harpa_integration import execute_harpa

# Initialize OpenAI client
client = OpenAI(api_key=Config.OPENAI_API_KEY)

# Validate API keys
if Config.OPENAI_API_KEY.startswith("sk-placeholder") or Config.OPENAI_API_KEY == "":
    print("\n⚠️ WARNING: Using placeholder OpenAI API key")
    print("Please set your real OpenAI API key in .env file\n")
    exit(1)

if Config.HARPA_API_KEY.startswith("harpa-placeholder") or Config.HARPA_API_KEY == "":
    print("\n⚠️ WARNING: Using placeholder HARPA API key")
    print("Please get your HARPA API key from HARPA extension → Automate tab\n")
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
    
    # Initialize messages with improved system prompt
    messages = [
        {
            "role": "system", 
            "content": """You are an AI assistant that controls HARPA AI for web automation tasks.

IMPORTANT RULES:
1. Generate specific, actionable commands for HARPA
2. Include target URLs when possible
3. When task is complete, end your response with [TASK_COMPLETE]
4. Break complex tasks into smaller steps
5. Use clear, direct language for commands

Format your responses as direct commands that HARPA can execute.
Example: "Go to bestbuy.com and find the return policy for Sony headphones"
"""
        },
        {
            "role": "user", 
            "content": f"Task: {task_description}\n\nPrevious state: {state.get('progress', []) if state else 'Starting fresh'}"
        }
    ]
    
    max_iterations = 5  # Prevent infinite loops
    iteration = 0
    
    while iteration < max_iterations:
        try:
            iteration += 1
            print(f"\n--- Iteration {iteration} ---")
            
            # Make API call to OpenAI with proper parameters
            response = client.chat.completions.create(
                model=Config.AI_MODEL,
                messages=messages,
                max_tokens=Config.MAX_TOKENS,
                timeout=Config.REQUEST_TIMEOUT,
                temperature=0.3  # Lower temperature for more consistent automation
            )
            
            # Extract AI response
            ai_response = response.choices[0].message.content
            print(f"AI Command: {ai_response}")
            
            # Check for task completion BEFORE executing
            if "[TASK_COMPLETE]" in ai_response:
                print("✅ Task completed successfully!")
                # Save final state
                if state:
                    state['status'] = 'completed'
                    state['final_result'] = ai_response
                    save_state(task_id, state)
                return ai_response.replace("[TASK_COMPLETE]", "").strip()
            
            # Execute command through HARPA
            print("Executing command through HARPA...")
            result = execute_harpa(ai_response)
            print(f"HARPA Result: {result}")
            
            # Update state and messages
            if not state:
                state = {"task": task_description, "progress": []}
            
            state["progress"].append({
                "iteration": iteration,
                "command": ai_response,
                "result": result
            })
            save_state(task_id, state)
            
            # Add both AI response and HARPA result to message history
            messages.append({"role": "assistant", "content": ai_response})
            messages.append({"role": "user", "content": f"HARPA executed and returned: {result}\n\nWhat's the next step?"})
            
            # Check if HARPA result indicates completion
            completion_indicators = ["task completed", "found the information", "successfully retrieved", "policy found"]
            if any(indicator in result.lower() for indicator in completion_indicators):
                messages.append({
                    "role": "user", 
                    "content": "It looks like the task might be complete. Please review the results and respond with [TASK_COMPLETE] if satisfied."
                })
                
        except Exception as e:
            print(f"❌ Error in iteration {iteration}: {str(e)}")
            
            # Try to recover
            if iteration < max_iterations:
                print("🔄 Attempting to recover...")
                messages.append({
                    "role": "user", 
                    "content": f"There was an error: {str(e)}. Please try a different approach."
                })
            else:
                print("💥 Max retries exceeded")
                return None
    
    print("⏰ Max iterations reached - task may be incomplete")
    return state.get("progress", [])

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='AI Task Orchestrator with HARPA')
    parser.add_argument('--task', type=str, required=True, help='Task description')
    parser.add_argument('--task-id', type=str, default="default_task", help='Task identifier')
    
    args = parser.parse_args()
    
    print(f"🚀 Starting task: {args.task}")
    print(f"📋 Task ID: {args.task_id}")
    
    result = run_task(args.task, args.task_id)
    
    if result:
        print(f"\n🎯 Final Result: {result}")
    else:
        print("\n❌ Task failed or incomplete")