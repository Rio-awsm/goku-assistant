@echo off
REM Goku Assistant Auto-Start Script
REM This script adds Goku to Windows startup

echo ====================================
echo Goku Assistant Startup Setup
echo ====================================
echo.

REM Get the current directory
set SCRIPT_DIR=%~dp0

REM Create a VBS script to run Python without console window
echo Set WshShell = CreateObject("WScript.Shell") > "%SCRIPT_DIR%run_goku_silent.vbs"
echo WshShell.Run chr(34) ^& "python" ^& chr(34) ^& " " ^& chr(34) ^& "%SCRIPT_DIR%src\main.py" ^& chr(34), 0 >> "%SCRIPT_DIR%run_goku_silent.vbs"
echo Set WshShell = Nothing >> "%SCRIPT_DIR%run_goku_silent.vbs"

REM Create shortcut in Startup folder
set STARTUP_FOLDER=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup

echo Creating startup shortcut...
powershell -Command "$WS = New-Object -ComObject WScript.Shell; $SC = $WS.CreateShortcut('%STARTUP_FOLDER%\Goku.lnk'); $SC.TargetPath = 'wscript.exe'; $SC.Arguments = '\"%SCRIPT_DIR%run_goku_silent.vbs\"'; $SC.WorkingDirectory = '%SCRIPT_DIR%'; $SC.WindowStyle = 7; $SC.Description = 'Goku Voice Assistant'; $SC.Save()"

echo.
echo ====================================
echo Setup Complete!
echo ====================================
echo Goku will now start automatically when you login.
echo.
echo To test, run: python src\main.py
echo To remove from startup, delete: %STARTUP_FOLDER%\Goku.lnk
echo.
pause