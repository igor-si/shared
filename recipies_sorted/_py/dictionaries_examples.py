	
def _METHODS():
	clear() # Removes all Items
	copy()	# Returns Shallow Copy of a Dictionary
	fromkeys()	# creates dictionary from given sequence
	get()	# Returns Value of The Key
	items()	# returns view of dictionary's (key, value) pair
	keys()	# Returns View Object of All Keys
	popitem()	# Returns & Removes Element From Dictionary
	setdefault()	# Inserts Key With a Value if Key is not Present
	pop()	# removes and returns element having given key
	values() #	returns view of all values in dictionary
	update() #	Updates the Dictionary
	any()	# Checks if any Element of an Iterable is True
	all()	# returns true when all elements in iterable is true
	ascii()	# Returns String Containing Printable Representation
	bool()	# Converts a Value to Boolean
	dict()	#Creates a Dictionary
	enumerate() #	Returns an Enumerate Object
	filter()	# constructs iterator from elements which are true
	iter()	# returns iterator for an object
	len()	# Returns Length of an Object
	max()	# returns largest element
	min()	# returns smallest element
	map()	#Applies Function and Returns a List
	sorted()	# returns sorted list from a given iterable
	sum()	# Add items of an Iterable
	zip()	# Returns an Iterator of Tuples
	pass

def _update():
	# === === === update
	# They update() method updates the dictionary with elements 
	# from a dictionary object or an iterable object of key/value pairs.
	# It doesn't return any value (returns None).
	print "\n"*2,"Example 1: How update() works in Python?"
	d = {1: "one", 2: "three"}
	d1 = {2: "two"}

	# updates the value of key 2
	d.update(d1)
	print(d),"updates the value of key 2"

	d1 = {3: "three"}
	# adds element with key 3
	d.update(d1)
	print(d),"adds element with key 3"

	# Example 2: How update() Works With an Iterable?
	d = {'x': 2}
	d.update(y = 3, z = 0)
	print(d)

	data['a']=1  
	data.update({'a':1})
	data.update(dict(a=1))
	data.update(a=1)


# _update()

def _popitem():
	# --- --- --- --- --- --- ---  
	#			popitem()

	# returns an arbitrary element (key, value) pair from the dictionary
	# removes an arbitrary element (the same element which is returned)
	# from the dictionary.
	# Note: Arbitrary elements and random elements are not same. 
	# The popitem() doesn't return a random element. 
	print "\n"*2,"Example: How popitem() works?"
	person = {'name': 'Phill', 'age': 22, 'salary': 3500.0}
	result = person.popitem()
	print('person = ',person)
	print('Return Value = ',result),"Example: How popitem() works?"
# _popitem()

def _setdefault():
	# 			setdefault() 
	# The setdefault() takes maximum of two parameters:
	# key - key to be searched in the dictionary
	# default_value (optional) - key with a value default_value is
	# inserted to the dictionary if key is not in the dictionary.
	# If not provided, the default_value will be None.
	print "\n"*2,"Example 1: How setdefault() works when key is in the dictionary?"
	person = {'name': 'Phill', 'age': 22}
	age = person.setdefault('age')
	print('person = ',person)
	print('Age = ',age),

	print "\n"*2,"Example 2: How setdefault() works when key is not in the dictionary?"
	person = {'name': 'Phill'}
	# key is not in the dictionary
	salary = person.setdefault('salary')
	print('person = ',person)
	print('salary = ',salary)
	# key is not in the dictionary
	# default_value is provided
	age = person.setdefault('age', 22)
	print('person = ',person)
	print('age = ',age)
# _setdefault()

def _filter():
	# 				filter()
	# In simple words, the filter() method filters the 
	# given iterable with the help of a function that 
	# tests each element in the iterable to be true or not.

	# The filter() method takes two parameters:

	# function - function that tests if elements of an 
	# iterable returns true or false
	# If None, the function defaults to Identity function 
	# - which returns false if any elements are false
	# iterable - iterable which is to be filtered,
	# could be sets, lists, tuples, or containers of any iterators

	# The filter() method returns an iterator that passed the
	# function check for each element in the iterable.
	# list of alphabets
	print "\n"*2,"Example 1: How filter() works for iterable list?"
	alphabets = ['a', 'b', 'd', 'e', 'i', 'j', 'o']
	# function that filters vowels
	def filterVowels(alphabet):
	    vowels = ['a', 'e', 'i', 'o', 'u']

	    if(alphabet in vowels):
	        return True
	    else:
	        return False
	filteredVowels = filter(filterVowels, alphabets)
	print('The filtered vowels are:')
	for vowel in filteredVowels:
	    print(vowel)

	print "\n","Example 2: How filter() method works without the filter function?"
	# random list
	randomList = [1, 'a', 0, False, True, '0']
	filteredList = filter(None, randomList)
	print('The filtered elements are:')
	for element in filteredList:
	    print(element)
# _filter()

def _map():
	# 			map() Parameter
	# function - map() passes each item of the iterable to this function.
	# iterable iterable which is to be mapped

	# The map() function applies a given to function to 
	# each item of an iterable and returns a list of the results.
	# The returned value from map() (map object) then
	# can be passed to functions like list() 
	# (to create a list), set() (to create a set) and so on.
	print "\n"*2,"Example 1: How map() works?"
	def calculateSquare(n):
	  return n*n

	numbers = (1, 2, 3, 4)
	result = map(calculateSquare, numbers)
	print(result)

	# converting map object to set
	numbersSquare = set(result)
	print(numbersSquare),"converting map object to set"

	# Since map() expects a function to be passed in,
	# lambda functions are commonly used while working with map() functions.

	# A lambda function is a function without a name. 
	# Visit this page to learn more about Python lambda Function.
	print "\n"*2,"Example 2: How to use lambda function with map()?"
	numbers = (1, 2, 3, 4)
	result = map(lambda x: x*x, numbers)
	print(result)

	# converting map object to set
	numbersSquare = set(result)
	print(numbersSquare),"converting map object to set"


	print"\n"*2,"Example 3: Passing Multiple Iterators to map() Using Lambda"
	num1 = [4, 5, 6]
	num2 = [5, 6, 7]

	result = map(lambda n1, n2: n1+n2, num1, num2)
	print(list(result))
# _map()

def _zip():
	# 		zip() Parameters
	# The zip() function takes:
	# iterables - can be built-in iterables (like: list, string, dict),
	# or user-defined iterables (object that has __iter__ method).


	# The zip() function returns an iterator of tuples based on 
	# the iterable object.

	# If no parameters are passed, zip() returns an empty iterator
	# If a single iterable is passed, zip() returns an iterator of
	# 1-tuples. Meaning, the number of elements in each tuple is 1.
	# If multiple iterables are passed, ith tuple contains ith 
	# Suppose, two iterables are passed; one iterable containing 3 
	# and other containing 5 elements. Then, the returned iterator has 
	# 3 tuples. It's because iterator stops when shortest iterable is exhaused.
	print "\n"*2,"Example 1: How zip() works in Python?"
	numberList = [1, 2, 3]
	strList = ['one', 'two', 'three']

	# No iterables are passed
	result = zip()

	# Converting itertor to list
	resultList = list(result)
	print(resultList),"Converting itertor to list"

	# Two iterables are passed
	result = zip(numberList, strList)

	# Converting itertor to set
	resultSet = set(result)
	print(resultSet),"Converting itertor to set"

	print "\n"*2,"Example 2: Different Number of Elements in Iterables Passed to zip()"
	numbersList = [1, 2, 3]
	strList = ['one', 'two']
	numbersTuple = ('ONE', 'TWO', 'THREE', 'FOUR')

	result = zip(numbersList, numbersTuple)

	# Converting to set
	resultSet = set(result)
	print(resultSet)

	result = zip(numbersList, strList, numbersTuple)

	# Converting to set
	resultSet = set(result)
	print(resultSet)

	print "\n"*2,"Example 3: Unzipping the Value Using zip()"
	coordinate = ['x', 'y', 'z']
	value = [3, 4, 5, 0, 9]

	result = zip(coordinate, value)
	resultList = list(result)
	print(resultList)

	c, v =  zip(*resultList)
	print('c =', c)
	print('v =', v)

	#How can I take two tuples to produce a dictionary? 
	x = (1,2,4)
	y = (5,6,7)
	dict(zip(y,x))


# _zip()

def _clear():
	# 				clear() Parameters
	# The clear() method doesn't take any parameters.
	# The clear() method doesn't return any value (returns None).
	print "\n"*2,"Example 1: How clear() method works for dictionaries?"
	d = {1: "one", 2: "two"}
	d.clear()
	print('d =', d),"Example 1: How clear() method works for dictionaries?"
# _clear()

def _copy():
	# 			Dictionary copy()
	# They copy() method returns a shallow copy of the dictionary.
	print "\n"*2,"Example 1: How copy works for dictionaries?"
	original = {1:'one', 2:'two'}
	new = original.copy()

	print('Orignal: ', original)
	print('New: ', new)

	# Difference in Using copy() method, and = Operator to Copy Dictionaries
	# When copy() method is used, a new dictionary is created which 
	# is filled with a copy of the references from the original dictionary.
	# When = operator is used, a new reference to the original dictionary is created.
 	print "\n"*2,"Example 2: Using = Operator to Copy Dictionaries"
 	original = {1:'one', 2:'two'}
	new = original

	# removing all elements from the list
	new.clear()
	print('new: ', new)
	print('original: ', original)

	print "\n"*2,"Example 3: Using copy() to Copy Dictionaries"
	original = {1:'one', 2:'two'}
	new = original.copy()
	# removing all elements from the list
	new.clear()
	print('new: ', new)
	print('original: ', original)
# _copy()

def _fromkeys():
	# Python Dictionary fromkeys()
	# The fromkeys() method creates a new dictionary from the given
	# sequence of elements with a value provided by the user.

	# The syntax of fromkeys() method is:
	# dictionary.fromkeys(sequence[, value])

	# The fromkeys() method takes two parameters:

	# sequence - sequence of elements which is to be used as keys for the new dictionary
	# value (Optional) - value which is set to each each element of the dictionary

	print "\n"*2,"Example 1: Create a dictionary from a sequence of keys"
	# vowels keys
	keys = {'a', 'e', 'i', 'o', 'u' }
	vowels = dict.fromkeys(keys)
	print(vowels)

	print "\n"*2,"Example 2: Create a dictionary from a sequence of keys with value"
	# vowels keys
	keys = {'a', 'e', 'i', 'o', 'u' }
	value = 'vowel'
	vowels = dict.fromkeys(keys, value)
	print(vowels)

	print "\n"*2,"Example 3: Create a dictionary from mutable object list"
	# vowels keys
	keys = {'a', 'e', 'i', 'o', 'u' }
	value = [1]
	vowels = dict.fromkeys(keys, value)
	print(vowels)
	# updating the value
	value.append(2)
	print(vowels)


	# If the provided value is a mutable object (whose value can be modified)
	# like list, dictionary, etc., when the mutable object is modified,
	# each element of the sequence also gets updated.

	# This is because, each element is assigned a reference to 
	# the same object (points to the same object in the memory).
	# To avoid this issue, we use dictionary comprehension.
	# vowels keys
	keys = {'a', 'e', 'i', 'o', 'u' }
	value = [1]

	vowels = { key : list(value) for key in keys }
	# you can also use { key : value[:] for key in keys }
	print(vowels)

	# updating the value
	value.append(2)
	print(vowels)
# _fromkeys()




def _get():
	# The get() method returns the value of the item with
	# the specified key.
	# syntax: dictionary.get(keyname, value)

	pass
_get()


# "Converting dictionary to list"
def convertDictToList():
	d = {'a': 'Arthur', 'b': 'Belling'}
	d.items()
	# [('a', 'Arthur'), ('b', 'Belling')]
	d.keys()
	['a', 'b']
	d.values()
	['Arthur', 'Belling']

	dl = [(k,v) for k,v in d.items()]
	print "\n"*2,"Example : Converting dictionary to list"
	print dl

def convertDictToListExtend():
	d = {'a': 'Arthur', 'b': 'Belling'}
	l=[]
	[l.extend([k,v]) for k,v in d.items()]
	print "example with extend",l

def convertDictToListLambda():
	d = {'a': 'Arthur', 'b': 'Belling'}
	dl = list(reduce(lambda x, y: x + y, d.items()))
	print "example with lambda",dl
convertDictToListLambda()


def AppendDictionaryToDictionary():
	orig = {'A': 1,
   			'B': 2,
   			'C': 3,}
   	extra = {'D': 4,
   			'E': 5,}
   	from itertools import chain
	# dest = dict(chain(orig.items(), extra.items())) #v1
	dest = dict(list(orig.items()) + list(extra.items())) #v2

	print "AppendDictionaryToDictionary",dest

AppendDictionaryToDictionary()






