from uuid import uuid4
from time import perf_counter
from helpers import save_json
import pyautogui
import keyboard

def get_zqsde_move() -> dict[str, any]:
    """
    Listen ZQSD keys to return list of keys usesd in the order and pressed time.

    Results:
        dict: dictionary of keys pressed in the order and time pressed.
        {
            "name": "script_name",
            "description": "script_description",
            "events": [
                {"time": 0.0, "event": "down", "key": "z"},
                {"time": 0.5, "event": "up", "key": "z"},
                {"time": 1.0, "event": "down", "key": "q"},
                {"time": 1.5, "event": "up", "key": "q"}
            ]
        }
    """
    keys = {"z", "q", "s", "d", "e"}
    events = []
    pressed_keys = set()

    print("Press ALT GR to start recording...")
    keyboard.wait("alt gr")

    start_time = perf_counter()
    print("Recording... Press CTRL to stop.")

    def on_key_event(event):
        key = event.name

        if key not in keys:
            return

        elapsed = perf_counter() - start_time

        if event.event_type == "down":
            # INFO: Avoid repeated key-down events when holding a key
            if key not in pressed_keys:
                pressed_keys.add(key)
                events.append({
                    "time": elapsed,
                    "event": "down",
                    "key": key
                })

        elif event.event_type == "up":
            if key in pressed_keys:
                pressed_keys.remove(key)
                events.append({
                    "time": elapsed,
                    "event": "up",
                    "key": key
                })

    hook = keyboard.hook(on_key_event)

    keyboard.wait("ctrl")
    keyboard.unhook(hook)

    # INFO: Close any keys still held when recording stops
    end_time = perf_counter() - start_time

    for key in list(pressed_keys):
        events.append({
            "time": end_time,
            "event": "up",
            "key": key
        })
    # INFO: Save the recorded events to a JSON file
    filename = f"zqsde_move_{uuid4().hex[:6]}"
    res = {
        "name": filename,
        "description": "Recorded ZQSD/E movement",
        "events": events
    }

    save_json(data=res, filename=f"{filename}.json")
    return res


def get_mouse_position():
    """Get the current mouse position and print it to the console"""
    # pyautogui.displayMousePosition()
    while True:
        keyboard.wait('alt')

        if keyboard.is_pressed('ctrl'):
                    print("Arrêt du script.")
                    break
        
        x, y = pyautogui.position()
        print(f"Position souris : X={x}, Y={y}", end="\r")
        