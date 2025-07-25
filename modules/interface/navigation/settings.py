import dearpygui.dearpygui as dpg

# --- PROJECT MODULES ---
from modules.data.config import config as cfg
from modules.interface.navigation.home import open_home_window
from modules.interface.utilities.settings_logic import save_callback, folder_select_callback

def create_settings_window():
    with dpg.window(label="Settings", tag="settings_window", show=False):
        dpg.add_text("  API CREDENTIALS")
        dpg.add_input_text(label="Trello API Key", tag="settings_api_key", width=400, password=True)
        dpg.add_input_text(label="Trello Token", tag="settings_token", width=400, password=True)
        dpg.add_spacer(height=9)
        dpg.add_text("  SHOP DIRECTORIES")
        dpg.add_text("MOZAIK JOBS FOLDER:")
        with dpg.group(horizontal=True):
            with dpg.file_dialog(
                directory_selector=True,
                show=False,
                tag="folder_dialog",
                callback=folder_select_callback,
                cancel_callback=lambda: dpg.hide_item("folder_dialog"),
                width=600,
                height=400,
            ):
                dpg.add_file_extension("")
            dpg.add_input_text(tag="settings_root", width=400)
            dpg.add_button(label="Browse", callback=lambda: dpg.show_item("folder_dialog"))
        dpg.add_spacer(height=18) 
        with dpg.group(horizontal=True):
            dpg.add_button(label="Save", callback=save_callback)
            dpg.add_button(label="Quit", callback=open_home_window)
        
def open_settings_window(show=True):
    dpg.set_value("settings_api_key", cfg.get("TRELLO_API_KEY", ""))
    dpg.set_value("settings_token", cfg.get("TRELLO_TOKEN", ""))
    dpg.set_value("settings_root", cfg.get("ROOT", ""))
    if show:
        dpg.show_item("settings_window")