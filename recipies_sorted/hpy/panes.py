hou.ui.findPaneTab('panetab15')
hou.NetworkEditor panetab15;
hou.ui.findPaneTab('panetab15').pwd()
hou.Node at /obj&gt;
hou.ui.findPaneTab('panetab15').pwd().childTypeCategory()
hou.NodeTypeCategory for Object
# Now inside a geo object (/obj/geo1)
hou.ui.findPaneTab('panetab15').pwd()
hou.ObjNode of type geo at /obj/geo1;
hou.ui.findPaneTab('panetab15').pwd().childTypeCategory()
hou.NodeTypeCategory for Sop

pane = kwargs['pane']
contextname = pane.pwd().childTypeCategory().name()