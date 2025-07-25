import threading
import dearpygui.dearpygui as dpg
from pathlib import Path
from modules.data.config import config as cfg
from modules.interface.utilities.search_io import read_raw, extract_products
from modules.interface.utilities.search_output import format_output, save_csv

def get_root():
    root = cfg.get("ROOT")
    if not root:
        raise ValueError("Mozaik Jobs Root Folder not set. Please set it in Settings.")
    return Path(root)

def threaded_search(name_filter, desc_filter):
    try:
        ROOT = get_root()
    except Exception as e:
        dpg.set_value("sp_results", str(e))
        dpg.configure_item("sp_search_btn", enabled=True)
        return

    des_files = list(ROOT.rglob("*.des"))
    rows = []
    for idx, des_path in enumerate(des_files):
        raw = read_raw(des_path)
        if not raw:
            continue
        for prod in extract_products(raw):
            if name_filter and name_filter.lower() not in prod["ProdName"].lower():
                continue
            if desc_filter and desc_filter.lower() not in prod["ProductDesc"].lower():
                continue
            prod["Job"] = des_path.relative_to(ROOT).parts[0]
            prod["File"] = des_path.name
            rows.append(prod)
        dpg.set_value("sp_progress", (idx + 1) / len(des_files))
    
    dpg.set_value("sp_results", "No matching products found." if not rows else format_output(rows))
    dpg.set_value("sp_progress", 1.0)
    dpg.configure_item("sp_search_btn", enabled=True)
    dpg.configure_item("sp_progress", show=False)

    dpg.set_item_user_data("sp_results", rows)
