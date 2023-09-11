@echo off
REM Delete the virtual environment if it exists
if exist venv rmdir /s /q venv

REM Create a virtual environment
python -m venv venv

REM Activate the virtual environment
call venv\Scripts\activate
