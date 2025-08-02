import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # OpenAI Configuration
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "sk-placeholder")
    MAX_TOKENS = 500  # Reduced from default 4096 to prevent quota overuse
    REQUEST_TIMEOUT = 30  # Increased from default 10 seconds
    AI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o")  # Updated to use GPT-4o as intended
    
    # HARPA Configuration - FIXED
    HARPA_API_KEY = os.getenv("HARPA_API_KEY", "harpa-placeholder")  # NEW: API key from HARPA's Automate tab
    HARPA_EXTENSION_PATH = "/path/to/harpa-extension"
    HARPA_EXTENSION_ID = "eanggfilgoajaocelnaflolkadkeghjp"  # CORRECTED: Real HARPA extension ID
    HARPA_API_URL = "https://api.harpa.ai/api/v1/grid"  # NEW: Actual API endpoint
    
    # Application Settings
    PERSISTENT_DIR = "persistent_data"
    MAX_REQUESTS_PER_MINUTE = 3  # Prevent rate limiting
    RETRY_ATTEMPTS = 2  # Auto-retry on failures