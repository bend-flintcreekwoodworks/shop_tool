import os
import dearpygui.dearpygui as dpg

def load_default_font():
    font_path = r"C:/Windows/Fonts/arial.ttf"
    with dpg.font_registry():
        font = dpg.add_font(font_path, 14)
    dpg.bind_font(font)