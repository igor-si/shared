


# Example 1: Function to add 3 numbers
print  "\n"*2,"Example 1"
def adder(x,y,z):
    print("sum:",x+y+z)
adder(10,12,13)
# *args (Non Keyword Arguments)
# **kwargs (Keyword Arguments)

# The arguments are passed as a tuple and these passed 
# arguments make tuple
# inside the function with same name as the 
# parameter excluding asterisk *.
# Example 2: Using *args to pass the variable length arguments to the function
print  "\n"*2,"Example 2 args"
def adder(*num):
    sum = 0
    for n in num:
        sum = sum + n
    print("Sum:",sum)

adder(3,5)
adder(4,5,6,7)
adder(1,2,3,5,6)
# In the above program, we used *num as a parameter which allows us to pass
# variable length argument list to the adder() function. Inside the function,
# we have a loop which adds the passed argument and prints the result. 
# We passed 3 different tuples with variable length as an argument to the function.


# Python **kwargs
# Python passes variable length non keyword argument to 
# function using *args but we cannot use this to pass 
# keyword argument. For this problem Python has got 
# a solution called **kwargs, it allows us to pass
# the variable length of keyword arguments to the function.

# The arguments are passed as a dictionary and 
# these arguments make a dictionary inside function
# with name same as the parameter excluding double asterisk **.

# Example 3: Using **kwargs to pass the variable keyword arguments to the function 
print  "\n"*2,"Example 3 kwargs"
def intro(**data):
    print("\n Data type of argument:",type(data))

    for key, value in data.items():
        print("{} is {}".format(key,value))

intro(Firstname="Sita", Lastname="Sharma", Age=22, Phone=1234567890)
intro(Firstname="John", Lastname="Wood", Email="johnwood@nomail.com",
 Country="Wakanda", Age=25, Phone=9876543210)
# In the above program, we have a function intro() with **data 
# as a parameter. We passed two dictionaries with variable argument 
# length to the intro() function. We have for loop inside intro()
 # function which works on the data of passed dictionary and prints the value of the dictionary.


#===========source https://pythontips.com/2013/08/04/args-and-kwargs-in-python-explained/
print "\n"*2,"Example 4 args"
def test_var_args(f_arg, *argv):
    print "first normal arg:", f_arg
    for arg in argv:
        print "another arg through *argv :", arg

test_var_args('yasoob','python','eggs','test')

print  "\n"*2,"Example 5 kwargs"
def greet_me(**kwargs):
    if kwargs is not None:
        for key, value in kwargs.iteritems():
            print "%s == %s" %(key,value)
greet_me(name="yasoob")


print "\n"*2,"Example 6 args"
# first with *args
def test_args_kwargs(arg1, arg2, arg3):
    print "arg1:", arg1
    print "arg2:", arg2
    print "arg3:", arg3

args = ("two", 3,5)
test_args_kwargs(*args)

# now with **kwargs:
kwargs = {"arg3": 3, "arg2": "two","arg1":5}
test_args_kwargs(**kwargs)
arg1: 5
arg2: two
arg3: 3