# =========== Methods
append() #	Adds an element at the end of the list
clear()	# Removes all the elements from the list
copy()	# Returns a copy of the list
count()	# Returns the number of elements with the specified value
extend() # Add the elements of a list (or any iterable), to the end of the current list
index()	# Returns the index of the first element with the specified value
insert() #	Adds an element at the specified position
pop() #Removes the element at the specified position
remove() # Removes the first item with the specified value
reverse() #	Reverses the order of the list
sort() #	Sorts the list



#from https://stackoverflow.com/questions/252703/what-is-the-difference-between-pythons-list-methods-append-and-extend

#=== append: Appends object at the end.
x = [1, 2, 3]
x.append([4, 5])
print (x)
#gives you: [1, 2, 3, [4, 5]]

#=== Extends list by appending elements from the iterable.
x = [1, 2, 3]
x.extend([4, 5])
print (x)
#gives you: [1, 2, 3, 4, 5]

#append adds an element to a list, 
#and extend concatenates the first list 
#with another list (or another iterable,
#not necessarily a list.)


# What is the difference between the list methods append and extend?
# append adds its argument as a single element to the end of a list. The length of the list itself will increase by one.
# extend iterates over its argument adding each element to the list, extending the list. The length of the list will increase by however many elements were in the iterable argument.
# append
# The list.append method appends an object to the end of the list.

my_list.append(object) 
Whatever the object is, whether a number, a string, another list, or something else, it gets added onto the end of my_list as a single entry on the list.

>>> my_list
['foo', 'bar']
>>> my_list.append('baz')
>>> my_list
['foo', 'bar', 'baz']
So keep in mind that a list is an object. If you append another list onto a list, the first list will be a single object at the end of the list (which may not be what you want):

>>> another_list = [1, 2, 3]
>>> my_list.append(another_list)
>>> my_list
['foo', 'bar', 'baz', [1, 2, 3]]
#^^^^^^^^^--- single item at the end of the list.

#extend
# The list.extend method extends a list by appending elements from an iterable:
# 
# my_list.extend(iterable)
# So with extend, each element of the iterable gets appended onto the list. For example:

my_list
['foo', 'bar']
>>> another_list = [1, 2, 3]
>>> my_list.extend(another_list)
>>> my_list
['foo', 'bar', 1, 2, 3]
Keep in mind that a string is an iterable, so if you extend a list with a string, you'll append each character as you iterate over the string (which may not be what you want):

>>> my_list.extend('baz')
>>> my_list
['foo', 'bar', 1, 2, 3, 'b', 'a', 'z']
Operator Overload, __add__ (+) and __iadd__ (+=)
Both + and += operators are defined for list. They are semantically similar to extend.

my_list + another_list creates a third list in memory, so you can return the result of it, but it requires that the second iterable be a list.

my_list += another_list modifies the list in-place (it is the in-place operator, and lists are mutable objects, as we've seen) so it does not create a new list. It also works like extend, in that the second iterable can be any kind of iterable.

# Don't get confused - my_list = my_list + another_list is not equivalent to += - it gives you a brand new list assigned to my_list.




# =====  Difference btw append and extend
x = [1, 2, 3]
x.append([4, 5])
print (x)
gives you: [1, 2, 3, [4, 5]]


# extend: Extends list by appending elements from the iterable.
x = [1, 2, 3]
x.extend([4, 5])
print (x)
gives you: [1, 2, 3, 4, 5]
# ----------------------------------------


# searching for values in list
a_list = ['a','b','new','mpiligrim','new']
print a_list.count('new')  # count number of element "new" in list
"new" in a_list  # check if something in list = bool
a_list.index('mpiligrim')  # get index position of 'mpiligim' in list

# remove item in list
del a_list[1] # by index

a_list.remove("new") # removes in list by name - value

# POP removes with a twist
a_list = ['a','b','new','mpiligrim']
a_list.pop() # remove mpiligrim
a_list.pop(1) # remove "b"


# check if list is empty










