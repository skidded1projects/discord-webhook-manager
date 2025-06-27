import os
import json

CFG_PATH = "Cfg/last_used.json"

def save_config(new_data):
    os.makedirs("Cfg", exist_ok=True)

    if os.path.exists(CFG_PATH):
        with open(CFG_PATH, "r") as f:
            try:
                existing_data = json.load(f)
            except json.JSONDecodeError:
                existing_data = {}
    else:
        existing_data = {}

    existing_data.update(new_data)

    with open(CFG_PATH, "w") as f:
        json.dump(existing_data, f, indent=4)
