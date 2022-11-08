# --- LIBRARIES ---
from PyQt6.QtWidgets import *

def showWindow(window, close = None):
    if close != None:
        close.close()
    window.window.show()
    window.app.exec()