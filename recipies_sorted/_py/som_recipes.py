# Menu scripts in HDA
# SEPTEMBER 11, 2017 D.LEAVE A COMMENT
# You can script a menu in Python as an alternative to Menu Items list. Advantage is reusability and potential of additional Python functionality.

# Function in HDA Python script module:

# This is where menu is actually built. It comes in pairs, first stands for a value, second stands for menu item. Following example will create a menu with two items (“Sunset beach” and “Over the clouds”) with corresponding values “C:/corsica_beach.exr” and “C:/over_the_clouds.exr”.

# Values are mapped to variables “zero” and “one” just to make the script more readable. Tuple of values in variable “result” must be written in one line so it is desirable to have rather short entries.

# I used this example to build enviro light presets menu for lookdev purposes.

def generateMenu():
 zero = "C:/corsica_beach.exr"
 one = "C:/over_the_clouds.exr"
 result = [zero, "Sunset beach", one, "Over the clouds"]
 return result
# To call the function in parameter menu script:

hou.pwd().hdaModule().generateMenu()


=================================
#Q - why do you use python zip instead of using subprocess tar gz? because of windows?
#A - 1: if possible, always use Pythons modules. 
#They are os independent, built in and generally fast


#Q - why do you use lambda function here?
NAME_REGEXES = [
	[r'[\w\d]+?_(.+)_v(\d+)_t(\d+)',lambda x: x.groups()],
	[r'fx_(.+)_v(\d+)_t(\d+)', lambda x: x.groups()],
	[r'fx_(.+)_v(\d+)',lambda x: list(x.groups()) + ['1']]

]
#A - 2: first item is the regex and the second is a function to retrieve the groups
#lambda is because they are too simple for a regular function


