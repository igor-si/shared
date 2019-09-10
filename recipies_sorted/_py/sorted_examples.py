

# URL https://www.geeksforgeeks.org/sorted-function-python/
# Sorted() sorts any sequence (list, tuple) and always returns
# a list with the elements in sorted manner, without modifying
# the original sequence.

# Syntax : sorted(iterable, key, reverse)
# Parameters :

def legend():
	Iterable 
	# : sequence (list, tuple, string) or collection 
	# (dictionary, set, frozenset) or any other iterator 
	# that needs to be sorted.

	Key(optional)
	# : A function that would server as a key or a basis 
	# of sort comparison.

	Reverse(optional)
	# : If set true, then the iterable would be sorted
	# in reverse (descending) order, by default it is set as false.

x = [2, 8, 1, 4, 6, 3, 7]
print "original list",x	
print "sorted", sorted(x)
print "sorted, reverse", sorted(x, reverse = True)

x = ['q', 'w', 'r', 'e', 't', 'y']
L = ["cccc", "b", "dd", "aaa"] 
print "Normal sort :", sorted(L)
print "Sort with len :", sorted(L, key = len)

# Sort a list of integers based on 
# their remainder on dividing from 7 
def func(x): 
    return x % 7

L = [15, 3, 11, 7] 
print "Normal sort :", sorted(L) 
print "Sorted with key:", sorted(L, key = func) 


(1) Slicing by position:
sorted(names, key=lambda x: int(x[5:-6]))

(2) Stripping substrings:
sorted(names, key=lambda x: int(x.replace('Test-', '').replace('.model', '')))

(3) Splitting characters (also possible via str.partition):
sorted(names, key=lambda x: int(x.split('-')[1].split('.')[0]))

(4) Map with np.argsort on any of (1)-(3):
list(map(names.__getitem__, np.argsort([int(x[5:-6]) for x in names])))