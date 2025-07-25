import dearpygui.dearpygui as dpg

# --- PROJECT MODULES ---
from modules.data.windows import WINDOWS

def resize_main_window(sender, app_data):
    w, h = dpg.get_viewport_width(), dpg.get_viewport_height()
    for tag in WINDOWS:
        if dpg.does_item_exist(tag):
            dpg.set_item_pos(tag, [0,0])
            dpg.set_item_width(tag, w)
            dpg.set_item_height(tag, h)
