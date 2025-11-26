"""
Command Executor Module
Executes system commands based on AI-generated action plans
"""

import os
import subprocess
import webbrowser
from pathlib import Path
from system_info import SystemInfo

class CommandExecutor:
    def __init__(self):
        self.system_info = SystemInfo()
        self.notes_file = Path("data/notes.txt")
        self.notes_file.parent.mkdir(exist_ok=True)
        
        # Common Windows apps
        self.app_paths = {
            "notepad": "notepad.exe",
            "calculator": "calc.exe",
            "paint": "mspaint.exe",
            "explorer": "explorer.exe",
            "chrome": "chrome.exe",
            "edge": "msedge.exe",
            "firefox": "firefox.exe",
            "cmd": "cmd.exe",
            "powershell": "powershell.exe",
            "vscode": "code.exe",
            "spotify": "spotify.exe",
        }
    
    def execute(self, command_data):
        """
        Execute command based on AI-generated plan
        
        Args:
            command_data: Dict with action, parameters, and response
            
        Returns:
            dict: Result with success status and message
        """
        action = command_data.get("action", "UNKNOWN")
        params = command_data.get("parameters", {})
        response = command_data.get("response", "Done")
        
        try:
            # Route to appropriate handler
            handlers = {
                "OPEN_BROWSER": self._open_browser,
                "SEARCH_WEB": self._search_web,
                "OPEN_APP": self._open_app,
                "OPEN_WEBSITE": self._open_website,
                "PLAY_YOUTUBE": self._play_youtube,
                "PLAY_MUSIC": self._play_music,
                "SYSTEM_STATS": self._system_stats,
                "CREATE_FOLDER": self._create_folder,
                "CREATE_FILE": self._create_file,
                "OPEN_FILE": self._open_file,
                "TAKE_NOTE": self._take_note,
                "CONVERSATION": self._conversation,
            }
            
            handler = handlers.get(action, self._unknown)
            result = handler(params)
            
            return {
                "success": result["success"],
                "message": response if result["success"] else result.get("message", "Unknown error")
            }
            
        except Exception as e:
            return {
                "success": False,
                "message": f"Execution error: {str(e)}"
            }
    
    def _open_browser(self, params):
        """Open default web browser"""
        webbrowser.open("about:blank")
        return {"success": True}
    
    def _search_web(self, params):
        """Search Google"""
        query = params.get("query", "")
        search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
        webbrowser.open(search_url)
        return {"success": True}
    
    def _open_app(self, params):
        """Launch application"""
        app_name = params.get("app_name", "").lower()
        
        # Check if it's a known app
        if app_name in self.app_paths:
            try:
                subprocess.Popen(self.app_paths[app_name])
                return {"success": True}
            except:
                pass
        
        # Try to open by name
        try:
            subprocess.Popen(app_name)
            return {"success": True}
        except:
            return {"success": False, "message": f"Could not find application: {app_name}"}
    
    def _open_website(self, params):
        """Open specific URL"""
        url = params.get("url", "")
        if not url.startswith("http"):
            url = "https://" + url
        webbrowser.open(url)
        return {"success": True}
    
    def _play_youtube(self, params):
        """Play video on YouTube"""
        query = params.get("query", "")
        youtube_url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
        webbrowser.open(youtube_url)
        return {"success": True}
    
    def _play_music(self, params):
        """Play music on YouTube Music"""
        query = params.get("query", "")
        music_url = f"https://music.youtube.com/search?q={query.replace(' ', '+')}"
        webbrowser.open(music_url)
        return {"success": True}
    
    def _system_stats(self, params):
        """Get system statistics"""
        stats = self.system_info.get_all_stats()
        
        # Format response
        message = (
            f"System stats: CPU usage is {stats['cpu']}%, "
            f"RAM usage is {stats['memory']}%, "
            f"Available storage is {stats['disk_free']} GB out of {stats['disk_total']} GB"
        )
        
        return {"success": True, "message": message}
    
    def _create_folder(self, params):
        """Create a directory"""
        path = params.get("path", "")
        try:
            Path(path).mkdir(parents=True, exist_ok=True)
            return {"success": True}
        except Exception as e:
            return {"success": False, "message": str(e)}
    
    def _create_file(self, params):
        """Create a file"""
        path = params.get("path", "")
        content = params.get("content", "")
        try:
            Path(path).parent.mkdir(parents=True, exist_ok=True)
            Path(path).write_text(content)
            return {"success": True}
        except Exception as e:
            return {"success": False, "message": str(e)}
    
    def _open_file(self, params):
        """Open file in default application"""
        path = params.get("path", "")
        try:
            os.startfile(path)
            return {"success": True}
        except Exception as e:
            return {"success": False, "message": str(e)}
    
    def _take_note(self, params):
        """Save a note to notes file"""
        note = params.get("note", "")
        try:
            with open(self.notes_file, "a", encoding="utf-8") as f:
                from datetime import datetime
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                f.write(f"[{timestamp}] {note}\n")
            return {"success": True}
        except Exception as e:
            return {"success": False, "message": str(e)}
    
    def _conversation(self, params):
        """Just conversation, no action needed"""
        return {"success": True}
    
    def _unknown(self, params):
        """Unknown action"""
        return {"success": False, "message": "I'm not sure how to do that yet"}