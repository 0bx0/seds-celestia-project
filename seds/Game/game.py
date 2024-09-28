from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import random


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.points = 0
        self.setGeometry(200,200,500,500)
        self.setWindowTitle("COOL GAME")
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("CLICK THE BUTTON FOR POINTS")
        self.label.move(25,20)
    
        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("+")
        self.b1.clicked.connect(self.randomize)
    
    def randomize(self):
        self.b1.move(random.randint(0,400),random.randint(0,400))
        if(self.points < 1000):
            self.points +=250
        elif(self.points >= 1000 and self.points <5000):
            self.points += 500
        elif(self.points >= 5000 and self.points <10000):
            self.points += 1000
        else:
            self.points += 5000
        self.label.setText("YOUR SCORE: "+str(self.points))

        self.update()

    def update(self):
        self.label.adjustSize()




def window(): 
    app = QApplication(sys.argv)
    win = MyWindow()

    win.show()
    sys.exit(app.exec_())

window()
