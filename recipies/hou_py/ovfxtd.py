import hou
def eventfunc():
    sel = hou.selectedNodes()
    if not sel:
        return
    elif len(sel)>1:
        return
    elif sel[0] is None: 
        return
    elif not sel[0].type().name() == "geo":
        return        
    else:
        primCount = len(sel[0].displayNode().geometry().iterPrims())
        hou.ui.displayMessage('%d Prims in this geometry' % primCount)
        sel[0].setSelected(False)
        hou.ui.displayMessage('%s Displayed node is' % sel[0])



#hou.ui.addEventLoopCallback(hou.session.eventfunc)
#hou.ui.removeEventLoopCallback(hou.session.eventfunc)
#hou.ui.eventLoopCallbacks()