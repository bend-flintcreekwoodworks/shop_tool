import dearpygui.dearpygui as dpg

# --- PROJECT MODULES ---
from modules.data.config import APP_NAME
from modules.data.features import FEATURES
def create_home_window():
    with dpg.window(label="Home", tag="home_window", show=True):
        dpg.add_spacer(height=3)
        dpg.add_text(f"You are currently using {APP_NAME}")
        dpg.add_spacer(height=9)
        dpg.add_text("RECENT UPDATES:")
        dpg.add_text(FEATURES, wrap=500)

def open_home_window():
    dpg.show_item("home_window")