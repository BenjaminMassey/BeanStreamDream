# --- LIBRARIES ---
from cryptography.fernet import Fernet
import os

# --- FILE HANDLING ---

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

# --- ENCRYPTION SPECIFIC ---

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

def fencrypt(text):
    global fernet
    text = fernet.encrypt(text.encode())
    return text.decode("utf-8")

def fdecrypt(text):
    global fernet
    return fernet.decrypt(text).decode()