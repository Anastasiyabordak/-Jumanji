import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5 import uic
from PyQt5.QtWidgets import QFileDialog
from game import GameWindow
from settings_theme import ThemeWindow
# from LoginWindow import LoginWindow
import test_1
from time import sleep
from rectangle_detecton.camera import online_detect

image_ui = None

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.fff = None
        test_1.clear_stripe()
        #online_detect()
        self.initUI()

    def initUI(self):
        uic.loadUi("/home/pi/Desktop/gui/Jumanji/GUI/startPage.ui", self)
        self.newGame.clicked.connect(self.nGame)
       # self.cont.clicked.connect(self.Continue)
        self.exit.clicked.connect(self.Exit)
        self.show()
        self.showFullScreen()

    def Exit(self):
        test_1.clear_stripe()
        self.close()

    def nGame(self):
        global image_ui
        image_ui = ThemeWindow(ex)
        image_ui.show()
        self.close()

    def Continue(self):
        global image_ui
        image_ui = GameWindow(ex)
        self.fff = image_ui
        image_ui.show()
        self.close()


if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    global ex
    ex = MainWindow()
    a = app.exec_()
    
    sys.exit(a)
