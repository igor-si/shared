
#Type checking:
print "type check ","\n"*2
def func(arg):
    if not isinstance(arg, (list, tuple)):
        arg = [arg]
    # process
func('abc')
func(['abc', '123'])

#Varargs:
print "Varargs ","\n"*2
def func(*arg):
    print arg
    #process

func('abc')
func('abc', '123')
func(*['abc', '123'])