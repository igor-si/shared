

# https://thomas-cokelaer.info/blog/2017/12/how-to-sort-a-dictionary-by-values-in-python/
# If you want to sort this dictionary by values (i.e., the age), 
# you must use another data structure such as a list, or 
# an ordered dictionary.

d = {"Pierre": 42, "Anne": 33, "Zoe": 24}
import operator
sorted_d = sorted(d.items(), key=operator.itemgetter(1))
print "sorted by value",sorted_d

# If you do not want to use the operator 
# module, you can use a lambda function:
d = {"Pierre": 42, "Anne": 33, "Zoe": 24}
sorted_d = sorted(d.items(), key=lambda x: x[1])
# equivalent version
# sorted_d = sorted(d.items(), key=lambda (k,v): v)
print "sorted by lambda",sorted_d


# sorting dict by key https://www.saltycrane.com/blog/2007/09/how-to-sort-python-dictionary-by-keys/
mydict = {
    "carl": 40,
    "alan": 2,
    "bob": 1,
    "danny": 3,
}
for key in sorted(mydict.keys()):
    print("sorting dict by key= %s: %s" % (key, mydict[key]))

# sorting dict by value
for key, value in sorted(mydict.items(), key=lambda item: item[1]):
    print("sorting dict by value=%s: %s" % (key, value))


list_comprehension = sorted((value, key) for (key,value) in d.items())
print "sorted by list comprehension:", list_comprehension
