import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        layout = QVBoxLayout()
        self.checks = []
        for i in xrange(5):
            c = QCheckBox("Option %i" % i)
            layout.addWidget(c)
            self.checks.append(c)

        self.setLayout(layout)

if(__name__ == "__main__"): # test locally
    import sys
    global mv
    add_path ='/studio/tools/hou/builds/hfs16.0.600/dsolib/Qt_plugins' #add qt path plugins
    QCoreApplication.addLibraryPath(add_path) 
    qapp = QtWidgets.QApplication(sys.argv) # Correct way how to use QApplication
    w = Example() # load window
    w.show()
    #mv.close()
    qapp.exec_() #sys.exit(qapp.exec_())