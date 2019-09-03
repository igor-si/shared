
# URL https://www.geeksforgeeks.org/currying-function-in-python/
# Demonstrate Currying of composition of function 
def change(b, c, d): 
    def a(x): 
        return b(c(d(x))) 
    return a 
      
def kilometer2meter(dist):  
    """ Function that converts km to m. """
    return dist * 1000
      
def meter2centimeter(dist):  
    """ Function that converts m to cm. """
    return dist * 100
      
def centimeter2feet(dist): 
    """ Function that converts cm to ft. """
    return dist / 30.48
      
if __name__ == '__main__': 
    transform = change(centimeter2feet, meter2centimeter, kilometer2meter ) 
    e = transform(565) 
    print(e) 


# Demonstrate Currying of composition of function 

def change(b, c, d): 
    def a(x): 
        return b(c(d(x))) 
    return a 
      
def daystohour(time):  
    """ Function that converts days to hours. """
    return time * 24
      
def hourstominutes(time):  
    """ Function that converts hours to minutes. """
    return time * 60
      
def minutestoseconds(time): 
    """ Function that converts minutes to seconds. """
    return time * 60
      
if __name__ == '__main__': 
    transform = change(minutestoseconds, hourstominutes, daystohour) 
    e = transform(10) 
    print(e) 
