""" Main entry point for the game bot """

import keyboard

from src.system import launch_loop, interruptible_sleep
from src.listener import get_zqsde_move
from src.execution import execute_move, execute_inverse_move
from src.helpers import load_json
from src.actions import collect, fight


def main_for_lin():
    """
    Se rendre champs des ingalsses
    en 7,8, se placer sur le lin du bas
    """
    move_lin = load_json("zqsde_move_lin.json")
    collect()
    collect()
    
    execute_move(move=move_lin)
    interruptible_sleep(5)
    execute_inverse_move(move=move_lin)
    interruptible_sleep(240)

MOVE = load_json("zqsde_move_lin.json")

@launch_loop
def main():

    # LISTENER PART
    # get_zqsde_move()

    # EXECUTION PART
    # execute_move(move=MOVE)
    # interruptible_sleep(5)
    # execute_inverse_move(move=MOVE)
    # interruptible_sleep(240)

    # BASIC COLLECT
    collect()


main()
# SCRIPT EXECUTION
# COMMAND: python -m src.main.py
