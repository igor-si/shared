

# checj access time of file:
(mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(file)
print "last access: %s" % time.ctime(atime)
# I recommend you to check official info at os.stat() documentation:
# To check creation&modification dates

print "last modified: %s" % time.ctime(os.path.getmtime(file))
print "created: %s" % time.ctime(os.path.getctime(file))
# OR
(mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(file)
print "Modification date: %s" % time.ctime(mtime)
print "Creation date: %s" % time.ctime(ctime)


# how to find the owner of a file or directory in python

from os import stat
from pwd import getpwuid

def find_owner(filename):
    return getpwuid(stat(filename).st_uid).pw_name



# os.stat(path)
#  Perform the equivalent of a stat() system call on the given path. 
#  (This function follows symlinks; to stat a symlink use lstat().)

# The return value is an object whose attributes correspond to the 
# members of the stat structure, namely:

# - st_mode - protection bits,
# - st_ino - inode number,
# - st_dev - device,
# - st_nlink - number of hard links,
# - st_uid - user id of owner,
# - st_gid - group id of owner,
# - st_size - size of file, in bytes,
# - st_atime - time of most recent access,
# - st_mtime - time of most recent content modification,
# - st_ctime - platform dependent; time of most recent metadata 
#              change on Unix, or the time of creation on Windows)    