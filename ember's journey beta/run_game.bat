@echo off
echo ========================================
echo   Ember's Journey - Setup and Launch
echo ========================================
echo.

echo Checking for Python...
python --version
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH!
    pause
    exit /b 1
)

echo.
echo Installing dependencies...
python -m pip install -r requirements.txt

echo.
echo ========================================
echo   Launching Ember's Journey...
echo ========================================
echo.

python main.py

pause
