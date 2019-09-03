

















 





































































			print nodeName,"force object ",fo
			fmo = ccNpde.parm("matte_objects").eval()
			print nodeName,"matte_objects =  ",fmo
			pho = ccNode.parm("forceobject").eval()
			print nodeName,"phantom object = ",pho
			cam = ccNode.parm("camera").eval()
			print nodeName,"cam = ",cam



































		try:
			hou.parm("out/L_wallLayeredMist/user").set(custom_name)
		except:
			pass

		try:
			hou.parm("out/L_wallLayeredMist_pts/user").set(custom_name)
		except:
			pass

		try:
			hou.parm("out/L_LaunchRender33/user").set(custom_name)
		except:
			pass


















	outCheck = hou.node(outControlCamPath.eval())
	print outControlCamPath,outCheck
	if outCheck==None:
		outControlCamPath.revertToDefaults()
		outControlCamPath.deleteAllKeyframes()
		wlmCamPathTmp = 'chs("/obj/L_wallLayeredMist/CONTROL/camPath")'
		outControlCamPath.setExpression(wlmCamPathTmp)















































			print "current part spooled = ", node.parm("part").eval() #?
			msNode.parm("submitAll").pressButton()
		except:
			print "pass"
		time.sleep(3)
	node.parm("part").set(partBup)
	dopNode.parm("opencl").set(oclBup)




	mistNode=hou.node(mistNodePath)

	combNodePath = node.parm("comb_release").eval()
	combNode=hou.node(combNodePath)








	except:
		print "cant release part ",i








	typelist = ["multilaunch_vol_sim", "multilaunch_vol_sim"] #?
	mn.set( node.parm(typeList[type]).eval() )












	names = ["ve_list", "ver_pts", "ver_mist_render"] #?
	for s in names:
		print "add version to ",s
		cv = node.parm(s).eval()
		node.parm(s).set(cv+1)




num = (int(n.evalParm("namingConventionColumn3") )+1	)*10
























	label_template = template.group.find(label)













path = os.path.join(hou.getenv("HIP"),"isutils/1.py")
path2 = os.path.join(hou.getenv("HIP"),"isutils/2.py")










from mpc.houdini.houdiniAssets.parmUtils import makeParameterMenu
types = hou.pwd().findStreamNames()
return makeParameterMenu(types)

# element names
from mpc.houdini.houdiniAssets.parmUtils import makeParameterMenu
types = hou.pwd().findElementNames()
return makeParameterMenu(types)

# type
from mpc.houdini.houdiniAssets.parmUtils import makeParameterMenu
types = hou.pwd().findTypeNames()
return makeParameterMenu(types)























		s.setPosition([n.position()[0]-1,n.position()[1]])

		s.parm("scale").set(0.05)
		s.parmTuple("t").set(p)
























































		elementNew = element.replace("l4", "l7").replace("l4", "l7") #?
			if(elementNew[:2]!="l7"):
				elementNew = "l7"+elementNew





































# print res


driver = hou.node("/obj/ANIMATION_CONTROLLER")
parms = [x for x in driver.parms() if x.name().startswith("impactframe")]
frames = [x.eval() for x in parms]
return not any([hou.frame() >= x for x in frames])






	raise RuntimeError ("%s does not have any inputs")

render_obj = inputs[0].node("render")




exec(hou.shelves.tools()['makeflipbooks'].script() )

n_parm = [x for x in n.parms() if re.findall("SumbitNode"x.name() )]














	lr_node = [x for x in doplr.children() if x.name() = n.name()][0]
	
	parms = lr.node.parms()
	pDict = {p.name():p for p in parms}



































paths = [x.eval() for x in n.parms() if bool(re.match(pattern, ))] #?
nodex = [hou.node(x) for x in paths if x is not None]
attribs = ["".join([str(x.geometry().attribValue("element")),str(x.geometry().attribValue('version')) ]) for x in nodes]  
attribs_str = "%s__%s" % (n.name(), ":".join(attribs))
return attribs_str









paths = [ [x.eval().re.sub("out_path","",x.name()) ] for x in n.parms() if bool(re.match(pattern,x.name() ) )  ] 
print paths

# enable =[x.eval() for x in n.parms() if bool(re.match(pattern,x.name())) ]
# nodes = [hou.node(x) for x in paths if x is not None]
# attribs = [''.join([str(x.evalParm('element')),str(x.evalParm('version')) ]) for x in nodes]









paths = [[x.eval(), re.sub('out_path', '', x.name())] for x in ] #? 
enable = [x.eval() for x in n.parms() if bool(re.match(pattern2,x.name()))]

nodes = [hou.node(x[0])for x in paths if x[0] in s not None and enable[int(x[1])-1 ]]
???
attribs_str = "%s__%s" % ('m',":".join(attribs))
return attribs_str







n_parm = [os.path.basename( x.eval() ).replace("dh_",'') for x in hou.pwd().parms() if re.findall("SubmitNode",x.name()) ]
return 'v'+str(n.evalParm('version'))+'_'+":".join(n_parm)











nodes = [x.destroy() for x in hou.node('/obj/out').recursiveGlob('*') if x.type().name() in ['LaunchRender',"ifd"]]








return "part{}:v{}__{}".format(n.evalParm("part"), n.evalParm("version"), n.name()) #?














































mpcpython /usr/people/igor-si/dev/third_party/error_tasks_ #?


n=hou.pwd();exec(n.evalParm('codeMain'));linkVersion(kwargs['parm'])



n=hou.pwd()
sim = hou.node("../../").simulation()
s_obj = sim.findAllObjects("*")
check_name = n.evalParm('by_objname')
s_id = [x.objid() for x in s_obj if s.name() == check_name][0]
return s_id

















































































