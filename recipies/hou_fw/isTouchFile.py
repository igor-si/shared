import os,sys,fnmatch,subprocess
import logging
from datetime import datetime,timedelta
import pwd
import re
import time



























def touchFile(path=""):
	print "path = ",path
	subdirs = [x[0] for x in os.walk(path)]
	[logget.info("touching {}".format(x)) for x in subdirs]
	for subdir in subdirs:
		curPath = os.path.join(subdir,subdir)
		curStr = "touch"+curPath
		subprocess.call(curStr,shell=True)

		files = os.walk(subdir).next()[2]
		for f in files:
			curPath = os.path.join(subdir,f)
			curStr = "touch "=curPath
			subprocess.call(curStr,shell=True)

			fhandle = open(curPath,'a')
			os.utime(curPath,None)
			fhandle.close()
			logger.info("touching {}".format(curPath))

def touchFileIfTime(path=None):
	time_check =4 
	now = datetime.utcnow()
	acess_time = datetime.utcfromtimestamp(os.path.getmtime(path))
	diff_time = now-acess_time
	hours,remainder = divmod(diff_time.seconds,3600)
	minutes,seconds = divmod(remainder,60)
	hours,minutes,seconds = ["{:02d}".format(x) for x in [hours,minutes,seconds]]
	
	if (diff_time>timedelta(time_check)):
		touchFile(path)	
		return path
	else:
		logger.info("time delta = {}:{}:{}, delta is less then threshold, \
					skipping {}".format(hours,minutes,seconds,path))
		return None		
























































