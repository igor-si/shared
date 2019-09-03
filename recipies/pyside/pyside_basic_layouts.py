#!/usr/bin/env python
# PyQt uses a layout-based approach to widget management. Widgets are arranged in
# the optimal positions in windows based on simple layout rules, leading to a
# consistent look and feel.

# Custom layouts can be used to provide more control over the positions and
# sizes of child widgets.


# The example launcher provided with PyQt can be used to explore each of the
# examples in this directory.

# Documentation for these examples can be found via the Tutorial and Examples
# link in the main Qt documentation.


# Finding the PyQt Examples and Demos launcher
# ============================================

# On Windows:

# The launcher can be accessed via the Windows Start menu. Select the menu
# entry entitled "Examples and Demos" entry in the submenu containing PyQt4.

# On all platforms:

# The source code for the launcher can be found in the examples/demos/qtdemo
# directory in the PyQt package.

"""PyQt4 port of the layouts/basiclayout example from Qt v4.x"""

from PySide import QtCore, QtGui


class Dialog(QtGui.QDialog):
    NumGridRows = 3
    NumButtons = 4

    def __init__(self):
        super(Dialog, self).__init__()

        self.createMenu()
        self.createHorizontalGroupBox()
        self.createGridGroupBox()
        self.createFormGroupBox()

        bigEditor = QtGui.QTextEdit()
        bigEditor.setPlainText("This widget takes up all the remaining space "
                "in the top-level layout.")

        buttonBox = QtGui.QDialogButtonBox(QtGui.QDialogButtonBox.Ok | QtGui.QDialogButtonBox.Cancel)

        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

        mainLayout = QtGui.QVBoxLayout()
        mainLayout.setMenuBar(self.menuBar)
        mainLayout.addWidget(self.horizontalGroupBox)
        mainLayout.addWidget(self.gridGroupBox)
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(bigEditor)
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)

        self.setWindowTitle("Basic Layouts")

    def createMenu(self):
        self.menuBar = QtGui.QMenuBar()

        self.fileMenu = QtGui.QMenu("&File", self)
        self.exitAction = self.fileMenu.addAction("E&xit")
        self.menuBar.addMenu(self.fileMenu)

        self.exitAction.triggered.connect(self.accept)

    def createHorizontalGroupBox(self):
        self.horizontalGroupBox = QtGui.QGroupBox("Horizontal layout")
        layout = QtGui.QHBoxLayout()

        for i in range(Dialog.NumButtons):
            button = QtGui.QPushButton("Button %d" % (i + 1))
            layout.addWidget(button)

        self.horizontalGroupBox.setLayout(layout)

    def createGridGroupBox(self):
        self.gridGroupBox = QtGui.QGroupBox("Grid layout")
        layout = QtGui.QGridLayout()

        for i in range(Dialog.NumGridRows):
            label = QtGui.QLabel("Line %d:" % (i + 1))
            lineEdit = QtGui.QLineEdit()
            layout.addWidget(label, i + 1, 0)
            layout.addWidget(lineEdit, i + 1, 1)

        self.smallEditor = QtGui.QTextEdit()
        self.smallEditor.setPlainText("This widget takes up about two thirds "
                "of the grid layout.")

        layout.addWidget(self.smallEditor, 0, 2, 4, 1)

        layout.setColumnStretch(1, 10)
        layout.setColumnStretch(2, 20)
        self.gridGroupBox.setLayout(layout)

    def createFormGroupBox(self):
        self.formGroupBox = QtGui.QGroupBox("Form layout")
        layout = QtGui.QFormLayout()
        layout.addRow(QtGui.QLabel("Line 1:"), QtGui.QLineEdit())
        layout.addRow(QtGui.QLabel("Line 2, long text:"), QtGui.QComboBox())
        layout.addRow(QtGui.QLabel("Line 3:"), QtGui.QSpinBox())
        self.formGroupBox.setLayout(layout)


if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)
    dialog = Dialog()
    sys.exit(dialog.exec_())