import dearpygui.dearpygui as dpg

# --- PROJECT MODULES ---
from modules.interface.utilities.hide_windows import show_only_window
from modules.interface.utilities.save_and_quit import save_and_quit

def setup_menu():
    with dpg.viewport_menu_bar():
        with dpg.menu(label="FILE"):
            dpg.add_menu_item(label="Home", callback=lambda: show_only_window("home_window"))
            dpg.add_menu_item(label="Save + Quit", callback=save_and_quit)
        dpg.add_menu_item(label="SETTINGS", callback=lambda: show_only_window("settings_window"))
        dpg.add_menu_item(label="PRODUCT SEARCH", callback=lambda: show_only_window("product_search_window"))