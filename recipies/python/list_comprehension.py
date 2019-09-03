# ========= 
#sourcehttps://www.programiz.com/python-programming/list-comprehension

# =====================================================
# == Syntax of List Comprehension
#We can now identify where list comprehensions are used.
#If you noticed, human is a string, not a list. 
#This is the power of list comprehension. It can identify 
#when it receives a string or a tuple and work on it like a list.
#
#You can do that using loops. However, not every loop can be
#rewritten as list comprehension. But as you learn and get
#comfortable with list comprehensions, you will find yourself
#replacing more and more loops with this elegant syntax.


#[expression for item in list]

#		Example 2: Iterating through a string Using List Comprehension
h_letters = [ letter for letter in 'human' ]
print('Example 2',h_letters)

#		List Comprehensions vs Lambda functions
#
#List comprehensions arent the only way to work on lists.
#Various built-in functions and lambda functions can create
#and modify lists in less lines of code.
#
#		Example 3: Using Lambda functions inside List
letters = list(map(lambda x: x, 'human'))
print('Example 3',letters)
#However, list comprehensions are usually more human readable 
#than lambda functions. It is easier to understand what the 
#programmer was trying to accomplish when list comprehensions are used.


# =====================================================
#		== Conditionals in List Comprehension
#List comprehensions can utilize conditional statement to modify
#existing list (or other tuples). We will create list that uses 
#mathematical operators, integers, and range().
#
#		Example 4: Using if with List Comprehension
number_list = [ x for x in range(20) if x % 2 == 0]
print('Example 4',number_list)

#		Example 5: Nested IF with List Comprehension
num_list = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]
print('Example 5',num_list)
#Here, list comprehension checks:
#Is y divisible by 2 or not?
#Is y divisible by 5 or not?


#		Example 6: if...else With List Comprehension
obj = ["Even" if i%2==0 else "Odd" for i in range(10)]
print('Example 6',obj)
#Here, list comprehension will check the 10 numbers from 0 to 9. 
#If i is divisible by 2, then Even is appended to the obj list. If not, Odd is appended.


# =====================================================
#		!Nested Loops in List Comprehension	
#Suppose, we need to compute transpose of a matrix which requires nested for loop. 
#Lets see how it is done using normal for loop first. 

#		Example 7: Transpose of Matrix using Nested Loops
transposed = []
matrix = [[1, 2, 3, 4], [4, 5, 6, 8]]

for i in range(len(matrix[0])):
    transposed_row = []

    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print('Example 7',transposed)
#Output: [[1, 4], [2, 5], [3, 6]]
#The above code use two for loops to find transpose of the matrix.
#We can also perform nested iteration inside a list comprehension.
#In this section, we will find transpose of a matrix using nested loop inside list comprehension.

#		Example 8: Transpose of a Matrix using List Comprehension
matrix = [[1, 2], [3,4], [5,6], [7,8]]
transpose = [[row[i] for row in matrix] for i in range(2)]
print ('Example 8',transpose)
#In above program, we have a variable matrix which have 4 rows and 2 columns.
#We need to find transpose of the matrix. For that, we used list comprehension.
#**Note: The nested loops in list comprehension don’t work like normal nested loops. 
#In the above program, for i in range(2) is executed before row[i] for row in matrix. 
#Hence at first, a value is assigned to i then item directed by row[i] 
#is appended in the transpose variable.

#Key Points to Remember
#List comprehension is an elegant way to define and create lists based on existing lists.
#List comprehension is generally more compact and faster than normal 
#functions and loops for creating list.
#However, we should avoid writing very long list comprehensions in one line
#to ensure that code is user-friendly.
#Remember, every list comprehension can be rewritten in for loop,
#but every for loop can’t be rewritten in the form of list comprehension.

#  float list from list of tuples
_items = [z for y in [x.allSubChildren() for x in _items] for z in y]





