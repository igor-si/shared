import gzip

class FirstClass: # NOT THE CONSTRUCTOR !
	"simple class"

	def say_hay(self,name="anonymous"):
		# Don't worry about 'self' we will come back soon
		print "Hi, " + name

def print_FirstClass():
	first_object = FirstClass()
	first_object.say_hay("python")
	first_object.say_hay()
	second_object = FirstClass()
	second_object.say_hay("test")


class Person():
	def __init__(self,name,age=0):
		self.name = name
		self.age = age

	def print_name(self):
		print "my name is " + self.name

	def print_age(self):
		print "my age is " + str(self.age)

def print_Person():
	adult = Person("jeff",23)
	new_born_baby = Person("alice")

	adult.print_name()
	adult.print_age()
	new_born_baby.print_name()
# print_Person()

class Seven():
	def __init__(self):
		self.d = {}





#============ ! My simple example how to work with vars in instance
class TestClass():
  def __init__(self):
	self.var = 2
	pass
  def changeVar(self,mult=2):
	self.var *=mult


def example_TestClass():
	c = TestClass() # INSTANCE
	print  "\n"*4,c 
	print 'base var ',c.var
	c.changeVar()
	print 'default mult var ',c.var
	c.changeVar(3)
	print 'again mult var ',c.var
	# -----------------------------


#=============== !My class inheritance 
class FileName(object):
	def __init__(self):
		self.filename = "untitled"

class SaveScene(FileName):
	def __init__(self):
		FileName.__init__(self)
		super(SaveScene,self).__init__()

		self.scene = "h16.hip"

def inheritance_examples():
	print "\n example inheritance","\n"*2
	saveobj = SaveScene()
	print "saveobj.scene ", saveobj.scene
	print "saveobj.filename ", saveobj.filename



