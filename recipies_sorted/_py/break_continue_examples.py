

# Break Statement
# The break statement provides you with the opportunity to exit 
# out of a loop when an external condition is triggered. 
for number in range(10):
   number = number + 1

   if number == 5:
      break    # break here

   print('Number is ' + str(number))

print('Out of loop')

# Continue Statement
# The continue statement gives you the option to skip over 
# the part of a loop where an external condition is triggered, 
# but to go on to complete the rest of the loop

number = 0

for number in range(10):
   number = number + 1

   if number == 5:
      continue    # continue here

   print('Number is ' + str(number))

print('Out of loop')

# Pass Statement
# When an external condition is triggered, the pass statement allows
# you to handle the condition without the loop being impacted in any
# way; all of the code will continue to be read unless a break or
# other statement occurs.
number = 0

for number in range(10):
   number = number + 1

   if number == 5:
      pass    # pass here

   print('Number is ' + str(number))

print('Out of loop')