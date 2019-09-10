import logging
import os
# DEBUG. Detailed information, typically of interest
# only when diagnostic problem

# INFO. Confirmation that things are working expected

# WARNING. An indicator that something unexpected happened, or indicative
# of some problem in the near future (e.g. "disp space low").space
# the software is still working as expected

# ERROR. Due to a more serious problem. The software has not been able
# to perform some function

# CRITICAL. A serious error, indicating that the program itself
# may be unable to continue running
#============================================================

# logging_level = logging.DEBUG
# logging_level = logging.INFO

# # Basic configuration
# logging.basicConfig(filename=log_file,level=logging.INFO,
# 	format='%(asctime)s:%(levelname)s:%(name)s:%(message)s:')

script_dir = os.path.dirname(__file__)
log_file = os.path.join(script_dir,'trash','test.log')

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('\n%(asctime)s:%(levelname)s:%(name)s:%(message)s:') #%(asctime)s #%(pathname)s:

file_handler = logging.FileHandler(log_file)
file_handler.setFormatter(formatter)
#file_handler.setLevel(logging.ERROR) #level to ERROR
file_handler.setLevel(logging.INFO)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler) #add log debug handler in the console


def add(x,y):
	return x+y

def subtract(x,y):
	return x-y

def multiply(x,y):
	return x*y

def divide(x,y):
	try:
		result = x/y
	except ZeroDivisionError:
		# logger.error("divided by zero") # for grab simple error
		logger.exception("divided by zero") # for grab traceback simple error
	else:
		return x/y

num_1 = 10
num_2 = 2

add_result = add(num_1,num_2)
divide_result = divide(num_1,num_2)
multiply_result = multiply(num_1,num_2)
# print('Add: {} + {} = {}'.format(num_1,num_2,add_result))
# logging.warning('Add: {} + {} = {}'.format(num_1,num_2,add_result))
# logging.info('Add: {} + {} = {}'.format(num_1,num_2,add_result))
logger.info('Add: {} + {} = {}'.format(num_1,num_2,add_result))





# args				You shouldnt need to format this yourself.	The tuple of arguments merged into msg to produce message, or a dict whose values are used for the merge (when there is only one argument, and it is a dictionary).
# asctime			%(asctime)s			Human-readable time when the LogRecord was created. By default this is of the form 2003-07-08 16:49:45,896 (the numbers after the comma are millisecond portion of the time).
# created			%(created)f			Time when the LogRecord was created (as returned by time.time()).
# exc_info			You shouldnt need to format this yourself.	Exception tuple (a la sys.exc_info) or, if no exception has occurred, None.
# filename			%(filename)s		Filename portion of pathname.
# funcName			%(funcName)s		Name of function containing the logging call.
# levelname			%(levelname)s		Text logging level for the message ('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL').
# levelno			%(levelno)s			Numeric logging level for the message (DEBUG, INFO, WARNING, ERROR, CRITICAL).
# lineno			%(lineno)d			Source line number where the logging call was issued (if available).
# module			%(module)s			Module (name portion of filename).
# msecs				%(msecs)d			Millisecond portion of the time when the LogRecord was created.
# message			%(message)s			The logged message, computed as msg % args. This is set when Formatter.format() is invoked.
# msg				You shouldnt need to format this yourself.	The format string passed in the original logging call. Merged with args to produce message, or an arbitrary object (see Using arbitrary objects as messages).
# name				%(name)s			Name of the logger used to log the call.
# pathname			%(pathname)s		Full pathname of the source file where the logging call was issued (if available).
# process			%(process)d			Process ID (if available).
# processName		%(processName)s		Process name (if available).
# relativeCreated	%(relativeCreated)d	Time in milliseconds when the LogRecord was created, relative to the time the logging module was loaded.
# thread			%(thread)d			Thread ID (if available).
# threadName		%(threadName)s		Thread name (if available).


# ==================================================================
# Q. Python logging module is printing lines multiple times
# URL https://stackoverflow.com/questions/17745914/python-logging-module-is-printing-lines-multiple-times
# In my case , the root loggers handler were also being called , 
# All I did was to set propagate attribute of logger instance to False.
# import logging
# logger = logging.getLogger("MyLogger")

# # stop propagting to root logger
# logger.propagate = False

# other log configuration stuff
# ....
# ==================================================================

#=========== Simple Logging
logger_name =  os.path.basename(__file__) + "2"
logger = logging.getLogger(logger_name)
logging.basicConfig(level=logging.DEBUG,
	format='%(asctime)s:%(levelname)s:%(name)s:%(message)s:'
	)
logger.info('multiply: {} + {} = {}'.format(num_1,num_2,multiply_result))

#=========== Advanced Logging
logger_name =  os.path.basename(__file__) + "3"
logger = logging.getLogger(logger_name)
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s:')
file_handler = logging.FileHandler(os.path.join(os.path.dirname(__file__),'trash','test2.log'))
logger.addHandler(file_handler)
logger.info('advanced multiply: {} + {} = {}'.format(num_1,num_2,multiply_result))





#==============basic config example
logging.basicConfig(
    filename='HISTORYlistener.log',
    level=logging.DEBUG,
    format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
    datefmt="%Y-%m-%d %H:%M:%S")



#=====================formatter
# create formatter
formatter = logging.Formatter("%(asctime)s;%(levelname)s;%(message)s")
# changed formatting
formatter = logging.Formatter("%(asctime)s;%(levelname)s;%(message)s",
                              "%Y-%m-%d %H:%M:%S")