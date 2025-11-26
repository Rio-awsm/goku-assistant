"""
Voice Input Module
Handles speech-to-text conversion using Google Speech Recognition
"""

import speech_recognition as sr

class VoiceInput:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        
        # Adjust for ambient noise
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
    
    def listen(self, timeout=5, phrase_time_limit=10):
        """
        Listen for voice input and convert to text
        
        Args:
            timeout: Seconds to wait for speech to start
            phrase_time_limit: Maximum seconds for phrase
            
        Returns:
            str: Recognized text or None
        """
        try:
            with self.microphone as source:
                # Listen for audio
                audio = self.recognizer.listen(
                    source, 
                    timeout=timeout,
                    phrase_time_limit=phrase_time_limit
                )
                
            # Convert speech to text using Google
            text = self.recognizer.recognize_google(audio)
            return text
            
        except sr.WaitTimeoutError:
            return None
        except sr.UnknownValueError:
            return None
        except sr.RequestError as e:
            print(f"Speech recognition service error: {e}")
            return None
        except Exception as e:
            print(f"Error in voice input: {e}")
            return None
    
    def listen_continuous(self, callback, stop_event=None):
        """
        Continuously listen and pass recognized text to callback
        
        Args:
            callback: Function to call with recognized text
            stop_event: Threading event to stop listening
        """
        with self.microphone as source:
            while True:
                if stop_event and stop_event.is_set():
                    break
                    
                try:
                    audio = self.recognizer.listen(source, timeout=3)
                    text = self.recognizer.recognize_google(audio)
                    callback(text)
                except:
                    continue