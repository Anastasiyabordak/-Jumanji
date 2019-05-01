import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5 import uic
from PyQt5.QtWidgets import QFileDialog
from game import GameWindow
from settings_theme import ThemeWindow
# from LoginWindow import LoginWindow


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi("GUI/startPage.ui", self)
        self.newGame.clicked.connect(self.nGame)
       # self.cont.clicked.connect(self.Continue)
        self.exit.clicked.connect(self.Exit)
        self.show()
        self.setFixedSize(480, 320)

    def Exit(self):
        self.close()

    def nGame(self):
        global image_ui
        image_ui = ThemeWindow(ex)
        image_ui.show()
        self.close()

    def Continue(self):
        global image_ui
        image_ui = GameWindow(ex)
        image_ui.show()
        self.close()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    global ex
    ex = MainWindow()
    a = app.exec_()
    sys.exit(a)
