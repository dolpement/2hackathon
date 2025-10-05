@echo off
call .venv\Scripts\activate.bat
uvicorn backend.main:app --reload
deactivate
pause