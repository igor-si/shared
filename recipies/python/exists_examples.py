
import os  
# URL https://stackabuse.com/python-check-if-a-file-or-directory-exists/
# Checking if a File Exists
# isfile is actually just a helper method that internally 
# uses os.stat and stat.S_ISREG(mode) underneath, 
# which we'll touch on later.
os.path.isfile('./file.txt')    # True  
os.path.isfile('./link.txt')    # True  
os.path.isfile('./fake.txt')    # False  
os.path.isfile('./dir')    # False  
os.path.isfile('./sym')    # False  
os.path.isfile('./foo')    # False  

# Checking if a Directory Exists
os.path.isdir('./file.txt')    # False  
os.path.isdir('./link.txt')    # False  
os.path.isdir('./fake.txt')    # False  
os.path.isdir('./dir')    # True  
os.path.isdir('./sym')    # True  
os.path.isdir('./foo')    # False  

# Advanced
# Like all the other methods we'v already covered,
 # os.stat follows symlinks, so if you want to get the stat info on a link, try using os.lstat() instead



# Since every operating system is different, the data provided by os.stat varies greatly. 
# Here is just some of the data that each OS has in common:

st_mode: # protection bits
st_uid: # owner's user id
st_gid: # owner's group id
st_size: # size of file in bytes
st_atime: # time of last access
st_mtime: # time of last modification
st_ctime: #time of last metadata change on Unix, 
# or time of creation on Windows

# You can then use this data with the stat module to get
# interesting information, like whether a path points 
# to a socket (stat.S_ISSOCK(mode)), or if a file is 
# actually a named pipe (stat.S_ISFIFO(mode)).

# self.path = os.path.join("/jobs",self.show,self.seq,self.shot,"houdini/fx",self.user,"fx_"+self.elementName)
os.path.join(hip,pb,element,element,"v"+str("%04d" % version) )
os.path.join(self.getInfoPath(),self.shot+"_info"+".json")

def function():
	pass

#====Example, this is a snippet.

#"------------------------------------"
