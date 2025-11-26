# 🐉 Goku Voice Assistant

A powerful AI-powered voice assistant for Windows that responds to voice commands and automates tasks using Google Gemini AI.

## ✨ Features

- **Voice Activation**: Wake word detection ("Hey Goku")
- **Natural Language Understanding**: Powered by Google Gemini AI
- **Voice Input/Output**: Speak to Goku and hear responses
- **Dynamic Command Execution**: No hardcoded if-else chains
- **Web Browsing**: Open browsers, search Google, navigate to websites
- **Media Playback**: Play YouTube videos and music
- **App Launcher**: Open any Windows application
- **System Monitoring**: Check CPU, RAM, GPU, and storage stats
- **File Management**: Create folders, files, and take notes
- **Auto-Start**: Runs automatically on Windows startup

## 📋 Prerequisites

- Windows 10/11
- Python 3.8 or higher
- Microphone
- Internet connection
- Google Gemini API key ([Get one here](https://makersuite.google.com/app/apikey))

## 🚀 Installation

### 1. Clone or Download the Project

```bash
git clone https://github.com/yourusername/goku-assistant.git
cd goku-assistant
```

### 2. Create Virtual Environment (Recommended)

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

**Note**: If `pyaudio` installation fails, download the appropriate wheel file from [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) and install it:

```bash
pip install PyAudio‑0.2.13‑cp311‑cp311‑win_amd64.whl
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key_here
WAKE_WORD=hey goku
VOICE_RATE=180
VOICE_VOLUME=0.9
```

### 5. Create Required Directories

The following directories will be created automatically:
- `logs/` - Application logs
- `data/` - Notes and data storage

## 🎮 Usage

### Running Goku

```bash
python src/main.py
```

### Voice Commands Examples

**General Conversation:**
- "Hey Goku, are you up?"
- "Hey Goku, how are you?"

**Web Browsing:**
- "Hey Goku, open my browser"
- "Hey Goku, search for Python tutorials"
- "Hey Goku, open YouTube"
- "Hey Goku, go to GitHub.com"

**Media:**
- "Hey Goku, play Linkin Park on YouTube"
- "Hey Goku, search for cooking recipes on YouTube"
- "Hey Goku, play some jazz music"

**Applications:**
- "Hey Goku, open Notepad"
- "Hey Goku, launch Calculator"
- "Hey Goku, open Visual Studio Code"

**System Information:**
- "Hey Goku, what's my CPU usage?"
- "Hey Goku, show me system stats"
- "Hey Goku, how much storage do I have?"

**File Management:**
- "Hey Goku, create a folder called Projects"
- "Hey Goku, make a file named test.txt"
- "Hey Goku, take a note: Buy groceries tomorrow"

## 🔧 Auto-Start Setup

To make Goku start automatically when Windows boots:

1. Run the startup script:
   ```bash
   startup.bat
   ```

2. Or manually add to startup:
   - Press `Win + R`
   - Type `shell:startup`
   - Create a shortcut to `src/main.py`

## 📁 Project Structure

```
goku-assistant/
├── src/
│   ├── main.py              # Entry point
│   ├── voice_input.py       # Speech recognition
│   ├── voice_output.py      # Text-to-speech
│   ├── ai_brain.py          # Gemini AI integration
│   ├── command_executor.py  # Command execution
│   └── system_info.py       # System stats
├── config/
│   └── settings.py          # Configuration
├── logs/                    # Application logs
├── data/                    # Notes and data
├── requirements.txt         # Dependencies
├── startup.bat             # Auto-start script
├── .env                    # Environment variables
└── README.md              # This file
```

## 🎯 Supported Commands

### Action Types
- `OPEN_BROWSER` - Open default web browser
- `SEARCH_WEB` - Search on Google
- `OPEN_APP` - Launch Windows applications
- `OPEN_WEBSITE` - Navigate to specific URLs
- `PLAY_YOUTUBE` - Play videos on YouTube
- `PLAY_MUSIC` - Play music on YouTube Music
- `SYSTEM_STATS` - Display system information
- `CREATE_FOLDER` - Create directories
- `CREATE_FILE` - Create files
- `OPEN_FILE` - Open files in default apps
- `TAKE_NOTE` - Save notes
- `CONVERSATION` - General chat

## 🛠️ Customization

### Change Wake Word

Edit `.env` file:
```env
WAKE_WORD=hey jarvis
```

### Adjust Voice Settings

Edit `.env` file:
```env
VOICE_RATE=200      # Speech speed (words per minute)
VOICE_VOLUME=1.0    # Volume (0.0 to 1.0)
```

### Add Custom Applications

Edit `command_executor.py` and add to `app_paths` dictionary:
```python
self.app_paths = {
    "notepad": "notepad.exe",
    "your_app": "path/to/your/app.exe",
}
```

## 🔍 Troubleshooting

### Microphone Not Working
1. Check Windows microphone permissions
2. Verify microphone is set as default input device
3. Test with Windows Voice Recorder

### API Key Issues
1. Verify API key in `.env` file
2. Check API quota at Google AI Studio
3. Ensure internet connection is active

### PyAudio Installation Fails
Download the appropriate wheel file for your Python version from:
https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio

### Voice Recognition Not Working
1. Speak clearly and at normal pace
2. Reduce background noise
3. Check microphone input level in Windows settings

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License.

## 🙏 Acknowledgments

- Google Gemini AI for natural language understanding
- SpeechRecognition library for voice input
- pyttsx3 for text-to-speech
- All other open-source libraries used

## 📧 Support

For issues, questions, or suggestions, please open an issue on GitHub.

---

**Made with ❤️ by [Your Name]**

🐉 *"With great power comes great responsibility"* - Use Goku wisely!