import os
import hou
from hutil.Qt import QtWidgets
#print "test"


class SampleWindow(QtWidgets.QWidget): #OtWidgets.QMainWindow
	def __init__(self, element, message, parent=None):
		super(SampleWindow, self).__init__(parent=parent)
		self.element = element


		self.main_layout = QtWidgets.QHBoxLayout(self)
		#for a,b in enumerate(element):
		#print e

		msg = element.evalParm("element")+'has not been cached,'
		self.textMsg = QtWidgets.QLabel(msg)

		self.btn_spool = QtWidgets.QPushButton('spool')
		self.btn_cache = QtWidgets.QPushButton('cache')
		self.btn_cancel = QtWidgets.QPushButton('cancel')

		verticalSpacer = QtWidgets.QSpacerItem(
			40, 40, QtWidgets.QSizePolicy.Minimum, 
			QtWidgets.QSizePolicy.Expanding)

		self.main_layout.addItem(verticalSpacer)
		#self.btn_add.setMaximumHeight(18)
		#self.btn_add.setMaximumWidth(55)
		#self.btn_rm.setMaximumHeight(18)
		#self.btn_rm.setMaximumWidth(55)

			#self.main_layout.addWidget(self.element)

		self.main_layout.addWidget(self.textMsg)
		self.main_layout.addWidget(self.btn_spool)
		self.main_layout.addWidget(self.btn_cache)
		self.main_layout.addWidget(self.btn_cancel)
		self.btn_spool.clicked.connect(lambda:self.onSpool(self.element))
		self.btn_cache.clicked.connect(lambda:self.onCache(self.element))
		self.btn_cancel.clicked.connect(self.onCancel)


	def onSpool(self.var):
		var.parm("enFarm").pressButton()
		self.close()

	def onCache(self.var):
		var.parm("enCache").pressButton()
		self.close()

	def onCancel(self):
		self.close()



class BundleWidget(QtWidgets.QtWidget): #QtWidgets.QMainWindow
	def __init__(self, path, message, parent=None):
		super(BundleWidget, self).__init__(parent=parent)
		self.path = path
		self.message = message
		self.text = QtWidgets.QLabel('message')

		self.main_layout = QtWidgets.QHBoxLayout(self)
		self.btn_spool = QtWidgets.QPushButton('spool')
		self.btn_cache = QtWidgets.QPushButton('cache')
		self.btn_cancel = QtWidgets.QPushButton('cancel')

		#self.btn_add.setMaximumHeight(18)
		#self.btn_add.setMaximumWidth(55)
		#self.btn_rm.setMaximumHeight(18)
		#self.btn_rm.setMaximumWidth(55)

		self.main_layout.addWidget(self.text)
		self.main_layout.addWidget(self.btn_spool)
		self.main_layout.addWidget(self.btn_cache)
		self.main_layout.addWidget(self.btn_cancel)

		
		self.btn_spool.clicked.connect(self.onSpool)
		self.btn_cache.clicked.connect(self.onCache)
		self.btn_cancel.clicked.connect(self.onCancel)

	def onSpool(self):
		#print self
		pass

	def onCache(self):
		#print self
		pass

	def onCancel(self):
		self.close()

	def onCacheButtonPressed(self.message='2message'):
		#print self
		#print self.close()
		#print self.message
		pass

	def test():
		pass


	def onSpoolButtonPressed(self):
		self.vlad = 'spool'
		self.close()

	def onCancelButtonPressed(self):
		self.vlad = 'cancel'
		self.close()

class Control(objects)

	userOrig = '${USER}'
	shotOrig = '${SHOTNAME}'
	userCustom = 'igor-si'
	shotCustom = 'CWS6340'
	n = hou.pwd() #?


	def getAllCacheNodes(self):
		parentPath = hou.pwd().parent().path()
		cacheNodes = []
		for x in hou.node(parentPath).recursiveGlob('*'):
			if x.type().name() == 'dh_h14_bakegeo':
				cacheNodes.append(x)
			return cacheNodes

	def cacheNode(self.mode):
		if mode==0:
			for x in self.getAllCacheNodes():
				x.parm("user").set(self.userOrig)
				x.parm("shot").set(self.shotOrig)
		if mode==1:
			for x in self.getAllCacheNodes():
				x.parm("user").set(self.userCustom)
				x.parm("shot").set(self.shotCustom)

	def replaceCode(self):
		dirname, filename = os.path.split(os.path.abspath(__file__)) #?
		pyCodeFile = os.path.join(dirname,"pyCode.py")
		nowCodeFile = open(pyCodePath, "r")
		newCode = newCodeFile.read()
		newCodeFile.close()
		hou.pwd().parm("pyCode").set(newCode)
		#print newCode



	def spoolRender(self, *args):

		if 0 in args:
			rN = hou.node(self.n.evalParm("volumeRenderNode")) #?
			print 'volumeRenderNode = ', rN
			try:
				rN.parm("release").pressButton()
			except:
				pass
				#rN.parm("enFarm").pressButton()

		#depricated
		if 1 in agrs:
			rN = hou.node(self.n.evalParm("ptsRenderNode"))
			try:
				rN.parm("enFarm").pressButton()
			except:
				rN.parm("release").pressButton()

	def filesInFolder(self.path):
		dirPath = os.path.dirname(path)
		filesList = []
		if os.path.exists(dirPath):
			for f in os.listdir(dirPath):
				index = f.finf('bgeo')
				if index != -1:
					filesList.append(f)
					#print 'f=', f
					#if os.path.isfile(f):
					#	filesList.append(f)
		return filesList


	def check(self):
		checkList = ["cache_shipCollision","cache_shipAdditional"]

		checkList = []
		for c in checkList:
			cC = hou.node(self.n.evalParm(c))
			cPath = cC.evalParm("display_path")
			cFiles = self.filesInFolder(cPath)
			print cFiles
			if len(cFiles)==0:
				cacheList.append(c)	

		#print cacheList
		operList = []
		for c in cacheList:
			#print c
			sC = hou.node(self.n.evalParm(c))
			operList.append(sC)
		#print operList
		global window
		for a,b in enumerate(operList):

			window = SampleWindow(element=b,message='messageList')
			window.setGeomentry(200+a*500,200,100,100)
			window.show()
			pass
		if len(operList)==0:
			hou.ui.displayMessage("everything is ready", buttons = ("OK",))
			pass



		def prepare(self):
			print "test"

		def spoolSim(self):
			self.check()
			rN = hou.node(self.n.evalParm("cache_volumeSim"))
			rN.parm("enFarm").pressButton()
			pass

		def spoolSimNotify(self):
			warnMessage = 'you are in custom sim mode. do you want to' #?
			res = hou.ui.displayMessage(warnMessage, buttons=('Spool')) #?
			#print 'choice = ', res
			return res
			pass


		def spoolGlobal(self,mode=0):
			mode = self.n.evalParm("cache_mode")
			if mode == 0:
				self.spoolRender(0)
				if self.n.evalParm("work_with_particles")==1:
					self.spoolRender(1)

			if mode == 1:
				simChoice = self.spoolSimNotify()
				if simChoice == 0:

					self.spoolSim()
				if simChoice == 1:
					self.spoolRender(0)
				if simChoice == 2:
					print "cancel spooling"
					#submit = hou.node(self.n.evalParm("submit_node"))
					#submit.parm =("submitAll").pressButton()


			print "spoolGlobal here with node = ". mode
			#submit = hou.node(self.n.evalParm("submit_node"))
			#submit.parm =("submitAll").pressButton()



	def test(self):
		#print self.cacheMode()
		#self.replaceCode()
		pass
		#self.getAllCacheNodes()
		#print "Control here"


def getControl():
	return Control()
	#return Control.test()
	#print "bla"
	#return Control()
	pass





#print args[0]
		#for x in hou.node('/out/').children():
		#	if x.type().name()=='mpc_LaunchRender':
		#		print x
			#if x.type().name()=='mpc_LaunchRender':

			#	print x
				#if x.eval.Parm("hscale")==0:
			#res = x.path()
		#mpc_LaunchRender
		#print args
		#print "blabla"




#def patchByNumber(num="latest"):
#	if num!="latest":
#		initTxt = "latest"
#		choice = hou.ui.readInput("choose string to process")
#		sr_patch.patch(choice[1])
#	else:
#		closeMistPatcher.patch("latest")
#	pass

# # Currently the window does not have anything, we need to #?
#		#an empty widget that will contain everything. This #?
#		#creates the widget, but does not assign it.
#		#self.central_widget = QtWidgets.QWidget()
#		#We now create a layout for that widget #?
#
