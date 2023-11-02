# We are going to create Person, Student and Staff classes
# They are derived from the parent class object
# because Python follows OOP paradigm where everything is an object!

# Person is a parent class. It is also an abstract class.
class Person:
    # constructor with 2 arguments
    def __init__(self, ID, name):
        self.ID = ID   # promote class variable ID to private data
        self.name = name  # promote class variable name to private data

    def getID(self):
        # provide access function public getter for ID
        # for indirect access to private class variables outside the class

    def getName(self):
        # provide access function public getter for name

    def setID(self, newID):
        # provide access function public setter for ID

    def setName(self, newName):
        # provide access function public setter for name

    def printMe(self):
        print('== Information ==')
        print('ID:%s Name:%s' % (??, ??)) # access properties ID and name within class

    def whoAmI(self):
        raise ??('subclass must implement abstract method')


# testing
#obj0 = Person('99', 'Test')
#obj0.whoAmI()





