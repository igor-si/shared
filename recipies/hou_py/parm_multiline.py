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