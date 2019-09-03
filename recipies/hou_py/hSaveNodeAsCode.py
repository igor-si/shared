import os

#saver
node = hou.node("/obj/geo1/")

# Add code to modify contained geometries.
# Use drop down menu to select examples.

if(node != None):
    dir = os.path.dirname(hou.hipFile.path())
    
    node_file = open(dir + "/node_reconstruction.py", "w")
    
    node_file.write(node.asCode(False, True))
    
    node_file.close()



#loader
node = hou.pwd()

# Add code to modify contained geometries.
# Use drop down menu to select examples.

import os

def load_node():
    dir = os.path.dirname(hou.hipFile.path())
    
    filename = dir + "/node_reconstruction.py"
    
    execfile(filename)   