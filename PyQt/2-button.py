import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, 
    QPushButton, QApplication)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QCoreApplication

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('this is a <b>QWidget</b> widget')
        btn = QPushButton('Button', self)
        btn.setToolTip('this is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint()) #默认大小
        btn.move(50,50)
        btq = QPushButton('Quit',self)
        btq.resize(btn.sizeHint())
        btq.move(150,50)
        btq.clicked.connect(QCoreApplication.instance().quit)  #退出窗口

        self.setGeometry(300,300,300,200)
        self.setWindowTitle('ToolTips')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv) # 创建应用程序对象
    ex = Example()
    sys.exit(app.exec_())

