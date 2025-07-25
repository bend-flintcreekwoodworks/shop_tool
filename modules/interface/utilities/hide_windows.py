import dearpygui.dearpygui as dpg

# --- PROJECT MODULES ---
from modules.data.windows import WINDOWS

def show_only_window(tag_to_show):
    for tag in WINDOWS:
        if dpg.does_item_exist(tag):
            if tag == tag_to_show:
                dpg.show_item(tag)
            else:
                dpg.hide_item(tag)