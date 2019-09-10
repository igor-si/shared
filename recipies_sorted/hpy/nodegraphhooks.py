import hou
from canvaseventtypes import *
import nodegraphdisplay as display
import nodegraphview as view
import nodegraph
    
#debug by:
#import nodegraphhooks
#reload(nodegraphhooks)

    
def createEventHandler(uievent, pending_actions):
    if isinstance(uievent, KeyboardEvent) and \
       uievent.eventtype == 'keyhit' and \
       uievent.key == 'Shift+X':
       
        # Get the current node.
        current_node = uievent.editor.currentNode()
        if current_node is not None:
            #get available attributes
            
            
            geo = current_node.geometry()
            #get list of choices
            attrib_excludes = ['P'] #creating a visualizer for P could trigger a chrash in H16.5.314
            attrib_choices = []
            pt_attribs = [attrib for attrib in geo.pointAttribs() if not attrib.name() in attrib_excludes]
            pt_attrib_choices = ['point/'+attrib.name() +" (" + str( attrib.dataType() ).split(".")[-1] + str(attrib.size()) + ")" for attrib in pt_attribs ]
            attrib_choices.extend(pt_attrib_choices )
            prim_attrib_choices = ['primitive/'+attrib.name() +" (" + str( attrib.dataType() ).split(".")[-1] + str(attrib.size()) + ")" for attrib in geo.primAttribs() ]
            attrib_choices.extend(prim_attrib_choices)
            
            #get matching list of names
            attribs =  []
            attribs.extend(pt_attribs)
            attribs.extend(geo.primAttribs())
            attrib_names = [attr.name() for attr in attribs]
            #attribs.extend(geo.primAttribs())
            
            #inAttribNames = {}
            #for attrib in attribs :
                #inAttribNames[ attrib.name() + " (" + str( attrib.dataType() ).split(".")[-1] + str(attrib.size()) + ")" ] = attrib
            #sortedKeys = sorted( inAttribNames.keys() )
            
            pick = hou.ui.selectFromTree(attrib_choices, exclusive=True, message="Pick Attributes to Visualize", title="Select Attribute for visualizer" )

            if not pick: print "failed"
            if pick :
                index = attrib_choices.index(pick[0])
                attribute_name = str(attrib_names[index])
                #print "attrib name: ", attribute_name

                vis_category=hou.viewportVisualizerCategory.Scene
                vis_type = hou.viewportVisualizers.type('vis_marker')
                vis = hou.viewportVisualizers.createVisualizer(vis_type, category=vis_category)
                
                vis.setParm("attrib", attribute_name)
                if 'Float3' in pick[0]:
                    vis.setParm("style", 4)
                else: 
                    vis.setParm("style", 0)
                vis.setName(attribute_name)
                vis.setLabel(attribute_name)
                
                #print "visualizer: ", vis
                desktop = hou.ui.curDesktop() 
                
                #set the visualizer to visible in all scenes viewports
                desktop_scenes = [t for t in desktop.paneTabs() if t.type() == hou.paneTabType.SceneViewer]
                
                #vis.setIsActive(True, viewport=desktop_scenes[0].viewports())
                for s in desktop_scenes:
                    for geo_view in s.viewports():
                        vis.setIsActive(True, viewport=geo_view)
                return None, True

        # We handled this event, but don't need to return an event handler
        # because this is a one-off event. We don't care what happens next.
        
    return None, False

