# {y[i]:x[i] for i,_ in enumerate(x)}
# {'a': 1, 'b': 2, 'c': 3}

# hot to create dict from two tuples
keys = ('name', 'age', 'food')
values = ('Monty', 42, 'spam')    
data = {keys[i]: values[i] for i in range(len(keys))}
print data

 

