

# ================ Dynamic menu list
# =========== ordered menu menu list
n=hou.pwd()
exec(n.evalParm("code"))
return test()

# =============== function for providing list
def test():
    print "test"

    menuList = []
    for i in range(1,10):
        menuList.extend(["t_"+str(i), "m_"+str(i)])
    return menuList

# callback from ordered menu    
n=hou.pwd();exec(n.evalParm("code"));onUpdate()
# ------------------------------------------------


# ========= exec colde with globals 
exec(smth, globals())
# ------------------------------------------------




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





