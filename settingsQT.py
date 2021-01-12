import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget, QListWidgetItem, QWidget, QTableWidgetItem
from PyQt5.QtGui import QPixmap
import sqlite3
import datetime as dt
from settings import *
import settings

con = sqlite3.connect("3d_game_settings")
cur = con.cursor()


class StWi(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('settings.ui', self)
        self.setWindowTitle('Меню настроек')

        self.textEdit.setText('-_-')
        self.textEdit.setReadOnly(True)

        self.pushButton_2.clicked.connect(self.leave)
        self.pushButton.clicked.connect(self.apply)

        self.lineEdit.setText(str(FPS))
        self.lineEdit_2.setText(str(player_speed))
        self.lineEdit_3.setText(str(sensivity))

        self.label.hide()

    def apply(self):
        cur.execute(f"""UPDATE settings_for_3d_game SET FPS = {self.lineEdit.text()}""")
        cur.execute(f"""UPDATE settings_for_3d_game SET player_speed = {self.lineEdit_2.text()}""")
        cur.execute(f"""UPDATE settings_for_3d_game SET sensivity = {self.lineEdit_3.text()}""")
        self.label.setText("чтобы изменения вступили в силу перезапустите игру")
        self.label.show()
        con.commit()

    def leave(self):
        self.label.hide()
        self.hide()


app = QApplication(sys.argv)
