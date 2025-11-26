@echo off
REM Quick run script for Goku Assistant

echo ====================================
echo      STARTING GOKU ASSISTANT
echo ====================================
echo.

REM Check if virtual environment exists
if exist "venv\Scripts\activate.bat" (
    echo Activating virtual environment...
    call venv\Scripts\activate.bat
    echo.
)

REM Run Goku
python src\main.py

REM Keep window open if there's an error
if errorlevel 1 (
    echo.
    echo ====================================
    echo ERROR: Goku failed to start
    echo ====================================
    echo.
    echo Common solutions:
    echo 1. Make sure Python is installed
    echo 2. Run: pip install -r requirements.txt
    echo 3. Create .env file with GEMINI_API_KEY
    echo.
    pause
)