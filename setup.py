"""
Goku Assistant Setup Script
Quick setup and verification
"""

import os
import sys
from pathlib import Path

def create_directories():
    """Create necessary directories"""
    dirs = ['src', 'config', 'logs', 'data']
    for dir_name in dirs:
        Path(dir_name).mkdir(exist_ok=True)
    print("✓ Directories created")

def create_init_files():
    """Create __init__.py files"""
    init_files = ['src/__init__.py', 'config/__init__.py']
    for file_path in init_files:
        Path(file_path).touch(exist_ok=True)
    print("✓ Init files created")

def check_env_file():
    """Check if .env file exists"""
    if not Path('.env').exists():
        print("\n❌ .env file not found!")
        print("\nCreating template .env file...")
        
        env_content = """# Goku Assistant Configuration
GEMINI_API_KEY=your_gemini_api_key_here
WAKE_WORD=hey goku
VOICE_RATE=180
VOICE_VOLUME=0.9
"""
        Path('.env').write_text(env_content)
        print("✓ Template .env file created")
        print("\n⚠️  IMPORTANT: Edit .env file and add your Gemini API key!")
        print("Get your API key from: https://makersuite.google.com/app/apikey")
        return False
    else:
        print("✓ .env file found")
        return True

def check_dependencies():
    """Check if required packages are installed"""
    required = [
        'google.generativeai',
        'speech_recognition',
        'pyttsx3',
        'psutil',
        'dotenv',
        'colorama'
    ]
    
    missing = []
    for package in required:
        try:
            __import__(package.replace('-', '_').replace('.', '_'))
        except ImportError:
            missing.append(package)
    
    if missing:
        print(f"\n❌ Missing packages: {', '.join(missing)}")
        print("\nInstall them using:")
        print("pip install -r requirements.txt")
        return False
    else:
        print("✓ All dependencies installed")
        return True

def main():
    print("=" * 50)
    print("🐉 GOKU ASSISTANT SETUP")
    print("=" * 50)
    print()
    
    # Create structure
    create_directories()
    create_init_files()
    
    # Check configuration
    env_ok = check_env_file()
    deps_ok = check_dependencies()
    
    print("\n" + "=" * 50)
    if env_ok and deps_ok:
        print("✅ Setup Complete! You're ready to use Goku!")
        print("\nTo start Goku, run:")
        print("  python src/main.py")
        print("\nFor auto-start on boot, run:")
        print("  startup.bat")
    else:
        print("⚠️  Setup Incomplete")
        print("\nPlease fix the issues above and run setup.py again")
    print("=" * 50)

if __name__ == "__main__":
    main()