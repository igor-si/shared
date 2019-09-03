
























































































































































































































































	typelist = ["multilaunch_vol_sim", "multilaunch_vol_sim"] #?













	names = ["ve_list", "ver_pts", "ver_mist_render"] #?















































path = os.path.join(hou.getenv("HIP"), "isutils/1.py") #???
path2 = os.path.join(hou.getenv("HIP"), "isutils/2.py") #???





























































































======= finally
mantra_node = hou.nowd(path_to_mantra_node)

try:
	use_motion_blur = mantra_node.parm("allowmotionblur")
	shutter_offset = mantra_node.parm("shutteroffset")
except Exception as e:
	print e
finally:
	return



		elementNew = element.replace("l4", "l7").replace("l4", "l7") #???











==============salvadors create ch
import traceback
import hou

node = hou.pwd()

parent = node.parent()
kwargs = {}
for parm in parent.parms():
	if not parm.name().startswith('toggle_'):
		continue

	is_enabled = parm.eval() == 1
	if not is_enabled:
		continue

	parm_name = parm.name().replace('toggle_','')
	value_parm = parent.parm(parm_name).eval()
	kwargs[parm_name] = value_parm

kwargs['silent'] = parent.parm('silent').eval()

try:
	parent.hdaModule().createConvexHullForGeo(node.geometry(), ** kwargs)
except Exception:
	traceback.print_exc()
	raise







































============find most frequent common element
from collections import Counter

n = hou.pwd()
g = n.geometry()

cGL = []
for prim in g.prims():
	cG = prim.attribValue("classGuide")
	cGL.append(cG)


#  collect list
new_vals = Counter(cGL).most_common()
new_vals = new_vals[::-1]









bCount = -1
mFreq = -1
#  find max value for more common element
for a,b in new_vals:
	if b>bCount:
		bCount=b

#  find more frequent classGuide
for a,b in new_vals:
	if b==bCount:
		mFreq=a 

g.addAttrib(hou.attribType.Global,"mostFreq",mFreq)
# g.setGlobalAttribValue("mostFreq",mostFreq)
















































































































mpcpython / ???

user = 'user={0}'.format(os.environ["USER"])















