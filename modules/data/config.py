import os
import json
import sys

# --- VERSION AND APP NAME LOGIC ---
VERSION_NUMBER = 1
PATCH = 1
BETA = True

VERSION_NAME = f"{VERSION_NUMBER}.{PATCH}-beta" if BETA else f"{VERSION_NUMBER}.{PATCH}"
APP_NAME = f"ShopTool-{VERSION_NAME}"

# --- CONFIG PATH AND DEFAULTS ---
def get_config_path():
    if hasattr(sys, '_MEIPASS'):
        base = os.path.expandvars(r'%LOCALAPPDATA%')
        config_dir = os.path.join(base, "ShopTool")
    else:
        config_dir = os.path.dirname(os.path.abspath(__file__))
    os.makedirs(config_dir, exist_ok=True)
    return os.path.join(config_dir, "settings.json")

CONFIG_FILE = get_config_path()

DEFAULTS = {
    "TRELLO_API_KEY": None,
    "TRELLO_TOKEN": None,
    "ROOT": None
}

# --- LOAD AND SAVE CONFIG ---
def load_config():
    if not os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "w") as f:
            json.dump(DEFAULTS, f, indent=2)
    with open(CONFIG_FILE, "r") as f:
        return json.load(f)

def save_config(config):
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=2)

config = load_config()