# Goku Voice Assistant - Complete Setup Guide

## 📁 Project Structure

```
goku-assistant/
│
├── src/
│   ├── __init__.py
│   ├── main.py                 
│   ├── voice_input.py          
│   ├── voice_output.py        
│   ├── ai_brain.py             
│   ├── command_executor.py     
│   └── system_info.py         
│
├── config/
│   ├── __init__.py
│   └── settings.py             
│
├── logs/
│   └── goku.log               
│
├── data/
│   └── notes.txt               
│
├── requirements.txt            
├── setup.py                   
├── startup.bat                 
└── README.md                   
```

## 🚀 Step 1: Install Required Dependencies

Create `requirements.txt`:
```
google-generativeai
speechrecognition
pyttsx3
pyaudio
psutil
pyautogui
keyboard
python-dotenv
colorama
```

## 🔑 Step 2: Setup Configuration

Create a `.env` file in the root directory:
```
GEMINI_API_KEY=your_gemini_api_key_here
WAKE_WORD=hey goku
```

## 💻 Step 3: Core Implementation

The assistant will:
- Listen for wake word "hey goku"
- Process voice commands using speech recognition
- Use Gemini AI to understand intent and generate execution commands
- Execute system tasks dynamically
- Respond with natural voice

## 🎯 Key Features Implemented:
1. ✅ Voice input/output
2. ✅ Dynamic command understanding (no if-else)
3. ✅ Browser control (open, search)
4. ✅ YouTube playback
5. ✅ Music streaming
6. ✅ Google search
7. ✅ App launcher
8. ✅ System stats (CPU, GPU, RAM, Storage)
9. ✅ File/folder operations
10. ✅ Note taking
11. ✅ Auto-start on boot

## 📝 Installation Steps:

1. Clone/create the project directory
2. Install Python 3.8+ if not installed
3. Install dependencies: `pip install -r requirements.txt`
4. Add your Gemini API key to `.env` file
5. Run: `python src/main.py`
6. For auto-start: Run `startup.bat` once

## 🎤 Voice Commands Examples:
- "Hey Goku, are you up?"
- "Open Chrome"
- "Search Python tutorials on YouTube"
- "Play music on YouTube Music"
- "What's my CPU usage?"
- "Create a folder called Projects"
- "Take a note: Meeting at 3 PM"
- "Open Google and search for AI news"

## 🔧 Next Steps:
I'll now create all the individual files with complete code implementation!