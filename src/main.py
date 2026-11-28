""" Main entry point for the game bot """

import keyboard

from src.system import launch_loop, interruptible_wait_until, interruptible_sleep
from src.listener import get_zqsde_move
from src.execution import execute_move, execute_inverse_move
from src.helpers import load_json
from src.actions import collect, fight, peche_ocr
from src.ocr import take_screen_zone, predict_text


def main_for_bois_cereales():
    """
    Se rendre champs des ingalsses
    en 7,8, se placer dans le coin au dessus du zaap
    """
    move_bois = load_json("zqsde_move_bois.json")
    execute_move(move=move_bois)
    interruptible_wait_until(6)
    move_coin = load_json("zqsde_move_back_coin.json")
    execute_move(move=move_coin)
    # move_cereales = load_json("zqsde_move_cereales.json")
    move_cereales = load_json("zqsde_move_cereales2.json")
    execute_move(move=move_cereales)

def main_for_peche_astrub():
    """
    Se rendre à Astrub et aller au milieu du lac
    """
    move_top = load_json("zqsde_move_peche_top.json")
    move_bot = load_json("zqsde_move_peche_bot.json")
    list_is_fish = []

    interruptible_sleep(1)
    is_fish = peche_ocr()
    list_is_fish.append(is_fish)
    while any(list_is_fish[-3:]):
        is_fish = peche_ocr()
        list_is_fish.append(is_fish)

    if not any(list_is_fish[-3:]):
        execute_move(move=move_bot)
        interruptible_sleep(2)

    list_is_fish = []
    is_fish = peche_ocr()
    list_is_fish.append(is_fish)
    while any(list_is_fish[-3:]):
        is_fish = peche_ocr()
        list_is_fish.append(is_fish)
    
    if not any(list_is_fish[-3:]):
        execute_move(move=move_top)
        interruptible_sleep(120)



# MOVE = load_json("zqsde_move_bois2.json")

@launch_loop
def main():

    # LISTENER PART
    # get_zqsde_move(name="peche_top")

    # EXECUTION PART
    # execute_move(move=MOVE)
    # interruptible_wait_until(2)
    # execute_inverse_move(move=MOVE)
    # interruptible_wait_until(120)

    # main_for_bois_cereales()
    main_for_peche_astrub()

    # BASIC COLLECT
    # collect()


main()
# SCRIPT EXECUTION
# COMMAND: python -m src.main.py
