

# URL https://www.geeksforgeeks.org/multiple-exception-handling-in-python/


# If you can handle different exceptions all using a single
# block of code, they can be grouped together in a tuple
# as shown in the code given below :

def single_handling():
	try: 
	    client_obj.get_url(url) 
	except (URLError, ValueError, SocketTimeout): 
	    client_obj.remove_url(url) 
	# The remove_url() method will be called if any 
	# of the listed exceptions occurs.


# if one of the exceptions has to be handled differently,
# then put it into its own except clause as shown: 

def multiple_handling():
	try: 
	    client_obj.get_url(url) 
	except (URLError, ValueError): 
	    client_obj.remove_url(url) 
	except SocketTimeout: 
	    client_obj.handle_url_timeout(url) 


def grouped_handling():
	try: 
	    f = open(filename) 
	except (FileNotFoundError, PermissionError): 
	    pass 

# Except statement can be re-written as in the code given below.
# This works because OSError is a base class that's
# common to both the FileNotFoundError and PermissionError exceptions.

# Although it's not specific to handle multiple exceptions per se,
# it is worth noting that one can get a handle to the thrown
# exception using them as a keyword as shown in the code

def multiple_handling():
	try: 
	    f = open(filename) 
	  
	except OSError as e: 
	    if e.errno == errno.ENOENT: 
	        logger.error('File not found') 
	    elif e.errno == errno.EACCES: 
	        logger.error('Permission denied') 
	    else: 
	        logger.error('Unexpected error: % d', e.errno) 


#  Create situations where multiple except clauses might match
def multiple_custom_exceptions():
	try: 
	    f = open('missing') 
	except OSError: 
	    print('It failed') 
	except FileNotFoundError: 
	    print('File not found') 



def multiple_exceptions():
	try:
   		pass
	except FirstException:
   		handle_first_one()

	except SecondException:
   		handle_second_one()

	except (ThirdException, FourthException, FifthException) as e:
   		handle_either_of_3rd_4th_or_5th()

	except Exception:
   		handle_all_other_exceptions()


try: 
	shutil.rmtree(self.tempdir)
except OSError as e: 
	print ("Error: %s - %s." % (e.filename, e.strerror))