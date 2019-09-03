import hou
import os
import sys

def splitall(path):
    allparts = []
    while 1:
        parts = os.path.split(path)
        if parts[0] == path:  # sentinel for absolute paths
            allparts.insert(0, parts[0])
            break
        elif parts[1] == path: # sentinel for relative paths
            allparts.insert(0, parts[1])
            break
        else:
            path = parts[0]
            allparts.insert(0, parts[1])
    return allparts




def setupQuick():
    print "scene quick setup"
    filepath = hou.hipFile.name()
    path_list = splitall(filepath)
    shot = path_list[-2]
    show = path_list[-3]
    hou.putenv("SHOT",shot)
    hou.putenv("SHOW",show)

    cache = "/studio/cache/job"
    hou.putenv("CACHE",cache)	
    # hou.putenv("TEST","blabla")	
    print "setting SHOW to %s" % show
    print "setting SHOT to %s" % shot
    print "setting CACHE to %s" % cache

try: setupQuick()
except:print "cant setup 456"
