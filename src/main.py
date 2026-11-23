""" Main entry point for the game bot """

import keyboard

from src.system import launch_loop, interruptible_sleep
from src.listener import get_zqsde_move
from src.execution import execute_move, execute_inverse_move
from src.helpers import load_json



@launch_loop
def main():

    # LISTENER PART
    # get_zqsde_move()

    # EXECUTION PART
    first_move = load_json("zqsde_move_fc7889.json")
    execute_inverse_move(move=first_move)
    interruptible_sleep(2)
    execute_move(move=first_move)
    





main()
