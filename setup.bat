@echo off

:: Create the virtual environment
virtualenv env --python=python3.9

:: Activate the virtual environment (Windows-specific syntax)
call env\Scripts\activate.bat

:: Install dependencies from requirements.txt
pip install -r requirements.txt
