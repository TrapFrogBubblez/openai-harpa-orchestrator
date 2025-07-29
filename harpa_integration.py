from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError
from config import Config
import time
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def execute_harpa(command: str) -> str:
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch_persistent_context(
                user_data_dir="/tmp/harpa-profile",
                args=[
                    f"--disable-extensions-except={Config.HARPA_EXTENSION_PATH}",
                    f"--load-extension={Config.HARPA_EXTENSION_PATH}",
                    "--headless=new"  # You can remove this for visual debugging
                ]
            )

            page = browser.new_page()
            logger.info("Opening HARPA extension popup...")
            page.goto(f"chrome-extension://{Config.HARPA_EXTENSION_ID}/popup.html")

            logger.info(f"Filling command: {command}")
            page.fill("textarea#harpa-command", command)
            page.click("button#execute-command")

            logger.info("Waiting for HARPA to respond...")
            time.sleep(3)  # Ensure command has time to begin processing

            result = page.locator("div#harpa-output").inner_text(timeout=60000)

            logger.info("Execution complete, closing browser...")
            browser.close()

            return result.strip()
    except PlaywrightTimeoutError:
        logger.error("Timeout while waiting for HARPA output.")
        return "HARPA execution timed out."
    except Exception as e:
        logger.exception(f"Unexpected error during HARPA execution: {e}")
        return f"Error: {str(e)}"
