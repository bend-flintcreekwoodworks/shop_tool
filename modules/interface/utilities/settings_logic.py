import dearpygui.dearpygui as dpg

# --- PROJECT MODULES ---
from modules.data.config import config as cfg, save_config

def save_callback():
    cfg["TRELLO_API_KEY"] = dpg.get_value("settings_api_key")
    cfg["TRELLO_TOKEN"] = dpg.get_value("settings_token")
    cfg["ROOT"] = dpg.get_value("settings_root")
    save_config(cfg)
    dpg.hide_item("settings_window")
    dpg.show_item("home_window")

def folder_select_callback(sender, app_data):
    dpg.set_value("settings_root", app_data["file_path_name"])
    dpg.hide_item("folder_dialog")