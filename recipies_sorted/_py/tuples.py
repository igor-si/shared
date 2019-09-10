
# URL https://stackoverflow.com/questions/16730339/python-add-item-to-the-tuple
a = ('2',)
b = 'b'
l = list(a)
l.append(b)
print tuple(l)


a = ('2',)
items = ['o', 'k', 'd', 'o']
l = list(a)
for x in items:
    l.append(x)
print tuple(l)

# 1 Form
a = ('x', 'y')
b = a + ('z',)
print(b)

# 2 Form
a = ('x', 'y')
b = a + tuple('b')
print(b)

# extend tuple
a = ('x','y')
b = ('r','t')
c = a+b
a += b
# ---------------

