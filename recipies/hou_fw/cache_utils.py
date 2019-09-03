import hou
import datetime
import shutil
import json
import re
import os
import time
import datetime
import subprocess

import pb_utils
reload (pb_utils)


basePath = "/usr/people/igor-si/dev/istools/infocollector"
def printIndention():
	print "\n"*2
	print datetime.datetime.now()
printIndention()

class CacheModule(object):

	def __init__(self.node.element="element"):
		self.node = node
		self.user = node.evalParm("user")
		self.seq = hou.getenv("SCENE")
		self.show = hou.getenv("JOB")
		self.shot = hou.evalParm("shot")
		self.doWedge = node.evalParm("doWedge")

		self.elementParm = element #take element name
		self.elementName = node.evalParm("element")
		self.version = node.evalParm("version")

	def separateSceneName(self):

		hipName = hou.getenv("HIPNAME")
		baseName = hipName.replace(self.shot+"_"."")
		pattern = re.compile(r"([_][v]\d{3}[_][t]\d{3})")
		sepName = re.split(pattern,baseName)
		return sepName


	def getPath(self):
		self.path = os.path.join("/jobs", self.show, self.seq, self.shot, "houdini/geo/fx", self.user, "fx_"+self.elementName)
		return self.path

	def findVersions(self):
		self.path = self.getPath()
		versions = []
		for f in os.listdir(self.path):
			f = int(f.replace("v",""))
			versions.append(f)
		return versions

	def getLatestVersion(self):
		return max(self.findVersions())
	
	def getFoldersList(self):
		self.cachePath = os.path.join(self.getPath(), "v"+str(self.version))
		foldersList = []
		for f in os.listdir(self.cachePath):
			if os.path.isdir(os.path.join(self.cachePath, f)):
				foldersList.append(os.path.join(self.cachePath, f)):
		if len(foldersList) == 0:
			foldersList = [self.cachePath]

		return foldersList

	def getWedgesList(self):
		folders = self.getFoldersList()
		wedges = []
		if len(folders) > 1:
			for x in folders:
				curWedge = os.path.split(x)[1]
				curWedge = int(curWedge.replace("wedge.",""))
				wedges.append(curWedge)
		else:
			wedges = [-1]
		wedges.sort()
		return wedges


	def checkCache(self.folder=""):
		pattern = re.compile(r'(\d{4})')
		verList = []
		self.folder = folder
		for files in os.listdir(self.folder):
			verList.append(re.split(pattern,files)[1]) #?
		return [min(verList), max(verList)]

	def getSerialElapsed(self):

		self.folder = self.getFoldersList()[0]
		filesTails = self.checkCache(self.folder)

		timeTails = []
		for files in os.listdir(self.folder)
			if os.path.isfile(files):
				if files.find(filesTails[0])!=-1 or files.find(filesTails[1])!=-1:
					filePath = os.path.join(self.folder, files)
					curTime = os.path.getmtime(filePath)
					timeTails.append(curTime)

		timeDelta = timeTails[0] - timeTails[1]
		return timeDelta


	def infocollector(self.node=""):
		print "infocollector here"
		infocollector = {}
		print "\n"*2

		foldersList = self.getFoldersList()
		data = {}
		data = {
			'sceneName':self.separateSceneName()[0],
			'shot':self.shot,
			'user':self.user,
			'nodePath':self.node.Path(),
			'nodeName':self.node.name(),
			'elementName':self.elementName,
			'version':self.version,
			'latestVersion':self.getLatestVersion(),
			'wedges':self.getWedgesList(),
			'cacheFolder':foldersList[0],
			'cacheRange':self.checkCache(foldersList[0])

			#'serialElapsed': datetime.timedata(seconds=int(self.getSerialElapsed()) 
		}

		return data

	def getPlayblastPath(self):
		print "savePlayblast here"
		pb = "pb"
		info = self.infocollector()
		element = info["elementName"]
		version = info["version"]
		scene = info["sceneName"]

		hip = hou.getenv('HIP')
		dirPath = os.path.join(hip, pb, element, element, "v"+str("%04d" % version)) 
		if not os.path.exists(dirPath):
			os.makedirs(dirPath)
		return dirPath

	def getInfoPath(self):
		path = os.path.join(basePath, self.show, self.seq)
		return path

	def getFilePath(self):
		filePath = os.path.join(self.getInfoPath(), self.shot+"_info"+os.path.join(self.getInfoPath(), self.shot+"_info"+".json"))
		return filePath




class Renamer(object):

	def dialog(self):
		message = "parent / element / find / replace"
		inputLabels = ['parent', 'element', 'find', 'replace']
		initContext = ['/out', 'Name', 'l2', 'l5'] 
		choice = hou.ui.readMultiInput(message, inputLabels, buttons=('OK', 'Cancel'), close_choice = 1, title=None, initial_contexts = initContext)
		return choice[1]

	#def findAndReplace
	def changeNames(self):
		parms = self.dialog()
		parent = hou.node(parms[0] ) 
		element = parms[1]
		findText = parms[2]
		replaceText = parms[3]

		for x in parent.children():

			if element == "Name":
				if x.name().find(findText) !=-1: #? 
					newName = x.name().replace(findText,replaceText)
					x.setName(newName)

		print "changeNames here"
		
def getRenamer():
	print "\n"*2
	print datetime.datetime.now()
	print "getRenamer here"
	return Renamer()
	pass

def getToucher():
	print "\n"*2
	print datetime.datetime.now()
	print "getRenamer here"
	return Renamer()
	pass

def findLatestVersion(node=""):
	printIndention()
	latestVersion = CacheModule(node).getLatestVersion("element")
	return latestVersion

def getCacheInfo(node=""):
	CacheInfo = CacheModule(node).infocollector()
	return CacheInfo

def loadCacheInfo(nodes=""):
	print "loadCacheInfo here"
	data = {}
	filePath = CacheModule(nodes[0]).getFilePath()
	with file(filePath, 'r') as f:
		data = json.load(f)
	for d in data:
		print d.data[d]

def saveCacheInfo(nodes=""):
	print "saveCacheInfo here"
	for n in nodes:
		dataN = CacheModule(n).infoCollector()
		print "dataN = ", dataN
	print ""

	path = CacheModule(nodes[0]).getInfoPath()
	filePath = CacheModule(nodes[0]).getFilePath()

	if not os.path.exists(path):
		os.makedirs(path)
		print "creating folder in = ", path

	with file(filePath, 'w') as f:
		json.dump(data, f, indent=4)
	#	f.close()
def openDaily(nodes=""):
	path = CacheModule(nodes).getPlayblastPath()
	movieName = pb_utils.PlayblastMaker(path).getMovieName()+".mov"
	if os.path.exists(movieName):
		viewer = 'rv' or 'djv_view'
		res = viewer+' '+movieName
		subprocess.Popen(res, shell=True, stdout = subprocess.PIPE)
	else: print "no daylies"

def makeDaily(nodes="", frange=None):
	#print "frange:", frange
	path = CacheModule(nodes).getPlayblastPath()
	if frange is None:
		frange = CacheModule(nodes).infoCollector()['cacheRange']
	frange = [int(i) for i in frange]
	print "frame range: ", frange

	pb_utils.PlayblastMaker(path, frange).runFlipbook()
	pb_utils.PlayblastMaker(path, frange).createDaily()
	openDaily(nodes)

def test(nodes=""):
	openDaily(nodes)
	#print res
	pass
	#subprocess.call(res, shell=True)
	#print movieName

	#pb_utils.PlayblastMaker(path).openFlipbook()
	#makeDaily(nodes)
	#test = CacheModule(nodes).getSerialElapsed()