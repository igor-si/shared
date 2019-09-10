import os

#How do I get the path and name of the file 
#that is currently executing?
this_file = os.path.realpath(__file__)
path = os.path.split(this_file)[0]

#===================limit depth of walk dir
for root,dirs,files in os.walk(path):
	if root[len(path)+1:].count(os.sep)<2: #limit depth
		for d in dirs: #print d
			print(os.path.join(root,d))