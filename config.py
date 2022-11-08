# --- LIBRARIES ---
from PyQt6.QtWidgets import *

# --- PROJECT FILES ---
import data

# --- INITIALIZATION ---

app = QApplication([])

window = QWidget()

layout = QGridLayout()

# --- FUNCTIONS ---

def writeEntryToPath(entry, path, encrypt=False):
    file = open(path, 'w')
    text = entry.text()
    if encrypt:
        text = data.fencrypt(text)
        entry.setText("<<<SAVED>>>")
        entry.setEchoMode(QLineEdit.EchoMode.Normal)
    file.write(text)
    file.close()

# --- CHAT CHANNEL ---

chat_label = QLabel("Chat Channel:")
layout.addWidget(chat_label, 0, 0)

file = open(data.chat_path, 'r')
chat_saved = file.read()
file.close()

chat_entry = QLineEdit(chat_saved)
layout.addWidget(chat_entry, 0, 1)

chat_button = QPushButton("Submit")
layout.addWidget(chat_button, 0, 2)

chat_button.clicked.connect(
    lambda: writeEntryToPath(chat_entry, data.chat_path)
)

# --- BOT NAME ---

bot_label = QLabel("Bot Username:")
layout.addWidget(bot_label, 1, 0)

file = open(data.bot_path, 'r')
bot_saved = file.read()
file.close()

bot_entry = QLineEdit(bot_saved)
layout.addWidget(bot_entry, 1, 1)

bot_button = QPushButton("Submit")
layout.addWidget(bot_button, 1, 2)

bot_button.clicked.connect(
    lambda: writeEntryToPath(bot_entry, data.bot_path)
)

# --- OAUTH ---

oauth_label = QLabel("Bot Oauth Token:")
layout.addWidget(oauth_label, 2, 0)

oauth_saved = ""
file = open(data.oauth_path, 'r')
if len(file.read()) > 0:
    oauth_saved = "<<<FOUND>>>"

oauth_entry = QLineEdit(oauth_saved)
layout.addWidget(oauth_entry, 2, 1)

def hideOauth():
    global oauth_entry
    oauth_entry.setEchoMode(QLineEdit.EchoMode.Password)
oauth_entry.textChanged[str].connect(hideOauth)

oauth_button = QPushButton("Submit")
layout.addWidget(oauth_button, 2, 2)

oauth_button.clicked.connect(
    lambda: writeEntryToPath(oauth_entry, data.oauth_path, True)
)

# --- CLOSE ---

temp = QLabel()
layout.addWidget(temp, 3, 1)

close_button = QPushButton("Close")
layout.addWidget(close_button, 4, 1)

# --- FINALIZATION ---

window.setWindowTitle("BSD Config")

window.setLayout(layout)