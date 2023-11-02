from selfCheckPerson import Person

# Staff inherits from Person
# It is a concrete class which can be instantiated
class Staff(Person):
    # override parent's constructor
    def __init__(self, ID, name, salary):
        self.__salary = salary
        # invoke parent's constructor

    def printMe(self):
        # can you replace the following 2 lines with one-line codes?
        print('== Information ==')
        print('ID:%s Name:%s' % (self.getID(),self.getName()))
        print('Salary: %d' % self.__salary)

    # Staff derived from abstract class Person
    # must implement the abstract method whoAmI
    def whoAmI(self):
        print('I am a staff')

# testing
#obj2 = Staff('ST02', 'Susan', 4000)
#obj2.printMe()
#obj2.whoAmI()

