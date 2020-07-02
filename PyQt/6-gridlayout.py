import sys
from PyQt5.QtWidgets import (QWidget,QGridLayout,
    QPushButton,QApplication,QLCDNumber)

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):

        grid = QGridLayout()
        self.setLayout(grid)
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('Calculator')

        self.lcd = QLCDNumber()
        grid.addWidget(self.lcd, 0, 0, 3, 0)
        grid.setSpacing(10)
        names = ['Cls', 'Bck','', 'Close',
                '7', '8', '9', '/',
                '4', '5', '6', '*',
                '1', '2', '3', '-',
                '0', '.', '=','+']
        positions = [(i,j) for i in range(4, 9) for j in range(4, 8)]

        for position, name in zip(positions, names):

            if name == '':
                continue
            button = QPushButton(name)
            grid.addWidget(button, *position)
            button.clicked.connect(self.Cli)

        self.move(300,150)
        
        self.show()
    
    def Cli(self):
        sender = self.sender().text()
        ls = ['/', '.', '-', '=', '+']
        if sender in ls:
            self.lcd.display('A')
        else:
            self.lcd.display(sender)

if __name__ == '__main__':
    app = QApplication(sys.argv) # 创建应用程序对象
    ex = Example()
    sys.exit(app.exec_())  
