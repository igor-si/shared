import hou
import os
import datetime
import shutil
import logging
n = hou.pwd()

logging.basicConfig(
        format ='[%(asctime)-15s:%(levelname)-8s]:%(name)s:%(message)s:')
logger = logging.getLogger('filecache')
logger.setLevel(logging.INFO)

def saveFileTo(path=None,copymode="versions"):
    timestamp = str(datetime.datetime.now().strftime("%m%d%H%M%S"))
    
    filepath = ""
    if copymode == "versions":
        filepath = hou.hipFile.path()

    if copymode == "cache":
        filepath_parms = [x for x in n.parms() if x.name() == "file"] or None
        if filepath_parms:
            filepath = filepath_parms[0].evalAsString()
    
    version = 1
    version_parms = [x for x in n.parms() if x.name() == "version"] or None

    if version_parms:
         version = version_parms[0].eval()

    element = ""
    element_parms = [x for x in n.parms() if x.name() == "element"] or None
    if element_parms:
        element = element_parms[0].eval()

    filepath_root,filepath_basename = os.path.split(filepath)  
    filepath_new = os.path.join(filepath_root,"versions","filecache_backup")
    filename = "{filename}__{element}__{filecache}_v{version}_{timestamp}.{ext}".format(
            filename = hou.hipFile.basename().split(".")[0],
            element = element,
            filecache = n.parent().name(),
            version = str(version).zfill(3),
            timestamp = timestamp,
            ext = "hip"
            )
            
    if not os.path.exists(filepath_new):
        os.makedirs(filepath_new)

    try:
        shutil.copy2(hou.hipFile.name(), os.path.join(filepath_new,filename))
        logger.info('\ncopying {} \n to: {}\n'.format(
                hou.hipFile.basename(),os.path.join(filepath_new,filename)) )
        
    except (RuntimeError, TypeError, NameError):
        print "cannot copy {} to {}".format(hou.hipFile.name(),filepath_new)

def test():
    saveFileTo()


    n=hou.pwd();nn=hou.node(n.path()+"/CONTROL");nn.parm("test").pressButton()