# Importing everything from hou py plugins
if(__name__=='__main__'):
    import os
    os.environ['PATH']+='/studio/tools/hou/builds/hfs16.0.600/bin'

from PySide2.QtCore import *
from PySide2 import QtCore, QtGui, QtWidgets, QtUiTools, QtUiTools

#class Ui_Frame(object):
class Ui_Frame(QtWidgets.QDialog):
    def __init__(self,parent=None):
        super(Ui_Frame,self).__init__(parent=parent)
        self.setupUi(self)

    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(757, 501)
        #Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        #Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.verticalLayoutWidget = QtWidgets.QWidget(Frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 90, 160, 88))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.listView = QtWidgets.QListView(Frame)
        self.listView.setGeometry(QtCore.QRect(220, 90, 256, 192))
        self.listView.setObjectName("listView")
        self.comboBox = QtWidgets.QComboBox(Frame)
        self.comboBox.setGeometry(QtCore.QRect(50, 190, 161, 36))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("test1")
        self.comboBox.addItem("test2")
        self.comboBox.addItem("test3")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.pushButton.setText(_translate("Frame", "PushButton"))
        self.pushButton_2.setText(_translate("Frame", "PushButton"))
        self.comboBox.setItemText(0, _translate("Frame", "New Item"))
        self.comboBox.setItemText(1, _translate("Frame", "New Item"))
        self.comboBox.setItemText(2, _translate("Frame", "New Item"))


class MyTestClass(QtWidgets.QFrame, Ui_Frame):
    def __init__(self):
        super(MyTestClass, self).__init__()
        self.setupUi(self)


def showManagerWindow():
    import sys
    global mv
    add_path ='/studio/tools/hou/builds/hfs16.0.600/dsolib/Qt_plugins' #add qt path plugins
    QCoreApplication.addLibraryPath(add_path) 
    mv = MyTestClass()
    #window = MyWidget()
    mv.show()
    pass

if(__name__ == "__main__"):
    import sys
    global mv
    add_path ='/studio/tools/hou/builds/hfs16.0.600/dsolib/Qt_plugins' #add qt path plugins
    QCoreApplication.addLibraryPath(add_path) 
    qapp = QtWidgets.QApplication(sys.argv) # Correct way how to use QApplication
    #mv = MyTestClass() # it works
    mv = Ui_Frame( )
    mv.show()
    qapp.exec_() #sys.exit(qapp.exec_())
