import dearpygui.dearpygui as dpg

# --- PROJECT MODULES ---
from modules.data.config import APP_NAME
from modules.interface.utilities.fullscreen_windows import resize_main_window
from modules.interface.utilities.load_content import load_content
from modules.interface.utilities.fonts import load_default_font
from modules.interface.navigation.settings import open_settings_window

def main():
    dpg.create_context()
    load_default_font()
    dpg.create_viewport(title=APP_NAME, width=800, height=600)

    load_content()

    dpg.setup_dearpygui()
    dpg.show_viewport()

    # --- KEEPS THE WINDOW SYNCED WITH VIEWPORT SIZE ---
    dpg.set_viewport_resize_callback(resize_main_window)
    resize_main_window(None, None)

    dpg.start_dearpygui()
    dpg.destroy_context()

if __name__ == "__main__":
    main()