import sys
items = [1,2,4,5,6,"balalaika",2,456,7,77,88,6]

# Importing everything from hou py plugins
if(__name__=='__main__'):
	import os
	os.environ['PATH']+='/studio/tools/hou/builds/hfs16.0.600/bin'
	from PySide2.QtCore import *
	from PySide2 import QtCore, QtGui, QtWidgets, QtUiTools, QtUiTools
else:
	from hutil.Qt import QtWidgets,QtGui,QtCore  

class Example(QtWidgets.QWidget):
	def __init__(self,parms=None):
		super(Example,self).__init__()
		self.parms = parms

		def addCheckBox(checkbox_name):
			checkbox = QtWidgets.QCheckBox(checkbox_name)
			return checkbox

		listBox = QtWidgets.QVBoxLayout(self)
		self.setLayout(listBox)

		scroll = QtWidgets.QScrollArea(self)
		listBox.addWidget(scroll)
		scroll.setWidgetResizable(True)
		scrollContent = QtWidgets.QWidget(scroll)

		scrollLayout = QtWidgets.QVBoxLayout(scrollContent)
		scrollContent.setLayout(scrollLayout)
		for parm in parms:
			cb = addCheckBox(str(parm) )
			scrollLayout.addWidget(cb)
		scroll.setWidget(scrollContent)

def showExample():
	if(__name__ == "__main__"): # test locally
		import sys
		global w
		add_path ='/studio/tools/hou/builds/hfs16.0.600/dsolib/Qt_plugins' #add qt path plugins
		QCoreApplication.addLibraryPath(add_path) 
		qapp = QtWidgets.QApplication(sys.argv) # Correct way how to use QApplication
		w = Example(items)
		w.show()
		qapp.exec_()
showExample()

#==================how scroll area works
# from PySide.QtGui import *
# app = QApplication([])

# scroll = QScrollArea()
# scroll.setWidgetResizable(True) # CRITICAL

# inner = QFrame(scroll)
# # inner = (scroll)

# inner.setLayout(QVBoxLayout())

# scroll.setWidget(inner) # CRITICAL

# for i in range(40):
#     b = QPushButton(inner)
#     b.setText(str(i))
#     inner.layout().addWidget(b)

# scroll.show()
# app.exec_()
#----------------------------------------

class Example(QtWidgets.QWidget):

    def __init__(self):
        super(Example,self).__init__()

        layout = QtWidgets.QVBoxLayout()

        # lbl_arr = QtWidgets.makeArrayOfLabelsHTML()
        lbl_arr = [2,4,6]

        for i in range(1,8):
            qb = lbl_arr[i]
            layout.addWidget(qb)

        layout.setAlignment(Qt.AlignTop)

        scroll = QScrollArea()
        scroll.setWidget(self)
        scroll.setWidgetResizable(True)
        scroll.setFixedHeight(400)
        layout.addWidget(scroll)

        # set layout after adding scroll bar 
        self.setLayout(layout)

        self.setGeometry(0, 0, 600, 220)
        self.setWindowTitle('SnP watchlist')

        self.show()


def showExample():
	if __name__ == '__main__':
		import sys
		global w
		add_path ='/studio/tools/hou/builds/hfs16.0.600/dsolib/Qt_plugins' #add qt path plugins
		QCoreApplication.addLibraryPath(add_path) 
		app = QtWidgets.QApplication(sys.argv)
		# print(QDesktopWidget().availableGeometry())
		ex = Example()
		ex.show()
		qapp.exec_()

		# sys.exit(app.exec_()
# showExample()