
# URL https://www.programiz.com/python-programming/nested-dictionary
# ==================================================================
#In Python, a dictionary is an    
#unordered collection of items. For example:
dictionary = {'key' : 'value',
'key_2': 'value_2'}
#Here, dictionary has a key:value pair enclosed within curly brackets {}.


#=====================================
#What is Nested Dictionary in Python?
#In Python, a nested dictionary is a dictionary 
#inside a dictionary. 
#It's a collection of dictionaries into one single dictionary.

nested_dict = { 'dictA': {'key_1': 'value_1'},
                'dictB': {'key_2': 'value_2'}}
#Here, the nested_dict is a nested dictionary with 
#the dictionary dictA and dictB. They are two dictionary each having own key and value.

#Example 1: How to create a nested dictionary
people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}

print 'Example 1 \n',people
#In the above program, people is a nested dictionary. 
#The internal dictionary 1 and 2 is assigned to people. 
#Here, both the dictionary have key name, age , sex with different values. 
#Now, we print the result of people.



#Access elements of a Nested Dictionary
#To access element of a nested dictionary, we use indexing [] syntax in Python.
#
#Example 2: Access the elements using the [] syntax
print "\n Example 2 " 
people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}

print(people[1]['name'])
print(people[1]['age'])
print(people[1]['sex'])
#In the above program, 
#we print the value of key name using i.e. 
#people[1]['name'] from internal dictionary 1. Similarly, 
#we print the value of age and sex one by one.



#Add element to a Nested Dictionary
#Example 3: How to change or add elements in a nested dictionary?
print "\n Example 3" 
people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}

people[3] = {}

people[3]['name'] = 'Luna'
people[3]['age'] = '24'
people[3]['sex'] = 'Female'
people[3]['married'] = 'No'

print(people[3])
#In the above program, we create an empty dictionary 3 inside the dictionary people.
#Then, we add the key:value pair i.e people[3]['Name'] = 'Luna' 
#inside the dictionary 3. Similarly, we do this for key age, 
#sex and married one by one. When we print the people[3], 
#we get key:value pairs of dictionary 3.


#Example 4: Add another dictionary to the nested dictionar
print "\n Example 4" 
people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'},
          3: {'name': 'Luna', 'age': '24', 'sex': 'Female', 'married': 'No'}}

people[4] = {'name': 'Peter', 'age': '29', 'sex': 'Male', 'married': 'Yes'}
print(people[4])
#In the above program, we assign a dictionary literal to people[4]. 
#The literal have keys name, age and sex with respective values. 
#Then we print the people[4], to see that the dictionary 4 is 
#added in nested dictionary people.


#Delete elements from a Nested Dictionary
#In Python, we use "del" statement to delete elements 
#from nested dictionary.
print "\n Example 5"
people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'},
          3: {'name': 'Luna', 'age': '24', 'sex': 'Female', 'married': 'No'},
          4: {'name': 'Peter', 'age': '29', 'sex': 'Male', 'married': 'Yes'}}

del people[3]['married']
del people[4]['married']

print(people[3])
print(people[4])
#In the above program, we delete the key:value pairs of
# married from internal dictionary 3 and 4. 
#Then, we print the people[3] and people[4] to confirm changes.


#Example 6: How to delete dictionary from a nested dictionary?
print "\n Example 6"
people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'},
          3: {'name': 'Luna', 'age': '24', 'sex': 'Female'},
          4: {'name': 'Peter', 'age': '29', 'sex': 'Male'}}

del people[3], people[4]
print(people)
#In the above program, we delete both the internal
#dictionary 3 and 4 using del from the nested dictionary people.
#Then, we print the nested dictionary people to confirm changes



#Iterating Through a Nested Dictionary
#Using the for loops, we can iterate through each
#elements in a nested dictionary.

#Example 7: How to iterate through a Nested dictionary?
print "\n Example 7"
people = {1: {'Name': 'John', 'Age': '27', 'Sex': 'Male'},
          2: {'Name': 'Marie', 'Age': '22', 'Sex': 'Female'}}

for p_id, p_info in people.items():
    print "\n Person ID:", p_id
    
    for key in p_info:
        print(key + ':', p_info[key])

#In the above program, the first loop returns all the keys
#in the nested dictionary people. It consist of the IDs p_id 
#of each person. We use these IDs to unpack the information 
#p_info of each person.

#The second loop goes through the information of each person. 
#Then, it returns all of the keys name, age, sex of each 
#person's dictionary.

#Now, we print the key of the person s information 
#and the value for that key.

# Key Points to Remember:
# Nested dictionary is an unordered collection of dictionary
# Slicing Nested Dictionary is not possible.
# We can shrink or grow nested dictionary as need.
# Like Dictionary, it also has key and value.
# Dictionary are accessed using key.