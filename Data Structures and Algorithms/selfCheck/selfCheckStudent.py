from selfCheckPerson import Person

# Student inherits from Person
# It is a concrete class which can be instantiated
class Student(??):
    # override parent's constructor
    def __init__(self, ID, name, gpa):
        self.__gpa = gpa
        # invoke parent's constructor

    # override parent's printMe function
    def printMe(self):
        # can you replace the following 2 lines with one-line codes?
        print('== Information ==')
        print('ID:%s Name:%s' % (self.getID(),self.getName()))
        print('GPA: %.2f' % self.__gpa)

    # Student derived from abstract class Person
    # must implement the abstract method whoAmI
    def whoAmI(self):
        print('I am a student')

# testing
#obj1 = Student('S02', 'Peter', 3.9)
#obj1.printMe()
#obj1.whoAmI()
