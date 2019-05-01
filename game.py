import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5 import uic
from PyQt5.QtWidgets import QFileDialog
import random
import csv 

class GameWindow(QtWidgets.QMainWindow):

    def __init__(self, mainWindow, theme, players):

        super().__init__()
        self.initUI()
        self.mainWindow = mainWindow
        self.theme = theme
        self.players = players
        print("theme: ", self.theme)
        print("players: ", self.players)
        self.df = []
        with open('data/music.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                self.df.append(row)
        self.max_question = len(self.df)
        self.scores = [0,0,0,0]
        self.player = 0
        self.setPlayer()
        print(self.df[0][0])
        self.question.setText(self.df[random.randint(1,self.max_question-1)][0])

    def initUI(self):
        uic.loadUi("GUI/game.ui", self)
        self.back.clicked.connect(self.showMainWindow)
        self.one.clicked.connect(self.oneB)
        self.two.clicked.connect(self.twoB)
        self.three.clicked.connect(self.threeB)
        self.three.setVisible(False)
        self.show()
        self.setFixedSize(480, 320)

    def setPlayer(self):
        self.id.setText("Player " + str(self.player%int(self.players)))
# not done
    def oneB(self):
        print("not done")
        print("Player:", self.player%int(self.players))
        self.question.setText(self.df[random.randint(1,self.max_question-1)][0])
        self.player = self.player + 1 
        self.setPlayer()
        
# done
    def twoB(self):
        print("done")
        print("Player:", self.player%int(self.players))
        self.two.setVisible(False)
        self.one.setVisible(False)
        self.three.setVisible(True)
        self.question.setText("Roll the dice")

# roll the dice       
    def threeB(self):
        print("roll the dice")
        print("Player:", self.player%int(self.players))
        self.two.setVisible(True)
        self.one.setVisible(True)
        self.three.setVisible(False)
        self.question.setText(self.df[random.randint(1,self.max_question-1)][0])
        score = random.randint(1,6)
        self.scores[self.player%int(self.players)] = self.scores[self.player%int(self.players)] + score
        print("Score: ", score)   
        print("Scores: ", self.scores)
        if self.scores[self.player%int(self.players)] > 10:
            self.quit()
        self.player = self.player + 1 
        self.setPlayer()

        

    def quit(self):
        print("QUIT")
        self.two.setVisible(False)
        self.one.setVisible(False)
        self.three.setVisible(False)
        self.question.setText("WIN")
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
