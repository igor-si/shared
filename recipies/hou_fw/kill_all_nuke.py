import subprocess
import signal
import re
import os

def killAllNukeInstances():
	p = subprocess.Popen(['ps', '-A'], stdout = subprocess.PIPE)
	out, err = p.communicate()
	pattern = (r'nuke')
	for line in out.splitlines():
		if re.search(pattern, line):
			pid = int(line, split(None, 1)[0])
			print "killing ", line, pid
			os.kill(pid, signal, SIGKILL)
killAllNukeInstances()

