import keyboard
import numpy as np
from time import perf_counter
from src.system import interruptible_wait_until
from src.ocr import take_screen_zone, predict_text
from src.helpers import search_word_in_list

def collect() -> None:
    keyboard.press_and_release('e')
    interruptible_wait_until(4)

def fight() -> None:
    keyboard.press_and_release('1')
    interruptible_wait_until(1)
    keyboard.press_and_release('3')
    interruptible_wait_until(1)
    keyboard.press_and_release('2')
    interruptible_wait_until(1)

def peche_ocr():
    """Peche with OCR method"""

    interruptible_wait_until(1)
    img = take_screen_zone()
    texts: list[str] = predict_text(img)

    # INFO: Possibility to fish
    if search_word_in_list(search_word="pecher", words_list=texts):
        keyboard.press_and_release('e')

        # INFO: 5 secondes to check 'ferrage'
        wait_time_ferrage = 5
        previous_frame = img
        end_time = perf_counter() + wait_time_ferrage
        while perf_counter() < end_time:
            img = take_screen_zone()

            # INFO: if the screenshot is same wait and take new screenshot
            if previous_frame is not None and np.array_equal(img, previous_frame):
                interruptible_wait_until(0.2)
                continue
            previous_frame = img
            texts: list[str] = predict_text(img)
            if search_word_in_list(search_word="fer", words_list=texts):
                keyboard.press_and_release('e')
                # break
                return True
            interruptible_wait_until(0.2)

    else: 
        # INFO: No fish found
        # interruptible_wait_until(10)
        return False

