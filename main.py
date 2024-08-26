import PySide6.QtCore
import contest
import contestant
import serialReader
from datetime import datetime
import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
import qdarktheme
import time

print(PySide6.__version__)
print(PySide6.QtCore.__version__)
QWidget=QtWidgets.QWidget
QVBoxLayout=QtWidgets.QVBoxLayout
QLabel=QtWidgets.QLabel
QPushButton=QtWidgets.QPushButton
QHBoxLayout = QtWidgets.QHBoxLayout
QLineEdit = QtWidgets.QLineEdit
QListWidget = QtWidgets.QListWidget
contest = contest.contest
serialReader = serialReader.serialConnector


class My_Environment(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.timer =  QtCore.QTimer(self)
        self.stage = 0
        self.timer.start(50)
        self.timer.timeout.connect(self.refresh)
        self.port = 'COM3'
        self.baudrate = 9600
        self.contest = None
        self.title = 'RunningContest2024'
        self.left = 10
        self.top = 10
        self.width = 400
        self.height = 140
        self.connector = serialReader(self.port , self.baudrate)
        self.initUI()

    def initUI(self):
        self.player_ID_integer = 0
        self.stacked_widget = QtWidgets.QStackedWidget() 

        self.page1 = QWidget()
        self.page1_layout = QHBoxLayout()
        self.col_1_page_1 = QVBoxLayout()
        self.create_game_button = QPushButton("Create round")
        self.welcome = QLabel("welcome, enter the round number to proceed to the next page which you will add compatitors in.")
        self.round_text_box = QLineEdit(self)
        self.round_text_box.setPlaceholderText("Enter the round")
        self.col_1_page_1.addWidget(self.welcome)
        self.col_1_page_1.addWidget(self.round_text_box)
        self.col_1_page_1.addWidget(self.create_game_button)
        self.page1_layout.addLayout(self.col_1_page_1)
        self.create_game_button.clicked.connect(self.make_contest)
        self.page1.setLayout(self.page1_layout)

        self.list_players_registered = QListWidget()
        self.page2 = QWidget()
        self.page2_layout = QVBoxLayout()
        self.page2_layout_row_1 = QHBoxLayout()
        self.col_1_page_2 = QVBoxLayout()
        self.col_2_page_2 = QVBoxLayout()
        self.player_name = QLineEdit()
        self.start_match_button = QPushButton("start the match!!!")
        self.player_name.setPlaceholderText('Enter player\'s name')
        self.player_group = QLineEdit()
        self.player_group.setPlaceholderText("Enter player's Group")
        self.player_ID_label = QLabel("NO_ID")
        self.add_player_button = QPushButton("add player")
        self.refresh_serial = QPushButton("refresh serial port")
        self.player_number = QLineEdit()
        self.player_number.setPlaceholderText("Enter player number")
        self.col_1_page_2.addWidget(self.player_ID_label)
        self.col_1_page_2.addWidget(self.player_number)
        self.col_1_page_2.addWidget(self.player_name)
        self.col_1_page_2.addWidget(self.player_group)
        self.col_1_page_2.addWidget(self.refresh_serial)
        self.col_1_page_2.addWidget(self.add_player_button)
        self.button_to_page1 = QPushButton("## remake contest ##")
        self.button_to_page1.setStyleSheet("background-color: black")
        self.page2_layout_row_1.addLayout(self.col_1_page_2)
        self.page2_layout_row_1.addLayout(self.col_2_page_2)
        self.page2_layout_row_1.addWidget(self.list_players_registered)
        self.add_player_button.clicked.connect(self.add_player)
        self.button_to_page1.clicked.connect(self.show_main_page)
        self.page2_layout.addLayout(self.page2_layout_row_1)
        self.start_match_button.setStyleSheet("background-color:green")
        self.page2_layout.addWidget(self.button_to_page1)
        self.page2_layout.addWidget(self.start_match_button)
        self.page2.setLayout(self.page2_layout)
        self.start_match_button.clicked.connect(self.start_match)

        self.page3 = QWidget()
        self.list_players_in_game = QListWidget()
        self.list_players_finished = QListWidget()
        self.page3_layout = QVBoxLayout()
        self.page_3_row_1 = QHBoxLayout()
        self.page_3_row_1_2 = QHBoxLayout()
        self.page_3_row_1_2.addWidget(QLabel("Finished"))
        self.page_3_row_1_2.addWidget(QLabel("In Game"))
        self.page_3_row_1.addWidget(self.list_players_finished)
        self.page_3_row_1.addWidget(self.list_players_in_game)
        self.page3_layout.addLayout(self.page_3_row_1_2)
        self.page3_layout.addLayout(self.page_3_row_1)
        self.end_match_button = QPushButton("end the match. (player finish time will be current time if not finished)")
        self.page3_layout.addWidget(self.end_match_button)
        self.page3.setLayout(self.page3_layout)
        self.end_match_button.clicked.connect(self.finish_match)


        self.page4 = QWidget()
        self.match_leaderboard = QListWidget()
        self.page4_layout = QVBoxLayout()
        self.page4_layout.addWidget(self.match_leaderboard)
        self.page4_layout.addWidget(self.button_to_page1)
        self.page4.setLayout(self.page4_layout)

        self.stacked_widget.addWidget(self.page1)
        self.stacked_widget.addWidget(self.page2)
        self.stacked_widget.addWidget(self.page3)
        self.stacked_widget.addWidget(self.page4)

        main_layout = QVBoxLayout()
        self.global_time_layout = QLabel("GlobalTime: "+str(datetime.now()))
        self.reconnect_button = QPushButton("Reconnect serial")
        self.rigid_data = QHBoxLayout()
        self.rigid_data.addWidget(self.global_time_layout)
        self.rigid_data.addWidget(self.reconnect_button)
        self.reconnect_button.clicked.connect(self.reconnect)
        main_layout.addLayout(self.rigid_data)
        main_layout.addWidget(self.stacked_widget)
        self.setLayout(main_layout)
        self.setWindowTitle("RunningContest2024")
        self.resize(300, 200)

    def show_main_page(self):
        self.stacked_widget.setCurrentIndex(0)
    def show_second_page(self):
        self.stacked_widget.setCurrentIndex(1)
    def show_in_contest_page(self):
        self.stacked_widget.setCurrentIndex(2)
    def show_forth_page(self):
        self.stacked_widget.setCurrentIndex(3)
    def refresh(self):
        try:
            self.global_time_layout.setText("GlobalTime: "+str(datetime.now())\
                                            +"  MatchStart: "+str(self.contest.start_time))
        except:
            pass
        last_serial_read = self.connector.get_ID()
        print(last_serial_read)
        if last_serial_read != 0:
            self.player_ID_integer = last_serial_read
            self.player_ID_label.setText(f"Detected player_ID: {self.player_ID_integer}")  
            if self.contest.started:   
                player = self.contest.return_contestant_by_id(self.player_ID_integer)
                if not player.finished_competition:
                    item = self.list_players_in_game.takeItem(\
                                self.find_Item_by_ID(self.list_players_in_game,self.player_ID_integer))
                    del item
                    player.finished()
                    player_data = player.to_string(True)
                    self.list_players_finished.addItem(player_data)
                    
                    
        self.reconnect_button.setStyleSheet("background-color :green" if self.connector.is_connected() else\
                                            "background-color :red")

    def reconnect(self):
        if not self.connector.is_connected():
            self.connector.reconnect(self.port,self.baudrate)
    def make_contest(self):
        try:
            self.contest = contest(int(self.round_text_box.text()))
            self.show_second_page()
        except:
            print("unacceptable input or can't make contest.")
    def add_player(self):
        player = contestant.contestant(self.player_name.text(),\
                                        int(self.player_group.text()),self.player_ID_integer,\
                                        int(self.player_number.text()))
        if self.contest.add_contestant(player):
            player_data = player.to_string(False)
            self.list_players_registered.addItem(player_data)
            self.player_group.clear()
            self.player_number.clear()
            self.player_name.clear()
        print(self.contest.people_in_groups)
    def find_Item_by_ID(self,itemList:QListWidget,ID):
        for index in range(itemList.count()):
            print(itemList.item(index).text() , self.contest.return_contestant_by_id(ID).to_string(False))
            if itemList.item(index).text() == self.contest.return_contestant_by_id(ID).to_string(False):
                print("found item in Qlist")
                return index
    def start_match(self):
        self.player_ID_integer = 0
        self.list_players_registered.clear()
        if len(self.contest.contestants) != 0:
            self.contest.start_competition()
            self.show_in_contest_page()
        else:
            print("No competitor added.")
        for contestant_ in self.contest.contestants:
            player_data = contestant_.to_string(False)
            self.list_players_in_game.addItem(player_data)
    def finish_match(self):
        self.contest.finish_competition()
        
        self.list_players_in_game.clear()
        self.list_players_finished.clear()
        self.show_forth_page()
        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    qdarktheme.setup_theme()
    widget = My_Environment()
    widget.resize(800, 600)
    widget.show()
    sys.exit(app.exec())
