

def make_flat_list_of_lists():
	print '\n',"How to make a flat list out of list of lists?"
	# reduce(lambda x, y: x.extend(y), l)
	l = [[1, 2, 3], [4, 5, 6], [7], [8, 9]]
	flatten = lambda l: [item for sublist in l for item in sublist]
	print flatten

	from functools import reduce 
	l = [[1,2,3],[4,5,6], [7], [8,9]]
	reduce(lambda x,y: x+y,l)
	print l


# ======================================================================
#What are lambda functions in Python?
#In Python, anonymous function is a function that is defined without a name.
#
#While normal functions are defined using the def keyword, 
#in Python anonymous functions are defined using the lambda keyword.
#
#Hence, anonymous functions are also called lambda functions.
#
#		How to use lambda Functions in Python?
#A lambda function in python has the following syntax.
#
#Syntax of Lambda Function in python
#lambda arguments: expression

#Lambda functions can have any number of arguments but only one expression. 
#The expression is evaluated and returned. Lambda functions can be used
#wherever function objects are required.


# ======================================================================
#Example of Lambda Function in python
#Here is an example of lambda function that doubles the input value.

# 		Program to show the use of lambda functions
def simple_lambda_function():
	print '\n'*2,'Example of Lambda Function in python '
	double = lambda x: x * 2
	print(double(5))

#In the above program, lambda x: x * 2 is the lambda function. 
#Here x is the argument and x * 2 is the expression that gets evaluated and returned.
#This function has no name. It returns a function object which 
#is assigned to the identifier double. We can now call it as a normal function. The statement
def double_lambds():
	double = lambda x: x * 2
#is nearly the same as
def double(x):
   return x * 2

#Use of Lambda Function in python

#We use lambda functions when we require a nameless function for a short period of time.
#
#In Python, we generally use it as an argument to a higher-order function
# (a function that takes in other functions as arguments). 
#Lambda functions are used along with built-in functions like filter(), map() etc.

#		====Example use with filter()
#The filter() function in Python takes in a function and a list as arguments.
#The function is called with all the items in the list and a new list is returned
# which contains items for which the function evaluats to True.

#Here is an example use of filter() function to filter out only even numbers from a list.
def lambds_with_filter():
	print '\n'*2,'Example of Lambda Function with filter() '
	my_list = [1, 5, 4, 6, 8, 11, 3, 12]
	new_list = list(filter(lambda x: (x%2 == 0) , my_list))
	print(new_list)



#		====Example use with map()
#The map() function in Python takes in a function and a list.
#The function is called with all the items in the list and
# a new list is returned which contains items returned by that function for each item.
#Here is an example use of map() function to double all the items in a list.
print '\n'*2,'Example of Lambda Function with map() '
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(map(lambda x: x * 2 , my_list))
print(new_list)


#	Powers of 2 Using Anonymous Function
#In the program below, we have used anonymous (lambda) 
#function inside the map() built-in function to find the powers of 2.
print '\n'*2,'Powers of 2 Using Anonymous Function'
# Python Program to display the powers of 2 using anonymous function

# Change this value for a different result
terms = 10

# Uncomment to take number of terms from user
#terms = int(input("How many terms? "))

# use anonymous function
result = list(map(lambda x: 2 ** x, range(terms)))

# display the result
print("The total terms is:",terms)
for i in range(terms):
   print("2 raised to power",i,"is",result[i])

#==========
#! === filter()
# filter(lambda x : x % 3 == 0, list)   


# ======== return sorted lambda
return sorted(text_list, key=lambda x:re.split(r'(\d+)',x) )


# ===============
var1 = [['a', 'b'], ['c', 'd']]
f = lambda x: list(map(lambda y: y.extend('\n'), x))

# ===========
f = lambda x: x + ['\n']