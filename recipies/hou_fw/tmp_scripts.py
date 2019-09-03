Basycally be able to be used bellow commands

	hou.hscriptExpression('  ')
#?
#?

Hscript Equivalents

	$FF = frame()
	$F = intFrame()
	$T = time()
	ch() = hou.node('obj/node/node').parm("px").eval()
	the animation functions are the same between python and hscript

Local Variable Equivalent in Python

	$PT: lvar("PT") or pwd().curPoint().number()
	$NPT: lvar("NPT") or len(pwd().geometry().iterPoints())
	$PR: lvar("PR") or pwd().curPrim().number()
	$NPR: lvar("NPR") or len(pwd().geometry().iterPrims())
	$VTX: lvar("VTX") or pwd().curVertex().number()
	$NVTX: lvar("NVTX") or pwd().curPrim().numVertices()
	$TX: lvar("TX") or pwd().curPoint().position()[0]
	$CR: lvar("CR") or pwd().curPoint.attribValue("Cd")[0] #? (or )
	$ID: lvar("ID") or pwd().curPoint.attribValue("id")





node = hou.pwd();sp0=node.parm("multilaunch_node").eval();spNode= #?
node = hou.pwd();sp0=node.parm("multilaunch_node").eval();spNode= #?

