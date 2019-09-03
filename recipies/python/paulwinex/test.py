import sys
import os
#path = "/usr/lib/x86_64-linux-gnu/qt5/plugins/platforms" #platforms
#sys.path.append(path)
#os.environ.setdefault('QT_QPA_PLATFORM_PLUGIN_PATH', path)
#os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = path
#os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = os.path.dirname(PySide2.__file__) + '/plugins/platforms'
#QCoreApplication.addLibraryPath(r'/path/to/houdini/bin/Qt_plugins')

#from PySide2 import QtGui,QtWidgets,QtCore
from PySide2 import QtWidgets

#QCoreApplication.addLibraryPath(r'/opt/hfs16.0.600/dsolib/Qt_plugins')
app = QtWidgets.QApplication(sys.argv)
button = QtWidgets.QPushButton()
button.show()
app.exec_()



#print os.getenv("PATH")
#print os.getenv("QT_QPA_PLATFORM_PLUGIN_PATH")
#path = os.path.join(path, '.bin', utils.OS.suffix(), 'python', 'Lib', 'site-packages', 'PyQt5', 'Qt', 'plugins', 'platforms')
#print('Add real path to QT_QPA_PLATFORM_PLUGIN_PATH', path)
#os.environ.setdefault('QT_QPA_PLATFORM_PLUGIN_PATH', path)