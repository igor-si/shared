    
# METHODS
# clear() 	Removes all Items
# copy()	# Returns Shallow Copy of a Dictionary
# fromkeys()	# creates dictionary from given sequence
# get()	# Returns Value of The Key
# items()	# returns view of dictionary's (key, value) pair
# keys()	# Returns View Object of All Keys
# popitem()	# Returns & Removes Element From Dictionary
# setdefault()	# Inserts Key With a Value if Key is not Present
# pop()	# removes and returns element having given key
# values() #	returns view of all values in dictionary
# update() #	Updates the Dictionary
# any()	# Checks if any Element of an Iterable is True
# all()	# returns true when all elements in iterable is true
# ascii()	# Returns String Containing Printable Representation
# bool()	# Converts a Value to Boolean
# dict()	#Creates a Dictionary
# enumerate() #	Returns an Enumerate Object
# filter()	# constructs iterator from elements which are true
# iter()	# returns iterator for an object
# len()	# Returns Length of an Object
# max()	# returns largest element
# min()	# returns smallest element
# map()	#Applies Function and Returns a List
# sorted()	# returns sorted list from a given iterable
# sum()	# Add items of an Iterable
# zip()	# Returns an Iterator of Tuples




# They update() method updates the dictionary with elements 
# from a dictionary object or an iterable object of key/value pairs.
# It doesn't return any value (returns None).
d = {1: "one", 2: "three"}
d1 = {2: "two"}

# updates the value of key 2
d.update(d1)
print(d)

d1 = {3: "three"}

# adds element with key 3
d.update(d1)
print(d)



# =======================================
 # !How to create a dictionary?
# empty dictionary
my_dict = {}

# dictionary with integer keys
my_dict = {1: 'apple', 2: 'ball'}

# dictionary with mixed keys
my_dict = {'name': 'John', 1: [2, 4, 3]}

# using dict()
my_dict = dict({1:'apple', 2:'ball'})

# from sequence having each item as a pair
my_dict = dict([(1,'apple'), (2,'ball')])


#Dictionaries implement a tp_iter slot that returns 
#an efficient iterator that iterates over the keys 
#of the dictionary. [...] This means that we can write

for k in my_dict: 
	print k
#which is equivalent to, but much faster than

for k in my_dict.keys(): 
	print k
#as long as the restriction on 
#modifications to the dictionary 
#(either by the loop or by another thread) are not violated.

#Add methods to dictionaries that return 
#different kinds of iterators explicitly:

for key in my_dict.iterkeys(): 
	print key

for value in my_dict.itervalues(): 
	print key

for key, value in my_dict.iteritems(): 
	print key,value
#is shorthand for 
for key in my_dict.iterkeys():
	print key

#key is simply a variable.
d = {'x': 1, 'y': 2, 'z': 3} 
for my_var in d:
    print my_var, 'corresponds to', d[my_var]

d = {'x': 1, 'y': 2, 'z': 3} 
for the_key, the_value in d.iteritems():
    print the_key, 'corresponds to', the_value

d = {'x': 1, 'y': 2, 'z': 3} 
for i, (key, value) in enumerate(d.items()):
   print(i, key, value)

# Checking if a 'Dictionary' is empty
dct = {}
bool(dct)

# Count len of dict
print "Count len of dict",len(d.keys())


# If you like to count unique words in the file,
# you could just use set and do like
len(set(open(my_dict).read().split()))


# Convert Tuple of Tupples to Dict
t = ((1, 'a'),(2, 'b'))
print dict((x, y) for x, y in t)









