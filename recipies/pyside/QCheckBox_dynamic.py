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

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = Window()
    w.show()

    app.exec_()


# 0
# I ended up figuring it out myself. Part of it was my fault, 
# and the other part is a little bit hacky (seeing as it 
# probably doesn't use a Qt function it could be using). 
# First, I needed to lay everything out on a grid layout, 
# this made it so my check marks started showing up when I added them
# Sadly, the window didn't resize with the checkboxes, 
# so I wrote a function like this to fix it:

def addCheckbox(self, name):
    checkBox = QtGui.QCheckBox(self.window.CheckboxField)
    self.window.CheckboxLayout.addWidget(checkBox)
    checkBox.setText(name)
    newHeight = self.geometry().height()+21#Compensate for new checkbox
    self.resize(self.geometry().width(),  newHeight)