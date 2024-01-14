def mergeSort(l):
    if len(l) > 1:
        mid = int(len(l)/2)
        leftHalf = l[:mid]
        rightHalf = l[mid:]
        mergeSort(leftHalf)
        mergeSort(rightHalf)

        leftIndex, rightIndex, index = 0, 0, 0

        mergeList = l
        while leftIndex < len(leftHalf) and rightIndex < len(rightHalf):
            if leftHalf[leftIndex] < rightHalf[rightIndex]:
                mergeList[index] = leftHalf[leftIndex]
                leftIndex += 1
            else:
                mergeList[index] = rightHalf[rightIndex]
                rightIndex += 1
            index += 1

        while leftIndex < len(leftHalf):
            mergeList[index] = leftHalf[leftIndex]
            leftIndex += 1
            index += 1
        
        while rightIndex < len(rightHalf):
            mergeList[index] = rightHalf[rightIndex]
            rightIndex += 1
            index += 1

class Fruit:
    def __init__(self, name):
        self.name = name

    def __lt__(self, other):
        return self.name < other.name

    def __str__(self):
        return self.name

# Main
l = []

# Read fruits from a file and sort in list
f = open('fruits.txt', 'r')
for fruit in f:
    fruit = fruit.strip()
    l.append(Fruit(fruit))
f.close()

# Do a merge sort
mergeSort(l)

# Write sorted fruits into file
f = open('fruits_sorted_v2.txt', 'w')
for fruit in l:
    f.write(fruit.name+"\n")
f.close()

# print(l)