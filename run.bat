@echo off

:: Activate the virtual environment (Windows-specific syntax)
call env\Scripts\activate.bat

:: Run uvicorn with specified arguments
python -m uvicorn "manage:app" --host "0.0.0.0" --port 8000 --reload
