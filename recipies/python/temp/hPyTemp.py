Python in Houdini
MARCH 15, 2016 D.LEAVE A COMMENT
 .Pieces of code for using Python in Houdini. For general Python syntax and tutorials see https://www.tutorialspoint.com/python/ or https://docs.python.org/3/tutorial/


Display a message window with “Hello” text
hou is a library of Houdini specific methods. It has to be imported in order to Python have access to those methods.

Method is a function that works in relation to specific classes. Class is an object template that allows you to run specified methods that are related to it. In this example, ‘ui’ is a class and ‘displayMessage()’ is a method of that class. 

Whatever is inside parentheses following the method name is called ‘argument‘.

import hou
hou.ui.displayMessage('Hello
Pop up a message window with a text ‘hello’ and buttons ‘ok’ and ‘cancel’. returns 0 and 1 upon clicking on the buttons.
As you can see, methods can have multiple arguments that can change a way the method is executed.

import hou
hou.ui.displayMessage('hello'ok','cancel'])
Pop up an user input window with a text “Type your input”
import hou
hou.ui.readInput('Typer input')
Get a path to a first selected node, save it as a variable and print it.
Variable is any user defined data that can be referenced later by its name. This way you can execute the code once, save the result as a variable and then call it by name without having to execute it again. It also helps to keep your code clean and easy to work with.

import hou
my_variable = hou.selectedNodes()[0].path()
print my_variable
Select a node
Selects object sphere1 on /obj

import hou

node = hou.node('obj/sphere1
node.setCurrent(1, True)
For loops
This example shows a simple for loop. It loops over selected nodes and for each of them it prints out its path in the console. for and in are Python reserved words, ‘selected’ represents a list of objects to loop over, ‘item’ stands for any single item in that list (it can be called whatever you want). After this initial statement follows a colon ‘:’ Next line (or lines) has to be indented and states a code to be executed at each cycle of the loop (in this case prints a path to the currently processed node).

import hou
selected = hou.selectedNodes()
for item in selected:
  print item.path()
Another example of for loop:

Take selected nodes and assign a new name to each of them with trailing digit based on order in which they have been processed. This time list of our objects is called ‘nodes’ and each item is refered to as ‘n’

Resulting names will be newName1, newName2, newName3, etc.

import hou
count = 0
nodes = hou.selectedNodes()
for n in nodes:
 count += 1
 n.setName('newName' + str(count))
This example creates a sphere
This example introduces concept of function. Function is isolated block of code that has some functionality on its own and can be later called by its name, similar to variables. It allows to create modular code that can be reused, stacked and executed in desired order, and can also be easily modified. Function starts like this:

def createSphereGeo(): – def states this is a function. ‘createSphereGeo’ is its name. Name is up to the user, it can be anything. After name there always follows closed parentheses which can contain arguments (for example you may need some user input or something). Similar to loops, there has to be a colon after parentheses.

Follows an indented block of code with some functionality on its own. In this example function is to create a sphere object.

Function can be executed by typing name of a function: createSphereGeo() – without colon.

Important methods in this example:

hou.node(‘obj’).createNode(‘geo’) – this is a function that basically sets a scene location (path) at which you wish to operate (‘obj’). createNode() is a method that places a new node (which type has been set to ‘geo’) at the location specified by hou.node().

Another node will be created as a child of the geo node and it will be actual sphere this time aGeoNode.createNode(‘sphere’)

aSphereNode.setDisplayFlag() – sets a display flag on aSphereNode object. Argument is either 0 or 1.

import hou
def createSphereGeo():
  aGeoNode = hou.node('obj').createNode('geo
  aSphereNode = aGeoNode.createNode('sphere')
  aSphereNode.setDisplayFlag(1)
createSphereGeo()
List primitive groups on the current node
primGroups = hou.selectedNodes()[0].geometry().primGroups()
for prim in primGroups:
  print prim.name()
Set render flag on selected node
node = hou.selectedNodes()[0]
node.setRenderFlag(True)
Set node position in network view
import hou

newNode = hou.node('obj').createNode('geo
newNode.setPosition([1, 0])
Working with nodes. Nodes creation, naming, connections.
Interesting functions:

setPosition() – allows to set a nodes’ position in the network view

newShopNode.setPosition([4,0])

setInput() – this is for making new connections between nodes. it takes 3 arguments: 1. input connector number, 2. node to make connection to (destination), 3. destination nodes’ connector number.

addLayerUnpack.setInput(0,addPrincipled,2)

parm().set() – useful combo for setting values into existing parameters. “parm” and “set” both take one argument: parameter name and parameter value to set

newMatNode.parm(‘shop_materialpath1’).set(“../shopnet1/vopmaterial1”)

setName() – obviously, allows you to rename a node. argument is a new name (string)

newOutNode.setName(“OUT”)

note that name can be also added directly upon nodes’ creation by adding another argument:

newGeoNode.createNode(‘null’, “OUT”)

setColor() – assigning a color to a node is a bit trickier as it requires hou.Color object, containing tuple of values. so the syntax looks like this:

newOutNode.setColor(hou.Color((0,0.5,0)))

import hou

def createNewGeo():
 newGeoNode = hou.node('obj').createNode('geo
 
 newShopNode = newGeoNode.createNode('shopnet')
 newShopNode.setPosition([4,0])
 
 newMatBuilder = newShopNode.createNode('vopmaterial')
 
 addPrincipled = newMatBuilder.createNode('principledshader')
 addPrincipled.setPosition([0,7])
 
 addLayerUnpack = newMatBuilder.createNode('layerunpack')
 addLayerUnpack.setPosition([3,7])
 addLayerUnpack.setInput(0,addPrincipled,2)
 
 newMatNode = newGeoNode.createNode('material')
 newMatNode.setPosition([0,-1])
 newMatNode.parm('shop_materialpath1').set("../shopnet1/vopmaterial1
 
 newOutNode = newGeoNode.createNode('null')
 newOutNode.setPosition([0,-2])
 newOutNode.setColor(hou.Color((0,0.5,0)))
 newOutNode.setInput(0,newMatNode)
 newOutNode.setName("OUT")
 
createNewGeo()
When creating new nodes, moveToGoodPosition() comes in handy
node.moveToGoodPosition() – it will simply create node at a convenient location, avoiding any overlaps.

import hou

aNode = hou.node('obj').createNode('geo
aNode.moveToGoodPosition()
Button callback in HDA
kwargs[‘node’] – stands for “currently processed node”

hdaModule().onLoadPress() – says to execute function called onLoadPress() inside of hdaModule in digital assets’ scripts tab.

kwargs['node'].hdaModule().onLoadPress()
Add new UI items to a selected node interface
adding new parameters by Python is a bit tricky and there are few things you need to know:

hou.parmTemplateGroup() – this function is essential to call first. It represents nodes’ ui layout you can put your parameters into.

hou.addParmTemplate() – by this function you add a new parameter to the group. The argument in brackets defines what kind of parameter it will be. In this case we have FloatParmTemplate(), which is obviously a float parameter. Arguments  are name (‘myparm’), label (‘My Parm’) and number of components (1). Similarly, you can have StringParmTemplate(), IntParmTemplate(), ButtonParmTemplate(), FolderParmTemplate(), etc., with respective arguments.

see the docs for more info and syntax on Parameter templates: http://www.sidefx.com/docs/houdini/hom/hou/ParmTemplate

setParmTemplateGroup() – this line actually creates a user interface defined by templateGroup we’ve defined.

import hou
node = hou.selectedNodes()[0]
group = node.parmTemplateGroup()
group.addParmTemplate(hou.FloatParmTemplate('myparm', 'My Parm', 1))
node.setParmTemplateGroup(group)
as you can see, this way parameter is created as a last element at the bottom of a Parameter pane. Chances are you want to organize your stuff into a folder. It may seem simple to just add a line for creating a folder:

import hou
node = hou.selectedNodes()[0]
group = node.parmTemplateGroup()
group.addParmTemplate(hou.FolderParmTemplate('myfolder', 'My Folder'))
group.addParmTemplate(hou.FloatParmTemplate('myparm', 'My Parm', 1))
node.setParmTemplateGroup(group)
Unfortunately, even though the folder is created, there is no indication that our parameter is supposed to be a content of that folder and it is still placed outside of it.

What you need to do is to create sort of a hierarchy and specify that ‘myparm’ template is a child of ‘folder’ template:

import hou
node = hou.selectedNodes()[0]
group = node.parmTemplateGroup()
folder = hou.FolderParmTemplate('folder', 'My Parms') 
folder.addParmTemplate(hou.FloatParmTemplate('myparm', 'My Parm', 1))
group.append(folder)
node.setParmTemplateGroup(group)
so as you can see, folder = hou.FolderParmTemplate(‘folder’, ‘My Parms’) now defines its own template that is a Folder type.

folder.addParmTemplate(hou.FloatParmTemplate(‘myparm’, ‘My Parm’, 1)) – this line now says not to place the parameter directly into the main group but rather as a child of the ‘folder’.

group.append(folder) – this statement specifies the layout of our ui. it says to append our folder at the end of the nodes’ layout.

So that covers basics of ui elements. Say now I need to add something more complicated like a menu. This is how you go about that:

import hou
newGeo = hou.node('obj').createNode('geo
newUi = newGeo.parmTemplateGroup()
newUi.addParmTemplate(hou.MenuParmTemplate('geoType', 'Geo type', ('01','02','03','04'), ('Disk file','Grid','Sphere','Box'), 1))
newGeo.setParmTemplateGroup(newUi)
As you can see, it’s actually not very different from what we’ve done before. Syntax of MenuParmTemplate() calls for brief explanation though. MenuParmTemplate() takes multiple arguments:

‘name’, ‘label’, (menu_items), (menu_labels), default_value

Name and label are pretty self explanatory. Another two arguments enclosed in parentheses are tuples (it’s like groups of arguments) and they put together a list of menu items, their internal names and labels. Last integer argument default value – says which menu item will be selected by default (starting from 0 and going up).

Set viewport camera
It’s a nasty long and tricky line of code, but if you need your Python script to switch a viewport to desired camera for you, here’s what you can do about it:

hou.ui.paneTabOfType(hou.paneTabType.SceneViewer).curViewport().setCamera(hou.node('/obj/cam1
Now how that works:

ui.paneTabOfType() is a function of hou.ui module. Takes an argument that says what type of pane are you looking for. You might think that giving it something like SceneViewer will be enough, but no. You have to call a special module for that so argument looks like this: hou.paneTabType.SceneViewer. If you happen to have more viewports of the same type, there is a good news that viewports are indexed (0,1,2…) and you can add an optional second integer argument that helps to identify a desired instance.

curViewport() is a method of sceneViewer class and it just returns this viewer’s current viewport. The current viewport is the one containing the mouse cursor. If the cursor is not in a viewport, then the selected, or active, viewport is returned.

And finally, setCamera() lets you actually set the camera after all the hard work of picking up the viewport. setCamera() is a method of geometryViewport class and again, it takes one argument and it has to be a node instance. That means it’s not enough to specify a path to the node but it has to be encapsulated in hou.node class: hou.node(‘/obj/cam1’) 

How to load a node preset with Python
Only option right now seems to be using hscript within Python:

hou.hscript('oppresetload /out/mantra1 mantra_lookdev')
hou.script() is obviously a function that allows you to execute any hscript you put inside parenthesses.

oppresetload is a hscript command allowing to load an existing preset. out/mantra1 is then node you wish to modify and mantra_lookdev is a preset name you want to load.

Filtering nodes by name
import hou

sel = hou.selectedNodes()[0]
children = sel.children()
lookfor = "OUT"
for child in children:
 name = child.name()
 fndstr = name.find(lookfor)
 if fndstr != -1:
  print "found:" + name
Using variables outside functions
Basic syntax looks like this:

def myfunction():
 var = "this is my variable"
 second = 11
 return var, second

one, two = myfunction()
print one, two
As you can see, there is a function that defines two variables, named “var” and “second”. Then I can assign this function to couple of different (or same) variables and original variables are picked up by their order in return statement. This is great when you need to run function inside functions. Example:

 

import hou

def evalRops():
 current = hou.pwd()
 arnold = hou.node('/out/lookdev/arnold1
 mantra = hou.node('/out/lookdev/mantra1
 getValue = current.parm('rendererMenu').eval
 return arnold, mantra, getValue 

def setRop(): 
 arnold, mantra, getValue = evalRops() 
 if getValue == 0: 
  hou.ui.paneTabOfType(hou.paneTabType.IPRViewer).setRopNode(arnold)
 if getValue == 1:
  hou.ui.paneTabOfType(hou.paneTabType.IPRViewer).setRopNode(mantra)

def openRopDialog():
 arnold, mantra, getValue = evalRops() 

 if getValue == 0:
  node = arnold
 if getValue == 1:
  node = mantra
 
 desktop = hou.ui.curDesktop()
 pane = desktop.createFloatingPane(hou.paneTabType.Parm)
 pane.setCurrentNode(node)
 pane.setPin(True)
I have defined code for evaluating our variables in evalRops() function and then I’m calling that function inside two different functions. The return statement inside the evalRops() is what makes listed variables available even outside of the current function.

Without being able to do this I would have to embed the whole code of evalRops() function inside each of those functions. That would make my script not only longer but also harder to read and work with, more prone to errors.

Pop up floating windows
Quite commonly you may want to pop up a floating window with some content on button click. This is how you go about it, give you’ve got Mantra1 ROP in /out network:

import hou
node = hou.node('/out/mantra1')
desktop = hou.ui.curDesktop()
pane = desktop.createFloatingPane(hou.paneTabType.Parm)
pane.setCurrentNode(node)
pane.setPin(True)
This is similar to previous example but you need to work with curDesktop() method.

Accessing geometry attributes
Basic way of reading geometry attributes. Note that in hou.node() you have to point at SOP node, not an object itself. Code returns a string attribute called ‘str’, and it is a tuple of values (one for each primitive). Similarly you can access all kinds of primitive and point attributes with corresponding methods (pointFloatAttribValues(), primIntAttributeValues(), etc… you get the idea 🙂 For detail attributes you call similar methods but without type specification: FloatAttribValues()

import hou
geo = hou.node('obj/box_object1/material1').geometry()
attrib = geo.primStringAttribValues('str')
print attrib

Print kwargs
print hou.node("/obj/myHDA").hdaModule().kwargs


import hou
hou.ui.readInput('Typer input')