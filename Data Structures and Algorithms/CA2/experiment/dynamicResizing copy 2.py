import re

def block_sort(arr, block_size):
 
    # Create an empty list to
    # hold the sorted blocks
    blocks = []
 
    # Divide the input array into
# blocks of size block_size
 
    for i in range(0, len(arr), block_size):
 
        block = arr[i:i + block_size]
 
        # Sort each block and append
        # it to the list of sorted blocks
        blocks.append(sorted(block))
 
    # Merge the sorted blocks into
    # a single sorted list
    result = []
    while blocks:
 
        # Find the smallest element in
        # the first block of
        # each sorted block
        min_idx = 0
        for i in range(1, len(blocks)):
            if blocks[i][0] < blocks[min_idx][0]:
                min_idx = i
 
        # Remove the smallest element and
        # append it to the result list
        result.append(blocks[min_idx].pop(0))
 
        # If the block is now empty, remove
        # it from the list of sorted blocks
        if len(blocks[min_idx]) == 0:
            blocks.pop(min_idx)
    return result

class HashTable:
    def __init__(self, size):
        self.size = size
        self.keys = [None] * size
        self.buckets = [None] * size

    # Pass the current size as an argument to hashFunction
    def hashFunction(self, key, current_size):
        if key == 0:
            return 0
        return sum(ord(char) for char in key) % current_size

    def rehashFunction(self, oldHash):
        return (oldHash + 1) % self.size

    # def rehashFunction(self, oldHash, attempt):
    #     return (oldHash + attempt) % self.size

    def _resize_and_rehash(self):
        new_size = self.size * 2 
        new_keys = [None] * new_size
        new_buckets = [None] * new_size

        # Use a while loop to ensure all non-empty buckets are processed
        index = 0
        while index < self.size:
            if self.keys[index] is not None: # a key exists
                # new_index = self.hashFunction(self.keys[index], self.size)  # Use the new size for hashing
                new_index = self.hashFunction(self.keys[index], new_size) #get new index for this key using the new size
                condition = True
                while condition:
                    # use bucket if empty
                    if new_buckets[new_index] == None:
                        # set the bucket by indexing the old bucket 
                        new_buckets[new_index] = self.buckets[index] 
                        condition = False # break the loop when bucket is found
                    else: # look for another available bucket
                        new_index = self.rehashFunction(new_index)
                        condition = True # run the loop again
                new_keys[new_index] = self.keys[index]
                new_buckets[new_index] = self.buckets[index]
            index += 1

        # Update the hash table 
        self.size = new_size  
        self.keys = new_keys
        self.buckets = new_buckets

    def __setitem__(self, key, value):
        index = self.hashFunction(key, self.size)
        startIndex = index
        while True:
            # Set new or replace existing key
            if self.keys[index % self.size] is None or self.keys[index % self.size] == key:
                self.buckets[index % self.size] = value
                self.keys[index % self.size] = key
                break
            else: 
                index = self.rehashFunction(index) # rehash and try to find empty bucket 
                if index == startIndex: # if there is no space, enter this condition
                    # Resize the hash table
                    # if sum(bucket is not None for bucket in self.buckets) >= self.size:
                        self._resize_and_rehash()
                        
                        # Recalculate the index using the new size
                        index = self.hashFunction(key, self.size)
                                                    
                        # insert the key and value
                        # there will definitely be space in this new hashtable
                        condition = True
                        while condition:
                            # if new resized hashtable bucket is empty use it
                            if self.buckets[index] == None: 
                                self.buckets[index] = value
                                self.keys[index] = key
                                condition = False # break loop when bucket found
                            else: #don't need to handle same key as handled above already
                                index = self.rehashFunction(index)
                                condition = True #continue loop/rehashing until bucket found
                        break

    def __getitem__(self, key):
        index = self.hashFunction(key, self.size)
        count = 0
        while True:
            if self.keys[index % self.size] == key:
                return self.buckets[index % self.size]
            else:
                index = self.rehashFunction(index)
                count += 1
                if count == self.size:
                    return None


def tokenize_expression(exp):
    # Use regular expression to tokenize the expression
    # \d+ is one or more digits, \. is a literal dot, \S is one or more non-whitespace characters and | is an OR operator, [a-zA-Z]+ is one or more letters
    pattern = r'\d+\.\d+|\d+|[a-zA-Z]+|\S'
    # print(re.findall(pattern, exp))
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
    # print(f"Hello," , splitExp)
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
    def __init__(self, key, leftTree = None, rightTree = None):
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
        if self.rightTree != None:
            self.rightTree.printPreorder(level+1)
        print(str(level*'.') + str(self.key))
        if self.leftTree != None:
            self.leftTree.printPreorder(level+1)


class ParseTree(BinaryTree):
    def __init__(self, expression):
        self.expression = expression
        super().__init__('?')
        
    def buildParseTree(self):
        tokens = tokenize_expression(self.expression)
        tokens = exponentConverter(tokens)              
        stack = Stack()               
        tree = self 
        stack.push(self)
        currentTree = tree
        for t in tokens:
            # RULE 1: If token is '(' add a new node as left child
            # and descend into that node
                if t == '(':
                    currentTree.insertLeft('?')
                    stack.push(currentTree)
                    currentTree = currentTree.getLeftTree()
            # RULE 2: If token is operator set key of current node
            # to that operator and add a new node as right child
            # and descend into that node
                elif t in ['+', '-', '*', '/', '**']:
                    currentTree.setKey(t)
                    currentTree.insertRight('?')
                    stack.push(currentTree)
                    currentTree = currentTree.getRightTree()
            # RULE 3: If token is number, set key of the current node
            # to that number and return to parent
                elif t not in ['+', '-', '*', '/', ')','**'] :
                    try:
                        currentTree.setKey(float(t))
                        parent = stack.pop()
                        currentTree = parent
                    except ValueError:
                        currentTree.setKey(t)
                        parent = stack.pop()
                        currentTree = parent
            # RULE 4: If token is ')' go to parent of current node
                elif t == ')':
                    currentTree = stack.pop()
                else:
                    raise ValueError
        return tree
    
    def printPreorder(self, level):
        return super().printPreorder(level)

    
def evaluateParseTree(tree, hashtable):
        leftTree = tree.getLeftTree()
        rightTree = tree.getRightTree()
        op = tree.getKey()
        
        if leftTree != None and rightTree != None:
           
            # Replace left tree and right tree if they are variables
            # 
            if str(leftTree.getKey()).isalpha():
                try:
                    eqn = hashtable[leftTree.getKey()]
                    tree = ParseTree(eqn)
                    parse_tree = tree.buildParseTree()
                    new_key = evaluateParseTree(parse_tree, hashtable)
                    leftTree.setKey(new_key)
                except TypeError:
                    return None
            elif str(rightTree.getKey()).isalpha():
                try:
                    eqn = hashtable[rightTree.getKey()]
                    tree = ParseTree(eqn)
                    parse_tree = tree.buildParseTree()
                    new_key = evaluateParseTree(parse_tree, hashtable)
                    leftTree.setKey(new_key)
                except TypeError:
                    return None
            
            # Evaluate Parse Tree  
            if op == '+':
                try:
                    return evaluateParseTree(leftTree, hashtable) + evaluateParseTree(rightTree, hashtable)
                except TypeError:
                    return None
            elif op == '**':
                try:
                    return evaluateParseTree(leftTree, hashtable) ** evaluateParseTree(rightTree, hashtable)
                except TypeError:
                    return None
            elif op == '-':
                try:
                    return evaluateParseTree(leftTree, hashtable) - evaluateParseTree(rightTree, hashtable)
                except TypeError:
                    return None
            elif op == '*':
                try:
                    return evaluateParseTree(leftTree, hashtable) * evaluateParseTree(rightTree, hashtable)
                except TypeError:
                    return None
            elif op == '/':
                try:
                    return evaluateParseTree(leftTree, hashtable) / evaluateParseTree(rightTree, hashtable)
                except TypeError:
                    return None
        else:
            return tree.getKey()        
     

# # Parse Tree Builder and Solver
# def buildParseTree(exp):
#         # tokens = exp.split()
#         tokens = tokenize_expression(exp)
#         tokens = exponentConverter(tokens)
#         # print(tokens)
#         stack = Stack()
#         tree = BinaryTree('?')
#         stack.push(tree)
#         currentTree = tree
#         for t in tokens:
#         # RULE 1: If token is '(' add a new node as left child
#         # and descend into that node
#             if t == '(':
#                 currentTree.insertLeft('?')
#                 stack.push(currentTree)
#                 currentTree = currentTree.getLeftTree()

#         # RULE 2: If token is operator set key of current node
#         # to that operator and add a new node as right child
#         # and descend into that node
#             elif t in ['+', '-', '*', '/', '**']:
#                 currentTree.setKey(t)
#                 currentTree.insertRight('?')
#                 stack.push(currentTree)
#                 currentTree = currentTree.getRightTree()
                    
#         # RULE 3: If token is number, set key of the current node
#         # to that number and return to parent
#             elif t not in ['+', '-', '*', '/', ')', '**']:
#                 try:
#                     currentTree.setKey(float(t))
#                     # print(currentTree.getKey())
#                     parent = stack.pop()
#                     currentTree = parent
#                 except ValueError:
#                     currentTree.setKey(t)
#                     parent = stack.pop()
#                     currentTree = parent
                
#         # RULE 4: If token is ')' go to parent of current node
#             elif t == ')':
#                 currentTree = stack.pop()
#             else:
#                 raise ValueError
#         return tree

# def evaluateParseTree(tree, hashtable):
#         leftTree = tree.getLeftTree()
#         rightTree = tree.getRightTree()
#         op = tree.getKey()
        
#         if leftTree != None and rightTree != None:
#             print(leftTree.getKey())
#             print(rightTree.getKey())
#             # Replace left tree and right tree if they are variables
#             if str(leftTree.getKey()).isalpha():
#                 try:
#                     eqn = hashtable[leftTree.getKey()]
#                     new_tree = buildParseTree(eqn)
#                     new_key = evaluateParseTree(new_tree, hashtable)
#                     leftTree.setKey(new_key)
#                 except TypeError:
#                     return None
#             elif str(rightTree.getKey()).isalpha():
#                 try:
#                     eqn = hashtable[rightTree.getKey()]
#                     new_tree = buildParseTree(eqn)
#                     new_key = evaluateParseTree(new_tree, hashtable)
#                     rightTree.setKey(new_key)
#                 except TypeError:
#                     return None
            
#             # Evaluate Parse Tree  
#             if op == '+':
#                 try:
#                     return evaluateParseTree(leftTree, hashtable) + evaluateParseTree(rightTree, hashtable)
#                 except TypeError:
#                     return None
#             elif op == '**':
#                 try:
#                     return evaluateParseTree(leftTree, hashtable) ** evaluateParseTree(rightTree, hashtable)
#                 except TypeError:
#                     return None
#             elif op == '-':
#                 try:
#                     # a = evaluateParseTree(leftTree, hashtable)
#                     # b = evaluateParseTree(rightTree, hashtable)
#                     # print(a, type(a))
#                     # print(b, type(b))
#                     return evaluateParseTree(leftTree, hashtable) - evaluateParseTree(rightTree, hashtable)
#                 except TypeError as t:
#                     return print(t)
#             elif op == '*':
#                 try:
#                     return evaluateParseTree(leftTree, hashtable) * evaluateParseTree(rightTree, hashtable)
#                 except TypeError:
#                     return None
#             elif op == '/':
#                 try:
#                     return evaluateParseTree(leftTree, hashtable) / evaluateParseTree(rightTree, hashtable)
#                 except TypeError:
#                     return None
#         else:
#             return tree.getKey()

# exp = 'A=(2**2)' # 4
# exp1 = 'Balls=(A+1)' # 5
# exp2 = 'Can=(Balls**A)' # 5^4 = 625
# exp3 = 'D=(4+(5+6))'
# exp4 = 'E=(2**6.4)'

# WHY DOES a=(2+3) get removed?
mango = 'Mango=((Apple+(Durian+(Pear*(Blueberry*(Coconut/Strawberry)))))/2)'
# exp = 'a=(2+3)'
# exp1 = 'bc=(a*3)'
# exp2 = 'abc=(a+(bc/2))'
# exp3 = 'D=(4+(5+6))'
# exp4 = 'E=(2**6.4)'

# a = 'Mango=((Apple+(Durian+(Pear*(Blueberry*(Coconut/Strawberry)))))/2)'
# b = 'a=(2+3)'
# c = 'bc=(a*3)'

# a = 'a=((Apple+(Durian+(Pear*(Blueberry*(Coconut/Strawberry)))))/2)'
# b = 'b=(2+3)'
# c = 'c=(a*3)'

a = 'a=(1+2)'
b = 'b=(a+2)'
# c = 'c=(1+2)'
# d = 'd=(1+2)'
# e = 'e=(1+2)'
# f = 'f=(1+2)'
# g = 'g=(1+2)'
# h = 'h=(1+2)'

# a = 'a=(3**8)'
# a = 'a=(1-mango)'


eqn_table = HashTable(1)

# print()

# # for e in [mango, exp, exp1]:
# for e in [a]:
#     eq_idx = e.index("=")  # get idx of equal
#     variable = e[:eq_idx]
#     equation = e[eq_idx + 1:]

#     tree = buildParseTree(equation)
#     eqn_table[variable] = equation
#     print(variable, equation)
#     # print(f'\nThe expression: {e} evaluates to: {evaluateParseTree(tree, eqn_table)}')
#     print(f"This is the hashtable: {eqn_table.keys} => {eqn_table.buckets}\n")

for e in [a, b]:
    eq_idx = e.index("=")  # get idx of equal
    variable = e[:eq_idx]
    equation = e[eq_idx + 1:]

    tree = ParseTree(equation)
    eqn_table[variable] = equation
    
    tree.buildParseTree()
    
    # tree.printPreorder(0)
    
    
    print(f'\nThe expression: {e} evaluates to: {evaluateParseTree(tree, eqn_table)}')
    # print(f"This is the hashtable: {eqn_table.keys} => {eqn_table.buckets}\n")