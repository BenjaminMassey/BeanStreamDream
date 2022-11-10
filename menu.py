# --- LIBRARIES ---
from PyQt6.QtWidgets import *
import threading

# --- PROJECT FILES ---
import data
import twitch

# --- INITIALIZATION ---

class Menu(QWidget):
    def __init__(self, parent=None):
        super(Menu, self).__init__(parent)
        self.layout = QGridLayout()

        # --- BUTTONS ---

        self.config_button = QPushButton("Redo Config")
        self.layout.addWidget(self.config_button, 0, 0)
        
        self.layout.addWidget(QLabel(), 1, 0)
            
        self.count_button = QPushButton("Count Mode")
        self.layout.addWidget(self.count_button, 2, 0)
            
        self.match_button = QPushButton("Match Mode")
        self.layout.addWidget(self.match_button, 3, 0)
            
        self.poll_button = QPushButton("Poll Mode")
        self.layout.addWidget(self.poll_button, 4, 0)

        # --- FINALIZATION ---

        self.setWindowTitle("BSD Menu")

        self.setLayout(self.layout)
    
    def setButtonFunc(self, button, func):
        button.clicked.connect(func)