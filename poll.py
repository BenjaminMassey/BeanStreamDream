# --- LIBRARIES ---
from PyQt6.QtWidgets import *
from enum import Enum

class Poll(QWidget):
    
    polling = False
    
    results = []
    
    running_msg = "Poll running...<br><br>Write <i>\"!vote X\"</i> to vote for X"

    def __init__(self, xbot, parent=None):
        super(Poll, self).__init__(parent)
        
        self.xbot = xbot
    
        self.layout = QGridLayout()

        base_html_file = open("./html/poll.html", 'r')
        self.base_html = base_html_file.read()
        base_html_file.close()

        # --- ACTUAL GUI ---

        self.poll_button = QPushButton("Start")
        self.layout.addWidget(self.poll_button, 0, 0)
        self.poll_button.clicked.connect(self.pollToggle)

        # --- CLOSE ---

        self.layout.addWidget(QLabel(), 1, 0) # spacer

        self.close_button = QPushButton("Close")
        self.layout.addWidget(self.close_button, 2, 0)

        # --- INIT THE HTML ---

        self.pushToHTML()

        # --- FINALIZATION ---

        self.setWindowTitle("BSD Poll")

        self.setLayout(self.layout)
        
    def pushToHTML(self, results=None):
        html = self.base_html
        data = "Poll pending..."
        if results == None and self.polling:
            data = self.running_msg
        if results != None:
            data = results
        html = html.replace("{{DATA}}", data)
        file = open("./output.html", 'w')
        file.write(html)
        file.close()
        
    def startPolling(self):
        print("STARTED POLLING")
        polling = True
        self.xbot.start_poll()
        self.pushToHTML()
    
    def stopPolling(self):
        print("FINISHED POLLING")
        polling = False
        self.xbot.stop_poll()
        self.pushToHTML(self.parseData())
        
    def parseData(self):
        raw = self.xbot.poll_values
        unordered = []
        for key, value in raw.items():
            unordered.append((key, value))
        ordered = sorted(unordered, key=lambda item: item[1])
        ordered.reverse()
        result = ""
        for item in ordered:
            result += str(item[0]) + ": " + str(item[1]) + "<br>"
        return result
        
    def pollToggle(self):
        self.polling = not self.polling
        if (self.polling):
            self.poll_button.setText("Stop")
            self.startPolling()
        else:
            self.poll_button.setText("Start")
            self.stopPolling()
        
    def setClose(self, func):
        self.close_button.clicked.connect(func)
        
    def show(self):
        super(Poll, self).show()
        self.pushToHTML()