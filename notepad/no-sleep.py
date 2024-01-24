import pyautogui
import time
from random import randrange
import ctypes

def prevent_screen_lock():
    ctypes.windll.kernel32.SetThreadExecutionState(0x80000002)

interval_seconds = 150

try:
    while True:
        prevent_screen_lock()
        time.sleep(interval_seconds)
except KeyboardInterrupt:
    print("Script terminated by user.")
finally:
    ctypes.windll.kernel32.SetThreadExecutionState(0x00000000)