# --- LIBRARIES ---
from PyQt6.QtWidgets import *
import threading
import sys

# --- PROJECT FILES ---
import data
import config
import menu
import count
import match
import twitch

# --- TWITCH BOT ---

Bot = None
BotThread = None

def doBot():
    global Bot, BotThread, Data

    Bot = twitch.Bot(Data)

    def bot():
        global Bot
        Bot.run()
        
    BotThread = threading.Thread(target=bot)
    BotThread.start()
    
# --- FUNCTIONS ---
    
def showHide(shows, hides):
    for s in shows:
        s.show()
    for h in hides:
        h.hide()
        
def configClose():
    global Data, Bot
    Data = data.Data()
    if not Data.needToConfig:
        if Bot == None:
            doBot()
        else:
            print("\n\nYou will need to restart to use your new config\n\n")
        showHide([Menu], [Config])

# --- MAIN SECTION ---

Data = data.Data()

App = QApplication(sys.argv)

Config = config.Config(Data)
Config.setClose(configClose)

Count = count.Count()
Count.setClose(lambda: showHide([Menu], [Count]))

Match = match.Match()
Match.setClose(lambda: showHide([Menu], [Match]))

Menu = menu.Menu()
Menu.setButtonFunc(Menu.config_button, lambda: showHide([Config], [Menu]))
Menu.setButtonFunc(Menu.count_button, lambda: showHide([Count], [Menu]))
Menu.setButtonFunc(Menu.match_button, lambda: showHide([Match], [Menu]))

if Data.needToConfig:
    Config.show()
else:
    if Bot == None:
        doBot()
    Menu.show()

sys.exit(App.exec())