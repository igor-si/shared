# URL https://stackoverflow.com/questions/51173728/python-how-can-i-display-a-checkbox-as-checked-in
from PyQt4 import QtCore, QtGui
from functools import partial


class Widget(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        lay = QtGui.QVBoxLayout(self)

        button = QtGui.QPushButton("Default")
        lay.addWidget(button)

        options = ["A", "B", "C", "D", "E", "F"]
        default = ["A", "B", "C"] 

        for option in options:
            checkbox = QtGui.QCheckBox(option)
            lay.addWidget(checkbox)
            if option in default:
                button.clicked.connect(partial(checkbox.setChecked, True))


if __name__ == '__main__':
    import sys

    app = QtGui.QApplication(sys.argv)
    w = Widget()
    w.show()
    sys.exit(app.exec_())