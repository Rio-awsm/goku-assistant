"""
Configuration Settings
Loads environment variables and application settings
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load .env file from project root
env_path = Path(__file__).parent.parent / '.env'
load_dotenv(env_path)

class Settings:
    def __init__(self):
        # API Keys
        self.GEMINI_API_KEY = os.getenv('GEMINI_API_KEY', '')
        
        # Wake word configuration
        self.WAKE_WORD = os.getenv('WAKE_WORD', 'hey goku')
        
        # Voice settings
        self.VOICE_RATE = int(os.getenv('VOICE_RATE', '180'))
        self.VOICE_VOLUME = float(os.getenv('VOICE_VOLUME', '0.9'))
        
        # Paths
        self.PROJECT_ROOT = Path(__file__).parent.parent
        self.LOGS_DIR = self.PROJECT_ROOT / 'logs'
        self.DATA_DIR = self.PROJECT_ROOT / 'data'
        
        # Create directories if they don't exist
        self.LOGS_DIR.mkdir(exist_ok=True)
        self.DATA_DIR.mkdir(exist_ok=True)
        
        # Validate API key
        if not self.GEMINI_API_KEY:
            raise ValueError(
                "GEMINI_API_KEY not found in .env file. "
                "Please create a .env file with your API key."
            )