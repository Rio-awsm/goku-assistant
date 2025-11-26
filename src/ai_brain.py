"""
AI Brain Module
Uses Google Gemini AI to understand commands and generate execution plans
"""

import google.generativeai as genai
import json

class AIBrain:
    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-2.5-flash')
        
        # System prompt to guide AI behavior
        self.system_context = """You are Goku, a Windows voice assistant. Your job is to understand user commands and generate structured execution plans.

Analyze the user's command and respond with ONLY a JSON object in this format:
{
    "intent": "brief description of what user wants",
    "action": "PRIMARY_ACTION_TYPE",
    "parameters": {
        "key": "value"
    },
    "response": "Natural language response to speak to user"
}

Available PRIMARY_ACTION_TYPES:
- OPEN_BROWSER: Open default browser
- SEARCH_WEB: Search Google
- OPEN_APP: Launch an application
- OPEN_WEBSITE: Open specific URL
- PLAY_YOUTUBE: Play video on YouTube
- PLAY_MUSIC: Play music on YouTube Music
- SYSTEM_STATS: Show CPU/GPU/RAM/Storage stats
- CREATE_FOLDER: Create a directory
- CREATE_FILE: Create a file
- OPEN_FILE: Open a file in default app
- TAKE_NOTE: Save a note
- CONVERSATION: Just chatting/asking questions
- UNKNOWN: Cannot determine action

Parameter examples:
- For SEARCH_WEB: {"query": "search term"}
- For OPEN_APP: {"app_name": "chrome"/"notepad"/"calculator"}
- For OPEN_WEBSITE: {"url": "https://example.com"}
- For PLAY_YOUTUBE: {"query": "video search term"}
- For PLAY_MUSIC: {"query": "song name"}
- For CREATE_FOLDER: {"path": "folder_name"}
- For CREATE_FILE: {"path": "file_name.txt", "content": "optional content"}
- For TAKE_NOTE: {"note": "note text"}

Respond ONLY with valid JSON, no other text."""

    def process_command(self, command):
        """
        Process user command using Gemini AI
        
        Args:
            command: User's voice command
            
        Returns:
            dict: Structured command with intent, action, parameters, response
        """
        try:
            # Create prompt
            prompt = f"{self.system_context}\n\nUser command: {command}\n\nRespond with JSON:"
            
            # Get AI response
            response = self.model.generate_content(prompt)
            response_text = response.text.strip()
            
            # Clean response (remove markdown code blocks if present)
            if response_text.startswith("```"):
                response_text = response_text.split("```")[1]
                if response_text.startswith("json"):
                    response_text = response_text[4:]
                response_text = response_text.strip()
            
            # Parse JSON
            command_data = json.loads(response_text)
            
            return command_data
            
        except json.JSONDecodeError as e:
            print(f"JSON parsing error: {e}")
            return {
                "intent": "unknown",
                "action": "UNKNOWN",
                "parameters": {},
                "response": "I didn't quite understand that. Could you rephrase?"
            }
        except Exception as e:
            print(f"AI processing error: {e}")
            return {
                "intent": "error",
                "action": "UNKNOWN",
                "parameters": {},
                "response": "I encountered an error processing your request."
            }
    
    def chat(self, message):
        """
        Simple chat without command structure
        
        Args:
            message: User's message
            
        Returns:
            str: AI response
        """
        try:
            response = self.model.generate_content(f"You are Goku, a helpful Windows voice assistant. Respond naturally and briefly to: {message}")
            return response.text
        except Exception as e:
            return f"Error: {e}"