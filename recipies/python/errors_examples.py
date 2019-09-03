
# URL https://www.programiz.com/python-programming/exceptions
# When writing a program, we, more often than not
#  will encounter errors.

# Error caused by not following the proper structure (syntax)
# of the language is called syntax error or parsing error.

# We can notice here that a colon is missing in the if statement.
# Errors can also occur at runtime and these are called exceptions. 
# They occur, for example, when a file we try to open does 
# not exist (FileNotFoundError), dividing a number by zero 
# (ZeroDivisionError), module we try to import is not found (ImportError) etc.

# Whenever these type of runtime error occur, Python creates
# an exception object. If not handled properly, it prints a 
# traceback to that error along with some details about why that error occurred.


# 1 / 0
# Traceback (most recent call last):
#  File "<string>", line 301, in runcode
#  File "<interactive input>", line 1, in <module>
# ZeroDivisionError: division by zero

# >>> open("imaginary.txt")
# Traceback (most recent call last):
#  File "<string>", line 301, in runcode
#  File "<interactive input>", line 1, in <module>
# FileNotFoundError: [Errno 2] No such file or directory: 'imaginary.txt'

# Exception	Cause of Error
# AssertionError	Raised when assert statement fails.
# AttributeError	Raised when attribute assignment or reference fails.
# EOFError	Raised when the input() functions hits end-of-file condition.
# FloatingPointError	Raised when a floating point operation fails.
# GeneratorExit	Raise when a generator's close() method is called.
# ImportError	Raised when the imported module is not found.
# IndexError	Raised when index of a sequence is out of range.
# KeyError	Raised when a key is not found in a dictionary.
# KeyboardInterrupt	Raised when the user hits interrupt key (Ctrl+c or delete).
# MemoryError	Raised when an operation runs out of memory.
# NameError	Raised when a variable is not found in local or global scope.
# NotImplementedError	Raised by abstract methods.
# OSError	Raised when system operation causes system related error.
# OverflowError	Raised when result of an arithmetic operation is too large to be represented.
# ReferenceError	Raised when a weak reference proxy is used to access a garbage collected referent.
# RuntimeError	Raised when an error does not fall under any other category.
# StopIteration	Raised by next() function to indicate that there is no further item to be returned by iterator.
# SyntaxError	Raised by parser when syntax error is encountered.
# IndentationError	Raised when there is incorrect indentation.
# TabError	Raised when indentation consists of inconsistent tabs and spaces.
# SystemError	Raised when interpreter detects internal error.
# SystemExit	Raised by sys.exit() function.
# TypeError	Raised when a function or operation is applied to an object of incorrect type.
# UnboundLocalError	Raised when a reference is made to a local variable in a function or method, but no value has been bound to that variable.
# UnicodeError	Raised when a Unicode-related encoding or decoding error occurs.
# UnicodeEncodeError	Raised when a Unicode-related error occurs during encoding.
# UnicodeDecodeError	Raised when a Unicode-related error occurs during decoding.
# UnicodeTranslateError	Raised when a Unicode-related error occurs during translating.
# ValueError	Raised when a function gets argument of correct type but improper value.
# ZeroDivisionError	Raised when second operand of division or modulo operation is zero.