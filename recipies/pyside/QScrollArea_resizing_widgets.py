# Importing everything from hou py plugins
if(__name__=='__main__'):
    import os
    os.environ['PATH']+='/studio/tools/hou/builds/hfs16.0.600/bin'
    from PySide2.QtCore import *
    from PySide2 import QtCore, QtGui, QtWidgets, QtUiTools, QtUiTools
else:
    from hutil.Qt import QtWidgets,QtGui,QtCore  


class Example(QtWidgets.QWidget):
    def __init__(self):
        super(Example,self).__init__()

        container = QtWidgets.QWidget()
        list_layout = QtWidgets.QVBoxLayout()
        container.setLayout(list_layout)
        scroll = QtWidgets.QScrollArea()
        scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        scroll.setWidgetResizable(True)
        scroll.setWidget(container)

        for x in range(10):
            product_container = QtWidgets.QFrame()
            product_container .setFixedHeight(50)
            row = QtWidgets.QHBoxLayout(product_container)
            name = QtWidgets.QLabel("test") # y
            cbox = QtWidgets.QCheckBox()
            row.addWidget(name)
            row.addWidget(cbox)
            separator = QtWidgets.QFrame()
            separator.setFrameStyle(QtWidgets.QFrame.HLine | QtWidgets.QFrame.Plain)
            list_layout.addWidget(product_container)
            list_layout.addWidget(separator)
            list_layout.addStretch()

def showExample():
    if(__name__ == "__main__"): # test locally
        import sys
        global w
        add_path ='/studio/tools/hou/builds/hfs16.0.600/dsolib/Qt_plugins' #add qt path plugins
        QCoreApplication.addLibraryPath(add_path) 
        qapp = QtWidgets.QApplication(sys.argv) # Correct way how to use QApplication
        w = Example()
        w.show()
        qapp.exec_()
showExample()