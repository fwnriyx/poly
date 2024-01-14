#Task 1
def findLocationsOfName(name, nameList):
    locations = []
    for i in range(len(nameList)):
        if nameList[i] == name:
            locations.append(i)
    return locations


nameList = ['Johny','Mary','Barry','Gaby','Mary','Barry','Collin','Mary']
name= 'Mary'
print(name,'shows up at the following locations', findLocationsOfName(name,nameList) )

class HashTable:
    def __init__(self,size):
        self.size = size
        self.keys = [None] * self.size
        self.buckets = [None] * self.size
    # A simple remainder method to convert key to index
    def hashFunction(self, key ):
        return key % self.size
    # Deal with collision resolution by means of
    # linear probing with a 'plus 1' rehash
    def rehashFunction(self, oldHash ):
        return (oldHash + 1) % self.size
    def __setitem__(self, key, value):
        index = self.hashFunction( key)
        startIndex = index
        while True:
        # If bucket is empty then just use it
            if self.buckets[index] == None:
                self.buckets[index] = value
                self.keys[index] = key
                break
            else: # If not empty and the same key then just overwrite
                if self.keys[index] == key:
                    self.buckets[index] = value
                    break
                else: # Look for another available bucket
                    index = self.rehashFunction(index)
            # We must stop if no more buckets
                    if index == startIndex:
                        break
    def __getitem__(self,key):
        index = self.hashFunction(key)
        startIndex = index
        while True:
            if self.keys [index] == key: # Will be mostly the case unless value
        # had been previously rehashed at insertion
        # time
                return self.buckets[index]
            else: # Value for the key is somewhere else
        # (due to imperfect hash function)
                index = self.rehashFunction(index )
                if index == startIndex:
                    return None

class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
    def __str__(self):
        # return f'-------------------------------\nName= {self.name}\nAge= {self.age}\nCourse= {self.course}'
        return f'-------------------------------\nName = {self.name: >76}\nAge = {self.age: >77}\nCourse = {self.course: >74}'


    

studentTable = HashTable(5)
studentTable[1488] = Student('John Tan',18,'DIT')
studentTable[1486] = Student('Liz Cruz',17,'DAAA')
studentTable[1000] = Student('Rai Rao',19,'DISM')
studentTable[2000] = Student('Adam Azis',18,'DAAA')
studentTable[3001] = Student('Mary Oh',20,'DIT')
studentIDs = [1000, 1486, 2000, 1488, 3001,8888]
for id in studentIDs:
    student = studentTable[id]
    if student != None:
        print(f'id={id}\n',studentTable[id],'\n')
    else:
        print(f'No student found with id={id}')