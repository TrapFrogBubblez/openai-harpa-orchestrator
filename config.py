import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """
    Configuration class for OpenAI, HARPA, and application-wide settings.
    All sensitive or environment-specific values are loaded from environment variables.
    """

    # OpenAI Configuration
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "sk-placeholder")  # Replace with your actual key in .env
    MAX_TOKENS = 500  # Reduced from default 4096 to prevent quota overuse
    REQUEST_TIMEOUT = 30  # Increased from default 10 seconds for slower networks
    AI_MODEL = "gpt-3.5-turbo"  # Cheaper model to conserve tokens

    # HARPA Configuration
    HARPA_EXTENSION_PATH = os.getenv("HARPA_EXTENSION_PATH", "/path/to/harpa-extension")
    HARPA_EXTENSION_ID = os.getenv("HARPA_EXTENSION_ID", "omifkgejbbnmoljehblpnmhclmhplmha")  # Public ID

    # Application Settings
    PERSISTENT_DIR = "persistent_data"
    MAX_REQUESTS_PER_MINUTE = 3  # Rate limit to avoid throttling
    RETRY_ATTEMPTS = 2  # Number of retries on failed requests

    @classmethod
    def validate(cls):
        """
        Validate critical configuration parameters.
        Raises an error or warning if config is incomplete or insecure.
        """
        if cls.OPENAI_API_KEY == "sk-placeholder" or not cls.OPENAI_API_KEY:
            raise ValueError("OpenAI API key is not set. Please update your .env file with a valid key.")
