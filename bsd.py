from PyQt6.QtWidgets import *
from cryptography.fernet import Fernet
import os

# --- DATA INITIALIZATION --

data_dir = "./data/"
chat_path = data_dir + "chat.txt"
bot_path = data_dir + "bot.txt"
oauth_path = data_dir + "oauth.txt"
key_path = data_dir + "private-key.txt"

if not os.path.isdir(data_dir):
    os.mkdir(data_dir, 0o666)
   
for path in [chat_path, bot_path, oauth_path]:
    if not os.path.isfile(path):
        file = open(path, 'w')
        file.close()
        
key = None

if os.path.isfile(key_path):
    file = open(key_path, 'r')
    key = file.read()
    file.close
else:
    key = Fernet.generate_key()
    file = open(key_path, 'w')
    file.write(key.decode("utf-8"))
    file.close()
    
fernet = Fernet(key)

# --- FUNCTIONS ---

def fencrypt(text):
    global fernet
    text = fernet.encrypt(text.encode())
    return text.decode("utf-8")

def fdecrypt(text):
    global fernet
    return fernet.decrypt(text).decode()

# --- GUI INITIALIZATION ---

app = QApplication([])

window = QWidget()

layout = QVBoxLayout()

# --- GUI FUNCTIONS ---

def writeEntryToPath(entry, path, encrypt=False):
    file = open(path, 'w')
    text = entry.text()
    if encrypt:
        text = fencrypt(text)
    file.write(text)
    file.close()

# --- CHAT CHANNEL ---

chat_label = QLabel("Chat Channel:")
layout.addWidget(chat_label)

file = open(chat_path, 'r')
chat_saved = file.read()
file.close()

chat_entry = QLineEdit(chat_saved)
layout.addWidget(chat_entry)

chat_button = QPushButton("Submit")
layout.addWidget(chat_button)

chat_button.clicked.connect(
    lambda: writeEntryToPath(chat_entry, chat_path)
)

# --- BOT NAME ---

bot_label = QLabel("Bot Username:")
layout.addWidget(bot_label)

file = open(bot_path, 'r')
bot_saved = file.read()
file.close()

bot_entry = QLineEdit(bot_saved)
layout.addWidget(bot_entry)

bot_button = QPushButton("Submit")
layout.addWidget(bot_button)

bot_button.clicked.connect(
    lambda: writeEntryToPath(bot_entry, bot_path)
)

# --- OAUTH ---

oauth_label = QLabel("Bot Oauth Token:")
layout.addWidget(oauth_label)

oauth_entry = QLineEdit()
oauth_entry.setEchoMode(QLineEdit.EchoMode.Password)
layout.addWidget(oauth_entry)

oauth_button = QPushButton("Submit")
layout.addWidget(oauth_button)

oauth_button.clicked.connect(
    lambda: writeEntryToPath(oauth_entry, oauth_path, True)
)

# --- FINALIZATION ---

window.setLayout(layout)

window.show()

app.exec()