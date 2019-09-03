

# multiline
import hou
node = hou.node('/obj').createNode('geo')
group = node.parmTemplateGroup()
folder = hou.FolderParmTemplate('folder', 'My Parms')
template = hou.StringParmTemplate('myparm', 'My Parm',1)
template.setTags({"editor": "1"}) #it's "0" by default
folder.addParmTemplate(template)
group.append(folder)
node.setParmTemplateGroup(group)

#========== create label parameter
import hou
import datetime
n = hou.selectedNodes()
label = "created_igor_si_"+datetime.datetime.now().strftime("%Y%m%d")
template = hou.LabelParmTeplate('name',label,is_hidden=True)
group = n.parmTemplateGroup()
group.addParmTemplate(template)
#----------
