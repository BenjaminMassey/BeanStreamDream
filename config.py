# --- LIBRARIES ---
from PyQt6.QtWidgets import *

# --- PROJECT FILES ---
import data

class Config(QWidget):
    def __init__(self, xdata, parent=None):
        super(Config, self).__init__(parent)

        self.layout = QGridLayout()

        # --- CHAT CHANNEL ---

        self.chat_label = QLabel("Chat Channel:")
        self.layout.addWidget(self.chat_label, 0, 0)

        file = open(xdata.chat_path, 'r')
        chat_saved = file.read()
        file.close()

        self.chat_entry = QLineEdit(chat_saved)
        self.layout.addWidget(self.chat_entry, 0, 1)

        self.chat_button = QPushButton("Submit")
        self.layout.addWidget(self.chat_button, 0, 2)
        self.chat_button.clicked.connect(
            lambda: self.writeEntryToPath(self.chat_entry, xdata.chat_path)
        )

        # --- BOT NAME ---

        self.bot_label = QLabel("Bot Username:")
        self.layout.addWidget(self.bot_label, 1, 0)

        file = open(xdata.bot_path, 'r')
        bot_saved = file.read()
        file.close()

        self.bot_entry = QLineEdit(bot_saved)
        self.layout.addWidget(self.bot_entry, 1, 1)

        self.bot_button = QPushButton("Submit")
        self.layout.addWidget(self.bot_button, 1, 2)
        self.bot_button.clicked.connect(
            lambda: self.writeEntryToPath(self.bot_entry, xdata.bot_path)
        )

        # --- OAUTH ---

        self.oauth_label = QLabel("Bot Oauth Token:")
        self.layout.addWidget(self.oauth_label, 2, 0)

        oauth_saved = ""
        file = open(xdata.oauth_path, 'r')
        if len(file.read()) > 0:
            oauth_saved = "<<<FOUND>>>"

        self.oauth_entry = QLineEdit(oauth_saved)
        self.layout.addWidget(self.oauth_entry, 2, 1)
        
        self.oauth_entry.textChanged[str].connect(self.hideOauth)

        self.oauth_button = QPushButton("Submit")
        self.layout.addWidget(self.oauth_button, 2, 2)
        self.oauth_button.clicked.connect(
            lambda: self.writeEntryToPath(self.oauth_entry, xdata.oauth_path, True)
        )

        # --- CLOSE ---
        
        self.layout.addWidget(QLabel(), 3, 1)

        self.close_button = QPushButton("Close")
        self.layout.addWidget(self.close_button, 4, 1)

        # --- FINALIZATION ---

        self.setWindowTitle("BSD Config")

        self.setLayout(self.layout)
        
        self.xdata = xdata
        
    def writeEntryToPath(self, entry, path, encrypt=False):
        file = open(path, 'w')
        text = entry.text()
        if encrypt:
            text = self.xdata.fencrypt(text)
            entry.setText("<<<SAVED>>>")
            entry.setEchoMode(QLineEdit.EchoMode.Normal)
        file.write(text)
        file.close()
        
    def hideOauth(self):
        self.oauth_entry.setEchoMode(QLineEdit.EchoMode.Password)
        
    def setClose(self, func):
        self.close_button.clicked.connect(func)