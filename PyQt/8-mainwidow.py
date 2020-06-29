import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon

class Example(QMainWindow):

    def __init__(self):

        super().__init__()
        self.initUI()

    def initUI(self):

        exit_action = QAction(QIcon('web.png'),'&Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit application')
        exit_action.triggered.connect(qApp.quit)

        self.statusBar().showMessage('Ready')  #状态栏
        menubar = self.menuBar()               #菜单栏
        file_menu = menubar.addMenu('&File')
        file_menu.addAction(exit_action)

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exit_action)
        
        self.setGeometry(300,300,250,150)
        self.setWindowTitle('Statusbar')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv) # 创建应用程序对象
    ex = Example()
    sys.exit(app.exec_())            