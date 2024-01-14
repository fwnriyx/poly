'''
Name:       Liang Zheng Kai Lucas & Muhammad Fitri Amir Bin Abdullah
Admin No.:  2222770
Class:      DAAA2B06

DSAA Assignment 2
'''

# Stack Class
class Stack:
    def __init__(self):
        self.__list = []

    def isEmpty(self):
        return self.__list == []

    def size(self):
        return len(self.__list)

    def clear(self):
        self.__list.clear()

    def push(self, item):
        self.__list.append(item)

    def pop(self):
        if self.isEmpty():
            return None
        else:
            return self.__list.pop()

    def get(self):
        if self.isEmpty():
            return None
        else:
            return self.__list[-1]

    def __str__(self):
        output = '<'
        for i in range(len(self.__list)-1, -1, -1):
            item = self.__list[i]
            if i < len(self.__list)-1:
                output += f', {str(item)}       '
            else:
                output += f'{str(item)}'
        output += '>'
        return output
