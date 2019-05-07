import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5 import uic
from PyQt5.QtWidgets import QFileDialog
from game import GameWindow


class PlayerWindow(QtWidgets.QMainWindow):

    def __init__(self, mainWindow, themes):
        self.theme = ['2', '3', '4']
        super().__init__()
        self.initUI()
        self.mainWindow = mainWindow
        self.theme = themes

    def initUI(self):
        uic.loadUi("/home/pi/Desktop/gui/Jumanji/GUI/settings_player.ui", self)
        self.back.clicked.connect(self.showMainWindow)
        self.themeBox.addItems(self.theme)
        self.select.clicked.connect(self.nextWindow)
        self.show()
        self.showFullScreen()

    def nextWindow(self):
        global image_ui
        image_ui = GameWindow(self.mainWindow, self.theme, self.themeBox.currentText())
        image_ui.show()
        self.close()

    # Back to main
    def showMainWindow(self):
        global main_ui
        self.mainWindow.show()
        self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    global ex
    ex = ThemeWindow()
    a = app.exec_()
    sys.exit(a)
