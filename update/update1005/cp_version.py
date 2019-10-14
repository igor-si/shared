import hou
import logging
import datetime
import subprocess

logging.basicConfig(
 	format ='[%(asctime)-8s:%(levelname)s]:%(name)s:%(message)s',
 	datefmt='%m%d %H:%M') 
logger = logging.getLogger('copy version')
logger.setLevel(logging.DEBUG)

def copy2clip(txt):
    cmd='echo '+txt.strip()+'|clip'
    return subprocess.check_call(cmd, shell=True)

def copyToString(nodes=None):
	# print "\n"*2
	if not nodes:
		nodes = hou.selectedNodes()
	if not nodes:
		return
		
	parms_checklist = ['ver','element','version','version2']
	res_str_comb = ""
	res_list = []
	parms_dict = {}
	for n in nodes:
		print "node",n
		parms_list = [x for x in n.parms() if x.name() in parms_checklist ]
		parms_dict = {p.name():p.eval() for p in parms_list}
		res_str = ""
		
		if "element" in parms_dict.keys():
			element = parms_dict['element']
			res_str+='element:{}'.format(element)

		if "version" in parms_dict.keys():
			version = parms_dict['version']
			res_str+='|version:{}'.format(version)

		if "version2" in parms_dict.keys():
			version2 = parms_dict['version2']
			res_str+='|version2:{}'.format(version2)


		res_list.append(res_str)
	res_str_comb = ",".join(res_list)

	message = "copy from {}\n".format(nodes[0].parent())
	hou.ui.readInput(message=message,buttons=('ok','cancel'),initial_contents=res_str_comb)
	return res_str_comb


def parser(parse_string=None):
	nodes_div = parse_string.split(",")
	parms_dict = {}
	for i,n in enumerate(nodes_div):
		parms_div = n.split("|")
		parm_dict = {}
		for p in parms_div:
			k,v = p.split(":")
			try:v = int(v)
			except:pass
			if k=="element":
				element = v
			parm_dict.update({k:v})
		element = parm_dict['element']
		del parm_dict['element']
		parms_dict.update({element:parm_dict })
		
	return parms_dict

def pasteToNodes(paste_string=None,pane=None,nodes=None,parent=None):
	# print "pasteToNodes here","\n"*4
	check_list = ['element','version']
	# paste_string = "element:test|version:15|version2:155,element:test2|version:15|version2:55"

 	if not nodes:
		if pane:
			parent =  hou.node(pane.pwd().path() ) # parent for paste node
		else:
			if hou.selectedNodes():
				parent = hou.selectedNodes()[0].parent()
			else:
				return

	(choice,paste_string) = hou.ui.readInput(message="paste to {}".format(parent),
					buttons=('ok','cancel'),initial_contents="",close_choice=1,
					severity=hou.severityType.Message) 
	if choice:
		return

	nodes_subnet = hou.nodeType(hou.sopNodeTypeCategory(), "subnet")
	nodes_subnet = [x for x in nodes_subnet.instances() if x.parent()==parent]
	nodes_fc = []
	for s in nodes_subnet:
		if any(x in check_list for x in [y.name() for y in s.parms()]):
			nodes_fc.append(s)
	
	parsed_dict = parser(parse_string=paste_string)

	for s in nodes_fc:
		for k,v in parsed_dict.items():
			if s.evalParm("element")==k:
				parms = [x for x in s.parms() if x.name() in v]
				for p in parms:
					p.set(v[p.name()])

				logger.info("\nsetting parms for {node} \n{value}\n".format(
					node=s.path(),
					value=v
					))
	return parsed_dict

