

#n-hou.pwd();exec(n.evalParm("codeMain"));test(kwargs["parm"])
def extractDigits(str="")
	import re
	res = re.findall('\d+',str)
	return res
def linkVersion(parm=""):
	parmName = parm.name()
	num=extraxctDigits(parmName)[0]
	opPath=n.evalParm("operators"+num)
	curNode = hou.node(opPath)
	curNode.parm("version").deleteAllKeyframes()
	hou.parm("version"+num).set(curNode.evalParm("version")) #backup current version
	curNode.parm("version").set(	hou.parm("version"+num)	)

def spoolToFarm(parm=""):
	parmName = parm.name()
	num=extraxctDigits(parmName)[0]
	opPath=n.evalParm("operators"+num)
	curNode = hou.node(opPath)
	curNode.parm("enFarm").pressButton()
