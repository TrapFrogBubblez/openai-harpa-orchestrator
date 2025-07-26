from playwright.sync_api import sync_playwright
from config import Config
import time

def execute_harpa(command: str) -> str:
    with sync_playwright() as p:
        browser = p.chromium.launch_persistent_context(
            user_data_dir="/tmp/harpa-profile",
            args=[
                f"--disable-extensions-except={Config.HARPA_EXTENSION_PATH}",
                f"--load-extension={Config.HARPA_EXTENSION_PATH}",
                "--headless=new"  # Remove for visible browser
            ]
        )
        
        page = browser.new_page()
        page.goto(f"chrome-extension://{Config.HARPA_EXTENSION_ID}/popup.html")
        
        page.fill("textarea#harpa-command", command)
        page.click("button#execute-command")
        
        # Wait for execution
        time.sleep(3)
        
        # Get output
        result = page.locator("div#harpa-output").inner_text(timeout=60000)
        browser.close()
        return result
