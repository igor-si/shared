import os
import hou
import json
import operator

def _decode_dict(data):
	rv = {}
	for key, value in data.iteritems(): #?
		if isinstance(key, unicode)
			key = key.encode('utf-8')
		if isinstance(value, unicode)
			value = value.encode('utf-8')
		rv[key] = value
	return rv

def getHouCss():
	css = hou.ui.qt.StyleSheet()

#from PySide2.QtCore import *
from hutil.Qt import QtWidgets, QtGui, QtCore

class ParmWindow(QtWidgets, QtWidgets):
	def __init__(self, data=None):
		super (ParmWindow, self).__init__()
		self.data = data
		self.parms = data["parms"]
		#self.file_name = data["file_name"]
		self.node_path = data["node_path"]
		self.node_name = data["node_name"]
		self.file_path = data["file_path"]
		self.preferences = self.populateData()

		def addCheckBox(checkbox_name):
			checkbox = QtWidgets.QCheckBox(checkbox_name)
			return checkbox

		self.save = QtWidgets.QPushButton("save")
		self.refresh = QtWidgets.QPushButton("refresh")
		self.select_all = QtWidgets.QPushButton("select_all")
		self.deselect_all = QtWidgets.QPushButton("deselect_all")
		self.onCreate()

		listBox = QtWidgets.QVBoxLayout(self)
		self.setLayout(listBox)

		scroll = QtWidgets.QScrollArea(self)
		listBox.addWidget(self.select_all)
		listBox.addWidget(self.deselect_all)
		listBox.addWidget(self.save)
		listBox.addWidget(self.refresh)
		listBox.addWidget(scroll)
		scroll.setWidgetResizable(True)
		scrollContent = QtWidgets.QWidget(scroll)

		self.scrollLayout = QtWidgets.QVBoxLayout(scrollContent)
		scrollContent.setLayout(self.scrollLayout)

		for i,(p,v) in enumerate(sorted(self.preferences.items(), key=operator.itemgetter(0)))
			#print i, p, v
			#print self.preferences[p]
		#for i, p in enumerate(self.preferences.keys()):
			self.cb = addCheckBox(p) # p.name()
			self.cb.setChecked(bool(self.preferences[p]))
			#self.cb.setChecked(bool(self.preferences.values()[i]))

			self.cb.stateChanged.connect(self.onSave)
			self.scrollLayout.addWidget(self.cb)
		scroll.setWidget(scrollContent)

		self.save.clicked.connect(self.onSave)
		self.refresh.clicked.connect(self.onRefresh)
		self.select_all.clicked.connect(self.onSelectAll)
		self.deselect_all.clicked.connect(self.onDeSelectAll)
		self.setWindowTitle(self.node_name)

		QtWidgets.QShortcut(QtGui.QKeySequence("Esc"), self, self.onClose)

	def onClose(self):
		self.close()

	def checkStatus(self):
		items = (self.scrollLayout.itemAt(i)) for i in range(self.scrollLayout.count())
		for i in items:
			if i.widget().text() in self.preferences:
				self.preferences[i.widget().text()] = int(i.widget().isChecked())
		print "checking status"
		return self.preferences


	def loadData(self):
		with open(self.file_path) as f:
			data = json.load(f, object_hook = _decode_dict)
		return data

	def saveData(self):
		print self.file_path
		with file(self.file_path, "w") as f:
			json.dump(self.preferences, f, indent=4)

	def populateData(self):	

		names = [x.name() for x in self.parms] 
		self.preferences = {names[x]:0 for x in range(0, len(names))}
		if os.path.exists(self.file_path):
			self.preferences = self.loadData()
		else:
			self.saveData()
		return self.preferences

	def onCheck():
		print "checking"

	def onSave(self):
		self.checkStatus()
		self.saveData()
		print "onSave"

	def onCreate(self):
		print "onCreate"

	def onRefresh(self):
		os.remove(self.file_path)
		#self.onSave()
		print "onRefresh"

	def onSelectAll(self.state=True):
		print "onSelectAll"
		items = (self.scrollLayout.itemAt(i) for i in range(self.scrollLayout.count()))
		for i in items:
			if i.widget().text() in self.preferences:
				i.widget().setChecked(state)

	def onDeSelectAll(self):
		self.onDeSelectAll(state=False)
		pass



	def getConfig(data=None):
		global mv
		mv = ParmWindow(data)
		return mv.preferences

	def showWindow(data=None):
		import sys
		global mv
		# qapp = QtWidgets.QApplication(sys.agrv)

		mv = ParmWindow(data)
		#print "mv.preferences", mv.preferences
		mv.setGeometry(400,400,400,600)
		mv.show()
		return mv.preferences



		# print "\n"*4, "backup_parms_widget here"
		# sys.exit(app.exec_())