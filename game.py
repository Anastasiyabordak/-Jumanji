import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5 import uic
from PyQt5.QtWidgets import QFileDialog
import pandas as pd


class GameWindow(QtWidgets.QMainWindow):

    def __init__(self, mainWindow, theme, players):

        super().__init__()
        self.initUI()
        self.mainWindow = mainWindow
        self.theme = theme
        self.players = players
        print("theme: ", self.theme)
        print("players: ", self.players)
        self.df = pd.read_csv('data/music.csv')
        print(self.df)

    def initUI(self):
        uic.loadUi("GUI/game.ui", self)
        self.back.clicked.connect(self.showMainWindow)
        self.one.clicked.connect(self.oneB)
        self.two.clicked.connect(self.twoB)
        self.three.clicked.connect(self.threeB)
        self.four.clicked.connect(self.fourB)
        self.show()
        self.setFixedSize(480, 320)


    def oneB(self):
        print("one")

    def twoB(self):
        print("two")

    def threeB(self):
        print("three")

    def fourB(self):
        print("four")

    # Back to main
    def showMainWindow(self):
        global main_ui
        self.mainWindow.show()
        self.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    global ex
    ex = GamesWindow()
    a = app.exec_()
    sys.exit(a)
