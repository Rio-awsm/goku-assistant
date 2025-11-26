"""
Voice Output Module
Handles text-to-speech conversion using pyttsx3
"""

import pyttsx3

class VoiceOutput:
    def __init__(self):
        self.engine = pyttsx3.init()
        self._configure_voice()
    
    def _configure_voice(self):
        """Configure voice properties"""
        # Get available voices
        voices = self.engine.getProperty('voices')
        
        # Set voice (try to use a male voice for Goku)
        # voices[0] is usually male, voices[1] is usually female
        if len(voices) > 0:
            self.engine.setProperty('voice', voices[0].id)
        
        # Set speech rate (default is 200)
        self.engine.setProperty('rate', 180)
        
        # Set volume (0.0 to 1.0)
        self.engine.setProperty('volume', 0.9)
    
    def speak(self, text):
        """
        Convert text to speech and play it
        
        Args:
            text: Text to speak
        """
        try:
            self.engine.say(text)
            self.engine.runAndWait()
        except Exception as e:
            print(f"Error in voice output: {e}")
    
    def set_rate(self, rate):
        """Set speech rate (words per minute)"""
        self.engine.setProperty('rate', rate)
    
    def set_volume(self, volume):
        """Set volume (0.0 to 1.0)"""
        self.engine.setProperty('volume', volume)
    
    def set_voice(self, voice_index=0):
        """
        Change voice
        
        Args:
            voice_index: Index of voice to use
        """
        voices = self.engine.getProperty('voices')
        if voice_index < len(voices):
            self.engine.setProperty('voice', voices[voice_index].id)