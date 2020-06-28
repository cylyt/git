import sys

from PyQt5.QtWidgets import (QWidget, QPushButton, 
    QHBoxLayout,QVBoxLayout,QApplication)

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        ok_botton = QPushButton('OK')
        cancel_botton = QPushButton('Cancel')

        hbox = QHBoxLayout()
        
        hbox.addStretch(1)
        hbox.addWidget(ok_botton)
        hbox.addStretch(0)
        hbox.addWidget(cancel_botton)
        
        vbox = QVBoxLayout()
        vbox.addStretch(0)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setGeometry(300,300,300,150)
        self.setWindowTitle('boxlayout')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv) # 创建应用程序对象
    ex = Example()
    sys.exit(app.exec_())       