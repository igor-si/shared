from PySide.QtCore import *
from PySide.QtGui import *

class windowClass(QMainWindow):
    def __init__(self):
        super(windowClass, self).__init__()
        self.w = QPushButton('ok')
        self.setCentralWidget(self.w)
        self.menuBar = QMenuBar()
        self.setMenuBar(self.menuBar)
        self.menu = QMenu('File')
        self.menuBar.addMenu(self.menu)
        self.act1 = QAction('Open', self)
        self.menu.addAction(self.act1)
        self.w.clicked.connect(self.pr)
    def pr(self):
        print 'PRESSED'

if __name__ == '__main__':
    app = QApplication([])
    w = windowClass()
    w.show()
    app.exec_()