===============basic=============


===Get selected nodes
hou.selectedNodes()

===list generator for selected nodes "n"
[n.path() for n in sel] #list generator
------------------------------------------------

===Get all upstream nodes
n = hou.node('/obj/grid1/null1')
n.inputAncestors()
------------------------------------------------

===To filter that down to 
#all ancestor nodes that are alembic nodes, for example:
[ x for x in n.inputAncestors() if 'alembic' in x.type().name() ]
------------------------------------------------

===Write out mmb error text to file
#Handy!
open('/tmp/error.txt','w').write(hou.node('/path/to/node').errors())

===Get parent vs get input
#Parent in houdini means the container; 
#ie if you have a subnet1, and inside is box1, 
#if you ask box1 for its parent, its subnet1.
n = hou.node('/obj/subnet1/null2')
n.parent()
# <hou.SopNode of type subnet at /obj/subnet1>

#If you have box1 connected to mountain1, 
#and ask mountain1 for its inputs, you'll get box1 (as a list).

n = hou.node('/obj/mountain1')
n.inputs()
# (<hou.SopNode of type box at /obj/box1>,)
------------------------------------------------

====#get attrib from point listed in group field of sop
#So many layers of indirection!

# get list of nodes, here i've dragged a bunch of nodes into a node list parm i added to a python script node I created above
nodes = kwargs['node'].parent().parm('nodes').eval()
 
# for each node in the list:
for n in nodes.split(' '):
	 n = hou.node(n)
 
	 # read the group field, here they're all in a format like '@myattrib=57-58' 
	 group = n.parm('group').eval()
 
	 # use the handy globPoints function to convert that group syntax to a list of points
	 for p in n.geometry().globPoints(group):
				# get the attrib we're after!
				print p.attribValue('awesomeattrib')
------------------------------------------------


===#Create a cop file node for every subdir of a directory
#Assumes a lot; that the image sequence within
#each folder is of the same name, 
#and the parent folder only contains subfolders 
#with images, no error checking is done, may
#contain traces of peanut etc...

import os
dir = '/path/to/parent/folder'
seq = 'render.$F4.exr'
 
subdirs = [x for x in os.listdir(dir) if os.path.isdir(os.path.join(dir,x))]
 
for d in subdirs:
		imgpath = os.path.join(dir,d)+'/'+seq
		filenode = hou.node('/img').createNode('file')
		filenode.parm('filename1').set(imgpath)
------------------------------------------------


*****************Group related:
===#import
import test
reload(test)
from test import *

===#Group related:
Create group:
myGrp=geo.createPrimGroup('name')


===#Add Point to group:
point=geo.createPoint()
myGrp=geo.createPointGroup('name')
myGrp.add(point)

===#Iterate group:
groups = geo.primGroups()
for group in groups:
		print group.name

===#Delete group, leaving contents intact:
group.destroy()

==========#Create group:
myGrp=geo.createPrimGroup('name')

*****************Attributes
===#Set attribute
points[index].setAttribValue("Cd",(1.0,1.0,1.0))

===#Get attribute:
redVal=point.attribValue("Cd")[0]

===#Get point attributes from a node
#From the node get its geometry, 
#then its point attributes, 
#then the short names of those attributes.
[ x.name() for x in hou.node('/obj/mygeo/mysop').geometry().pointAttribs() ]

#To go one further and make a nice list 
#to feed to an attribute delete node, 
#use a join() with a single space, 
#prepend with ^'s, and stick an asterisk on the front:
print '*',' '.join([ '^'+x.name() for x in hou.node('/obj/geo1/mysop').geometry().pointAttribs()])

#will return
* ^id ^Cd ^Alpha ^center ^orient ^P ^uniqueId ^materialId

===#Delete primitives
deleteList=[]
for i in boundingGrp.prims():
		deleteList.append(i)
geo.deletePrims(deleteList)

===#Access local variables:
xBoundSize=lvar('SIZEX')

===#Read node parameter:
bitmask = hou.ch("bitmask")

===#sort a dict, if needed into list of tuples
import operator
weightDict={"plane": 150, "car": 2, "house": 400, "banana":0.2}
sortedDict = sorted(weightDict.items(), key=operator.itemgetter(1),reverse=True)

===#List primitive groups on the current node
primGroups = hou.selectedNodes()[0].geometry().primGroups()
for prim in primGroups:
	print prim.name()

=====Accessing geometry attributes
#Basic way of reading geometry attributes. 
#Note that in hou.node() you have to point
#at SOP node, not an object itself.
#Code returns a string attribute called ‘str’, 
#and it is a tuple of values (one for each primitive). 
#Similarly you can access all kinds of primitive 
#and point attributes with corresponding 
#methods (pointFloatAttribValues(), 
#primIntAttributeValues(), etc… you get the idea 
#🙂 For detail attributes you call similar methods 
#but without type specification: FloatAttribValues()

import hou
geo = hou.node('obj/box_object1/material1').geometry()
attrib = geo.primStringAttribValues('str')
print attrib


==========Button callback in HDA
kwargs[‘node’] 
#– stands for “currently processed node”

hdaModule().onLoadPress() – says to execute function called onLoadPress() 
#inside of hdaModule in digital assets’ scripts tab.
kwargs['node'].hdaModule().onLoadPress()

===============Print kwargs
print hou.node("/obj/myHDA").hdaModule().kwargs


======CHANGE A CERTAIN PARAMETER IN ALL MANTRA NODES
# change a certain parameter in all Mantra nodes
parent = hou.node("/obj/ROPS"r node in parent.children():)
	 node_type_name = node.type().name()
	 if node_type_name == 'mantra':
			# Get the value of a parameter and store it in a variable
			param = node.parm("matte_objects")    # set the value of the parameter to a different value
			param.set("enduranceer")
-----------------------------------------------------

======#There are times when you want to
#perform an operation on nodes whose names contain
#a particular pattern. In this case, 
#all nodes with ‘thrusterA’ in their names are acted upon.

#Change the forced matte parameter of node with
# 'thrusterA' pattern to 'endurance_render'
parent = hou.node("/obj/ROPString")
temp = 'endurance_render'
for child in parent.children():
	 if sstring in child.name():
			param = child.parm("matte_objects    if param is None:")
				 pass
			else: 
				 print searchStr
				 print replStr
				 param.set(temp)
-----------------------------------------------------

================REMOVE A NODE FROM A PARTICULAR BUNDLE
node = hou.node('/obj/testNode path')
bundlename = 'testy' #name of bundle

for nn in hou.nodeBundles():
	 if nn.name() ==bundlename:
			if nn.containsNode(node):
				 nn.removeNode(node)
-----------------------------------------------------

====Copy Bundles From Scene
#THIS TWO PART CODE ALLOWS YOU TO COPY BUNDLES 
#FROM ONE HOUDINI SCENE TO THE OTHER

# write bundle names, filter and pattern to file
import hou
namedumpfile = '/u/toa/Desktop/b_name.txt'
patterndumpfile = '/u/toa/Desktop/b_pattern.txt'
filterdumpfile = '/u/toa/Desktop/b_filter.txt'
a = file(namedumpfile, 'w')
b = file(patterndumpfile, 'w')
c = file(filterdumpfile, 'w')

# write bundle names, filter and pattern
for bdl in hou.nodeBundles():
	 a.write(str(bdl.name()))
	 a.write("\n")
	 a.close

	 b.write(str(bdl.pattern()))
	 b.write("\n")
	 b.close

	 c.write(str(bdl.filter()))
	 c.write("\n")
	 c.close
# Read bundle names, filter and pattern from file

namedumpfile = '/u/toa/Desktop/b_name.txt'
patterndumpfile = '/u/toa/Desktop/b_pattern.txt'
filterdumpfile = '/u/toa/Desktop/b_filter.txt'
import hou
a = file(namedumpfile, 'r')
b = file(patterndumpfile, 'r')
c = file(filterdumpfile, 'r')
global need
for lin in b:
	 for line in a:
		 need = hou.addNodeBundle(line.rstrip())
		 need.setPattern(lin.rstrip())
		 break
-----------------------------------------------------


==========#REPLACE A SUBSET OF STRINGS IN A SPECIFIC PARAMETER

'''
matchStr is the value to be replaced and replaceStr is the replacement
make sure the nodes you want to change are selected
'''

def forceObjects():

	 for node in hou.selectedNodes():
			param = node.parm("forceobject"    searchStr = param.evalAsString() )
 
			matchStr = "thrusterDelayedBB"
			replaceStr = "thrusterDelayedBC"

			#Change the values here
			if matchStr in searchStr:
				 replStr = searchStr.replace(matchStr,replaceStr)
				 #Replace the string
				 param.set(replStr)


def forceLights():

	 for node in hou.selectedNodes():
			param = node.parm("forcelights"    searchStr = param.evalAsString() )

			#Change the values here
			matchStr = "thrusterDelayedCA"
			replaceStr = "thrusterDelayedBA"

			if matchStr in searchStr:
				 replStr = searchStr.replace(matchStr,replaceStr)
				 #Replace the string
				 param.set(replStr)


forceObjects()
forceLights()
-------------------------------------------------------------


=========#RENAME ALL SELECTED ‘ALFHOU’ NODES 
#TO THE NAME OF THEIR ANCESTORS PREFIXED WITH ALFHOU

import hou
for node in hou.selectedNodes():
	 ans = node.inputAncestors()
	 suff = ans[0].name()
	 node.setName("alfhou_" + str(suff))
-------------------------------------------------------------

===========#APPEND AN ALFOU NODE TO THE SELECTED NODES 
#AND RENAME THEM SUFFIXED WITH ITS ANCESTORS NAME

import hou
parent = hou.node("/obj/ROPSr" node in hou.selectedNodes():)
		alfu = parent.createNode("alfhou")
		alfu.setFirstInput(node)
		alfu.moveToGoodPosition()
		ans = alfu.inputAncestors()
		suffix = ans[0].name()
		alfu.setName("alfhou_" + str(suffix))
-------------------------------------------------------------

============#REPLACE A CHARACTER IN ALL SELECTED NODE NAMES
import hou
for node in hou.selectedNodes():
	 name = node.name()
	 str = "D"
	 rep = "A"
	 if str in name:
		 newN = name.replace(str,rep)
		 node.setName(newN)
-------------------------------------------------------------

===========#WRITE A SET OF NODES TO DISK AS CODE
import hou
dumpfile='/u/toa/Desktop/nodeAsCode.txt'
a = file(dumpfile,'w')
for node in hou.selectedNodes():
	 acode = node.asCode()
	 a.write(acode)
	 a.close
-------------------------------------------------------------

========#COPY RAMP PARAMETERS
import hou

#Change path to source and destination nodes here
import hou

#Change path to source and destination nodes here
#sourceNode = hou.node("/obj/Rnd/color1stNode = hou.node("/obj/Rnd/color2urceParm = sourceNode.parm("rampstParm = destNode.parm("rampdedestParm.set(sourceParm.eval())
-------------------------------------------------------------

============#COPY ALL PARAMETERS FROM ONE NODE TO ANOTHER

import hou
source = hou.node('/shop/fireballest' = hou.node('/shop/test1or') pp in source.parms():)
		sourceParm = pp.name() #source parameter
		destParm = dest.parm(sourceParm) #Destination parameter
		destParm.set(pp.eval())


=========Get node from the scene
import hou
node = hou.node('/<nodePath>/<nodeName>') # By name
node = hou.selectedNodes() # By selection
# Get node content
node.children()
====================================

=========Create node in the scene
# Get scene root node
OBJ = hou.node('/obj/')
# Create Geometry node in scene root
geometry = OBJ.createNode('geo')
import hou
# Create transform node inside geo1
geometry = hou.node('/obj/geo1')
xform = geometry.createNode('xform') 
xform.moveToGoodPosition() # Align new node

# Create new transform node linked to existing transform
xformNew= xform.createOutputNode('xform')
====================================

******************************UI
#Add new UI items to a selected node interface
#adding new parameters by Python is a bit tricky 
#and there are few things you need to know:

#this function is essential to call first. It 
#represents nodes’ ui layout you can put your parameters into.
hou.parmTemplateGroup() 

#by this function you add a new parameter to the group.
#The argument in brackets defines what kind 
#of parameter it will be.
#In this case we have FloatParmTemplate(), which is obviously
#a float parameter. Arguments  are name (‘myparm’),
#label (‘My Parm’) and number of components (1).
#Similarly, you can have StringParmTemplate(), IntParmTemplate(), 
#ButtonParmTemplate(),FolderParmTemplate(), etc.,
#with respective arguments.
hou.addParmTemplate()      

#see the docs for more info and syntax on 
#Parameter templates: 
#http://www.sidefx.com/docs/houdini/hom/hou/ParmTemplate

#this line actually creates a user interface defined
#by templateGroup we’ve defined.
setParmTemplateGroup()

import hou
node = hou.selectedNodes()[0]
group = node.parmTemplateGroup()
group.addParmTemplate(hou.FloatParmTemplate('myparm', 'My Parm', 1))
node.setParmTemplateGroup(group)
#as you can see, this way parameter is created
#as a last element at the bottom of a Parameter pane.
#Chances are you want to organize your stuff into a folder.
#It may seem simple to just add a line for creating a folder:

#Unfortunately, even though the folder is created,
#there is no indication that our parameter
#is supposed to be a content of that folder
#and it is still placed outside of it.
import hou
node = hou.selectedNodes()[0]
group = node.parmTemplateGroup()
group.addParmTemplate(hou.FolderParmTemplate('myfolder', 'My Folder'))
group.addParmTemplate(hou.FloatParmTemplate('myparm', 'My Parm', 1))
node.setParmTemplateGroup(group)

#What you need to do is to create sort of a 
#hierarchy and specify that ‘myparm’ template
#is a child of ‘folder’ template:

import hou
node = hou.selectedNodes()[0]
group = node.parmTemplateGroup()
folder = hou.FolderParmTemplate('folder', 'My Parms') 
folder.addParmTemplate(hou.FloatParmTemplate('myparm', 'My Parm', 1))
group.append(folder)
node.setParmTemplateGroup(group)
#so as you can see, 
#folder = hou.FolderParmTemplate(‘folder’, ‘My Parms’)
#now defines its own template that is a Folder type.

#folder.addParmTemplate(hou.FloatParmTemplate(‘myparm’, ‘My Parm’, 1))
#– this line now says not to place the parameter
#directly into the main group but rather as a child of the ‘folder’.

#this statement specifies the layout of our ui.
#it says to append our folder at the end of the nodes’ layout.

group.append(folder) 
#So that covers basics of ui elements.
#Say now I need to add something more 
#complicated like a menu. This is how you go about that:

import hou
newGeo = hou.node('obj').createNode('geo')
newUi = newGeo.parmTemplateGroup()
newUi.addParmTemplate(hou.MenuParmTemplate('geoType', 'Geo type', ('01','02','03','04'), ('Disk file','Grid','Sphere','Box'), 1))
newGeo.setParmTemplateGroup(newUi)

#As you can see, it’s actually 
#not very different from what we’ve done before.
#Syntax of MenuParmTemplate() calls for
#brief explanation though. 
#MenuParmTemplate() takes multiple arguments:

#‘name’, ‘label’, (menu_items), (menu_labels), default_value
#Name and label are pretty self explanatory.
#Another two arguments enclosed in parentheses
#are tuples (it’s like groups of arguments) 
#and they put together a list of menu items, 
#their internal names and labels. 
#Last integer argument default value – 
#says which menu item will be selected by
#default (starting from 0 and going up).
---------------------------------------------------------------------

**********************************viewport
#Set viewport camera
#It’s a nasty long and tricky line of code,
#but if you need your Python script to switch
#a viewport to desired camera for you, 
#here’s what you can do about it:

hou.ui.paneTabOfType(hou.paneTabType.SceneViewer).curViewport().setCamera(hou.node('/obj/cam1'))

#Now how that works:
ui.paneTabOfType() 
#is a function of hou.ui module. 
#Takes an argument that says what type
#of pane are you looking for. 
#You might think that giving it something 
#like SceneViewer will be enough, but no. 
#You have to call a special module for 
#that so argument looks like this: 
#hou.paneTabType.SceneViewer. 
#If you happen to have more viewports of the same type,
#there is a good news that viewports 
#are indexed (0,1,2…) and you can add an 
#optional second integer argument that helps 
#to identify a desired instance.

curViewport() 
#is a method of sceneViewer class and it
#just returns this viewer’s current viewport. 
#The current viewport is the one containing the mouse cursor.
#If the cursor is not in a viewport, then the selected, 
#or active, viewport is returned.

#And finally, setCamera() lets you actually 
#set the camera after all the hard work of 
#picking up the viewport. 
#setCamera() is a method of geometryViewport class
#and again, it takes one argument and it has 
#to be a node instance. That means it’s not
#enough to specify a path to the node but it
#has to be encapsulated in hou.node class: hou.node(‘/obj/cam1’) 
----------------------------------------------------------------------


*************How to load a node preset with Python
#Only option right now seems to be using hscript within Python:

hou.hscript('oppresetload /out/mantra1 mantra_lookdev')
hou.script() 
#is obviously a function that allows you 
#to execute any hscript you put inside parenthesses.

oppresetload 
#is a hscript command allowing to load
#an existing preset. 
#out/mantra1 is then node you wish to 
#modify and mantra_lookdev is a preset name you want to load.


=================Filtering nodes by name
import hou
sel = hou.selectedNodes()[0]
children = sel.children()
lookfor = "OUT"
for child in children:
	name = child.name()
	fndstr = name.find(lookfor)
	if fndstr != -1:
		print "found:" + name
----------------------------------------------


====================Pop up floating windows
#Quite commonly you may want to pop up 
#a floating window with some content on button click. 
#This is how you go about it, give you’ve got
# Mantra1 ROP in /out network:

import hou
node = hou.node('/out/mantra1')
desktop = hou.ui.curDesktop()
pane = desktop.createFloatingPane(hou.paneTabType.Parm)
pane.setCurrentNode(node)
pane.setPin(True)
----------------------------------------------





============Run hscript command form Python
# Run Redshift IPR
hou.hscript('Redshift_openIPR')
====================================


============Get all node parameters names
def getAllNodeParameters(node):
		# Return list of all parameters names for input node object 
		allParameters = [param.name()for param in node.parms()]
		return allParameters

====================================


============Connect nodes
import hou
# Create transform nodes
xform_A = hou.node('/obj/geo1/transform1') 
xform_B = hou.node('/obj/geo1/transform2')
 # Connect transform_A to transform_B
xform_B.setInput(0, xform_A)

# Create merge
merge = node.createNode('merge')
# Connect xforms to a merge
merge.setNextInput(xform_A)
merge.setNextInput(xform_B)

# Get node inputs
merge.inputs()
# Get node outputs
merge.outputs()
====================================

============Builder workflow (shop context)
import hou
shader = hou.node('/shop/vopmaterial1/lambert1')
out = hou.node('/shop/vopmaterial1/surface_output')
out.setNamedInput('Cf', shader, 'clr') # Set connection by name
out.setNamedInput(0, shader, 0) # Set connection by parameter index

# List all inputs for node 'surface_output'
print out.inputNames()
====================================

============Filter node.children() output
import hou
selectedNode = hou.selectedNodes()

def extractVop(listOfChildrens):
		for node in listOfChildrens:
				if node.type().name() == 'vopsurface':
						return node

# return vopsurface nodes
vops = extractVop(selectedNode.children())

====================================

============blast code in python================
frames = [78, 85, 90]
result = '3'
if hou.intFrame() in frames:
		result = frames.index(hou.intFrame())
return str(result)
===============================================
findPointAttrib

===========read detail attrib value from geo===
hda = hou.node("../")
ip = hda.parm("instance_points").eval()
node = hou.node(ip)

nodeGeo = node.geometry()
clustermax = nodeGeo.attribValue("clustermax")
return clustermax
===============================================

====================read spare input===========
node = hou.pwd()
geo = node.geometry()
sN = node.parm("spare_input0").eval()
===============================================

====================read spare input geo===========
node = hou.pwd()
sN = node.parm("spare_input0").eval()
iG = hou.node(sN)
pG = iG.geometry()
name = pG.attribValue("splitName")
===============================================

=======read spare input geo and geo boundingBox===========
node = hou.pwd()
geo = node.geometry()
sN = node.parm("spare_input0").eval()
geoCk = hou.node(sN).geometry()
bb = geoCk.boundingBox()
bbmin = bb.minvec()
bbmax = bb.maxvec()
return bbmax,bbmin
==========================================================

========================
revertToDefaults() - delete all parameter links 
>>> k.setExpression('')
>>> k.deleteAllKeyframes()    #this is the same as revertToDefaults

deleteAllKeyframes() - delete all keyframes

==================read prim attribValue =============
node = hou.pwd()
geo = node.geometry()
prims = geo.iterPrims()
for pr in prims:
		path = pr.attribValue("path")
		print path
=====================================================


===============set primitive attribute floor========
node = hou.pwd()
geo = node.geometry()
prims = geo.iterPrims()

for pr in prims:
		path = pr.attribValue("path")
		pL= path.split("/")[2] #path list
		pr.setAttribValue("floor", pL)
=====================================================

=================set point attribute value
node = hou.pwd()
geo = node.geometry()
geo.addAttrib(hou.attribType.Point, "test", 1)
for pt in geo.points():
		pt.setAttribValue("test",29)
=====================================

=================split string by digit==================================
import os
import re

node = hou.pwd()
geo = node.geometry()
geo.addAttrib(hou.attribType.Prim, "objnameOrig","1")
prims = geo.iterPrims()
for pr in prims:
		name = pr.attribValue("name")
		mob = re.search('\d', name)
		name_nd = name[:mob.start()]
		pr.setAttribValue("objnameOrig", name_nd)
=====================================================

=======================set object name from path and name from prim attrib==========
import re
node = hou.pwd()
path = node.parm("soppath").eval()
rnode = hou.node(path)
geo = rnode.geometry()
prims = geo.iterPrims()
nameArray = []
for pr in prims:
		name = pr.attribValue("name")
		mob = re.search('\d', name)
		name_nd = name[:mob.start()]
		nameArray.append(name_nd)
return "rbd_"+nameArray[0]
=====================================================

=======================set object name from path and name from point attrib==========
import re
node = hou.pwd()
path = node.parm("soppath").eval()
rnode = hou.node(path)
geo = rnode.geometry()
points = geo.iterPoints()
nameArray = []
for pr in points:
		name = pr.attribValue("name")
		mob = re.search('\d', name)
		name_nd = name[:mob.start()]
		nameArray.append(name_nd)
return "rbd_"+nameArray[0]
=====================================================



==========callback resimulate this network============================
hou.parm(kwargs["node"].parent().path()+"/resimulate").pressButton()
=============================================================


================load hip file========================
k = path
hou.hipFile.load(k)
=====================================================



=====================read_inputs=====================
n = hou.pwd()
pfc = n.parm("fc_node").evalAsString()
sp = hou.node(pfc).inputs()[0].path()
res = sp

return res
=====================================================

=====================recursuve glob example==========
for x in hou.node("/obj/").recursiveGlob('*')
		if x.type.name()='filecacheHt':
				x.parm("output").eval()
=====================================================



========Pop up an user input window with a text “Type your input”
import hou
hou.ui.readInput('Typer input')
---------------------------------------------------

=================Pop up a message window with a text ‘hello’ and buttons ‘ok’ and ‘cancel’. returns 0 and 1 upon clicking on the buttons.
import hou
hou.ui.displayMessage(['hello ok','cancel'])
--------------------------------------------------

==========Select a node Selects object sphere1 on /obj
import hou
node = hou.node('obj/sphere1')
node.setCurrent(1, True)
-------------------------------------------------


===========set expression to python in parm
p.setExpression('',hou.exprLanguage.Python)


=====================================================

==============current evaluating parm name
evaluatingParm().name()
------------------------------------------

==============extract digits from string 
str = "blabla12"
res = re.findall('\d+',str)
------------------------------------------

=================open parm editor
cmd = 'oppane -t parmeditor '+ afNode.path() #open afNode
		hou.hscript(cmd)
------------------------------------------


==============add geometry using python
You just give poly.addVertex() the point objects you created where poly is the result of createPolygon(). hou.Polygon is derived from hou.Face. A quick test shows that the following works for me. Just make sure to set the number of inputs 0 in the Type Properties dialog (first tab) to avoid requiring an input.

geo = hou.pwd().geometry()
pt0 = geo.createPoint()
pt0.setPosition(hou.Vector3(1, 0, 0))
pt1 = geo.createPoint()
pt1.setPosition(hou.Vector3(0, 1, 0))
pt2 = geo.createPoint()
pt2.setPosition(hou.Vector3(0, 0, 1))
poly = geo.createPolygon()
poly.addVertex(pt0);
poly.addVertex(pt1);
poly.addVertex(pt2);
==============================================


==========Get functions in an OTL
#in button callback
hou.pwd().hdaModule().hello()
#in script window
def hello:
		....
-------------------------------------


=======================create objects from voronoi
from math import cos, sin, pi

obj = hou.selectedNodes()[0]
node = obj.displayNode()
prims = node.geometry().prims()

lastprim = prims[ len(prims)-1 ]
lastprimName = lastprim.attribValue("name")
lastprimName = lastprimName.partition("piece")
lastprimName = int( lastprimName[ len(lastprimName)-1 ] )

print lastprimName

subnet = hou.node("obj").createNode("subnet")

for i in range(0,lastprimName+1):
		geo = subnet.createNode("geo")
		geo.setPosition([cos( (1.0*i/lastprimName+1 ) * 2.0 * pi )*4.0, sin( (1.0*i/lastprimName+1 ) * 2.0 * pi )*4.0 ]) # lol
		objectMerge = geo.createNode("object_merge")
		delete = objectMerge.createOutputNode("delete")
		objectMerge.parm("objpath1").set(node.path())
		delete.parm("negate").set(1)
		delete.parm("group").set("@name=piece"+str(i))
		delete.setDisplayFlag(1)

---------------------------------------------------

====Set expresions linking light visible parameter to display flag
#idk why the candidate light didn't work on my machine so i used this

for child in hou.node('/obj').children():
		if 'light' in child.type().name():
				child.parm('light_enable').setExpression('hou.pwd().isDisplayFlagSet()', language=hou.exprLanguage.Python)
---------------------------------------------------


================Paste dlipboard nodes to object merges
# this snippet will paste nodes in clipboard to object merges
# use it with a shortcut (I overrode 'alt-v' in network pane context)

import hou

network = hou.ui.curDesktop().paneTabUnderCursor()
networkpath = network.pwd().path()
pos = network.cursorPosition()

clipboard = hou.ui.getTextFromClipboard()

n = 0

if clipboard:
		list = clipboard.split()
		for item in list:
				if hou.node(item) != None:
						merge = hou.node(networkpath).createNode('object_merge','merge_'+item.split('/')[-1])
						merge.parm('objpath1').set(str(item))
						merge.setPosition(pos)
						merge.move([n*2,0])
						if n == 0:
								merge.setSelected(True,True)
						else:
								merge.setSelected(True,False)
						n = n + 1
---------------------------------------------------


===================reconnect inputs===========
#With hou.NodeConnection class

import hou
nodes = hou.selectedNodes()
for node in nodes:
#disconnect inputs:
ins = node.inputConnections()
for inCon in ins:
inIndex = inCon.inputIndex()
inNode = inCon.outputNode()
inNode.setInput(inIndex,None,0)

#disconnect outputs:
outs = node.outputConnections()
for outCon in outs:
outIndex = outCon.inputIndex()
outNode = outCon.outputNode()
outNode.setInput(outIndex,None,0)

==============================================

============python equivalent 
opinputpath(“../”, 0)
hou.pwd().parent().inputs()[0].path()

opinputpath(“.”, 0)
hou.pwd().inputs()[0].path()
==============================================

========extract version v001_t001
re.compile(r"([_]\d{3}[_][t]\d{3})")
re.compile(r"([v]\d+\.*\d+)")
re.compile(r'([v]\d{4})')
==============================================

========convert list of strings to int of strings
val = [int(i) for i in val]
==============================================


============connect two nodes==============
n = hou.pwd()
path = hou.node( n.parent().evalParm('spare_input0'))
path = '../'+n.parent().evalParm('spare_input0')
doplr = hou.node(path)
lr_node =[x for x in doplr.children() of x.name() == n.name()][0]

parms = lr_node.parms()
pDict = {p.name():p for p in parms}

for p in n.parms():
	if p.name() in p.Dict:
		p.deleteAllKeyframes()
		p.set(pDict[p.name()])


===============relative path to absolute path  
#You can ask your node with the parameter on it to give 
#you the node the parm points to, then get the path from there. 
#hou.Node.node() will accept a relative path so you 
#can look for the node relative to the main node.
node = hou.node(“/obj/nodewithparm”)
relPath = node.evalParm(“path”)
relNode = node.node(relPath)
fullpath = relNode.path()
============================================

#Getting the number of individual attribute values is trickier. 
#Personally I'd do it using Python with the result of 
hou.Geometry.pointFloatAttribValues()



=====list if unique attrib values
values = geo.pointIntAttribValues("objid")
sorted_list = list(set(values))
new_attribs = geo.addArrayAttrib(hou.attribType.Point,"objid_array",hou.attribData.Int)
for pt in geo.iterPoints():
	pt.setAttribValue("objid_array",sorted_list)

	
==== callback for resimulate
hou.parm(kwargs["node"].parent().path()+"/resimulate").pressButton()
--------------------------------

======== how to get cam lists ---
camlist = hou.hscript('opfind -t cam')
cams = []
for cam in camlist:
  if cam.strip() != "":
    cams.append(cam.strip())

cams = sorted(cams)

return cams[-1]
--------------------------------

=========== how to add note comment 
node.setGenericFlag(hou.nodeFlag.DisplayComment,True)
--------------------------------

=========== set parms  from dictionary ----------
obj = hou.node("/obj")
cam = obj.createNode("cam", "cam_1080")
cam.setParms({"resx": 1920, "resy": 1080})
--------------------------------

========add vis
VIEW_visualization
import soputils
kwargs['attribname'] = 'name'
soputils.actionToggleVisualizer(kwargs)
--------------------------------


===how to use kwargs
print hou.node("/obj/myHDA").hdaModule().kwargs
exec(kwargs['node'].parm('parm').eval())
nodes = kwargs['node'].parent().parm('nodes').eval()


--------------------------------


=========how to create vizualizer ----
category=hou.viewportVisualizerCategory.Scene
type = hou.viewportVisualizers.type('vis_marker')
vis = hou.viewportVisualizers.createVisualizer(type, category=category)

desktop = hou.ui.curDesktop() 
desktop_scenes = [t for t in desktop.paneTabs() if t.type() == hou.paneTabType.SceneViewer]

for s in desktop_scenes:
    for geo_view in s.viewports():
        vis.setIsActive(True,viewport=geo_view)

--------------------------------

=========how to turn on vis / toggle
vis_name = 'name'
vis = [x for x in hou.viewportVisualizers.visualizers() if x.name()==vis_name ][0]
desktop = hou.ui.curDesktop() 
desktop_scenes = [t for t in desktop.paneTabs() if t.type() == hou.paneTabType.SceneViewer]

for s in desktop_scenes:
    for geo_view in s.viewports():
		check = vis.isActive(viewport=geo_view)
		vis.setIsActive(not check,viewport=geo_view)


===================Matrices in python --
# Matrices in Houdini are not m×n arrays, but 4-, 9- 
# and 16-float "vectors". They rarely used as storage, 
# as there is one-dimension arrays available for this
# purpose. Python is generally used for more sophisticated
# arrays manipulation. NumPy available by default.

import numpy

node = hou.pwd()
geo = node.geometry()

mat = geo.floatListAttribValue('test');
val = numpy.array(mat).reshape((4, 4))

print(val)
--------------------------------------------------


=========== import object using python
node = hou.pwd()
geo = node.geometry()

geo1 = hou.Geometry()
geo1.loadFromFile('$HIP/geo/geo1.obj')

geo2 = hou.Geometry()
geo2.loadFromFile('$HIP/geo/geo2.obj')

geo.merge(geo1)
geo.merge(geo2)
--------------------------------------------------

















