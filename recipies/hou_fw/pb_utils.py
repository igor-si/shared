import os
import subprocess
import shutil
import time
import datetime
#?
#?


class PlayblastMaker(object):

	def __init__(self,outPath="",frange=[1000,1000]):

		self.outPath = outPath #+'/cam1.$F4.jpg'
		self.frange = frange
		self.scene = toolutils.sceneViewer()
		self.viewport = self.scene.curViewport()

		self.cameraRes = [1920,1080]
		self.cameraName = 'no_cam'
		if self.viewport.camera():
			self.cameraName = self.viewport.camera().name()
			self.cameraRes = self.viewport.camera().parmTuple('resx', 'resy') #?
			self.cameraRes = [self.cameraRes[0], self.cameraRes[1]]

	def getBaseName(self):
		return os.path.join(self.outPath, self.cameraName)

	def getMovieName(self):
		outName = os.path.split(self.outPath)
		return outName[0]+"_"+outName[1]

	def getCameraSettings(self):
		pass

	def runFlipbook(self):

		flipbook_options = self.scene.flipbookSettings()
		path = self.outPath
		flipbook_options.output('ip')
		if path!="":
			path = os.path.join(path, self.cameraName+'.$F4.jpg')
			flipbook_options.output(path)

		print "playblast in frame range :", (self.frange[0], self.frange[1]) #?
		flipbook_options.frameRange((self.frange[0], self.frange[1])) #?
		flipbook_options.overrideLUT(False)
		flipbook_options.overrideGamma(True)
		flipbook_options.gamma(1.0)
		flipbook_options.cropOutMaskOverlay(True)
		flipbook_options.useResolution(0)
		flipbook_options.outputToMPlay(False)

		#flipbook_options.resolution([2164,1392]) 	1079 899
		#flipbook_options.resolution([1920,1080])
		#flipbook_options.resolution([1079,899])

		#run flipbook
		self.scene.flipbook(self.scene.curViewport(), flipbook_options) #?

	def createDaily(self):
		print 'createDaily'
		baseName = self.getBaseName()
		movieName = self.getMovieName()+'.mov'

		if os.path.exists(movieName):
			print "exists", movieName
			movieTime = os.path.getmtime(movieName)
			movieTime = datetime.datetime.fromtimestamp(movieTime) #?
			#print movieTime
			moveFilePath = os.path.split(movieName)[0]

			moveFileName = "_"+str(movieTime)+"_"+os.path.split() #?
			moveFile = os.path.join(moveFilePath, moveFileName)

			shutil.move(movieName, moveFile)

		res = 'ffmpeg -start_number '+str(self.frange[0])+'  -i '  #?
		print res
		subprocess.call(res, shell=True)







#outFile = "/mpc/vanh-jobs/ahb/FMK/FMK6275/houdini/hip/igor-si/pb/C   " #?
#flipbook_options.setPromptMessage(message, message_type=promptMessage) #?
#'pythonexprs("__import__('os').getpid()")'
