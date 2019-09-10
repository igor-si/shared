



# ====== To avoid issues with floating-point rounding errors, 
# you can use decimal.Decimal objects:
"""
>>> rounded_tuple(('string 1', 1234.55555, 5.66666, 'string2'))
('string 1', Decimal('1234.56'), Decimal('5.67'), 'string2')
"""
from decimal import Decimal
def round_if_float(value):
    if isinstance(value, float):
        return Decimal(str(value)).quantize(Decimal('1.00'))
    else:
        return value

def rounded_tuple(tup):
    return tuple(round_if_float(value) for value in tup)

# List comprehension solution:
t = ('string 1', 1234.55555, 5.66666, 'string2')
solution = tuple([round(x,2) if isinstance(x, float) else x for x in t])


# The general solution would be: LAMBDA
t2 = tuple(map(lambda x: isinstance(x, float) and round(x, 2) or x, t))
print t2
# ('string 1', 1234.56, 5.67, 'string2')


# The round() method takes two parameters:
# number - number that is to be rounded
# ndigits (Optional) - number upto 
# which the given number is to be rounded
print(round(203414343.665, 2))