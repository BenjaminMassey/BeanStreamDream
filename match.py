# --- LIBRARIES ---
from PyQt6.QtWidgets import *

class Match(QWidget):
    def __init__(self, parent=None):
        super(Match, self).__init__(parent)
        
        self.layout = QGridLayout()
        
        self.title = "MATCH"
        self.first_score = 0
        self.second_score = 0
        self.first_name = "Player A"
        self.second_name = "Player B"

        base_html_file = open("./html/match.html", 'r')
        self.base_html = base_html_file.read()
        base_html_file.close()
        
        # --- ACTUAL GUI ---

        self.title_label = QLabel("Title:")
        self.layout.addWidget(self.title_label, 0, 0)

        self.title_entry = QLineEdit(self.title)
        self.layout.addWidget(self.title_entry, 0, 1)
        self.title_entry.textChanged[str].connect(self.tef)

        self.layout.addWidget(QLabel(), 1, 0) # spacer

        self.first_name_entry = QLineEdit(self.first_name)
        self.layout.addWidget(self.first_name_entry, 2, 0)
        self.first_name_entry.textChanged[str].connect(self.fnef)

        self.first_minus_button = QPushButton("-")
        self.layout.addWidget(self.first_minus_button, 2, 1)
        self.first_minus_button.clicked.connect(
            lambda: self.changeFirstScore(-1)
        )

        self.first_score_entry = QLineEdit(str(self.first_score))
        self.layout.addWidget(self.first_score_entry, 2, 2)
        self.first_score_entry.textChanged[str].connect(self.fsef)

        self.first_plus_button = QPushButton("+")
        self.layout.addWidget(self.first_plus_button, 2, 3)
        self.first_plus_button.clicked.connect(
            lambda: self.changeFirstScore(1)
        )

        self.second_name_entry = QLineEdit(self.second_name)
        self.layout.addWidget(self.second_name_entry, 3, 0)
        self.second_name_entry.textChanged[str].connect(self.snef)

        self.second_minus_button = QPushButton("-")
        self.layout.addWidget(self.second_minus_button, 3, 1)
        self.second_minus_button.clicked.connect(
            lambda: self.changeSecondScore(-1)
        )

        self.second_score_entry = QLineEdit(str(self.second_score))
        self.layout.addWidget(self.second_score_entry, 3, 2)
        self.second_score_entry.textChanged[str].connect(self.ssef)

        self.second_plus_button = QPushButton("+")
        self.layout.addWidget(self.second_plus_button, 3, 3)
        self.second_plus_button.clicked.connect(
            lambda: self.changeSecondScore(1)
        )

        # --- CLOSE ---

        self.layout.addWidget(QLabel(), 4, 2) # spacer

        self.close_button = QPushButton("Close")
        self.layout.addWidget(self.close_button, 5, 2)

        # --- INIT THE HTML ---

        self.pushToHTML()

        # --- FINALIZATION ---

        self.setWindowTitle("BSD Match")

        self.setLayout(self.layout)
        
    # --- FUNCTIONS ---

    def pushToHTML(self):
        html = self.base_html
        html = html.replace("{{TITLE}}", self.title)
        html = html.replace("{{FIRST_SCORE}}", str(self.first_score))
        html = html.replace("{{SECOND_SCORE}}", str(self.second_score))
        html = html.replace("{{FIRST_NAME}}", self.first_name)
        html = html.replace("{{SECOND_NAME}}", self.second_name)
        file = open("./output.html", 'w')
        file.write(html)
        file.close()
        
    # --- ANNOYING GUI FUNCTIONS ---

    def changeFirstScore(self, num):
        self.first_score += num
        self.first_score_entry.setText(str(self.first_score))
        self.pushToHTML()

    def changeSecondScore(self, num):
        self.second_score += num
        self.second_score_entry.setText(str(self.second_score))
        self.pushToHTML()

    # title entry function, infer the nexts
    def tef(self, text):
        self.title = text
        self.pushToHTML()

    def fnef(self, text):
        self.first_name = text
        self.pushToHTML()

    def fsef(self, text):
        try:
            self.first_score = int(text)
        except:
            self.first_score_entry.setText(str(self.first_score))
        self.pushToHTML()

    def snef(self, text):
        self.second_name = text
        self.pushToHTML()

    def ssef(self, text):
        try:
            self.second_score = int(text)
        except:
            self.second_score_entry.setText(str(self.second_score))
        self.pushToHTML()
    
    def setClose(self, func):
        self.close_button.clicked.connect(func)
        
    def show(self):
        super(Match, self).show()
        self.pushToHTML()