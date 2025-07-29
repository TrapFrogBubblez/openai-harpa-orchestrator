import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # OpenAI Configuration
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "sk-placeholder")
    MAX_TOKENS = 500  # Reduced from default 4096 to prevent quota overuse
    REQUEST_TIMEOUT = 30  # Increased from default 10 seconds
    AI_MODEL = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")
    
    # HARPA Configuration
    HARPA_EXTENSION_PATH = "/path/to/harpa-extension"
    HARPA_EXTENSION_ID = "omifkgejbbnmoljehblpnmhclmhplmha"  # Fixed public ID
    
    # Application Settings
    PERSISTENT_DIR = "persistent_data"
    MAX_REQUESTS_PER_MINUTE = 3  # Prevent rate limiting
    RETRY_ATTEMPTS = 2  # Auto-retry on failures
