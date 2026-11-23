import json

def save_json(data: dict, filename: str) -> None:
    """Save data to a JSON file"""
    with open(f"src/data/moves/{filename}", "w") as f:
        json.dump(data, f, indent=4)
    print(f"Data saved to {filename}")

def load_json(filename: str) -> dict:
    """Load data from a JSON file"""
    with open(f"src/data/moves/{filename}", "r") as f:
        data = json.load(f)
    print(f"Data loaded from {filename}")
    return data
