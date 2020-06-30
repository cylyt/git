import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLineEdit
from PyQt5.QtGui  import QIcon
from random import randint

class Example(QWidget):

    def __init__(self):

        super().__init__()
        self.initUI()
        self.num = randint(1,100)

    def initUI(self):

        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('guess-number')
        
        self.bt1 = QPushButton('Guess!', self)
        self.bt1.setGeometry(115, 150, 70, 30)
        self.bt1.setToolTip('<b>push here to guess</b>')
        self.bt1.clicked.connect(self.show_message)

        self.text = QLineEdit('enter your number!', self)
        self.text.selectAll()
        self.text.setFocus()
        self.text.setGeometry(80,50,150,30)

        self.show()
    
    def show_message(self):
        guess_number = int(self.text.text())
        print(self.num)

        if guess_number > self.num:
            QMessageBox.about(self, 'the answer', 'too big')
            self.text.setFocus()
        elif guess_number < self.num:
            QMessageBox.about(self, 'the answer', 'too small')
            self.text.setFocus()
        else:
            QMessageBox.about(self, 'the answer', 'bingo')
            self.num = randint(1, 100)
            self.text.clear()
            self.text.setFocus()

    def closeEvent(self, event):

        reply = QMessageBox.question(self,'sure', 'sure to quit?',
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv) 
    ex = Example()
    sys.exit(app.exec_())       
