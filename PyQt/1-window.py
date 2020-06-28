import sys
from PyQt5.QtWidgets import QApplication, QWidget,QDesktopWidget
from PyQt5.QtGui import QIcon

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5-window'
        self.left = 50
        self.top = 50
        self.width = 640
        self.height = 480
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowIcon(QIcon('web.png'))
        self.center()
        self.show()
    
    def center(self):
        
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__':
    app = QApplication(sys.argv) # 创建应用程序对象
    ex = App()
    '''
    ex.resize(250,150)
    ex.move(300,300)
    ex.setWindowTitle('abc')
    '''
    sys.exit(app.exec_())


