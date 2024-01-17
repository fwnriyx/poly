import re

class HashTable:
    def __init__(self,size):
        self.size = size
        self.keys = [None] * self.size
        self.buckets = [None] * self.size
    # A simple remainder method to convert key to index
    def hashFunction(self, key ):
        return sum(ord(char) for char in key) % self.size
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
                


def tokenize_expression(exp):
    # Use regular expression to tokenize the expression
    pattern = r'\d+|[a-zA-Z]+|\S'
    return re.findall(pattern, exp)

def exponentConverter(splitExp):
    #This helps to display the exponent in the correct format, as well as solve it correctly
    #e.g. ** will be  displayed in the tree as **, and solved as such. The problem is that when we use split,
    #it will split the ** into two *s, which will cause the program to not work properly.
    for i, token in enumerate(splitExp):
        if token == "*":
            if i < len(splitExp) - 1 and splitExp[i + 1] == "*":
                splitExp[i] = splitExp[i].replace('*', '**')
                splitExp.remove("*")
    # print(splitExp)
    return splitExp

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

# Binary Tree Class
class BinaryTree:
    def __init__(self,key, leftTree = None, rightTree = None):
        self.key = key
        self.leftTree = leftTree
        self.rightTree = rightTree
        
    def setKey(self, key):
        self.key = key
        
    def getKey(self):
        return self.key
    
    def getLeftTree(self):
        return self.leftTree
    
    def getRightTree(self):
        return self.rightTree
    
    def insertLeft(self, key):
        if self.leftTree == None:
            self.leftTree = BinaryTree(key)
        else:
            t =BinaryTree(key)
            self.leftTree , t.leftTree = t, self.leftTree
            
    def insertRight(self, key):
        if self.rightTree == None:
            self.rightTree = BinaryTree(key)
        else:
            t =BinaryTree(key)
            self.rightTree , t.rightTree = t, self.rightTree
    
    def printPreorder(self, level):
        print( str(level*'-') + str(self.key))
        if self.leftTree != None:
            self.leftTree.printPreorder(level+1)
        if self.rightTree != None:
            self.rightTree.printPreorder(level+1)
    # def printPreorder(self, level):
    #     print(f"{' ' * (level * 2)}{self.key}")
    #     if self.leftTree is not None:
    #         self.leftTree.printPreorder(level + 1)
    #     if self.rightTree is not None:
    #         self.rightTree.printPreorder(level + 1)

# Parse Tree Builder and Solver
def buildParseTree(exp):
        # tokens = exp.split()
        tokens = tokenize_expression(exp)
        tokens = exponentConverter(tokens)
        stack = Stack()
        tree = BinaryTree('?')
        stack.push(tree)
        currentTree = tree
        for t in tokens:
        # RULE 1: If token is '(' add a new node as left child
        # and descend into that node
            if t == '(':
                currentTree.insertLeft('?')
                stack.push(currentTree)
                currentTree = currentTree.getLeftTree()
            #Currently, its going into the right case
            #but for some reason, there is a 2 at the start and a ? instead of a 2 at the end..
            # elif t in ['**']:
            #     #Make it such that it loops downwards the amount of times the exponent is
            #     #First, insert asterisk, then insert number, loop that
            #     idx = tokens.index(t)
            #     #ORIGINAL LOOP
            #     try:
            #         # currentTree.setKey(t)
            #         timetoLoop = int(tokens[idx + 1])
            #         currentTree.setKey('*')
            #         # currentTree.insertRight('*')
            #         # stack.push(currentTree)
            #         # currentTree = currentTree.getRightTree()
            #         # print("Asterisk")
            #         for i in range(timetoLoop - 1):
            #             # Insert asterisk
            #             # currentTree.setKey('*')
            #             currentTree.insertRight('*')
            #             stack.push(currentTree)
            #             currentTree = currentTree.getRightTree()
                        
            #             print("Asterisk")

            #             # Insert left child
            #             # currentTree.setKey(tokens[idx - 1])
            #             currentTree.insertLeft(tokens[idx - 1])
            #             stack.push(currentTree)
            #             currentTree = currentTree.getLeftTree()
            #             print("Number")

            #         # Insert the last number
            #         currentTree.insertRight(tokens[idx - 1])
            #         stack.push(currentTree)
            #         currentTree = currentTree.getRightTree()
            #         print("Number")

            #         # Drop the exponent from the list
            #         tokens.pop(idx + 1)
            #     except ValueError:
            #         print("It's a letter!")
            elif t in ['**']:
                #Make it such that it loops downwards the amount of times the exponent is
                #First, insert asterisk, then insert number, loop that
                idx = tokens.index(t)
                #ORIGINAL LOOP
                try:
                    # currentTree.setKey(t)
                    timetoLoop = int(tokens[idx + 1])
                    currentTree.setKey('*')
                    # currentTree.insertRight('*')
                    # stack.push(currentTree)
                    # currentTree = currentTree.getRightTree()
                    # print("Asterisk")
                    try:
                        for i in range(timetoLoop - 2):
                            # Insert asterisk
                            currentTree.setKey('*')
                            currentTree.insertRight('*')
                            stack.push(currentTree)
                            currentTree = currentTree.getRightTree()

                            #Insert left child
                            currentTree.insertLeft('?')
                            stack.push(currentTree)
                            currentTree = currentTree.getLeftTree()
                            
                            # print("Asterisk")

                            # Insert left child
                            # currentTree.setKey(tokens[idx - 1])
                            currentTree.setKey(int(tokens[idx - 1]))
                            # stack.push(currentTree)
                            parent = stack.pop()
                            currentTree = parent
                            print("Number")

                        # Insert the last number
                        currentTree.insertRight(int(tokens[idx - 1]))
                        stack.push(currentTree)
                        currentTree = currentTree.getRightTree()
                        print("Number")

                        # Drop the exponent from the list
                        tokens.pop(idx + 1)
                    except ValueError:
                        print("First Digit is a letter or word!")
                except ValueError:
                    print("Exponent is a letter or word!")

        # RULE 2: If token is operator set key of current node
        # to that operator and add a new node as right child
        # and descend into that node
            elif t in ['+', '-', '*', '/']:
                # print("Wrong part")
                currentTree.setKey(t)
                currentTree.insertRight('?')
                stack.push(currentTree)
                currentTree = currentTree.getRightTree()
                    
        # RULE 3: If token is number, set key of the current node
        # to that number and return to parent
            elif t not in ['+', '-', '*', '/', ')'] :
                try:
                    currentTree.setKey(int(t))
                    parent = stack.pop()
                    currentTree = parent
                except ValueError:
                    currentTree.setKey(t)
                
        # RULE 4: If token is ')' go to parent of current node
            elif t == ')':
                currentTree = stack.pop()
            else:
                raise ValueError
        return tree



#WHY ISNT THIS WORKING???????//
def evaluateParseTree(tree):
        leftTree = tree.getLeftTree()
        rightTree = tree.getRightTree()
        op = tree.getKey()
        if leftTree != None and rightTree != None:
            if op == '+':
                return evaluateParseTree(leftTree) + evaluateParseTree(rightTree)
            # elif op == '**':
            #     print("Im here")
            #     return evaluateParseTree(leftTree) ** evaluateParseTree(rightTree)
            elif op == '-':
                return evaluateParseTree(leftTree) - evaluateParseTree(rightTree)
            elif op == '*':
                return evaluateParseTree(leftTree) * evaluateParseTree(rightTree)
            elif op == '/':
                return evaluateParseTree(leftTree) / evaluateParseTree(rightTree)
        else:
            return tree.getKey()
        
# Main Program
# exp = 'C=(2*(2*2))'
exp = 'C=(2**3)'
eq_idx = exp.index("=") # get idx of equal

# Slicing and storing variable and equation in new vars
variable = exp[:eq_idx]
equation = exp[eq_idx + 1:]

eqn_table = HashTable(100)
tree = buildParseTree(equation)
tree.printPreorder(0)

eqn_table[variable] = equation

print (f'The expression: {exp} evaluates to: {evaluateParseTree(tree)}')  
print (f'{exp}=> {evaluateParseTree(tree)}') 
# print(f'Hash Table: {eqn_table.keys} => {eqn_table=buckets}')


# exp1 = 'B=(2*C)'
# # exp = 'C=(2**3)'
# eq_idx = exp.index("=") # get idx of equal

# # Slicing and storing variable and equation in new vars
# variable1 = exp1[:eq_idx]
# equation1= exp1[eq_idx + 1:]

# # eqn_table = HashTable(100)
# tree = buildParseTree(equation1)
# tree.printPreorder(0)

# eqn_table[variable1] = equation1

# print (f'The expression: {exp} evaluates to: {evaluateParseTree(tree)}')  
# print (f'{exp}=> {evaluateParseTree(tree)}') 
# print(f'Hash Table: {eqn_table.keys} => {eqn_table.buckets}')