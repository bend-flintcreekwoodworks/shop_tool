# --- PROJECT MODULES ---
from modules.interface.navigation.menu.menu import setup_menu
from modules.interface.navigation.home import create_home_window
from modules.interface.navigation.settings import create_settings_window, open_settings_window
from modules.interface.navigation.product_search import create_product_search_window
from modules.data.config import config as cfg

def load_content():
    setup_menu()
    create_home_window()
    create_settings_window()
    open_settings_window(show=False)
    create_product_search_window()

    if not all(cfg.get(k) for k in ["TRELLO_API_KEY", "TRELLO_TOKEN", "ROOT"]):
        open_settings_window(show=True)
    