#from PySide.QtGui import *
#from PySide import *
#from PySide2 import QtWidgets,QtGui,QtCore
#from PySide import QtOpenGL
#from hutil.Qt import QtWidgets,QtGui
#from PySide import *

# try:
# 	from PySide2.QtWidgets import *
# 	from PySide2.QtGui import *
# 	from PySide2.QtCore import *
# except:
# 	#from PySide.QtWidgets import *
# 	from PySide.QtCore import *
# 	from PySide.QtGui import *

#from PySide2.QtWidgets import *
#from PySide2.QtGui import *
#from PySide2.QtCore import *
#from PySide2 import *
#from Qt import QtWidgets, QtCore, QtGui
#from Qt import *

from Qt import QtGui,QtCore,QtWidgets

from Qt.QtWidgets import *
from Qt.QtGui import *
from Qt.QtCore import *


app = QtWidgets.QApplication([])
w = QWidget()
l = QHBoxLayout()
w.setLayout(l)
label = QLabel('Text')
l.addWidget(label)
b = QPushButton('OK')
l.addWidget(b)
w.show()
app.exec_()