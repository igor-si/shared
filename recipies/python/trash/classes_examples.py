

class FirstClass: # NOT THE CONSTRUCTOR !
	"simple class"

	def say_hay(self,name="anonymous"):
		# Don't worry about 'self' we will come back soon
		print "Hi, " + name
first_object = FirstClass()
first_object.say_hay("python")
first_object.say_hay()

second_object = FirstClass()
second_object.say_hay("test")


