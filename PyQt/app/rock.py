import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QPushButton
from random import randint

class Example(QWidget):

    def __init__(self):

        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle('Rock')

        bt1 = QPushButton('Scissor', self)
        bt1.setGeometry(30, 180, 50, 50)
        bt2 = QPushButton('Rock', self)
        bt2.setGeometry(100, 180, 50, 50)
        bt3 = QPushButton('Paper', self)
        bt3.setGeometry(170, 180, 50, 50)

        bt1.clicked.connect(self.button_clicked)
        bt2.clicked.connect(self.button_clicked)
        bt3.clicked.connect(self.button_clicked)

        self.show()
    
    def who_win(self,p1,p2):
        if p1 == p2:
            return 'equal'
        elif (p1 + p2) != 4 and p1 > p2 :
            return True
        elif p2 == 3 and p1 == 1 :
            return True
        else:
            return False

    def button_clicked(self):
        computer  = randint(1 ,3)
        print(computer)
        player = 0
        sender = self.sender()
        if sender.text() == 'Scissor':
            player = 1
        elif sender.text() == 'Rock':
            player = 2
        else:
            player = 3
        
        result = self.who_win(computer, player)

        if result == 'equal':
            QMessageBox.about(self,'result', 'equal')
        elif result == True:
            QMessageBox.about(self,'result', 'you lost!')
        else:
            QMessageBox.about(self,'result', 'you win!')
        
    
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())