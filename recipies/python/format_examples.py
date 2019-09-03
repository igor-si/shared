"Old" '%s %s' % ('one', 'two')
"New" '{} {}'.format('one', 'two')



# URL https://www.programiz.com/python-programming/methods/string/format
# =======================================================================
print "\n Example 1: Basic formatting for default, positional and keyword arguments"
# default arguments
print("Hello {}, your balance is {}.".format("Adam", 230.2346))
# positional arguments
print("Hello {0}, your balance is {1}.".format("Adam", 230.2346))
# keyword arguments
print("Hello {name}, your balance is {blc}.".format(name="Adam", blc=230.2346))
# mixed arguments
print("Hello {0}, your balance is {blc}.".format("Adam", blc=230.2346))

print "\n Example 2: Simple number formatting"
# integer arguments
print("The number is:{:d}".format(123))
# float arguments
print("The float number is:{:f}".format(123.4567898))
# octal, binary and hexadecimal format
print("bin: {0:b}, oct: {0:o}, hex: {0:x}".format(12))

print "\n Example 3: Number formatting with padding for int and floats"
# integer numbers with minimum width
print("{:5d}".format(12))
# width doesn't work for numbers longer than padding
print("{:2d}".format(1234))
# padding for float numbers
print("{:8.3f}".format(12.2346))
# integer numbers with minimum width filled with zeros
print("{:05d}".format(12))
# padding for float numbers filled with zeros
print("{:08.3f}".format(12.2346))


print "\n Example 4: Number formatting for signed numbers"
# show the + sign
print("{:+f} {:+f}".format(12.23, -12.23))
# show the - sign only
print("{:-f} {:-f}".format(12.23, -12.23))
# show space for + sign
print("{: f} {: f}".format(12.23, -12.23))


print '\n Example 5: Number formatting with left, right and center alignment'
# integer numbers with right alignment
print("{:5d}".format(12))
# float numbers with center alignment
print("{:^10.3f}".format(12.2346))
# integer left alignment filled with zeros
print("{:<05d}".format(12))
# float numbers with center alignment
print("{:=8.3f}".format(-12.2346))


#String formatting with format()
print '\n Example 6: String formatting with padding and alignment'
# string padding with left alignment
print("{:5}".format("cat"))
# string padding with right alignment
print("{:>5}".format("cat"))
# string padding with center alignment
print("{:^5}".format("cat"))
# string padding with center alignment
# and '*' padding character
print("{:*^5}".format("cat"))

print "\n Example 7: Truncating strings with format()"
# truncating strings to 3 letters
print("{:.3}".format("caterpillar"))
# truncating strings to 3 letters
# and padding
print("{:5.3}".format("caterpillar"))
# truncating strings to 3 letters,
# padding and center alignment
print("{:^5.3}".format("caterpillar"))


# Formatting class and dictionary members using format()
# Python internally uses getattr() for class members in the form ".age".
# And, it uses __getitem__() lookup for dictionary members in the form "[index]".

print "\n Example 8: Formatting class members using format()"
# define Person class
class Person:
    age = 23
    name = "Adam"

# format age
print("{p.name}'s age is: {p.age}".format(p=Person()))


print "\n Example 9: Formatting dictionary members using format()"
# define Person dictionary
person = {'age': 23, 'name': 'Adam'}
# format age
print("{p[name]}'s age is: {p[age]}".format(p=person))


print "\n Example 9:There's an easier way to format dictionaries in Python using"
# str.format(**mapping).
# define Person dictionary
person = {'age': 23, 'name': 'Adam'}
# format age
print("{name}'s age is: {age}".format(**person))


print "\n Example 10: Dynamic formatting using format()"
# dynamic string format template
string = "{:{fill}{align}{width}}"
# passing format codes as arguments
print(string.format('cat', fill='*', align='^', width=5))
# dynamic float format template
num = "{:{align}{width}.{precision}f}"
# passing format codes as arguments
print(num.format(123.236, align='<', width=8, precision=2))


# Extra formatting options with format()
# format() also supports type-specific formatting options like datetime's
# and complex number formatting.
# format() internally calls __format__() for datetime, while format()
# accesses the attributes of the complex number.
# You can easily override the __format__() method of any object for
# custom formatting

print "\n Example 11: Type-specific formatting with format() and overriding __format__() method"
import datetime
# datetime formatting
date = datetime.datetime.now()
print("It's now: {:%Y/%m/%d %H:%M:%S}".format(date))
# complex number formatting
complexNumber = 1+2j
print("Real part: {0.real} and Imaginary part: {0.imag}".format(complexNumber))
# custom __format__() method
class Person:
    def __format__(self, format):
        if(format == 'age'):
            return '23'
        return 'None'
print("Adam's age is: {:age}".format(Person()))


# You can also use object's __str__() and __repr__() functionality 
# with shorthand notations using format().
# Like __format__(), you can easily override object's __str__()
# and __repr_() methods.

print "\n Example 12: __str()__ and __repr()__ shorthand !r and !s using format()"
# __str__() and __repr__() shorthand !r and !s
print("Quotes: {0!r}, Without Quotes: {0!s}".format("cat"))
# __str__() and __repr__() implementation for class
class Person:
    def __str__(self):
        return "STR"
    def __repr__(self):
        return "REPR"



# ==================================================================

print "\n"*2
# ==== Strings
n = '4'
t = n.zfill(3)
# print t
# 004
# ==== And for numbers:
n = 4
t = '%03d' % n
# print t
# 004

print format(n, '03') # python >= 2.6
# 004

t = '{0:03d}'.format(n)  # python >= 2.6
# print t
# 004

# s = {'first':'python', 'second':'rocks'}
# x = '%(first)s %(second)s' % '{foo:03d}'.format(foo=n)  # python >= 2.6
# 004

t = ('{:03d}'.format(n))  # python >= 2.7 + python3
# print t
# 004

t = ('{0:03d}'.format(n))  # python 3
# print t
# 004

# print(f'{n:03}') # python >= 3.6
# 004


n = 3
str(n).zfill(5)
#'00003'

n = '3'
str(n).zfill(5)
#'00003'

n = '3.0'
str(n).zfill(5)
#'003.0'

# ==================================================================

#============old formatting
s = ['language', 'Python', 'rocks']
some_text = "There is a %s called %s which %s."
x = some_text % tuple(s)

# new formatting
x = '{} {}'.format(*s)

# join tupple members
YourTuple = ('test','bla')
x = " ".join(YourTuple)

#If you want to use a list of items, 
#you can just pass a tuple directly:
s = ['Python', 'rocks']
x = '%s %s' % tuple(s)


s = {'first':'python', 'second':'rocks'}
x = '%(first)s %(second)s' % s

# === List Example
data = ["John", "Doe", 53.44]
format_string = "Hello"
print "Hello %s %s your current balance is %d$" % (data[0],data[1],data[2])
# Hello John Doe your current balance is 53$

# === Tuple example
data = ("John", "Doe", 53.44)
format_string = "Hello"
print "Hello %s %s your current balance is %d$" % (data[0],data[1],data[2])
# Hello John Doe your current balance is 53$

# === List FMT example
fields = [
    'Ghostly',
    'Stack Overflow',
    6129,]

fmt = '''
Welcome back to {}, {}!
Your current reputation sits at {}.
'''
output = fmt.format(*fields)
print output

# URL = https://stackoverflow.com/questions/5299796/how-to-use-list-or-tuple-as-string-formatting-value
# How to use list (or tuple) as String Formatting value
i = 4
tup = (10, 20, 30)
lis = [100, 200, 300]
num = 50
print '%d 	   %s'%(i,tup)
print '%d      %s'%(i,lis)
print '%s'%(tup,)
print '%s'%(lis,)

# formatting list to convert into string
print '\n'.join(["obs%i = mag_%i" % (item, item) for item in range (1, 4)])








#Numbers formatting with format()
# d	Decimal integer
# c	Corresponding Unicode character
# b	Binary format
# o	Octal format
# x	Hexadecimal format (lower case)
# X	Hexadecimal format (upper case)
# n	Same as 'd'. Except it uses current locale setting for number separator
# e	Exponential notation. (lowercase e)
# E	Exponential notation (uppercase E)
# f	Displays fixed point number (Default: 6)
# F	Same as 'f'. Except displays 'inf' as 'INF' and 'nan' as 'NAN'
# g	General format. Rounds number to p significant digits. (Default precision: 6)
# G	Same as 'g'. Except switches to 'E' if the number is large.
# %	Percentage. Multiples by 100 and puts % at the end.



# Number formatting with alignment
# The operators <, ^, > and = are used for alignment when assigned
# a certain width to the numbers.

# <	Left aligned to the remaining space
# ^	Center aligned to the remaining space
# >	Right aligned to the remaining space
# =	Forces the signed (+) (-) to the leftmost position

# = STRFTIME
# http://strftime.org/








