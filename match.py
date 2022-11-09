# --- LIBRARIES ---
from PyQt6.QtWidgets import *

# --- PROJECT FILES ---
import util

# --- INITIALIZATION ---

app = QApplication([])

window = QWidget()

layout = QGridLayout()

# --- GLOBALS ---

title = "MATCH"
first_score = 0
second_score = 0
first_name = "Player A"
second_name = "Player B"

base_html_file = open("./html/match.html", 'r')
base_html = base_html_file.read()
base_html_file.close()

# --- FUNCTIONS ---

def pushToHTML():
    global title, first_score, second_score, first_name, second_name, base_html
    html = base_html
    html = html.replace("{{TITLE}}", title)
    html = html.replace("{{FIRST_SCORE}}", str(first_score))
    html = html.replace("{{SECOND_SCORE}}", str(second_score))
    html = html.replace("{{FIRST_NAME}}", first_name)
    html = html.replace("{{SECOND_NAME}}", second_name)
    file = open("./output.html", 'w')
    file.write(html)
    file.close()
    
# --- ANNOYING GUI FUNCTIONS ---

def changeFirstScore(num):
    global first_score, first_score_entry
    first_score += num
    first_score_entry.setText(str(first_score))
    pushToHTML()

def changeSecondScore(num):
    global second_score, second_score_entry
    second_score += num
    second_score_entry.setText(str(second_score))
    pushToHTML()

# title entry function, infer the nexts
def tef(text):
    global title
    title = text
    pushToHTML()

def fnef(text):
    global first_name
    first_name = text
    pushToHTML()

def fsef(text):
    global first_score
    try:
        first_score = int(text)
    except:
        global first_score_entry
        first_score_entry.setText(str(first_score))
    pushToHTML()

def snef(text):
    global second_name
    second_name = text
    pushToHTML()

def ssef(text):
    global second_score
    try:
        second_score = int(text)
    except:
        global second_score_entry
        second_score_entry.setText(str(second_score))
    pushToHTML()

# --- ACTUAL GUI ---

title_label = QLabel("Title:")
layout.addWidget(title_label, 0, 0)

title_entry = QLineEdit(title)
layout.addWidget(title_entry, 0, 1)
title_entry.textChanged[str].connect(tef)

layout.addWidget(QLabel(), 1, 0) # spacer

first_name_entry = QLineEdit(first_name)
layout.addWidget(first_name_entry, 2, 0)
first_name_entry.textChanged[str].connect(fnef)

first_minus_button = QPushButton("-")
layout.addWidget(first_minus_button, 2, 1)
first_minus_button.clicked.connect(
    lambda: changeFirstScore(-1)
)

first_score_entry = QLineEdit(str(first_score))
layout.addWidget(first_score_entry, 2, 2)
first_score_entry.textChanged[str].connect(fsef)

first_plus_button = QPushButton("+")
layout.addWidget(first_plus_button, 2, 3)
first_plus_button.clicked.connect(
    lambda: changeFirstScore(1)
)

second_name_entry = QLineEdit(second_name)
layout.addWidget(second_name_entry, 3, 0)
second_name_entry.textChanged[str].connect(snef)

second_minus_button = QPushButton("-")
layout.addWidget(second_minus_button, 3, 1)
second_minus_button.clicked.connect(
    lambda: changeSecondScore(-1)
)

second_score_entry = QLineEdit(str(second_score))
layout.addWidget(second_score_entry, 3, 2)
second_score_entry.textChanged[str].connect(ssef)

second_plus_button = QPushButton("+")
layout.addWidget(second_plus_button, 3, 3)
second_plus_button.clicked.connect(
    lambda: changeSecondScore(1)
)

# --- CLOSE ---

layout.addWidget(QLabel(), 4, 2) # spacer

close_button = QPushButton("Close")
layout.addWidget(close_button, 5, 2)

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