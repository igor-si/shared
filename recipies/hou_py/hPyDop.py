

#===DOP find object id by name inside sop solver
n = hou.pwd()
sim = hou.node("../../").simulation()
s_obj = sim.findAllObjects("*")
check_name = n.evalParm("by_objname")
s_id = [s.objid() for s in s_obj if s.name() == check_name][0]
#-------------------------------


n = hou.pwd()
sim = hou.node("../../").simulation()
s_obj = sim.findAllObjects("*")
check_name = n.evalParm("check_name")
check_list = check_name.split(" ")
check_list = [x for x in check_list if len(x)>0]
object_array = [str(x.name())+":"+str(x.objid()) for x in s_obj if x.name() in check_list ]
print object_array

