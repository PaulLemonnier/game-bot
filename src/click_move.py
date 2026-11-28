import pyautogui
import keyboard

from src.system import STOP_EVENT, launch_loop, interruptible_sleep

BASE_IMAGE_PATH = "src/data/screenshots/"

def base():
    position = pyautogui.locateOnScreen(BASE_IMAGE_PATH + "icone_bois.png", 
                                        confidence=0.8,
                                        # grayscale=True,
                                        # # region=(10,10,10,10),
                                        )
    if position:
        pyautogui.click(pyautogui.center(position))
        interruptible_sleep(3)
    interruptible_sleep(1)

    
def peche():
    region_bouton = (838, 873, 1080, 918)

    interruptible_sleep(0.5)

    try:
        pos_pecher = pyautogui.locateOnScreen(
            BASE_IMAGE_PATH + "bouton_pecher.png",
            confidence=0.8,
            grayscale=True,
            region=region_bouton,
        )
    except pyautogui.ImageNotFoundException:
        pos_pecher = None

    if pos_pecher:
        keyboard.press_and_release("e")
        print("Pecher")
        try:
            pos_ferrer = pyautogui.locateOnScreen(
                BASE_IMAGE_PATH + "bouton_ferrer.png",
                confidence=0.5,
                grayscale=True,
                region=region_bouton,
            )
        except pyautogui.ImageNotFoundException:
            pos_ferrer = None
        while not pos_ferrer:
            continue

        keyboard.press_and_release("e")
        print("Ferrer")
        interruptible_sleep(1)


@launch_loop
def main():

    peche()


main()

# python -m src.click_move
# python -m mouseinfo

