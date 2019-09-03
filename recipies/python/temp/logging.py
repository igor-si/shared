import logging

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

def add(x,y):
	return x+y

def subtract(x,y):
	return x-y

def multiply(x,y):
	return x*y

def divide(x,y):
	return x/y

num_1 = 10
num_2 = 5

add_result = add(num_1,num_2)
print('Add: {} + {} = {}'.format(num_1,num_2,add_result))

