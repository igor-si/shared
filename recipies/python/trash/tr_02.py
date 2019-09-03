import operator
stats = {'a':1000, 'b':3000, 'c': 100}
print max(stats.iteritems(), key=operator.itemgetter(1))[0]