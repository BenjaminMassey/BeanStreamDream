# --- LIBRARIES ---
from PyQt6.QtWidgets import *

# --- PROJECT FILES ---
import util

# --- INITIALIZATION ---

app = QApplication([])

window = QWidget()

layout = QGridLayout()

# --- GLOBALS ---

counting = "Deaths:"
counter = 0

base_html_file = open("./html/count.html", 'r')
base_html = base_html_file.read()
base_html_file.close()

# --- FUNCTIONS ---

def pushToHTML():
    global counting, counter, base_html
    html = base_html
    html = html.replace("{{COUNTING}}", counting)
    html = html.replace("{{COUNTER}}", str(counter))
    file = open("./output.html", 'w')
    file.write(html)
    file.close()

def changeCounting(text):
    global counting
    counting = text
    pushToHTML()

def changeCounter(num):
    global counter, counter_entry
    counter += num
    counter_entry.setText(str(counter))
    pushToHTML()
    
def setCounter(text):
    global counter
    try:
        counter = int(text)
    except:
        global counter_entry
        counter_entry.setText(str(counter))
    pushToHTML()

# --- ACTUAL GUI ---

counting_entry = QLineEdit(counting)
layout.addWidget(counting_entry, 0, 0)
counting_entry.textChanged[str].connect(changeCounting)

counter_minus_button = QPushButton("-")
layout.addWidget(counter_minus_button, 1, 0)
counter_minus_button.clicked.connect(
    lambda: changeCounter(-1)
)

counter_entry = QLineEdit(str(counter))
layout.addWidget(counter_entry, 1, 1)
counter_entry.textChanged[str].connect(setCounter)

counter_plus_button = QPushButton("+")
layout.addWidget(counter_plus_button, 1, 2)
counter_plus_button.clicked.connect(
    lambda: changeCounter(1)
)

# --- CLOSE ---

layout.addWidget(QLabel(), 2, 0) # spacer

close_button = QPushButton("Close")
layout.addWidget(close_button, 3, 1)

def doClose():
    global window
    import menu
    util.showWindow(menu, window)
close_button.clicked.connect(doClose)

# --- INIT THE HTML ---

pushToHTML()

# --- FINALIZATION ---

window.setWindowTitle("BSD Match")

window.setLayout(layout)