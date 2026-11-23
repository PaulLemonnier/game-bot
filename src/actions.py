from uuid import uuid4
from time import sleep, perf_counter
from helpers import save_json
import pyautogui
import keyboard

from src.system import interruptible_sleep


def collect() -> None:
    keyboard.press_and_release('e')
    interruptible_sleep(4)

def fight() -> None:
    keyboard.press_and_release('1')
    interruptible_sleep(1)
    keyboard.press_and_release('3')
    interruptible_sleep(1)
    keyboard.press_and_release('2')
    interruptible_sleep(1)