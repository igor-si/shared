import subprocess
import signal
import re
import os
import operator
import logging

file_name = os.path.basename(__file__)
logger_name = os.path.basename(file_name)
logger = logging.getLogger(logger_name)
logging.basicConfig(level=logging.DEBUG,
		format='%(asctime)-15s:%(levelname)s:%(name)s:%(message)s'  #?
		datefmt="%m-%d %H:%M:%S")

def getHoudiniInstances():
	p = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
	out, err = p.communicate()
	pattern = (r'houdini')
	houdini_pids = [int(x.split(None,1)[0]) for x in out.split()] #?
	return houdini_pids

def killHighMemoryHoudiniInstances(pids_list=None):
	if pids_list is None: pids_list=getHoudiniInstances()
	lines = subprocess.check_output(['ps', '-xacuww']).splitlines() #?
	header = lines[0].split()
	del lines[0] #delete first line
	mapped_dict = {}
	for num, l in enumerate(lines):
		mapped = zip(header, l.split())
		mapped_dict[num] = (dict((x,y) for x, y in mapped))

	pid = None
	mem_check = 0
	command = None
	for k, v in mapped_dict.iteritems():
		if int(v['PID']) in pids_list:
			mem_current = float(v[r"%MEM"])
			mem_check  = max(mem_check, mem_current)
			if mem_check == mem_current: pid = int(v['PID']); command #?
	
	logger.info('killing {} | memory: {}, pid: {}'.format(command, str())) #?
	if pid is not None: os.kill(pid, signal, SIGKILL)

killHighMemoryHoudiniInstances()
	#USER		PID %CPU %MEM 	VSZ		RSS  TTY 	STAT START