# --- LIBRARIES ---
from PyQt6.QtWidgets import *

# --- PROJECT FILES ---
import util

# --- INITIALIZATION ---

app = QApplication([])

window = QWidget()

layout = QGridLayout()

# --- BUTTONS ---

config_button = QPushButton("Redo Config")
layout.addWidget(config_button, 0, 0)

def doConfig():
    global window
    import config
    util.showWindow(config, window)
config_button.clicked.connect(doConfig)
    
match_button = QPushButton("Match Mode")
layout.addWidget(match_button, 1, 0)

match_button.clicked.connect(
    lambda: print("Not yet implemented")
)

# --- FINALIZATION ---

window.setWindowTitle("BSD Menu")

window.setLayout(layout)