import dearpygui.dearpygui as dpg
import threading
from modules.interface.utilities.search_logic import threaded_search
from modules.interface.utilities.search_output import save_csv
from modules.interface.utilities.fullscreen_windows import resize_main_window

def run_search_callback():
    name = dpg.get_value("sp_name_filter") or None
    desc = dpg.get_value("sp_desc_filter") or None
    dpg.configure_item("sp_search_btn", enabled=False)
    dpg.set_value("sp_results", "Searching...")
    dpg.set_value("sp_progress", 0.0)
    dpg.configure_item("sp_progress", show=True)
    threading.Thread(target=threaded_search, args=(name, desc), daemon=True).start()

def export_results_callback():
    rows = dpg.get_item_user_data("sp_results")
    path = save_csv(rows)
    msg = f"Saved to: {path}" if path else "No results to export."
    dpg.set_value("sp_results", msg)

def create_product_search_window():
    with dpg.window(label="Product Search", tag="product_search_window", show=False):
        dpg.add_input_text(label="Product Name", tag="sp_name_filter", width=300)
        dpg.add_input_text(label="Product Description", tag="sp_desc_filter", width=300)
        dpg.add_button(label="Search", tag="sp_search_btn", callback=run_search_callback)
        dpg.add_progress_bar(tag="sp_progress", default_value=0.0, width=600, show=False)
        dpg.add_separator()
        dpg.add_input_text(tag="sp_results", multiline=True, readonly=True, width=700, height=300)
        with dpg.group(horizontal=True):
            dpg.add_button(label="Export CSV", callback=export_results_callback)
            dpg.add_button(label="Back", callback=lambda: dpg.hide_item("product_search_window"))

def open_product_search_window():
    dpg.show_item("product_search_window")
    resize_main_window(None, None)
