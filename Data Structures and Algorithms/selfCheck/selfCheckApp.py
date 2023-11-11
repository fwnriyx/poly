from selfCheckStaff import Staff
from selfCheckStudent import Student

class TestPerson:
    # constructor
    def __init__(self):
        # properties / class variables
        self.__studentList = [] # to fill a list with Student objects
        self.__staffList = [] # to fill a list with Staff objects

    def start(self):
        while True:
            print('a. Add new student')
            print('b. Add new staff')
            print('c. View students')
            print('d. View staff')
            print('e. Find Top Student')
            print('z. Exit')
            choice = input('Enter choice:')
            if choice == 'a':
                self.addNewStudent()
            elif choice == 'c':
                self.viewStudentInfo()
            elif choice == 'b':
                self.addNewStaff()
            elif choice == 'd':
                self.viewStaffInfo()
            elif choice == 'e':
                self.findTopStudent()
            else:
                break

    def addNewStudent(self):
        ID = input('enter student ID:')
        name = input('enter student name:')
        gpa = float(input('enter student GPA:'))
        studObj = Student(ID, name, gpa) # to instantiate Student object
        self.__studentList.append(studObj) # append Student object to class variable studentList

    def viewStudentInfo(self):
        for student in self.__studentList:
            student.printMe()  # invoke a function of Student object

    def addNewStaff(self):
        # prompt user for staff ID, name and salary
        ID = input('enter staff ID:')
        name = input('enter staff name:')
        salary = int(input('enter staff salary:'))
        staffObj = Staff(ID, name, salary) # to instantiate Staff object
        self.__staffList.append(staffObj) # append Staff object to class variable staffList

    def viewStaffInfo(self):
        for staff in self.__staffList:
            staff.printMe() # what is printed? is it what you wanted? how to resolve the printing problem?

    def findTopStudent(self):
        # refer to your Week 1-2 lecture notes, slide 31
        topStudent = self.__studentList[0]
        for student in self.__studentList:
            if student > topStudent: # need operator overloading for __lt__ in Student class (for comparison Student objects)
                topStudent = student
        print(topStudent) # need overriding for __str__ in Student class (for printing)

tp = TestPerson()
tp.start()
