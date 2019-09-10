


# URL - https://www.geeksforgeeks.org/taking-multiple-inputs-from-user-in-python/
# take multiple values or inputs in one line by two methods.

# Using split() method
# Using List comprehension

#  syntax
# input().split(separator, maxsplit)

#====Example, this is a snippet.
# taking two inputs at a time 
x, y = input("Enter a two value: ").split() 
print("Number of boys: ", x) 
print("Number of girls: ", y) 
print() 
#"------------------------------------"

# taking two inputs at a time 
a, b = input("Enter a two value: ").split() 
print("First number is {} and second number is {}".format(a, b)) 
print() 

# taking multiple inputs at a time  
# and type casting using list() function 
x = list(map(int, input("Enter a multiple value: ").split())) 
print("List of students: ", x)



# Using List comprehension :
# List comprehension is an elegant way to define and create 
# list in Python

# taking two input at a time 
x, y = [int(x) for x in input("Enter two value: ").split()] 
print("First Number is: ", x) 
print("Second Number is: ", y) 
print()

# taking two inputs at a time 
x, y = [int(x) for x in input("Enter two value: ").split()] 
print("First number is {} and second number is {}".format(x, y)) 
print() 
  
# taking multiple inputs at a time  
x = [int(x) for x in input("Enter multiple value: ").split()] 
print("Number of list is: ", x)   