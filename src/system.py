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
        remaining_time = end_time - perf_counter()
        sleep(min(remaining_time, 0.005))

def interruptible_wait_until(target_time: float) -> bool:
    """
    Sleep for a specified duration, but can be interrupted by pressing the 'ctrl' key.

    Args:
        target_time (float): The time to wait until.
    """
    while not STOP_EVENT.is_set():
        remaining_time = target_time - perf_counter()
        if remaining_time <= 0:
            return True
        # INFO: Sleep for a short duration to avoid busy waiting
        if remaining_time > 0.01:
            sleep(remaining_time - 0.005)
        # INFO: close approach
        elif remaining_time > 0.001:
            sleep(0.0005)
        # INFO: final moments
        else:
            pass
    return False