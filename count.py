# --- LIBRARIES ---
from PyQt6.QtWidgets import *

class Count(QWidget):
    def __init__(self, parent=None):
        super(Count, self).__init__(parent)
    
        self.layout = QGridLayout()

        self.counting = "Deaths:"
        self.counter = 0

        base_html_file = open("./html/count.html", 'r')
        self.base_html = base_html_file.read()
        base_html_file.close()

        # --- ACTUAL GUI ---

        self.counting_entry = QLineEdit(self.counting)
        self.layout.addWidget(self.counting_entry, 0, 0)
        self.counting_entry.textChanged[str].connect(self.changeCounting)

        self.counter_minus_button = QPushButton("-")
        self.layout.addWidget(self.counter_minus_button, 1, 0)
        self.counter_minus_button.clicked.connect(
            lambda: self.changeCounter(-1)
        )

        self.counter_entry = QLineEdit(str(self.counter))
        self.layout.addWidget(self.counter_entry, 1, 1)
        self.counter_entry.textChanged[str].connect(self.setCounter)

        self.counter_plus_button = QPushButton("+")
        self.layout.addWidget(self.counter_plus_button, 1, 2)
        self.counter_plus_button.clicked.connect(
            lambda: self.changeCounter(1)
        )

        # --- CLOSE ---

        self.layout.addWidget(QLabel(), 2, 0) # spacer

        self.close_button = QPushButton("Close")
        self.layout.addWidget(self.close_button, 3, 1)

        # --- INIT THE HTML ---

        self.pushToHTML()

        # --- FINALIZATION ---

        self.setWindowTitle("BSD Match")

        self.setLayout(self.layout)
        
    def pushToHTML(self):
        html = self.base_html
        html = html.replace("{{COUNTING}}", self.counting)
        html = html.replace("{{COUNTER}}", str(self.counter))
        file = open("./output.html", 'w')
        file.write(html)
        file.close()

    def changeCounting(self, text):
        self.counting = text
        self.pushToHTML()

    def changeCounter(self, num):
        self.counter += num
        self.counter_entry.setText(str(self.counter))
        self.pushToHTML()
        
    def setCounter(self, text):
        try:
            self.counter = int(text)
        except:
            self.counter_entry.setText(str(self.counter))
        self.pushToHTML()
        
    def setClose(self, func):
        self.close_button.clicked.connect(func)
        
    def show(self):
        super(Count, self).show()
        self.pushToHTML()