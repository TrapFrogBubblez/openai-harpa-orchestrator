from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError
from config import Config
import time
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class HarpaUnavailableException(Exception):
    """Raised when HARPA is unavailable or execution fails."""
    pass


class HarpaExtension:
    def __init__(self):
        self.browser = None
        self.page = None

    def _setup_browser(self):
        logger.info("Launching Chromium with HARPA extension...")
        playwright = sync_playwright().start()
        self.browser = playwright.chromium.launch_persistent_context(
            user_data_dir="/tmp/harpa-profile",
            args=[
                f"--disable-extensions-except={Config.HARPA_EXTENSION_PATH}",
                f"--load-extension={Config.HARPA_EXTENSION_PATH}",
                "--headless=new"
            ]
        )
        self.page = self.browser.new_page()
        logger.info("Opening HARPA popup...")
        self.page.goto(f"chrome-extension://{Config.HARPA_EXTENSION_ID}/popup.html")

    def execute_command(self, command: str) -> str:
        try:
            self._setup_browser()

            logger.info(f"Sending command to HARPA: {command}")
            self.page.fill("textarea#harpa-command", command)
            self.page.click("button#execute-command")

            logger.info("Waiting for HARPA to respond...")
            time.sleep(3)  # Initial wait to let processing start

            result = self.page.locator("div#harpa-output").inner_text(timeout=60000)
            logger.info("Command executed successfully.")

            return result.strip()
        except PlaywrightTimeoutError:
            logger.error("Timeout while waiting for HARPA output.")
            raise HarpaUnavailableException("HARPA execution timed out.")
        except Exception as e:
            logger.exception(f"Unexpected error during HARPA execution: {e}")
            raise HarpaUnavailableException(f"HARPA error: {str(e)}")
        finally:
            if self.browser:
                logger.info("Closing browser...")
                self.browser.close()
