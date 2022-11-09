# --- LIBRARIES ---
from cryptography.fernet import Fernet
import os

class Data(object):
    def __init__(self):
        
        # --- FOR BSD ---
        self.needToConfig = False

        # --- FILE HANDLING ---
        self.data_dir = "./data/"
        self.chat_path = self.data_dir + "chat.txt"
        self.bot_path = self.data_dir + "bot.txt"
        self.oauth_path = self.data_dir + "oauth.txt"
        self.key_path = self.data_dir + "private-key.txt"

        if not os.path.isdir(self.data_dir):
            os.mkdir(self.data_dir, 0o666)
           
        for path in [self.chat_path, self.bot_path, self.oauth_path]:
            if not os.path.isfile(path):
                self.needToConfig = True
                file = open(path, 'w')
                file.close()
            else:
                file = open(path, 'r')
                text = file.read()
                file.close()
                if len(text) == 0:
                    self.needToConfig = True
                
        key = None

        # --- ENCRYPTION SPECIFIC ---

        if os.path.isfile(self.key_path):
            file = open(self.key_path, 'r')
            key = file.read()
            file.close
        else:
            needToConfig = True
            key = Fernet.generate_key()
            file = open(self.key_path, 'w')
            file.write(key.decode("utf-8"))
            file.close()
            
        self.fernet = Fernet(key)

    def fencrypt(self, text):
        text = self.fernet.encrypt(text.encode())
        return text.decode("utf-8")

    def fdecrypt(self, text):
        return self.fernet.decrypt(text).decode()