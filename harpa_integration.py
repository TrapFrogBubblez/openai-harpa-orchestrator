import requests
from playwright.sync_api import sync_playwright
from config import Config
import time
import json

class HARPAIntegration:
    def __init__(self):
        self.api_key = Config.HARPA_API_KEY
        self.api_url = "https://api.harpa.ai/api/v1/grid"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
    
    def execute_harpa_command(self, command: str, url: str = None) -> str:
        """
        Execute a command through HARPA's corrected API
        
        Args:
            command: Natural language command from GPT-4o
            url: Target URL for the action (optional)
        """
        try:
            # Parse URL from command if not provided
            if not url:
                # Extract URL from common patterns
                import re
                url_pattern = r'https?://[^\s]+'
                urls = re.findall(url_pattern, command)
                if urls:
                    url = urls[0]
                elif "binance" in command.lower():
                    url = "https://www.binance.com"
                elif "google" in command.lower():
                    url = "https://www.google.com"
                else:
                    url = "https://www.google.com"  # Default fallback
            
            # Prepare the CORRECTED payload for HARPA API
            payload = {
                "action": "command",  # Changed from "prompt" to "command"
                "url": url,
                "name": "Custom Command",  # Required for command action
                "inputs": [command],  # Pass command as input
                "resultParam": "message",  # Get the result message
                "timeout": 30000,
                "node": "default"  # Use default node
            }
            
            print(f"Sending CORRECTED payload to HARPA API: {json.dumps(payload, indent=2)}")
            
            # Make the API request
            response = requests.post(
                self.api_url,
                json=payload,
                headers=self.headers,
                timeout=30
            )
            
            print(f"Response Status: {response.status_code}")
            print(f"Response Headers: {dict(response.headers)}")
            
            if response.status_code == 200:
                result = response.json()
                print(f"Full API Response: {json.dumps(result, indent=2)}")
                
                # Handle different response formats
                if isinstance(result, dict):
                    if "results" in result:
                        return str(result["results"])
                    elif "message" in result:
                        return result["message"]
                    elif "data" in result:
                        return str(result["data"])
                    else:
                        return str(result)
                else:
                    return str(result)
                    
            else:
                error_text = response.text
                print(f"HTTP Error Response: {error_text}")
                return f"HTTP Error {response.status_code}: {error_text}"
                
        except requests.exceptions.Timeout:
            return "HARPA API request timed out. The service might be busy or your node might be offline."
        except requests.exceptions.ConnectionError:
            return "Cannot connect to HARPA API. Check your internet connection and API endpoint."
        except Exception as e:
            return f"Integration Error: {str(e)}"
    
    def scrape_page(self, url: str, selector: str = None) -> str:
        """
        Use HARPA's scrape action to extract data from a webpage
        """
        try:
            payload = {
                "action": "scrape",
                "url": url,
                "timeout": 30000
            }
            
            # Add specific selector if provided
            if selector:
                payload["grab"] = [{
                    "selector": selector,
                    "selectorType": "css",
                    "at": "all",
                    "take": "innerText",
                    "label": "scraped_data"
                }]
            
            response = requests.post(
                self.api_url,
                json=payload,
                headers=self.headers,
                timeout=30
            )
            
            if response.status_code == 200:
                return str(response.json())
            else:
                return f"Scrape Error {response.status_code}: {response.text}"
                
        except Exception as e:
            return f"Scrape Error: {str(e)}"
    
    def search_web(self, query: str) -> str:
        """
        Use HARPA's serp action to search the web
        """
        try:
            payload = {
                "action": "serp",
                "query": query,
                "timeout": 30000
            }
            
            response = requests.post(
                self.api_url,
                json=payload,
                headers=self.headers,
                timeout=30
            )
            
            if response.status_code == 200:
                return str(response.json())
            else:
                return f"Search Error {response.status_code}: {response.text}"
                
        except Exception as e:
            return f"Search Error: {str(e)}"

# Backward compatibility function with improved error handling
def execute_harpa(command: str) -> str:
    """
    Main function with fallback strategies
    """
    harpa = HARPAIntegration()
    
    # Try the command action first
    result = harpa.execute_harpa_command(command)
    
    # If command fails, try alternative approaches
    if "Error" in result or "timeout" in result.lower():
        print("🔄 Command failed, trying alternative approaches...")
        
        # Try web search if command mentions searching
        if any(word in command.lower() for word in ['search', 'find', 'look', 'price']):
            search_query = command.replace('Go to', '').replace('go to', '').strip()
            search_result = harpa.search_web(search_query)
            if not "Error" in search_result:
                return f"Search result: {search_result}"
        
        # Try direct scraping if URL is mentioned
        if 'binance' in command.lower():
            scrape_result = harpa.scrape_page("https://www.binance.com")
            if not "Error" in scrape_result:
                return f"Scraped content: {scrape_result}"
    
    return result