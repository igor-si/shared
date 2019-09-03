#Another simple solution for processing 
#unknown or multiple arguments can be:

class ExampleClass(object):

    def __init__(self, x, y, **kwargs):
      self.x = x
      self.y = y
      self.attributes = kwargs

    def SomeFunction(self):
      if 'something' in self.attributes:
        dosomething()


# It will run this command only if it has not been
# imported from another file

if __name__ == '__main__':
    app = QApplication([])
    w = simpleWindow()
    w.show()
    app.exec_()