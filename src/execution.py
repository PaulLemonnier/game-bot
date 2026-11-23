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


def remove_idle_time(events) -> list[dict[str, any]]:
    """Remove idle time from a list of events."""
    
    # INFO: Ignore key E
    events = [e for e in events if e["key"] != "e"]

    active_keys = set()
    last_time = None
    removed_time = 0
    treated_events = []

    for event in events:
        current_time = event["time"]

        # INFO: If no keys are active, accumulate the idle time
        if last_time is not None and not active_keys:
            removed_time += current_time - last_time

        treated_events.append({
            **event,
            "time": current_time - removed_time
        })

        if event["event"] == "down":
            active_keys.add(event["key"])
        elif event["event"] == "up":
            active_keys.discard(event["key"])

        last_time = current_time

    return treated_events



def execute_inverse_move(move: dict[str, any]):
    """
    Execute a move recorded by get_zqsde_move.

    Args:
        move (dict): The move to execute.
    """
    events = move.get("events", [])
    treated_events = remove_idle_time(events)

    # INFO: Reverse the order of events
    inverse_events = treated_events[::-1]

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

    