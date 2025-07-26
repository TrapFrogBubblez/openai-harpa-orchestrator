import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Use placeholder if no .env found
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "sk-placeholder1234567890")
    
    # Keep your HARPA config below
    HARPA_EXTENSION_PATH = "/path/to/harpa-extension"
    HARPA_EXTENSION_ID = "omifkgejbbnmoljehblpnmhclmhplmha"
    PERSISTENT_DIR = "persistent_data"
