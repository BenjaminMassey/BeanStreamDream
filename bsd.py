from PyQt6.QtWidgets import *
import os

# --- DATA INITIALIZATION --

data_dir = "./data/"
chat_path = data_dir + "chat.txt"
bot_path = data_dir + "bot.txt"
oauth_path = data_dir + "oauth.txt"

if not os.path.isdir(data_dir):
    os.mkdir(data_dir, 0o666)
   
for path in [chat_path, bot_path, oauth_path]:
    if not os.path.isfile(path):
        file = open(path, 'w')
        file.close()

# --- GUI INITIALIZATION ---

app = QApplication([])

window = QWidget()

layout = QVBoxLayout()

# --- GUI FUNCTIONS ---

def writeEntryToPath(entry, path):
    file = open(path, 'w')
    file.write(entry.text())
    file.close()

# --- CHAT CHANNEL ---

chat_label = QLabel("Chat Channel:")
layout.addWidget(chat_label)

chat_entry = QLineEdit()
layout.addWidget(chat_entry)

chat_button = QPushButton("Submit")
layout.addWidget(chat_button)

chat_button.clicked.connect(
    lambda: writeEntryToPath(chat_entry, chat_path)
)

# --- BOT NAME ---

bot_label = QLabel("Bot Username:")
layout.addWidget(bot_label)

bot_entry = QLineEdit()
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
layout.addWidget(oauth_entry)

oauth_button = QPushButton("Submit")
layout.addWidget(oauth_button)

oauth_button.clicked.connect(
    lambda: writeEntryToPath(oauth_entry, oauth_path)
)

# --- FINALIZATION ---

window.setLayout(layout)

window.show()

app.exec()