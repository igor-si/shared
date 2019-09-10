import subprocess
import signal
import os
import re
import operator
import logging

# === Kill all processes by mask
def killHoudini():
	p = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
	out, err = p.communicate()
	#"gives you ps -A's output in the out variable (a string). 
	# You can break it down into lines and loop on them...:"
	pattern = (r'houdini') 
	for line in out.splitlines():
		if 'pattern' in line:
			pid = int(line.split(None, 1)[0])
			print "killing", pid
			# os.kill(pid, signal.SIGKILL)

killHoudini()
# # =========================================


def getHoudiniInstances():
	p = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
	out,err = p.communicate()
	pattern = (r'houdini')
	houdini_pids = [int(x.split(None,1)[0]) for x in out.splitlines() if re.search(pattern,x)]
	return houdini_pids
print "getHoudiniInstances",getHoudiniInstances()

def getOutputDict():
	lines = subprocess.check_output(['ps','-xacuww']).splitlines()	
	header = lines[0].split()
	del lines[0]
	mapped_dict = {}
	for num,l in enumerate(lines):
		mapped = zip(header,l.split())
		mapped_dict[num] = (dict((x,y) for x,y in mapped) )
	return mapped_dict
	
def sortTasksByMaxMem(pids_dict=None,pids_list=None):
	if pids_list is None: pids_list = getHoudiniInstances()
	if pids_dict is None: pids_dict=getOutputDict()
	pid = None
	mem_check = 0
	command = None
	for k,v in pids_dict.iteritems():
		if int(v['PID']) in pids_list:
			mem_current = float(v[r"%MEM"])
			mem_check = max(mem_check,mem_current)
			# print int(v['PID'])
			if mem_check == mem_current: pid=int(v['PID']); command = v["COMMAND"]
	return pid

print "sortTasksByMaxMem",sortTasksByMaxMem()

def kill_proc():
	import psutil
	# psutil can find process by name and kill it:
	PROCNAME = "python.exe"
	for proc in psutil.process_iter():
	    # check whether the process name matches
	    if proc.name() == PROCNAME:
	        proc.kill()


# Get stat by pid
# pid = 45504
# print subprocess.check_output(['ps', 'v', '-p', str(pid)])






# list(map(lambda x: x.split(' ')[0], list_m.split('\n'))
# Which is splitting you string line by line, then split by space and get first element.

# In Linux, how to tell how much memory processes are using?
# BASH
# First get the pid:
# ps ax | grep [process name]

# And then:
# top -p PID

# You can watch various processes in the same time:
# top -p PID1 -p PID2 
# pmap -x <process pid
