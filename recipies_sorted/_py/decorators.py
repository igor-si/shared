# URL https://www.programiz.com/python-programming/decorator
# Prerequisites for learning decorators
# In order to understand about decorators, 
# we must first know a few basic things in Python.

# We must be comfortable with the fact that, everything in Python
# (Yes! Even classes), are objects. Names that we define are 
# simply identifiers bound to these objects. Functions are 
# no exceptions,they are objects too (with attributes). 
# Various different names can be bound to the same function object.

print "\n Example 1: simple decorator"
def first(msg):
    print(msg)    

first("Hello")

second = first
second("Hello")

print "\n Example 2: "
def inc(x):
    return x + 1

def dec(x):
    return x - 1

def operate(func, x):
    result = func(x)
    return result
# print operate(inc(6),dec(8))

print "\n Example 3: "
def is_called():
    def is_returned():
        print("Hello")
    return is_returned

new = is_called()
#Outputs "Hello"
new()


# Getting back to Decorators
# Functions and methods are called callable as they can be called.

# In fact, any object which implements the special method __call__() 
# is termed callable. So, in the most basic sense, 
# a decorator is a callable that returns a callable.

# Basically, a decorator takes in a function, 
# adds some functionality and returns it.
print "\n Example 4: "
def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

def ordinary():
    print("I am ordinary")
ordinary()
pretty = make_pretty(ordinary)
ordinary = make_pretty(ordinary)

print "\n Example 5:  Decorating Functions with Parameters"
# The above decorator was simple and it only worked with 
# functions that did not have any parameters. What if we had
# functions that took in parameters like below?
def divide(a, b):
    return a/b
# This function has two parameters, a and b. We know, 
#it will give error if we pass in b as 0.
def smart_divide(func):
   def inner(a,b):
      print("I am going to divide",a,"and",b)
      if b == 0:
         print("Whoops! cannot divide")
         return

      return func(a,b)
   return inner

@smart_divide
def divide(a,b):
    return a/b
divide(4,5)
divide(4,0)


# In this manner we can decorate functions that take parameters.
# A keen observer will notice that parameters of the nested inner()
# function inside the decorator is same as the parameters
# of functions it decorates. Taking this into account,
# now we can make general decorators that work 
# with any number of parameter.

# In Python, this magic is done as function(*args, **kwargs).
# In this way, args will be the tuple of positional arguments
# and kwargs will be the dictionary of keyword arguments.
# An example of such decorator will be.
def works_for_all(func):
	def inner(*args, **kwargs):
	    print("I can decorate any function")
	    return func(*args, **kwargs)
	return inner


# Chaining Decorators in Python
print "\n Example 6:  Chaining Decorators in Python"
def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner

def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner

@star
@percent
def printer(msg):
    print(msg)
printer("Hello")

	# # The above syntax of,
	# @star
	# @percent
	# def printer(msg):
	#     print(msg)
	# is equivalent to

	# def printer(msg):
	#     print(msg)
	# printer = star(percent(printer))
