import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5 import uic
from PyQt5.QtWidgets import QFileDialog
from settings_player import PlayerWindow


class ThemeWindow(QtWidgets.QMainWindow):

    def __init__(self, mainWindow):
        self.theme = ['food', 'programming', 'books', 'movies', 'music', 'jokes', 'perplexity']
        super().__init__()
        self.initUI()
        self.mainWindow = mainWindow

    def initUI(self):
        uic.loadUi("GUI/settings_theme.ui", self)
        self.back.clicked.connect(self.showMainWindow)
        self.themeBox.addItems(self.theme)
        self.select.clicked.connect(self.nextWindow)
        self.show()
        self.setFixedSize(480, 320)

    def nextWindow(self):
        global image_ui
        image_ui = PlayerWindow(self.mainWindow, self.themeBox.currentText())
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
