
# SOURCE https://wiki.python.org/moin/PyQt/Adding%20auto-completion%20to%20a%20QLineEdit
# import sys
# from PyQt4.QtCore import Qt
# from PyQt4.QtGui import QApplication, QCompleter, QLineEdit, QStringListModel
 
# def get_data(model):
# 	model.setStringList(["completion", "data", "goes", "here"])
 
# if __name__ == "__main__":
# 	app = QApplication(sys.argv)
# 	edit = QLineEdit()
# 	completer = QCompleter()
# 	edit.setCompleter(completer)

# 	model = QStringListModel()
# 	completer.setModel(model)
# 	get_data(model)
 
# 	edit.show()

# sys.exit(app.exec_())



# SRC https://stackoverflow.com/questions/35628257/pyqt-auto-completer-with-qlineedit-multiple-times
# class Completer(QtWidgets.QCompleter):

#     def __init__(self, parent=None):
#         super(Completer, self).__init__(parent)

#         self.setCaseSensitivity(Qt.CaseInsensitive)
#         self.setCompletionMode(QtWidgets.QCompleter.PopupCompletion)
#         self.setWrapAround(False)

#     # Add texts instead of replace
#     def pathFromIndex(self, index):
#         path = QtWidgets.QCompleter.pathFromIndex(self, index)

#         lst = str(self.widget().text()).split(',')

#         if len(lst) > 1:
#             path = '%s, %s' % (','.join(lst[:-1]), path)

#         return path

#     # Add operator to separate between texts
#     def splitPath(self, path):
#         path = str(path.split(',')[-1]).lstrip(' ')
#         return [path]

# ===========================================================
# URL https://gist.github.com/EntityReborn/1101686

from PyQt4.QtCore import QEvent, Qt
from PyQt4.QtGui import QLineEdit

class MyLineEdit(QLineEdit):
	def __init__(self, *args, **kwargs):
		QLineEdit.__init__(self, *args, **kwargs)
		
		self.completions = [] # All available completions
		self.partials = [] # Parsed completions according to partially typed word
		
		self.cursorpos = 0
		self.wordstart = -1 # Start of word where cursor positioned
		self.wordend = -1 # End of word where cursor is positioned
		self.lastindex = -1 # Last used completion of available completions
		
	def addCompletion(self, word):
		if not word in self.completions:
			self.completions.append(word)
			
	def delCompletion(self, word):
		if word in self.completions:
			self.completions.remove(word)
			
	def setCompletions(self, items):
		self.completions = items
		
	def getWords(self):
		text = str(self.text())
		
		if self.lastindex == -1:
			self.cursorpos = self.cursorPosition()
			self.wordstart = text.rfind(" ", 0, self.cursorpos) + 1
		
		pattern = text[self.wordstart:self.cursorpos]
		
		self.partials = [item for item in self.completions if item.lower().startswith(pattern.lower())]
		return self.partials
		
	def applyCompletion(self, text):
		old = str(self.text())
		self.wordend = old.find(" ", self.cursorpos)
		
		if self.wordend == -1:
			self.wordend = len(old)
			
		new = old[:self.wordstart] + text + old[self.wordend:]
		self.setText(new)
		
	def event(self, event):
		if event.type() == QEvent.KeyPress:
			if event.key() == Qt.Key_Tab:
				if not len(self.completions):
					return True
				
				if self.lastindex >= len(self.getWords()) or self.lastindex == -1:
					self.lastindex = 0
					
				# only one item in the completion list
				if len(self.partials) == 1:
					self.applyCompletion(self.partials[0])

				# more than one remaining matches
				else:
					match = self.partials[self.lastindex]
					self.lastindex += 1
					self.applyCompletion(match)
				return True
			else:
				self.lastindex = -1
				
		return QLineEdit.event(self, event)

def main(): 
	import sys
	from PyQt4.QtGui import QLabel, QVBoxLayout, QApplication, QWidget
	
	LIST_DATA = ['a', 'aardvark', 'aardvarks', 'aardwolf',
			 'abacus', 'babel', 'bach', 'cache', 
			 'daggle', 'facet', 'kabob', 'kansas']
			 
	app = QApplication(sys.argv) 
	
	# objects
	w = QWidget() 
	label = QLabel(w)
	text = "Possible completions: \n" + \
		"%s\n" + \
		"Press Tab to autocomplete, multiple times " + \
		"to cycle thru available completions"
	label.setText(text % ", ".join(LIST_DATA))
	lineedit = MyLineEdit(w)
	lineedit.setCompletions(LIST_DATA)

	# layout
	layout = QVBoxLayout()
	layout.addWidget(label)
	layout.addWidget(lineedit)
	w.setLayout(layout)
	
	# go
	w.show() 
	sys.exit(app.exec_()) 
	
if __name__ == "__main__": 
	main()

# To be able to use it in the middle of a sentence, line 48 should be:
# self.setCursorPosition(self.wordstart+len(text))