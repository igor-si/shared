import sys, os
from PySide.QtCore import *
from PySide.QtGui import *

class fileListClass(QListWidget):
    def __init__(self, parent):
        super(fileListClass, self).__init__(parent)
        self.setAcceptDrops(True)
        self.pathList = []

    def appendImage(self, path):
        path = path.replace('/','\\')
        if not  path in self.pathList:
            name = os.path.basename(path)
            item = QListWidgetItem()
            item.setText(name)
            item.setData(32, path)
            self.addItem(item)
            self.pathList.append(path)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
            for url in event.mimeData().urls():
                self.appendImage(url.toLocalFile())
        else:
            event.ignore()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Delete:
            sel = self.selectedIndexes()
            for i in reversed(sel):
                if i.data(32) in self.pathList:
                    self.pathList.remove(i.data(32))
                self.takeItem(i.row())

class resourceCompileClass(QMainWindow):
    def __init__(self):
        super(resourceCompileClass, self).__init__()
        self.setWindowTitle('Resource Compiler')
        self.resize(250,300)
        self.w = QWidget()
        self.setCentralWidget(self.w)
        self.ly = QVBoxLayout()
        self.w.setLayout(self.ly)
        self.list = fileListClass(self)
        self.ly.addWidget(self.list)
        self.run_btn = QPushButton('RUN')
        self.ly.addWidget(self.run_btn)
        self.run_btn.clicked.connect(self.runCompile)
        if len(sys.argv) == 2:
            image = sys.argv[1]
            self.list.appendImage(image)

    def compileQrc(self, qrc):
        workDir = os.path.dirname(qrc)
        os.chdir(workDir)
        #PySide
        compiled = os.path.join(os.path.dirname(qrc), 'icons_rcs.py')
        rcc = 'C:/Python27/Lib/site-packages/PySide/pyside-rcc.exe'
        cmd = ' '.join([rcc, qrc, '-o', compiled])
        os.system(cmd)
        #PyQt
        compiled = os.path.join(os.path.dirname(qrc), 'icons_rc.py')
        rcc = 'C:/Python27/Lib/site-packages/PyQt4/pyrcc4.exe '
        cmd = ' '.join([rcc, qrc, '-o', compiled])
        os.system(cmd)
        return True

    def runCompile(self):
        files = [self.list.item(i).data(32) for i in range(self.list.count())]
        qrc = os.path.join(os.path.dirname(files[0]), 'resource.qrc')
        if self.writeFile(qrc, files):
            self.compileQrc(qrc)


    def writeFile(self, qrc, files):
        with open(qrc, 'w') as f:
            f.write('<RCC>\n\t<qresource>\n')
            for ico in files:
                f.write('\t\t<file>%s</file>\n' % os.path.basename(ico))
            f.write('\t</qresource>\n</RCC>')
        return True

app = QApplication(sys.argv)
window = resourceCompileClass()
window.show()
sys.exit(app.exec_())



    

