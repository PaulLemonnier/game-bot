import threading
import keyboard
from time import perf_counter, sleep

STOP_EVENT = threading.Event()

def launch_loop(func):

    def ctrl_listener():
        keyboard.wait('ctrl')
        print("STOP PROCESS")
        STOP_EVENT.set()

    def wrapper(*args, **kwargs):
        linstener = threading.Thread(target=ctrl_listener, daemon=True)
        linstener.start()

        print("Wait for start with ALT GR")
        keyboard.wait('alt gr')
        print("START PROCESS")
        sleep(0.5)

        while not STOP_EVENT.is_set():
            func(*args, **kwargs)

    return wrapper

def interruptible_sleep(seconds: float):
    """
    Sleep for a specified duration, but can be interrupted by pressing the 'ctrl' key.

    Args:
        duration (float): The duration to sleep in seconds.
    """
    end_time = perf_counter() + seconds
    while perf_counter() < end_time:
        if STOP_EVENT.is_set():
            return
        sleep(0.1)