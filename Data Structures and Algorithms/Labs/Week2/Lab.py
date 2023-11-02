# class Student:
#     def __init__(self, studentID, age, name):
#         self.__studentID = studentID
#         self.__age = age
#         self.__name = name

#     def getStudentID(self):
#         return self.__studentID
#     def getAge(self):
#         return self.__age
#     def getName(self):
#         return self.__name
    
#     def setName(self, name):
#         self.__name = name
#     def setAge(self, age):
#         self.__age = age
#     def setStudentID(self, studentID):
#         self.__studentID = studentID
# class Animal:
#     def __init__( self, name, xPos = 0):
#         self.name = name
#         self.xPos = xPos
#         self.yPos = 0
#     def walkForward(self):
#         self.xPos +=1
#     def walkBackward(self):
#         self.xPos -=1
#     def getLocation(self):
#         return self.xPos,self.yPos
#     def talk(self):
#         raise NotImplementedError("Subclass must implement abstract method")

# class Cat(Animal):
#     def talk(self):
#         return 'Meow!'
    
# class Dog(Animal):
#     def talk(self):
#         return 'Woof!'
    
# myPets = [Dog('Lassie'),
#         Cat('Silvester'),
#         Dog('Scooby'),
#         Cat('Oggie')]

# for pet in myPets:
#     pet.walkForward()
#     print( f'{pet.name}: {pet.talk()}' )

class Shape():
    def __init__(self,width, height, xPos, yPos):
        self.width = width
        self.height = height
        self.xPos = xPos
        self.yPos = yPos

    def getDimensions(self):
        return self.width, self.height

    def setDimensions(self, width, height):
        self.width = width
        self.height = height

    def getLocation(self):
        return self.xPos, self.yPos
    def setLocation(self, xPos, yPos):
        self.xPos = xPos
        self.yPos = yPos

    # Abstract function
    def draw(self):
        raise NotImplementedError("Subclass must implement abstract method")

obj = Shape(4,5,2,2)
obj.draw()
