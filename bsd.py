# --- LIBRARIES ---
from PyQt6.QtWidgets import *

# --- PROJECT FILES ---
import util
import data
import config
import menu

# --- MAIN SECTION ---

if data.needToConfig:
    util.showWindow(config)
else:
    util.showWindow(menu)