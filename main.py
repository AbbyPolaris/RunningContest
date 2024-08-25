import PySide6.QtCore
import contest
import serialReader
print(PySide6.__version__)
print(PySide6.QtCore.__version__)
from datetime import datetime
import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui

contest = contest.contest
serialReader = serialReader.serialConnector


class My_Environment(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        #self.timer =  QtCore.QTimer(self)
        #self.timer.start(500)
        #self.timer.timeout.connect(self.refresh())
        self.port = 'tty6'
        self.baudrate = 9600
        self.contest = None
        self.nextwidget = self
        self.connector = serialReader(self.port , self.baudrate)
        self.time_text = QtWidgets.QLabel(str(datetime.now()),
                                     alignment=QtCore.Qt.AlignLeft)
        
        self.button = QtWidgets.QPushButton("start_competition")
        
        self.reconnect_button = QtWidgets.QPushButton("reconnect")

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.time_text)
        self.layout.addWidget(self.button)
        self.reconnect_button.clicked.connect(self.reconnect)
        self.button.clicked.connect(self.make_contest())
    def refresh(self):
        print("vdf")
        self.time_text.setText("fgdffg")
    def reconnect(self):
        self.connector.reconnect(self.port,self.baudrate)
    def make_contest(self):
        self.contest = contest(1,5)
        print("contest created.")
        self.compatition_started()
    def compatition_started(self):
        self.button.setVisible(False)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = My_Environment()
    widget.resize(800, 600)
    widget.show()
    sys.exit(app.exec())
