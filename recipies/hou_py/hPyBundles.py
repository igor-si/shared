#bundle list
#Texport Editor:
#
#opbadd boltL010 boltL020 boltGlowL010 boltGlowL020 secondaryL010 secondaryL020
#
#
#Example for the Texport Editor:
#
#opbop boltL010 set /obj/FxLightningStrike*/Bolt*
#
#opbop boltGlowL010 set /obj/FxLightningStrike*/LightningG*
#
#opbop impactDebris set /obj/FxLightningImpact*/*Re* set /obj/FxLightningImpact*/ground_p* set /obj/FxLightningImpact*/grit_p* set /obj/FxLightningImpact*/sparks_p*
#etc.
#===============================================
#python script editor

import hou
##select all lightning node
def makeBundles():
    hou.addNodeBundle("boltL010")
    hou.addNodeBundle("boltLightL010")

def fillBundles():
    selection = hou.selectedNodes()
    lightBundle = hou.nodeBundle("boltLightL010")
    boltBundle = hou.nodeBundle("boltL010")

    nodes = []
    for item in selection:
        path = item.path()
        path = path + "/Bolt_display"

        nodes.append(hou.node(path))

    lightNodes = []
    for item in selection:
        path = item.path()
        path = path + "/boltLights1"

        lightNodes.append(hou.node(path))    

    
    for x in lightNodes:
        lightBundle.addNode(x)

    for x in nodes:
        boltBundle.addNode(x)

---------python shell------------------
hou.session.makeBundles()

hou.session.fillBundles()