"""
Goku Voice Assistant - Main Entry Point
Listens for Shift+Space hotkey and processes commands
"""

import os
import sys
from pathlib import Path
from colorama import init, Fore, Style
import keyboard
import time

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR))

from voice_input import VoiceInput
from voice_output import VoiceOutput
from ai_brain import AIBrain
from command_executor import CommandExecutor
from config.settings import Settings

# Initialize colorama for colored terminal output
init(autoreset=True)

class Goku:
    def __init__(self):
        print(f"{Fore.CYAN}{'='*50}")
        print(f"{Fore.YELLOW}🐉 Initializing GOKU Assistant...{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'='*50}\n")
        
        # Load settings
        self.settings = Settings()
        
        # Initialize components
        self.voice_input = VoiceInput()
        self.voice_output = VoiceOutput()
        self.ai_brain = AIBrain(self.settings.GEMINI_API_KEY)
        self.executor = CommandExecutor(self.voice_output)
        
        # Hotkey tracking
        self.last_press_time = 0
        self.double_press_window = 0.5  # 500ms window for double press
        self.is_listening = False
        
        print(f"{Fore.GREEN}✓ Voice Input Ready")
        print(f"{Fore.GREEN}✓ Voice Output Ready")
        print(f"{Fore.GREEN}✓ AI Brain Connected")
        print(f"{Fore.GREEN}✓ Command Executor Ready\n")
        
    def on_hotkey(self):
        """Handle Shift+Space double press"""
        current_time = time.time()
        
        # Check if this is a double press
        if current_time - self.last_press_time <= self.double_press_window:
            # Double press detected!
            if not self.is_listening:
                self.activate_listening()
        
        self.last_press_time = current_time
    
    def activate_listening(self):
        """Activate listening mode"""
        if self.is_listening:
            return
            
        self.is_listening = True
        print(f"\n{Fore.GREEN}🐉 GOKU ACTIVATED!{Style.RESET_ALL}")
        self.voice_output.speak("I'm listening")
        
        # Listen for command
        print(f"{Fore.YELLOW}[Listening for command...]{Style.RESET_ALL}")
        command = self.voice_input.listen(timeout=10, phrase_time_limit=15)
        
        if command:
            print(f"{Fore.CYAN}You: {command}{Style.RESET_ALL}")
            self.process_command(command)
        else:
            print(f"{Fore.RED}No command detected{Style.RESET_ALL}")
            self.voice_output.speak("I didn't hear anything")
        
        self.is_listening = False
        print(f"\n{Fore.CYAN}[Ready - Press Shift+Space twice to activate]{Style.RESET_ALL}\n")
    
    def start(self):
        """Main loop - listen for hotkey"""
        print(f"{Fore.MAGENTA}{'='*50}")
        print(f"{Fore.YELLOW}🎤 Goku is now running...")
        print(f"{Fore.CYAN}Press Shift+Space TWICE to activate!")
        print(f"{Fore.MAGENTA}{'='*50}\n")
        
        self.voice_output.speak("Goku assistant initialized. Press shift space twice to activate me")
        
        # Register hotkey
        keyboard.add_hotkey('shift+space', self.on_hotkey, suppress=True)
        
        try:
            # Keep running
            print(f"{Fore.GREEN}✓ Goku is active and waiting for your command{Style.RESET_ALL}")
            print(f"{Fore.CYAN}Press Ctrl+C to exit\n{Style.RESET_ALL}")
            keyboard.wait()  # Wait forever
            
        except KeyboardInterrupt:
            print(f"\n\n{Fore.RED}Shutting down Goku...{Style.RESET_ALL}")
            self.voice_output.speak("Goodbye! Powering down.")
            keyboard.unhook_all()
    
    def process_command(self, command):
        """Process user command through AI brain"""
        try:
            # Get AI interpretation and execution plan
            print(f"{Fore.MAGENTA}[Processing with AI...]{Style.RESET_ALL}")
            self.voice_output.speak("Processing")
            
            response = self.ai_brain.process_command(command)
            
            # Execute the command
            result = self.executor.execute(response)
            
            # Always speak the response
            if result['success']:
                print(f"{Fore.GREEN}Goku: {result['message']}{Style.RESET_ALL}")
                self.voice_output.speak(result['message'])
            else:
                print(f"{Fore.RED}Goku: {result['message']}{Style.RESET_ALL}")
                self.voice_output.speak(f"Sorry, I encountered an issue: {result['message']}")
                
        except Exception as e:
            error_msg = f"I couldn't process that command: {str(e)}"
            print(f"{Fore.RED}Error: {error_msg}{Style.RESET_ALL}")
            self.voice_output.speak(error_msg)

def main():
    """Entry point"""
    try:
        goku = Goku()
        goku.start()
    except Exception as e:
        print(f"{Fore.RED}Failed to start Goku: {e}{Style.RESET_ALL}")
        sys.exit(1)

if __name__ == "__main__":
    main()