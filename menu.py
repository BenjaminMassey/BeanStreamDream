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
    
count_button = QPushButton("Count Mode")
layout.addWidget(count_button, 1, 0)
def doCount():
    global window
    import count
    util.showWindow(count, window)
count_button.clicked.connect(doCount)
    
match_button = QPushButton("Match Mode")
layout.addWidget(match_button, 2, 0)
def doMatch():
    global window
    import match
    util.showWindow(match, window)
match_button.clicked.connect(doMatch)

# --- FINALIZATION ---

window.setWindowTitle("BSD Menu")

window.setLayout(layout)