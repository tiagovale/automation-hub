import json

FILE = "data/state.json"

def load_state():
    with open(FILE, "r") as f:
        return json.load(f)

def save_state(state):
    with open(FILE, "w") as f:
        json.dump(state, f, indent=2)