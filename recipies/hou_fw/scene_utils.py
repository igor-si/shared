# import hou
import re

# import psutil
# process_name = "houdini"
# for proc in psutil.process_iter():
# 	if process_name in proc.name():
# 		proc.kill()








































	def addToBundle(node=None):
		try:hou.addNodeBundle('cache_hmp')
		except: pass
		hou.nodeBundle('cache_hmp').addNode(node)





































































def addOwner():
	import hou
	import datetime

	nodes +=hou.node('/obj/').recursiveGlob("*")
	nodes +=hou.node('/mat/').recursiveGlob("*")
	nodes +=hou.node('/out/').recursiveGlob("*")
	nodes +=hou.node('/shop/').recursiveGlob("*")

	for n in nodes:


		label = "created_igor_si"+datetime.datetime.now().strftime("%Y%m%d")
		template = hou.LabelParmTemplate('name',label,is_hidden=True)
		group = n.parmTemplateGroup()
		group.addParmTemplate(template)

		try:
			n.setParmTemplateGroup(group)
			print "adding owner to %s" % n
		except: print "cannot add owner to %s" %n		



















