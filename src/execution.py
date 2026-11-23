from time import perf_counter
import keyboard

from src.system import interruptible_sleep

def execute_move(move: dict[str, any]) -> None:
    """
    Execute a move recorded by get_zqsde_move.

    Args:
        move (dict): The move to execute.
    """
    events = move.get("events", [])
    start_time = perf_counter()

    for event in events:
        elapsed = perf_counter() - start_time
        wait_time = event["time"] - elapsed

        if wait_time > 0:
            interruptible_sleep(wait_time)

        key = event["key"]
        if event["event"] == "down":
            keyboard.press(key)
        elif event["event"] == "up":
            keyboard.release(key)


def execute_inverse_move(move: dict[str, any]):
    """
    Execute a move recorded by get_zqsde_move.

    Args:
        move (dict): The move to execute.
    """
    events = move.get("events", [])

    # INFO: Reverse the order of events
    inverse_events = events[::-1]

    # INFO: Map keys to their inverse
    key_mapping = {"q": "d", "d": "q", "z": "s", "s": "z"}
    event_mapping = {"down": "up", "up": "down"}

    # INFO: recover max time without event key 'e' 
    max_time = max(event["time"] for event in inverse_events if event["key"] != "e")

    filtered_events = [
        {**item, "key": key_mapping.get(item["key"], item["key"]),
                 "event": event_mapping.get(item["event"], item["event"]), 
                 "time": max_time + 1 - item["time"]}
        for item in inverse_events
        if item["key"] != "e"
    ]

    return execute_move({"name": move["name"], "description": move["description"], "events": filtered_events})

    