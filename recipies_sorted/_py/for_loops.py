from itertools import izip

#		===While
#What is while loop in Python?
#The while loop in Python is used to iterate over a 
#block of code as long as the test expression (condition) is true.
#
#We generally use this loop when we don't know beforehand, the number of times to iterate.
#		Syntax of while Loop in Python
#
#	while test_expression:
 #   	Body of while
print '\n'*2, "example: WHILE LOOP"
n = 10
# initialize sum and counter
sum = 0
i = 1
while i <= n:
    sum = sum + i
    i = i+1    # update counter

# print the sum
print("The sum is", sum)


#		===while loop with else
#Same as that of for loop, we can have an optional else block with while loop as well.
#The else part is executed if the condition in the while loop evaluates to False.
#The while loop can be terminated with a break statement. 
#In such case, the else part is ignored. Hence, 
#a while loop's else part runs if no break occurs and the condition is false.
# Example to illustrate
# the use of else statement
# with the while loop
print '\n'*2, "example: WHILE LOOP WITH ELSE"
counter = 0
while counter < 3:
    print("Inside loop")
    counter = counter + 1
else:
    print("Inside else")






#		===Python break
# Use of break statement inside loop
print '\n'*2, "example: BREAK in for loop"
for val in "string":
    if val == "i":
        break
    print(val)
print("The end")
#In this program, we iterate through the "string" sequence. W
#e check if the letter is "i", upon which we break from the loop. 
#Hence, we see in our output that all the letters 
#up till "i" gets printed. After that, the loop terminates.


#		===Python continue
print '\n'*2, "example: CONTINUE in for loop"
for val in "string":
    if val == "i":
        continue
    print(val)
print("The end")





#	===The range() function
#We can generate a sequence of numbers using range() function.
# range(10) will generate numbers from 0 to 9 (10 numbers).
#
#We can also define the start, stop and step size as 
#range(start,stop,step size). step size defaults to 1 if not provided.

#This function does not store all the values in memory, 
#it would be inefficient. So it remembers the start, stop, step size
# and generates the next number on the go.
#
#To force this function to output all the items, we can use the function list().
#
#The following example will clarify this.
print '\n'*2, "example: range function"
print(range(10))
print(list(range(10)))
print(list(range(2, 8)))
print(list(range(2, 20, 3)))




#	===For loop with else
# 
#A for loop can have an optional else block as well. 
#The else part is executed if the items in the sequence used in for loop exhausts.
#
#break statement can be used to stop a for loop. 
#In such case, the else part is ignored.
#
#Hence, a for loop's else part runs if no break occurs.
#
#Here is an example to illustrate this.
print '\n'*2, "example: For loop with else"
digits = [0, 1, 5]
for i in digits:
    print(i)
else:
    print("No items left.")


# SRC https://www.youtube.com/watch?v=OSGv2VnC0go
print '\n',"Example with colors"
colors = ['red','green','blue','yellow']
names = ['raymond','raychel','matthew']

for i in range(len(colors)):
    print colors[i]

print '\n'
for color in colors:
    print color    

print '\n','Examples looping reverse'
for i in range(len(colors)-1,-1,-1):
    print colors[i]

print '\n'
for color in reversed(colors):
    print color

print '\n','Looping over a collection and indicies'
for i in range(len(colors)):
    print i,'-->',colors[i]

print '\n'
for name,color in zip(names,colors):
    print name,'-->',color

# print '\n'
# for name,color in izip(names,colors):
#     print name,'-->',color

print '\n','Looping in sorted order'
for color in sorted(colors):
    print 'sorted -->',color

print '\n'
for color in sorted(colors,reverse=True):
    print 'sorted reverse -->',color

print '\n','Custom sort order'
def compareLength(c1,c2):
    if len(c1) < len(c2): return -1
    if len(c2) < len(c1): return 1
    return 0

print sorted(colors,cmp=compareLength)
print sorted(colors,key=len)

# print "\nCall a function until a sentinel value"
# f = 'for_loops.py'
# blocks = []
# while True:
#     block = f.read(32)
#     if block == '':
#         break
#     blocks.append(block)

# blocks = []
# for block in iter(partial(f.read,32), ''):
#     blocks.append(block)


print "\nDestinguishing multiple exit points in loops"
def find(seq,target):
    found = False
    for i,value in enumerate(seq):
        if value == tgt:
            found = True
            break
    if not found:
        return -1
    return i

def find(seq,target):
    found = False
    for i,value in enumerate(seq):
        if value == tgt:
            break
    else:
        return -1
    return i

print "\nLooping over dictonaries"
d = {'matthew':'red','rachel':'green','raymond':'blue'}
for k in d: print k

print "\n"
for k in d.keys():
    if k.startswith('r'):
        print k
        # del d[k]

print "\nDict comprehension"
d = {k:d[k] for k in d if not k.startswith('r')}
for k in d: print k


print "\nLooping over dictonaries keys and values"
for k,v in d.iteritems():
    print k,v


print "\nConstuct dictoonary from pairs"
colors = ['red','green','blue']
names = ['raymond','raychel','matthew']

d = dict(izip(names,colors))
print d

print "\nLooping over a dictoonary with enumerate"
for i,(key,value) in enumerate(d.iteritems() ):
    print i,key,value






