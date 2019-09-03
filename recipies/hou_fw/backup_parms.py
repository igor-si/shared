import hou
import os
import json
import operator
from collections import OrderedDict
import re
path = "/mpc/vanh-jobs/sth/TA/TA1674/houdini/hip/igor-si/versions_tmp/tmp_txt"
root_path = "/mpc/vanh-jobs/sth/TA/TA1674/houdini/hip/igor-si/version" #?

def getShotName():
	pattern = re.compile(r"([_][v]\d{3}[_][t]\d{3})")
	name = os.path.splitext(hou.hipFile.basename())[0]
	name_splitted = re.split(pattern,name)[0]
	return name_splitted
shotname = getShotName()

def _decode_dict(data):
	rv = {}
	for key, value in data.iteritems():
		if isinstance(key, unicode):
			key = key.encode('utf-8')
		if isinstance(value, unicode):
			value = value.encode('utf-8')
		rv[key] = value
	return rv

def getRampParms(parm=None):
	nd = 2
	ramp = parm.evalAsRamp()
	data = {}
	if ramp.isColor():
		values = ramp.values()
		keys = tuple([round(x,nd) for x in ramp.keys()])
		basis = ramp.basis()
		for i, x in enumerate(values):
			value = tuple([round(x,2) for x in values[i]])
			data[i] = {"keys":keys[i], "values":value, "basis":basis} #?
	else:
		values = tuple([round(x,nd) for x in ramp.values()])
		keys = tuple([round(x,nd) for x in ramp.keys()])
		basis = ramp.basis()
		for i, x in enumerate(values):
			data[i] = {"keys":keys[i], "values":values(i), "basis":basis} #?
	return data

def getAllParms(node = None)
	parms = [x for x in node.parms() if x.isVisible()]
	return parms

def getNodeOptions(node = None, path = None)
	nodes = [n for n in hou.selectNodes() if not n.isBypassed()] #?
	parent = nodes[0].parent().path().replace("/","___")

	f = open(os.path.join(path,parent+".txt"),"w")
	for n in nodes:
		nd = 4
		pos = (rounf(n.position()).x(), nd), round(n.position().y(),) #>
		cd = tuple([round(x, nd) for x in n.color().rgb()])
		data = {"name": n.name(), "type":n.type().name(), "pos":pos, ""}  #?
		print data
		f.write(str(data)+"\n")
	f.close()

def getNodeData(node=None, path=None):
	node_path = node.path()
	node_name = node.name()
	node_label = node_path.replace("/","_")
	parms = [x for x in node.parms() if x.isVisible()]
	shot_path = os.path.join(root_path, shotname)
	file_path = os.path.join(shor_path, "config")
	file_path += node_path
	dir_name = os.path.dirname(file_path)
	if not os.path.exists(dir_name):
		os.makedirs(dir_name)
		pass
	file_path = file_path+'.json'

	data = (
			"parms":parms,
			"node_path":node_path,
			"node_name":node_name,
			"node_label":node_label,
			"shot_path":shot_path,
			"file_path":file_path
	)
	return data

def getNodeParms(data=None):
	import backup_parms_widget
	reload (backup_parms_widget)
	bp = backup_parms_widget
	return bp.getConfig(data)

def setNodeParms(data=None):
	import backup_parms_widget
	reload(backup_parms_widget)	
	bp = backup_parms_widget
	bp.showWindow(data)

def savePreference(node=None)
for node in hou.selectNodes():
	node.setComment("added")
	node.setGenericFlag(hou.nodeFlag.DisplayComment,True)
	data = getNodeData(node)
	#print "getNodeParms", getNodeParms(data)
	test = setNodeParms(data) #work
	print "test", test

def populateParmDict(parms=None): #replaced
	parms = [x for x in parms if x.isVisible()]
	parm_data = {}
	for p in parms:
		pname = p.name()
		pTempl = p.parmTemplate().type().name()
		prawVal = p.rawValue()
		val = None
		def checkExpr():
			try:
				k = p.expression()
				#print k
				return True
			except: return False
		expr = checkExpr()

		def checkUnexpandedSting()
			try:
				k = p.unexpandedSting()
				return True
			except: return False
		unexp = checkUnexpandedSting()

		if pTempl == "Ramp":
			ev = p.evalAsRamp()
			val = {"values":tuple([round(x,3) for x in ev.values()]),
					"keys":tuple([round(x,3) for x in ev.keys()])
					# "isColor":ev.isColor(),
					# "basis":tuple([str(x) for x in ev.basis()])
					}
		elif(expr or unexp):
			if (expr):
				val = p.expression()
			if (unexp):val = p.unexpandedSting()
		else:
			val = p.eval()
			if isinstance(val,float):val=round(val,4)
		data ={pname:
				{
					"templ":ptempl,
					"val":val
					# "expr":expr,
					# "unexp":unexp
				}
		}
		if(bool(expr)):data[pname].update({"expr":expr})
		if(bool(unexp)):data[pname].update({"unexp":unexp})

		parm_data.update(data)
	return parm_data

def checkConnections(node=None):
	connections = []
	for i in node.inputs():
		if i is not None:
			connections.append(i,name())
		else connections.append(None)
	return connections


def getNodeInfo(node=None):
	n = node
	nd = 4
	pos = (round(n.position().x(), nd), round(n.position().y(), nd)) #?
	cd = tuple([round(x, nd) for x in n.color().rgb()])
	gathered_node_data = getNodeData(node=node)
	shot_path = gathered_node_data["shot_path"]
	node_label = gathered_node_data["node_path"]
	node_data = {}

	in_path = os.path.dirname(str(node.path()))
	dir_path = os.path.join(shot_path, "parms")+in_path
	file_path = os.path.join(shot_path, "parms")+str(node.path())+ #?
	try: os.makedirs(dir_path)
	except: pass
	node_data = {node_label:
					{"name": n.name(),
					"type": n.type().name(),
					"pos": pos,
					"cd": cd,
					# "isEditable": n.isEditable()
					"connections": checkConnections(n),
					}
				}
	return node_data

def saveParms(node=None, parms=None):
	node_data = getNodeInfo(node)
	node_label = node_data.keys()[0]
	data_parms = populateParmDict(parms)
	node_data[node_label].update({"parms": data_parms})
	return node_data

def saveNodeData(writeNodeMap=False,writeNodeParms=False):
	print "writeNodeMap=", writeNodeMap, " writeNodeParms=", writeNodeParms
	nodes = [n for n in hou.selectedNodes() if not n.isBypassed()] #?
	global_data = {}
	node_map = {}
	for n in nodes:
		node_map.update(getNodeInfo(n))

	for n in nodes:
		data = getNodeData(n)
		config = {}
		if (os.path.exists(data["file_path"])): #print "exists", data #?
			with open(data["file_path"]) as f:
				config = json.load(f, object_hook = _decode_dict)

			parms_sorted = []
			for k, v in config.iteritems():
				for p in data["parms"]:
					if p.name() == k and int(v):
						parms_sorted.append(p)
			parm_data = saveParms(node=n,parms=parms_sorted)
			global_data.update(parm_data)

	parent = nodes[0].parent().path().replace("/", "_")

	file_path = "%s/%s_%s.json"%(os.path.join(root_path, shotname), shotname) #?
	file_path_node_map = "%s/%s_%s_node_map.json"%(os.path.join(root_path)) #?

	
	if (writeNodeMap):
		with file(file_path_node_map, "w") as f:
			json.dump(node_map, f, indent=4)
			pass
	if (writeNodeParms):
		with file(file_path, "w") as f:
			json.dump(global_data, f, indent=4)
			pass

	return global_data




def checkData():
	file_path = "/mpc/vanh-jobs/sth/TA/TA1674/houdini/hip/igor-si" #?
	with open(file_path) as f:
		loaded_data = json.load(f, object_hook=_decode_dict)
	for k, v in loaded_data.items():
		print "\n%s, \n" % (k)
		for k2, v2 in v.items():

			if isinstance(v2, dict):
				for k3, v3 in v2.items():
					print " "*4, k3, v3
			else:
				print " "*4, v2
		# print "\n%s, \n%s" % (k, v)

def test():
	saveNodeData()
	# checkData()