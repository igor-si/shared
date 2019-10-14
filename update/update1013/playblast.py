import os
import subprocess
import shutil
import time
import datetime
import hou
import toolutils



def populateData(node=None,path=None):
	# print "\n"*20
	data = {"element":"temp",
			"version":0,
			"version2":0,
			"f1":1000,
			"f2":1000}

	scene = toolutils.sceneViewer()
	viewport = scene.curViewport()
	camera_name = 'persp'
	camera_res = [1920,1080]
	frange = [1000,1000]

	if viewport.camera():
		camera_name = viewport.camera().name()
		camera_res = viewport.camera().parmTuple('res').eval() 

	if not path:
		path = os.path.dirname(hou.hipFile.path() )

	def updateFromParm(node,data,parm_name):
		if node:
			parms = node.parms()	
			if parm_name in [x.name() for x in parms]:
				data[parm_name] = node.evalParm(parm_name)	

	check_list = ["element","version","version2","f1","f2"]
	[updateFromParm(node,data,x) for x in check_list]

	path_dir = "{root}/playblast/{element}/{version}".format(
		root=path,
		element=data['element'],
		version=str(data['version']).zfill(4)
		)

	if not os.path.exists(path_dir):
		os.makedirs(path_dir)

	path_img = os.path.join(path_dir,camera_name+'.$F4.jpg')

	data["scene"] = scene
	data["viewport"] = viewport
	data["camera_name"] = camera_name
	data["camera_resx"] = camera_res[0]
	data["camera_resy"] = camera_res[1]
	data['path'] = path_img
	data['cropOutMaskOverlay'] = 1
	data['outputToMPlay'] = 0
	
	return data

def createDaily(data=None):
	# print "createDaily"
	path = data['path']
	base_name = os.path.dirname(data['path'])
	base_name = os.path.join(base_name,data['camera_name'])

	path_dir,version = os.path.split(os.path.dirname(base_name))
	timestamp = datetime.datetime.now().strftime("%H%M%S")   #strftime("%m%d%H%M%S") 
	movie_name = "{element}_{version}{timestamp}.mov".format(
		element=data['element'],
		version=version,
		timestamp=""
		)
	movie_name = os.path.join(path_dir,movie_name)
	if os.path.exists(movie_name):
		_dir,_name = os.path.split(movie_name)
		backup_dir = os.path.join(_dir,'backup')
		if not os.path.exists(backup_dir):
			os.makedirs(backup_dir)
			print "creating dir %s ",backup_dir

		move_path = os.path.join(backup_dir,timestamp+"_"+_name)
		shutil.move(movie_name,move_path )


	res = 'ffmpeg -start_number {start_number} -i \
	{base_name}.%04d.jpg -vcodec mpeg4 -b 15000k {movie_name}'.format(
		start_number = data['f1'],
		base_name=base_name,
		movie_name=movie_name
		)

	print "output : \n",res
	subprocess.call(res, shell=True)
	return movie_name

def getUI(data=None):
	input_labels = ["f1","f2","element","camera_name",
	"camera_resx","camera_resy","path"]
	initial_contents = [str(data[x]) for x in input_labels]

	choice,input_list = hou.ui.readMultiInput(
						message = 'inputs',
						input_labels=input_labels,
						buttons=('ok','cancel'),
						initial_contents = initial_contents,
						close_choice=1 )

	input_data = dict(zip(input_labels, input_list))
	if choice:
		return data

	
	for k,v in input_data.items():
		if k in data.keys():
			data[k] = v
	return data

def createFlipbook(data=None):
	scene = data['scene']

	fbo = scene.flipbookSettings() # flipbook_options
	
	fbo.output(data['path'])
	fbo.frameRange((float(data['f1']),float(data['f2']))) #?
	fbo.overrideLUT(False)
	fbo.overrideGamma(True)
	fbo.gamma(1.0)
	fbo.cropOutMaskOverlay(True)
	fbo.useResolution(0)
	fbo.outputToMPlay(False)

	#run flipbook
	scene.flipbook(scene.curViewport(),fbo)

def openVideo(player='vlc',path=None):
	try:
		res = "{} {}".format(player,path) 
		print "res",res
		subprocess.call(res, shell=True)
	except:
		print 'cannot use {}'.format(player)
	return path

def simplePlayblast():
	node = hou.selectedNodes() or None
	if node:
		node=node[0]
	data = populateData(node=node)
	data = getUI(data)
	createFlipbook(data=data)

	movie_path = createDaily(data=data)
	openVideo(path=movie_path)


