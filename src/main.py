"""
Goku Voice Assistant - Main Entry Point
Listens for wake word and processes commands
"""

import os
import sys
from pathlib import Path
from colorama import init, Fore, Style

# Add src to path
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
        self.executor = CommandExecutor()
        
        self.is_active = False
        
        print(f"{Fore.GREEN}✓ Voice Input Ready")
        print(f"{Fore.GREEN}✓ Voice Output Ready")
        print(f"{Fore.GREEN}✓ AI Brain Connected")
        print(f"{Fore.GREEN}✓ Command Executor Ready\n")
        
    def start(self):
        """Main loop - listen for wake word and process commands"""
        print(f"{Fore.MAGENTA}{'='*50}")
        print(f"{Fore.YELLOW}🎤 Goku is now listening...")
        print(f"{Fore.CYAN}Say '{self.settings.WAKE_WORD}' to activate!")
        print(f"{Fore.MAGENTA}{'='*50}\n")
        
        self.voice_output.speak("Goku assistant initialized and ready to serve")
        
        while True:
            try:
                # Listen for wake word or command
                if not self.is_active:
                    print(f"{Fore.CYAN}[Listening for wake word...]{Style.RESET_ALL}")
                    text = self.voice_input.listen(timeout=5)
                    
                    if text and self.settings.WAKE_WORD.lower() in text.lower():
                        self.is_active = True
                        print(f"\n{Fore.GREEN}🐉 GOKU ACTIVATED!{Style.RESET_ALL}")
                        self.voice_output.speak("Yes, I'm here. How can I help you?")
                        continue
                
                # Process command when active
                if self.is_active:
                    print(f"\n{Fore.YELLOW}[Listening for command...]{Style.RESET_ALL}")
                    command = self.voice_input.listen(timeout=8)
                    
                    if command:
                        print(f"{Fore.CYAN}You: {command}{Style.RESET_ALL}")
                        self.process_command(command)
                    
                    # Deactivate after processing
                    self.is_active = False
                    print(f"\n{Fore.CYAN}[Waiting for wake word...]{Style.RESET_ALL}\n")
                    
            except KeyboardInterrupt:
                print(f"\n\n{Fore.RED}Shutting down Goku...{Style.RESET_ALL}")
                self.voice_output.speak("Goodbye! Powering down.")
                break
            except Exception as e:
                print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")
                self.is_active = False
    
    def process_command(self, command):
        """Process user command through AI brain"""
        try:
            # Get AI interpretation and execution plan
            print(f"{Fore.MAGENTA}[Processing with AI...]{Style.RESET_ALL}")
            response = self.ai_brain.process_command(command)
            
            # Execute the command
            result = self.executor.execute(response)
            
            # Speak the response
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