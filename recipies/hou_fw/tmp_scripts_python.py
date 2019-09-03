node = hou.pwd();sp0=node.parm("spare_input0").eval();spNode=hou.node(sp0);spNode.parm('submitAll').pressButton()


import time
time.sleep(3)

#===sleep example
	for x in hou.node('/obj/').recursiveGlob('*'):
		if x.type().name() == 'dh_h14_bakegeo':
			userName = x.parm("user").eval()
			print "current_user_name", userName
			#x.parm("user").set('${USER}')
			x.parm("user").set(custom_name)












print "\n"*1
import time
import os

node = hou.pwd()
mc = node.parm("maxParts").eval()
msNodePath = node.parm("multilaunch_node").eval():
msNode = hou.node(msNodePath)
part = node.parm("part").eval()
partBup = part
check = node.parm("use_slice_precache").eval()

def checkCachedGeo():
	print "\n"*2
	print "=== checkCachedGeo here"
	ccNodePath = node.parm("keep_cached_part").eval()
	ccNode = hou.node(ccNodePath)
	ccGeo = ccNode.geometry()
	ptsNum = len(ccGeo.points())
	if ptsNum == 0:
		print "geo has not been cached"
	else:
		print "we are already have cached source"
	print "\n"*2
	#print ptsNum
	return ptsNum



def checkCollisionGeo(): 
	print "\n"*2
	print "=== checkCollisionGeo here"
	ccNodePath = node.parm("collision_out").eval()
	ccNode = hou.node(ccNodePath)
	ccGeo = ccNode.geometry()
	ptsNum = len(ccGeo.points())
	if ptsNum == 0:
		print "collision has not been cached"
	else:
		print "we are already have cached source"
	print "\n"*2
	return ptsNum

def cacheCollisionGeo(): 
	ptint "cacheCollisionGeo here"
	scNodePath = node.parm("collision_cache").eval()
	scNode = hou.node(scNodePath)
	try:
		scNode.parm("enCache").pressButton()
		print "cache geo under process"
	except:
		print "cant cache slices"
	print "\n"*2

def checkMantraNodes():
	print "\n"*2
	print "=== checkMantraNodes here"
	def check_node(nodeName=""):
		print "current node = ".nodeName
		ccNodePath = node.parm(nodeName).eval()
		ccNode = hou.node(ccNodePath)
		try:
			fo = ccNode.parm("force object").eval()
			print nodeName,"force object = ", fo
			fmo = ccNpde.parm("matte_objects").eval()
			print nodeName,"matte_objects = ",fmo
			pho = ccNode.parm("forceobject").eval()
			print nodeName,"phantom object = ", pho
			cam = ccNode.parm("camera").eval()
			print nodeName,"cam = ", cam
		except:
			print "cant find mantra node"

	check_node("mantra_vol")
	check_node("mantra_pts")


def cacheSlicesGeo():
	print "\n"*2 
	print "=== cacheSlicesGeo here"


	scNodePath = node.parm("slice_cache").eval()
	scNode = hou.node(scNodePath)
	try:
		scNode.parm("enCache").pressButton()
		print "cache geo under process"
	except:
		print "cant cache slices"
	print "\n"*2 

def correctUserNames():
	import os

	hN = hou.getenv("HIP")
	uN = os.path.basename(hN)
	#print uN
	custom_name = uN
	#custom_name = '${USER}'
	for x in hou.node('/obj/').recursiveGlob('*'):
		if x.type().name() == 'dh_h14_bakegeo':
			userName = x.parm("user").eval()
			print "current_user_name", userName
			x.parm('user').set(custom_name)
			#x.parm('user').set('${USER}')
		try:
			hou.parm("out/L_wallLayeredMist/user").set(custom_name)
		except:
			pass

		try:
			hou.parm("out/L_wallLayeredMist_pts/user").set(custom_name)
		except:
			pass

		try:
			hou.parm("out/L_LaunchRender33/user").set(custom_name)
		except:
			pass




def checkCamera():
	print "checkCamera here"
	autoCamPath = node.parm("autoCamPath")
	wlmCamPath = node.parm("camPath")
	wlmCam = hou.node(wlmCamPath.eval())
	#print wlmCam, autoCamPath
	if wlmCam == None
		print "wlmCam none"
		#wlmCam.set(autoCamPath)
		wlmCamPath.revertToDefaults()
		wlmCamPath.deleteAllKeyframes()
		wlmCamPath.set(autoCamPath)
	outControlCam = hou.node("/out/CONTROL")
	outControlCamPath = outControlCam.parm("camPath")
	outCheck = hou.node(outControlCamPath.eval())
	print outControlCamPath,outCheck
	if outCheck==None:
		outControlCamPath.revertToDefaults()
		outControlCamPath.deleteAllKeyfranes()
		wlmCamPathTmp = 'chs("/obj/L_wallLayeredMist/CONTROL/camPath")'
		outControlCamPath.setExpression(wlmCamPathTmp)









def checkFrustum():
	print "check frustum here"

def scenePreparation():
	print "prepare scene for work"
	checkCamera()
	cG = checkCachedGeo()
	if cG == 0:
		cacheSlicesGeo()
	cC = checkCollisionGeo()
	print cC
	if cC == 0:
		cacheCollisionGeo()
	checkMantraNodes()
	correctUserNames()


def multiSpool():
	checkGeo = checkCachedGeo()
	of checkGeo == 0:
		cacheSlicesGeo()

	#correctUserNames()
	scenePreparation()
	dopNodePath = node.parm("mist_dopnet").eval()
	dopNode = hou.node(dopNodePath)
	ocl = dopNode.parm("opencl").eval()
	print "\n"*2
	print "current OpenCL status is = ", ocl
	print "\n"*2
	oclBup = ocl
	dopNode.parm("opencl").set(0)


	for i in range(mc):
		print i
		try:
			node.parm("part").set(i+1)
			print "current part spooled = ", node.parm("part").eval()
			msNode.parm("submitAll").pressButton()
		except:
			print "pass"
		time.sleep(3)
	node.parm("part").set(partBup)
	dopNode.parm("opencl").set(oclBup)

def release():

	mistNodePath = node.parm("mist_release").eval()
	mistNode = hou.node(mistNodePath)

	combNodePath = node.parm("comb_release").eval()
	combNode = hou.node(combNodePath)

	partBup = node.parm("part").eval()

	for i in range(mc):
		try:
			node.parm("part").set(i+1)
			combNode.parm("release").pressButton()
			print "release_part_", combNode.parm("part").eval()
		except:
			print "cant release part ", i
	node.parm("part").set(parmBup)

def spoolOnlyOneStage(type=0)
	#type = 0
	print "soop"
	mn = node.parm("multilaunch_node")
	bup = mn.eval()
	print "old ml node", bup
	typelist = ["multilaunch_vol_sim", "multilaunch_vol_sim"] #?
	mn.set( node.parm(typeList[type]).eval() )
	print mn.eval()
	mn.set(bup)
	print mn.eval()
	multiSpool()




def test():
	correctUserNames()

def addVersion():
	names = ["ve_list", "ver_pts", "ver_mist_render"] #?
	for s in names:
		print "add_version_to_", s
		cv = node.parm(s).eval()
		node.parm(s).set(cv+1)

#make volume pkg naming convention
n = hou.pwd()
num = (int(n.evalParm("namingConventionColunm3"))+1)
num = '%03d' % num
path = n.evalParm("path") 
suffix = 'OUT_VOL'
res = path+'/'+suffix+"_"+str(num)
return res
#--------------------------------------

#--------------playblast session-------
`pythonexprs("__import__('os').getpid()")`
#--------------------------------------

#--------------color inputs------------
node = hou.node('/obj/geol/subnet1')
indirect_inputs = node.indirectInputs()
input1 = node.indirectInputs()[0]
input1.setColor(hou.Color(1, 0, 0))
#--------------------------------------


#--------------------------------------
import hou
node = hou.node('/obj/geol/subnet3')
template_group = node.parmTemplateGroup()

for label in ('label1', 'label2', 'label3', 'label4'):
	label_template = template_group.find(label)
	template_group.hide(label_template, True)

node.setParmTemplateGroup(template_group)
#--------------------------------------

#---------------set color by color-----
k.setColor(hou.Color(k.evalParmTuple("color")))
#--------------------------------------

#----------------save nodes------------
import hou
import os
n = hou.selectedNodes()
path = os.path.join(hou.getenv("HIP"), "isutils/1.py")
path2 = os.path.join(hou.getenv("HIP"), "isutils/2.py")
#n[0].parent().saveItemsToFile(n, (), path)
n[0].parent().saveItemsToFile(n, path2, False)

#print n[0].parent()
#hou.saveItemsToFile(n, path, False)
print path
#--------------------------------------

#-----------------mpc menu scripts-----
#stream
from mpc.houdini.houdiniAssets.parmUtils import makeParameterMenu
types = hou.pwd().findStreamNames()
return makeParameterMenu(types)

# element names
from mpc.houdini.houdiniAssets.parmUtils import makeParameterMenu
types = hou.pwd().findElementNames()
return makeParameterMenu(types)

# type
from mpc.houdini.houdiniAssets.parmUtils import makeParameterMenu
types = hou.pwd().findTypeNames()
return makeParameterMenu(types)
#--------------------------------------

#-----------------print names----------


#--------------------------------------
#-----------------iterate over pts-----
n = hou.selectedNodes()[0]
g = n.geometry()
for pr in g.iterPrims():
	k = pr.attribValue("name")
#--------------------------------------


#------set sphere from packed set------
def spheresFromPacked():
	import hou
	n = hou.selectedNodes()[0]
	g = n.geometry()
	parent = n.parent()
	for pt in g.iterPoint():
		p = pt.position()
		s = parent.createNode('sphere', "sphere_")
		s.setPosition([n.position()[0]-1,n.position()[1]])

		s.parm("scale").set(0.05)
		s.parmTuple("t").set(p)
#--------------------------------------





#--------keep highest two elements-----
print hou.frame()
node = hou.pwd()
geo = node.geometry()
gep.addAttrib(hou.attribType.Point, "keep", 0)

dist = geo.pointFloatAttribValues("dist")
vals = list(dist)
valsM = sorted(vals, reverse=True)
valsS = valsM[:2]
for pt in geo.iterPoint():
	curDist = pt.attribValue("dist")
	if curDist in valsS:
		pt.setAttribValue("keep", 1)
		print curDist
#--------------------------------------





#--read element from spare input cache--
import os
pN = hou.pwd()
pG = pN.geometry()
cnode = pN.parm("spare_input1").eval()
element = hou.node(cnode).parm("element").eval()
return element
#--------------------------------------




#----------multisubmit line------------
n = hou.pwd()
path = n.evalParm("path")
cache = hou.node("path")
element = cache.evalParm("element")
version = cache.evalParm("version")
res = n.name()+"_"+str(element)+"_sv"+str(version)
return res
#--------------------------------------



#-----------replace element------------
for x in hou.node('/obj/sim_debris/').recursiveGlob('*'):
	if x.type().name() == 'dh_h14_bakegeo':
		element = x.evalParm("element")
		print element
		elementNew = element.replace("l4", "l7").replace("l4", "l7") #?
		if(elementNew[:2]!="l7"):
			elementNew = "l7"+elementNew

		x.parm("element").set(elementNew)
		#print elementNew
#--------------------------------------

#-----------replace name---------------
import hou
#for x in hou.node('/out/').recursiveGlob('*'):
for x in hou.selectedNodes():
	if x.type().name() in ['ifd', "mpc_LaunchRender"]:
		name = x.name()
		name = name.replace("m_", "m_l7_")
		name = name.replace("mpc_", "mpc_l7")
		x.setName(name)
		#print name
#--------------------------------------




path = "/usr/people/igor-si/dev/istools"
import sys
import hou
sys.path.append(path)

import cache_utils
reload (cache_utils)
for n in hou.selectedNodes():
	res = cache_utils.getCacheInfo(n)

displ = ""
for k in res:
	#print k, res[k]
	displ+=" "+str(k)+" = "+str(res[k])+" "+"\n"
	#print displ
print displ
hou.ui.displayMessage(displ, buttons=('OK',))
#print res


driver = hou.node('/obj/ANIMATION_CONTROLLER')
parms = [x for x in driver.parms() if x.name().startswith("impactframe")]
frames = [x.eval() for x in parms]
return not any ([hou.frame() >= x for x in frames])
#--------------------------------------

#------------check for errors----------
node = hou.pwd()
inputs = node.parent().inputs()
if not inputs:
	raise RuntimeError('%s does not have any inputs' % node.parent()) #?

render_obj = inputs[0].node("render")
return render_obj.renderNode().path()
#--------------------------------------


exec(hou.shelves.tools()['makeflipbooks'].script())

n_parm = [x for x in n.parm() if re.findall('SubmitNode', x.name())]






def connect():
	print '\n'*2
	import hou
	n = hou.pwd()
	path = hou.node(n.parent().evalParm('spare_input0'))
		path = '../'+n.parent()evalParm('spare_input0')
		doplr = hou.node(path) 
		print doplr, doplr.name(), n.name()
		lr_node = [x for x in doplr.children() if x.name() == n.name()][0]

	parms = lr.node.parms()
	pDict = {p.name():p for p in parms}


	for p in n.parms():
		if p.name() in pDict:
			p.deleteAllKeyframes()
			p.set(pDict[p.name()])
#--------------------------------------

#--add detail attrib that is inputs version--
node = hou.pwd()
geo = node.geometry()
inputs = node.inputs()
version = inputs[0].evalParm('version')
element = inputs[0].evalParm('element')

geo.addAttrib(hou.attribType.Global, 'version', version)
geo.setGlobalAttribValue('version', version)

geo.addAttrib(hou.attribType.Global, 'element', element)
geo.setGlobalAttribValue('element', element)
#--------------------------------------

#--version from input detail attrib----
n = hou.pwd()
in_node = n.inputs()[0]
parm = [x for x in in_node.parms() if x.name() == "version"]
if len(parm)>0: return parm[0].eval()
else: return n.geometry().attribValue('version')
#--------------------------------------


#--mpc mantra name from detail attribs--
import re
n = hou.pwd()
pattern = r'(out_path*)'
paths = [x.eval() for x in n.parms() if bool(re.match(pattern, ))] #?
nodex = [hou.node(x) for x in paths if x is not None]
attribs = ["".join([str(x.geometry().attribValue("element")),str(x.geometry().attribValue('version')) ]) for x in nodes]  
attribs_str = "%s__%s" % (n.name(), ":".join(attribs))
return attribs_str
#print attribs_str
#--------------------------------------



import re
n = hou.pwd()
pattern = r'(out_path*)' 
pattern2 = r'(enable_path*)'
paths = [ [x.eval().re.sub("out_path","",x.name()) ] for x in n.parms() if bool(re.match(pattern,x.name() ) )  ] 
print paths

# enable =[x.eval() for x in n.parms() if bool(re.match(pattern,x.name())) ]
# nodes = [hou.node(x) for x in paths if x is not None]
# attribs = [''.join([str(x.evalParm('element')),str(x.evalParm('version')) ]) for x in nodes]
#attribs_str = '%s__%s' % ('m', ':'.join(attribs))
#return attribs_str
#print attribs_str

import re
print '\n'*2
n = hou.pwd()
pattern = r'(out_path*)' 
pattern2 = r'(enable_path*)'
paths = [[x.eval(), re.sub('out_path', '', x.name())] for x in ] #? 
enable = [x.eval() for x in n.parms() if bool(re.match(pattern2,x.name()))]

nodes = [hou.node(x[0])for x in paths if x[0] in s not None and enable[int(x[1])-1 ]]
attribs = [':'.join([x.evalParm('element'), str(x.evalParm())])] #?
attribs_str = "%s__%s" % ('m',":".join(attribs))
return attribs_str
#--------------------------------------

#----dh multilaunch name from nodes----
import hou
import re
import os
n = hou.pwd()
n_parm = [os.path.basename( x.eval() ).replace("dh_",'') for x in hou.pwd().parms() if re.findall("SubmitNode",x.name()) ]
return 'v'+str(n.evalParm('version'))+'_'+":".join(n_parm)

n = hou.pwd();exec(n.evalParm("code"));code(kwargs["parm"])
#--------------------------------------
node = hou.pwd()
geo = node.geometry()
values = geo.primStringAttribValues("pathGeo")
sorted = []
[sorted.append(x) for x in values if x not in values]
#--------------------------------------

#-------------clean out----------------
nodes = [x.destroy() for x in hou.node('/obj/out/').recursiveGlob('*') if x.type().name() in ['LaunchRender',"ifd"]]
#--------------------------------------


#----------number on inputs------------
n = hou.pwd()
node = hou.node(n.evalParm("spare_input0"))
return len(node.inputConnections())
#--------------------------------------
return "part{}:v{}__{}".format(n.evalParm("part"), n.evalParm("version"), n.name()) #?



#-----list of unique attrib values-----
node = hou.pwd()
geo = node.geometry()
values = geo.pointIntAttribValues("objid")
sorted = list(set(values))
new_attribs = geo.addArrayAttrib(hou.attribType.Point, "objid_array", hou.attribData.Int)
for pt in geo.iterPoints():
	pt.setAttribValue("objid_array", sorted)
#--------------------------------------


#--------------random------------------
import re
import random
print "\n"*4
node = hou.pwd()
geo = node.geometry()

point = geo.iterPoints()[0]
values = list(point.stringListAttribValue("mpkg_array"))

print "\n"*2

weight_predict = {"mudClod":90,
				"plant":5
		}

weight_dict = {}
for v in values:
	for key, value in weight_predict.iteritems():
		if v.find(key)!=-1:
			weight_dict[v] = value


for k, v in weight_dict.iteritems():
#	print k, v
	pass
items_list = [ x*y for x,y in weight_dict.iteritems() ]
for i in items_list:
	print i
#--------------------------------------

#--------------------------------------
mpcpython /usr/people/igor-si/dev/third_party/error_tasks_ #?

user = 'user={0}'.format(os.environ["USER"])
n=hou.pwd();exec(n.evalParm('codeMain'));linkVersion(kwargs['parm'])
#--------------------------------------

#------DOP find object id by name------
n=hou.pwd()
sim = hou.node("../../").simulation()
s_obj = sim.findAllObjects("*")
check_name = n.evalParm('by_objname')
s_id = [x.objid() for x in s_obj if s.name() == check_name][0]
return s_id
#--------------------------------------

#-------active in certain frames-------
val = 0 
node = hou.pwd()
expl_frame = node.parent().evalParm("expl_frame")
sim_frames
sim_frames
if hou.frame() in sim_chv("add_vec")frames:val=1
return val
#--------------------------------------

#------------remove frames-------------
val = 0
node = hou.pwd()
exc_fr = node.evalParm("exclude_frames").split()
fr = hou.frame()
count_fr = [int(x) for x in exc_fr if int(x)<=fr]
count = len(count_fr)
val = fr+count
return val
#--------------------------------------


#--------------------------------------
import hou

def test():
	print "test here"
#	try:
#		for x in hou.selectedItems():
#			print x
#	except: pass
test()


def addCallback():
	hou.ui.addEventLoopCallback(hou.session.test)
	hou.ui.removeEventLoopCallback(hou.session.test)
#addCallback




n = hou.pwd()
divsize = n.evalParm("divsize")
val = 1
if divsize<=0.038:val=2
if divsize<=0.028:val=4
if divsize<=0.016:val=6
if divsize<=0.008:val=8
return val



==============salvadors create ch
import traceback
import hou

node = hou.pwd()

parent = node.parent()
kwargs = {}
for parm in parent.parms():
	if not parm.name().startswith('toggle_'):
		continue

	is_enabled = parm.eval() == 1
	if not is_enabled:
		continue

	parm_name = parm.name().replace('toggle_','')
	value_parm = parent.parm(parm_name).eval()
	kwargs[parm_name] = value_parm

kwargs['silent'] = parent.parm('silent').eval()

try:
	parent.hdaModule().createConvexHullForGeo(node.geometry(), ** kwargs)
except Exception:
	traceback.print_exc()
	raise