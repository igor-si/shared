
# get parm type
parm.parmTemplate().type()

# get number of points
points_num =  len(geo.iterPoints() )

# Return a tuple containing points 5 and 7.
geo.globPoints("5 7")

# Return a tuple containing points 5 to 10.
geo.globPoints("5-10")

# Return a tuple containing all the points in the pointgroup called group1.
geo.globPoints("group1")

# Return all the points except those from 0 to 98.
geo.globPoints("!0-98")

# Return points 5, 10 to 20, and those in group1.
geo.globPoints("5 group1 10-20")


# Add array attrib to points
new_attribs = geo.addArrayAttrib(hou.attribType.Point,"obj_array",hou.attribData.Int)
for p in geo.iterPoints():
    p.setAttribValue("obj_array",obj_array)
# -------------------------------------------------- 

# Read list attribute from point
point = geo.iterPoints()[0]
value = list(point.stringListAttribValue("obj_array") )
# --------------------------------------------------

# how to show comment in network
node.setGenericFlag(hou.nodeFlag.DisplayComment,True)