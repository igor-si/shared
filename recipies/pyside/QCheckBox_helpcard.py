# Changes the state of checkbox button
def temp_setChecked():
	setChecked()

# Sets the label associated with the button
def temp_setText():
	setText()

# Retrieves the caption of the button
def temp_text():
	text()


# Checks if the button is selected
def temp_isChecked():
	isChecked()

# Provides no change state to checkbox
def temp_setTriState():
	setTriState()

# URL https://www.tutorialspoint.com/pyqt/pyqt_qcheckbox_widget.htm
# Example
# Here, two QCheckBox objects are added to a horizontal layout.
# Their stateChanged() signal is connected to btnstate() function. 
# The source object of signal is passed to the function using lambda.
def temp_lambda_connect():
	self.b1.stateChanged.connect(lambda:self.btnstate(self.b1))
	self.b2.toggled.connect(lambda:self.btnstate(self.b2))

# The isChecked() function is used to check if the button is 
# checked or not.
def temp_isChecked():
	if b.text() == "Button1":
	   if b.isChecked() == True:
	      print b.text()+" is selected"
	   else:
	      print b.text()+" is deselected"

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class checkdemo(QWidget):
   def __init__(self, parent = None):
      super(checkdemo, self).__init__(parent)
      
      layout = QHBoxLayout()
      self.b1 = QCheckBox("Button1")
      self.b1.setChecked(True)
      self.b1.stateChanged.connect(lambda:self.btnstate(self.b1))
      layout.addWidget(self.b1)
		
      self.b2 = QCheckBox("Button2")
      self.b2.toggled.connect(lambda:self.btnstate(self.b2))

      layout.addWidget(self.b2)
      self.setLayout(layout)
      self.setWindowTitle("checkbox demo")

   def btnstate(self,b):
      if b.text() == "Button1":
         if b.isChecked() == True:
            print b.text()+" is selected"
         else:
            print b.text()+" is deselected"
				
      if b.text() == "Button2":
         if b.isChecked() == True:
            print b.text()+" is selected"
         else:
            print b.text()+" is deselected"
				
def main():

   app = QApplication(sys.argv)
   ex = checkdemo()
   ex.show()
   sys.exit(app.exec_())
	
if __name__ == '__main__':
   main()

# As mentioned earlier, checkBox buttons can be made mutually 
# exclusive by adding them in the QButtonGroup object.
def temp_QButtonGroup():   
	self.bg = QButtonGroup()
	self.bg.addButton(self.b1,1)
	self.bg.addButton(self.b2,2)

# QButtonGroup object provides abstract container for buttons 
# and doesn't have a visual representation. It emits buttonCliked()
# signal and sends Button object's reference to the 
# slot function btngroup().
def temp_connect():
	self.bg.buttonClicked[QAbstractButton].connect(self.btngroup)
# The btngroup() function displays the caption 
# of the clicked checkbox.
def btngroup(self,btn):
   print btn.text()+" is selected"



