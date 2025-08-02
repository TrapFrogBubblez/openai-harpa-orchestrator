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
    
    # Initialize messages with FIXED system prompt
    messages = [
        {
            "role": "system", 
            "content": """You are an AI assistant that controls HARPA AI for web automation tasks.

CRITICAL RULES - FOLLOW EXACTLY:
1. You MUST execute commands through HARPA before completing any task
2. NEVER say [TASK_COMPLETE] until you have actually received results from HARPA
3. Give ONE specific command at a time for HARPA to execute
4. Wait for HARPA's response before proceeding
5. Only use [TASK_COMPLETE] after you have successfully completed the actual task

WORKFLOW:
- Step 1: Give HARPA a specific command (like "Go to google.com and search for Python automation")
- Step 2: Wait for HARPA to execute and return results
- Step 3: Review the results
- Step 4: If task is complete, THEN say [TASK_COMPLETE]

FORMAT YOUR COMMANDS CLEARLY:
- "Go to [website] and [specific action]"
- "Search for [query] on [website]"
- "Find [specific information] on [website]"

Do NOT complete tasks without actually executing them through HARPA first!"""
        },
        {
            "role": "user", 
            "content": f"Task: {task_description}\n\nPrevious state: {state.get('progress', []) if state else 'Starting fresh'}\n\nPlease execute this task step by step. Start by giving HARPA the first command."
        }
    ]
    
    max_iterations = 8  # Increased to allow for proper execution
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
                temperature=0.1  # Very low temperature for consistent automation
            )
            
            # Extract AI response
            ai_response = response.choices[0].message.content
            print(f"🤖 AI Command: {ai_response}")
            
            # Check for task completion BEFORE executing
            if "[TASK_COMPLETE]" in ai_response:
                print("✅ Task marked complete by AI!")
                # Save final state
                if state:
                    state['status'] = 'completed'
                    state['final_result'] = ai_response
                    save_state(task_id, state)
                return ai_response.replace("[TASK_COMPLETE]", "").strip()
            
            # Execute command through HARPA
            print("🔄 Executing command through HARPA...")
            result = execute_harpa(ai_response)
            print(f"🌐 HARPA Result: {result}")
            
            # Update state and messages
            if not state:
                state = {"task": task_description, "progress": []}
            
            state["progress"].append({
                "iteration": iteration,
                "command": ai_response,
                "result": result[:500]  # Truncate long results for storage
            })
            save_state(task_id, state)
            
            # Add both AI response and HARPA result to message history
            messages.append({"role": "assistant", "content": ai_response})
            messages.append({
                "role": "user", 
                "content": f"HARPA executed your command and returned:\n\n{result}\n\nBased on these results, what should we do next? If the task is successfully completed, respond with [TASK_COMPLETE]."
            })
            
            # Auto-detect potential completion based on result
            success_indicators = [
                "successfully", "completed", "found", "retrieved", 
                "search results", "information located", "task done"
            ]
            
            if any(indicator in result.lower() for indicator in success_indicators):
                print("🎯 HARPA result suggests possible completion...")
                # Don't auto-complete, let AI decide
            
        except Exception as e:
            print(f"❌ Error in iteration {iteration}: {str(e)}")
            
            # Try to recover with more specific error handling
            error_message = str(e)
            if "401" in error_message or "unauthorized" in error_message.lower():
                print("🔑 This looks like an API key issue. Check your HARPA API key.")
                return None
            elif "timeout" in error_message.lower():
                print("⏰ Request timed out. HARPA might be busy.")
                if iteration < max_iterations:
                    print("🔄 Retrying...")
                    messages.append({
                        "role": "user", 
                        "content": "The previous command timed out. Please try the same action again or try a simpler approach."
                    })
                    continue
            else:
                print(f"🐛 Unexpected error: {error_message}")
                if iteration < max_iterations:
                    print("🔄 Attempting to recover...")
                    messages.append({
                        "role": "user", 
                        "content": f"There was an error: {error_message}. Please try a different approach or simpler command."
                    })
                else:
                    print("💥 Max retries exceeded")
                    return None
    
    print("⏰ Max iterations reached - task may be incomplete")
    print("💡 Try breaking down the task into smaller steps")
    
    # Return the progress made
    if state and state.get("progress"):
        return f"Task incomplete but made progress: {len(state['progress'])} steps completed"
    return None

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='AI Task Orchestrator with HARPA')
    parser.add_argument('--task', type=str, required=True, help='Task description')
    parser.add_argument('--task-id', type=str, default="default_task", help='Task identifier')
    parser.add_argument('--debug', action='store_true', help='Enable debug output')
    
    args = parser.parse_args()
    
    print("🤖 AI-Powered HARPA Orchestrator")
    print("=" * 50)
    print(f"🚀 Starting task: {args.task}")
    print(f"📋 Task ID: {args.task_id}")
    print(f"🔧 Debug mode: {'ON' if args.debug else 'OFF'}")
    print("=" * 50)
    
    result = run_task(args.task, args.task_id)
    
    print("\n" + "=" * 50)
    if result:
        print(f"🎯 FINAL RESULT:\n{result}")
        print("✅ SUCCESS!")
    else:
        print("❌ TASK FAILED OR INCOMPLETE")
        print("💡 Try with a simpler task first to test the system")
    print("=" * 50)