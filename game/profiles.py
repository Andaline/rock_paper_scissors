# profiles.py
import os
import json

PROFILE_DIR = "profiles"
DEFAULT_PROFILE = "default"

def list_profiles():
    if not os.path.exists(PROFILE_DIR):
        os.makedirs(PROFILE_DIR)
    return [f.replace('.json', '') for f in os.listdir(PROFILE_DIR) if f.endswith('.json')]

def load_profile(name):
    profile_path = os.path.join(PROFILE_DIR, f"{name}.json")
    if not os.path.exists(profile_path):
        return {"player": 0, "computer": 0, "highscore": 0, "streak": 0}
    with open(profile_path, 'r') as file:
        return json.load(file)

def save_profile(name, data):
    profile_path = os.path.join(PROFILE_DIR, f"{name}.json")
    with open(profile_path, 'w') as file:
        json.dump(data, file, indent=2)

def delete_profile(name):
    profile_path = os.path.join(PROFILE_DIR, f"{name}.json")
    if os.path.exists(profile_path):
        os.remove(profile_path)
