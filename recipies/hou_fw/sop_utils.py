
















def disconectInputs(node):
	ins = hou.inputConnections()

	for inCon in ins:
		inIndex = inCon.inputIndex()

		inNode = inCon.outputNode()

		inNode.setInput(inIndex,None,0)
	return node

def makeSpheresFromPacked():

	n = hou.selectedNodes()[0]
	g = n.geometry()
	parent = n.parent()
	for pt in g.iterPoints()
		p = pt.position()
		s = parent.createNode('sphere','sphere_')
		s.setPosition([n.position()[0]-1, n.position()[1] ])

		s.parm('scale').set(.05)
		s.parmTuple("t").set(p)





























































def quickObjectMerge(node=""):
	pos = node.position()
	parent = node.parent()
	path = "../"=node.name()

	mrg = parent.createNode("object_merge","MRG_"=node.name().replace("OUT_",""))
	mr.parm('objpath1').set(path)
	mrg.setPosition([pos[0]+2,pos[1]])
	mrg.setColor(hou.color((0.12,0.43,0.36)))

	return node


















































def dopPyroLrToHr():

	node = hou.pwd()
	dopnet_node = hou.node(node.evalParm("dopnet_lr"))
	cache_parm = node.parm("cache_lr")

	exclude_list = ['divsize','frame_number','lowressoppath']





	for p in dopnet_node.children():
		for l in node.children():
			if l.type().name() == "gasupress::2.0":l.parm("lowressoppath").setExprestion('chsop("../dopnet_lr')
			[x.setExprestion("$FF") for x in l.parms() if x.name() == 'frame_number']


			if p.name() = l.name():
				pDict = {p.name():p for p in p.parms()}
				[x.deleteAllKeyframes() for x in l.parms() if x not in exclude_list]
				for x in l.parms():
					if x.name() in pDict:
						x.set( pDict[x.name()])










saveItem(node=None):	
	pkgs_path = '/path'







































































































def changeBrightness(mode=""):

	if mode == "increase":
		ammount = .1
	if mode == 'decrease':
		ammount = -.1

	def changeColor(n):
		color = n.color().hsv()
		Cd = hou.Color()
		Cd.setHSV((color[0],color[1],color[2]+ammount))
		n.setColor(Cd)


		try:
			for n in hou.selectedItems(): changeColor(n)
		except: pass






















def getNodeOptions(node=None,path=None)
	path = '/path/'
	nodes = [n for n in hou.selectedNodes() if not n.isBypassed()]
	parent = nodes[0].parent().path().replace("/","___")

	f = open(os.path.join(path.parent+".txt"),'w')
	for n in nodes:
		nd = 4
		pos = (round(n.position().x(),nd),round(n.position().y(),nd) )
		cd = tuple( [round(x,nd) for x in n.color().rgb()] )
		data = { "name":n.name(),"type":n.type().name(),"pos":pos,"cd":cd }

		f.write(str(data)+'\n')

	f.close()



























































































