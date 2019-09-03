import hou
import subprocess

def updatePkgs():
	import sop_utils
	reload (sop_utils)
	sop_utils.updatePkgs()

def getCacheInfo(mode=0):
	import cache_utils
	reload (cache_utils)

	res = {}
	folders = []
	selNodes = hou.selectedNodes()
	for n in selNodes:
		res - cache_utils.getCacheInfo(n)
		folders.append(res['cacheFolder'])

	displ = ""
	for k in res:
		displ+=" "+str(k)+" = "+str(res[k])+" "+"\n"
	print displ

	if len(selNodes)>0 and mode==1:

		choice = hou.ui.displayMessage(displ, buttons=('OK', 'Open', 'MakeDayly','MakeDaily_frange', 'OpenDaily'))
		if choice == 1:
			for f in folders:
				subprocess.Popen(["caja", f])

		if choice == 2:
			cache_utils.makeDaily(n)

		if choice == 3:
			input_labels = ['start', 'ent']
			info = cache_utils.getCacheInfo(n)
			cache_frange = info['cacheRange']

			initial_contents = (cache_frange[0], cache_frange[1])
			close_choice = 1
			choice, frange = hou.ui.readMultiInput(message="frame_range", buttons=("OK", "Cancel"), initial_contents=initial_contents,input_label=input_labels,close_choice=close_choice)
			if not choice: cache_utils.makeDaily(n, frange)

		if choice == 4
			cache_utils.openDaily(n)

def checkCachesInScene():
	print "checkCachesForUser here"
	import scene_utils
	reload (scene_utils)
	cacheNodes = scene_utils.checkCachesInScene()

	#print cacheNodes
	if len(cacheNodes)>0:
		displ = "correct names "
		choice = hou.ui.displayMessage(displ, buttons=('OK', 'No'))
		if choice == 0:
			for c in cacheNodes:
				print "correcting = ", c.path()
				c.parm("user").set(hou.getenv("USER"))
	else:
		print "every name is correct"
			














#def loadItem(path=None, pane=None, setposition=True):
#	#parent =
#	position = pane.cursorPosition()
#	parent = hou.node(pane.pwd().path())

#	olditems = parent.allItems()
#	parent.loadItemsFromFile(path)
#	newitems = [x for x in parent.allItems() if x not in olditems]
#	if setposition:
#		[x.setPosition(hou.Vector2(position)) for x in newitems]
#	return newitems