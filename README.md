# Key-Logger

This is a basic keylogger written in Python, created for educational and ethical hacking practice purposes only (:wink).

> ⚠️ Disclaimer: This project is intended for **educational use only**. Do not use it to monitor or log information from others without their knowledge and consent.

## Features
- Logs all keystrokes in the background.
- Can be compiled into an executable using PyInstaller.

## Requirements
- Python 3.x
- `pynput` module

Install dependencies:
```bash
pip install pynput

USAGE:
  python keylogger.py

To create Executable file:
  1) Open Command Prompt
  2) Use the given code
        pyinstaller --onefile keylogger.spec

