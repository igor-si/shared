# check if int or float
x = 12
print isinstance(x, int)

y = 12.0
print isinstance(y, float)

# As pointed out, in case of long integers
# the above won't work. So you need to do:
x = 12L
import numbers
print "example with numbers",isinstance(x, numbers.Integral)
print "example with numbers",isinstance(x, int)


n = 0.2
n = 1
# n = "1"
print "example with tuple ",isinstance(n, (int, long, float)) 


# One-liner:
# isinstance(yourNumber, numbers.Real)
# isinstance(99**10,int)

import numbers

someInt = 10
someLongInt = 100000L
someFloat = 0.5

print "example with numbers",isinstance(someInt, numbers.Real)
print "example with numbers",isinstance(someLongInt, numbers.Real)
print "example with numbers",isinstance(someFloat, numbers.Real)
