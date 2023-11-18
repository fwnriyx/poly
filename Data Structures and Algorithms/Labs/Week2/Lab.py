#Task 1
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


#Task 2
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

# class mouse(Animal):
#     def talk(self):
#         return 'Squeak!'

# myPet = mouse('Jerry')
# print(f"{myPet.name}: {myPet.talk()}")

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

# class Shape():
#     def __init__(self,width, height, xPos, yPos):
#         self.width = width
#         self.height = height
#         self.xPos = xPos
#         self.yPos = yPos

#     def getDimensions(self):
#         return self.width, self.height

#     def setDimensions(self, width, height):
#         self.width = width
#         self.height = height

#     def getLocation(self):
#         return self.xPos, self.yPos
#     def setLocation(self, xPos, yPos):
#         self.xPos = xPos
#         self.yPos = yPos

#     # Abstract function
#     def draw(self):
#         raise NotImplementedError("Subclass must implement abstract method")

# obj = Shape(4,5,2,2)
# obj.draw()

#Task 3
# class Stack1:
#     def __init__(self):
#         self.__list= []
#     def isEmpty(self):
#         return self.__list == []
#     def size(self):
#         return len(self.__list)
#     def clear(self):
#         self.__list.clear()
#     def push(self, item):
#         self.__list.append(item)
#     def pop(self):
#         if self.isEmpty():
#             return None
#         else:
#             return self.__list.pop()
#     def get(self):
#         if self.isEmpty():
#             return None
#         else:
#             return self.__list[-1]
#     def __str__(self):
#         output = '<'
#         for i in range( len(self.__list) ):
#             item = self.__list[i]
#             if i < len(self.__list)-1 :
#                 output += f'{str(item)}, '
#             else:
#                 output += f'{str(item)}'
#                 output += '>'
#                 return output
# s = Stack1()
# print(s.pop())

# for i in range(1,6):
#     s.push(i)

# print('Content of stack =',s)
# print('Item at top=',s.get())
# print('Size=', s.size())
# while not s.isEmpty():
#     print(s.pop())
#     print(s)

#Stack method 2
# class Stack:
#     def __init__(self):
#         self.__list = []

#     def isEmpty(self):
#         return self.__list == []

#     def size(self):
#         return len(self.__list)

#     def clear(self):
#         self.__list.clear()

#     def push(self, item):
#         self.__list.insert(0, item)

#     def pop(self):
#         if self.isEmpty():
#             return None
#         else:
#             return self.__list.pop(0)

#     def get(self):
#         if self.isEmpty():
#             return None
#         else:
#             return self.__list[-1]

#     def __str__(self):
#         output = '<'
#         for i in range(len(self.__list)):
#             item = self.__list[i]
#             if i < len(self.__list)-1:
#                 output += f'{str(item)}, '
#             else:
#                 output += f'{str(item)}'
#         output += '>'
#         return output

# s = Stack()
# print(s.pop())
# for i in range(1,6):
#     s.push(i)
#     print('Content of stack =',s)
#     print('Item at top=',s.get())
#     print('Size=', s.size())
# while not s.isEmpty():
#     print(s.pop())
#     print(s)

# class Stack3(Stack):
#     def __init__(self):
#         super().__init__()

#     def __str__(self):
#         output = '<'
#         for i in range(len(self._Stack__list)):
#             item = self._Stack__list[i]
#             if i < len(self._Stack__list)-1:
#                 output += f'{str(item)}, '
#             else:
#                 output += f'{str(item)}'
#         output += '>'
#         return output

    
# s = Stack3()
# print(s.pop())
# for i in range(1,6):
#     s.push(i)
#     print('Content of stack =',s)
#     print('Item at top=',s.get())
#     print('Size=', s.size())
# while not s.isEmpty():
#     print(s.pop())
#     print(s)


#Task 5
# class Queue():
#     def __init__(self):
#         self.__list = []
#     def enqueue(self, item):
#         self.__list.append(item)
#     def dequeue(self):
#         if self.isEmpty():
#             return None
#         else:
#             return self.__list.pop(0)
#     def isEmpty(self):
#         return self.__list == []
#     def size(self):
#         return len(self.__list)
#     def clear(self):
#         self.__list.clear()
#     def get(self):
#         if self.isEmpty():
#             return None
#         else:
#             return self.__list[0]
#     def __str__(self):
#         output = '<'
#         for i in range(len(self.__list)):
#             item = self.__list[i]
#             output += f'{str(item)}'
#             if i < len(self.__list) - 1:
#                 output += ', '
#         output += '>'
#         return output
# q = Queue()
# print(q.dequeue())

# for i in range(1,6):
#     q.enqueue(i)

# print('Content of queue is=',q)
# print('Item at front=',q.get())
# print('Size=', q.size())

# while not q.isEmpty():
#     print(q.dequeue())
#     print(q)



# class Deque():
#     def __init__(self):
#         self.__list = []
#     def addHead(self, item):
#         self.__list.insert(0, item)
#     def addTail(self, item):
#         self.__list.append(item)
#     def removeHead(self):
#         if self.isEmpty():
#             return None
#         else:
#             return self.__list.pop(0)
        
#     def removeTail(self):
#         if self.isEmpty():
#             return None
#         else:
#             return self.__list.pop()
        
#     def isEmpty(self):
#         return self.__list == []
    
#     def size(self):
#         return len(self.__list)
    
#     def clear(self):
#         self.__list.clear()

#     def getHead(self):
#         if self.isEmpty():
#             return None
#         else:
#             return self.__list[0]
#     def getTail(self):
#         if self.isEmpty():
#             return None
#         else:
#             return self.__list[-1]
#     def __str__(self):
#         output = '<'
#         for i in range(len(self.__list)):
#             item = self.__list[i]
#             output += f'{str(item)}'
#             if i < len(self.__list) - 1:
#                 output += ', '
#         output += '>'
#         return output
    
        

# d = Deque()
# print(d.removeHead())
# print(d.removeTail())

# for i in range(1,6):
#     d.addTail(i)

# print('Content of deque is=',d)
# print('Item at front=',d.getHead())
# print('Item at back=',d.getTail())
# print('Size=', d.size())

# count=0

# while not d.isEmpty():
# # Alternating remove head and tail
#     if count % 2 ==0:
#         print(d.removeHead())
#     else:
#         print(d.removeTail())
#     print(d)
#     count+=1


#Task 8 - Sorted List

class Node():
    def __init__(self):
        self.nextNode = None

class Temp(Node):
    def __init__(self,valCelsius):
        self.valCelsius = valCelsius
        super().__init__()
    def __eq__(self, otherNode):
        if otherNode == None:
            return False
        else:
            return self.valCelsius == otherNode.valCelsius
    def __lt__(self, otherNode):
        if otherNode == None:
            raise TypeError("'<' not supported between instances of 'Temp' and 'NoneType'")
        return self.valCelsius < otherNode.valCelsius
    def __str__(self):
        return f'{self.valCelsius}'


class Fruit(Node):
    def __init__(self, name):
        self.name = name
        self.name_length = len(name)
        super().__init__()

    def __eq__(self, otherNode):
        if otherNode == None:
            return False
        else:
            return self.name_length == otherNode.name_length
    
    def __lt__(self, otherNode):
        if otherNode == None:
            raise TypeError("'<' not supported between instances of 'Fruits' and 'NoneType'")
        return (self.name_length, self.name) < (otherNode.name_length, otherNode.name)
    
    def __str__(self):
        return f"'{self.name}'"


class SortedList(Node):
    def __init__(self):
        self.headNode = None
        self.currentNode = None
        self.length = 0
        super().__init__()

    def __appendToHead(self, newNode):
        oldHeadNode = self.headNode
        self.headNode = newNode
        self.headNode.nextNode = oldHeadNode
        self.length += 1

    def insert(self, newNode):
        self.length += 1
        if self.headNode == None:
            self.headNode = newNode
            return
    
        if newNode < self.headNode:
            self.__appendToHead(newNode)
            return
        
        leftNode = self.headNode
        rightNode = self.headNode.nextNode
        while rightNode != None:
            if newNode < rightNode:
                leftNode.nextNode = newNode
                newNode.nextNode = rightNode
                return
            leftNode = rightNode
            rightNode = rightNode.nextNode

        leftNode.nextNode = newNode
    
    def __str__(self):
        # We start at the head
        output = ""
        node = self.headNode
        firstNode = True
        while node != None:
            if firstNode:
                output = node.__str__()
                firstNode = False
            else:
                output += (',' + node.__str__())
            node = node.nextNode
        return output





l = SortedList()
# Populate a list with fruitnames
fruits = ['Cherry', 'Apricot','lime','blueberry','Apple', 'Date']
print('Before sorting')
print(fruits)
for fruit in fruits:
    l.insert(Fruit(fruit))

print('\nAfter sorting')
print(l)