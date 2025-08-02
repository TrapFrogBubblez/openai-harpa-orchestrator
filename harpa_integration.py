import requests
from playwright.sync_api import sync_playwright
from config import Config
import time
import json

class HARPAIntegration:
    def __init__(self):
        self.api_key = Config.HARPA_API_KEY  # We'll need to add this to config
        self.api_url = "https://api.harpa.ai/api/v1/grid"
        self.headers = {"Authorization": f"Bearer {self.api_key}"}
    
    def execute_harpa_command(self, command: str, url: str = None, action_type: str = "prompt") -> str:
        """
        Execute a command through HARPA's actual API
        
        Args:
            command: Natural language command from GPT-4o
            url: Target URL for the action (optional)
            action_type: Type of HARPA action (prompt, scrape, command)
        """
        try:
            # Parse the command to extract URL if not provided
            if not url and "http" in command:
                # Simple URL extraction - could be improved
                words = command.split()
                for word in words:
                    if word.startswith("http"):
                        url = word
                        break
            
            # Default URL if none found
            if not url:
                url = "https://www.google.com"
            
            # Prepare the payload for HARPA API
            payload = {
                "action": action_type,
                "url": url,
                "prompt": command,
                "connection": "GPT-4",  # Use GPT-4 model in HARPA
                "timeout": 30000,
                "node": "default"
            }
            
            print(f"Sending to HARPA API: {json.dumps(payload, indent=2)}")
            
            # Make the API request
            response = requests.post(
                self.api_url,
                json=payload,
                headers=self.headers,
                timeout=30
            )
            
            if response.status_code == 200:
                result = response.json()
                if result.get("status") == "completed":
                    return result["results"]["message"]
                else:
                    return f"HARPA Error: {result.get('message', 'Unknown error')}"
            else:
                return f"HTTP Error {response.status_code}: {response.text}"
                
        except Exception as e:
            return f"Integration Error: {str(e)}"
    
    def execute_with_browser_context(self, command: str, target_url: str) -> str:
        """
        Alternative method using Playwright + HARPA API for authenticated sites
        """
        try:
            with sync_playwright() as p:
                # Launch browser with persistent context for authentication
                browser = p.chromium.launch_persistent_context(
                    user_data_dir="/tmp/harpa-profile",
                    args=[
                        f"--disable-extensions-except={Config.HARPA_EXTENSION_PATH}",
                        f"--load-extension={Config.HARPA_EXTENSION_PATH}",
                        "--headless=new"
                    ]
                )
                
                page = browser.new_page()
                page.goto(target_url, wait_until="networkidle")
                
                # Get page content for context
                content = page.content()
                
                # Close browser before API call
                browser.close()
                
                # Now use HARPA API with the context
                return self.execute_harpa_command(
                    f"{command} Context: {content[:1000]}...",  # Truncate content
                    target_url
                )
                
        except Exception as e:
            return f"Browser Context Error: {str(e)}"

# Backward compatibility function
def execute_harpa(command: str) -> str:
    """
    Main function to replace the broken original
    """
    harpa = HARPAIntegration()
    return harpa.execute_harpa_command(command)