import csv
import os


# https://stackabuse.com/reading-and-writing-csv-files-in-python/
path =  os.path.dirname (os.path.realpath(__file__))
file_path = os.path.join(path,"trash")


weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']  
sales = ['10', '8', '19', '12', '25']

print file_path+"/out.csv"
with open(file_path+"/csv_out.csv", 'w') as csv_file:  
    csv_writer = csv.writer(csv_file, delimiter=',')
    csv_writer.writerow(weekdays)
    csv_writer.writerow(sales)

# We first need to import the csv library to get their helper
# functions. We open the file as we're accustomed to but
# instead of writing content on the csv_file object, 
# we create a new object called csv_writer.

# This object provides us with the writerow() method 
# which allows us to put all the row's data in the file
# in one go.

