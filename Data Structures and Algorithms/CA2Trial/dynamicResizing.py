import re

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

    # def rehashFunction(self, oldHash):
    #     return (oldHash + 1) % self.size

    def rehashFunction(self, oldHash, attempt):
        return (oldHash + attempt) % self.size

    def _resize_and_rehash(self):
        new_size = self.size * 2
        new_keys = [None] * new_size
        new_buckets = [None] * new_size

        # Use a while loop to ensure all non-empty buckets are processed
        index = 0
        while index < self.size:
            if self.keys[index] is not None:
                # new_index = self.hashFunction(self.keys[index], self.size)  # Use the new size for hashing
                new_index = self.hashFunction(self.keys[index], new_size)
                attempt = 1
                # while new_buckets[new_index] is not None:
                #     print("Collision")
                #     new_index = self.rehashFunction(new_index)
                while new_buckets[new_index] is not None:
                    print("Collision")
                    new_index = self.rehashFunction(new_index, attempt)
                    attempt += 1
                new_keys[new_index] = self.keys[index]
                new_buckets[new_index] = self.buckets[index]
            index += 1

        self.size = new_size  # Update the hash table size
        self.keys = new_keys
        self.buckets = new_buckets

    def __setitem__(self, key, value):
        index = self.hashFunction(key, self.size)
        startIndex = index
        attempt = 1
        while True:
            if self.keys[index % self.size] is None or self.keys[index % self.size] == key:
                self.buckets[index % self.size] = value
                self.keys[index % self.size] = key
                break
            else:
                index = self.rehashFunction(index, attempt)
                attempt += 1
                if index == startIndex:
                    # Resize the hash table if necessary
                    if sum(bucket is not None for bucket in self.buckets) >= self.size:
                        self._resize_and_rehash()
                        # Recalculate the index using the new size
                        index = self.hashFunction(key, self.size)
                        #insert the key and value
                        self.buckets[index % self.size] = value
                        self.keys[index % self.size] = key
                        break

    def __getitem__(self, key):
        index = self.hashFunction(key, self.size)
        startIndex = index
        attempt = 1
        while True:
            if self.keys[index % self.size] == key:
                return self.buckets[index % self.size]
            else:
                index = self.rehashFunction(startIndex, attempt)
                attempt += 1
                if index == startIndex:
                    return None


def tokenize_expression(exp):
    # Use regular expression to tokenize the expression
    # \d+ is one or more digits, \. is a literal dot, \S is one or more non-whitespace characters and | is an OR operator, [a-zA-Z]+ is one or more letters
    pattern = r'\d+\.\d+|\d+|[a-zA-Z]+|\S'
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

# Parse Tree Builder and Solver
def buildParseTree(exp):
        # tokens = exp.split()
        tokens = tokenize_expression(exp)
        tokens = exponentConverter(tokens)
        # print(tokens)
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
            elif t not in ['+', '-', '*', '/', ')', '**'] :
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

def evaluateParseTree(tree, hashtable):
        leftTree = tree.getLeftTree()
        rightTree = tree.getRightTree()
        op = tree.getKey()
        if leftTree != None and rightTree != None:
            try:
                if op == '+':
                    return evaluateParseTree(leftTree, hashtable) + evaluateParseTree(rightTree, hashtable)
                elif op == '**':
                    return evaluateParseTree(leftTree, hashtable) ** evaluateParseTree(rightTree, hashtable)
                elif op == '-':
                    return evaluateParseTree(leftTree, hashtable) - evaluateParseTree(rightTree, hashtable)
                elif op == '*':
                    return evaluateParseTree(leftTree, hashtable) * evaluateParseTree(rightTree, hashtable)
                elif op == '/':
                    return evaluateParseTree(leftTree, hashtable) / evaluateParseTree(rightTree, hashtable)
            except TypeError:
                if isinstance(tree.getKey(), str):
                    variable_value = hashtable[tree.getKey()]
                    if variable_value is not None or tree.getKey() in hashtable.keys:
                        return variable_value
        else:
            return tree.getKey()

exp = 'A=(2*(2*2))'
exp1 = 'B=(2*10)'
exp2 = 'C=(2+6.4)'
exp3 = 'D=(4+(5+6))'
exp4 = 'E=(2**6.4)'

eqn_table = HashTable(1)

for e in [exp, exp1, exp2, exp3, exp4]:
    eq_idx = e.index("=")  # get idx of equal
    variable = e[:eq_idx]
    equation = e[eq_idx + 1:]

    tree = buildParseTree(equation)
    eqn_table[variable] = equation
    print(variable, equation)
    print(f'The expression: {e} evaluates to: {evaluateParseTree(tree, eqn_table)}')
    print(f"This is the hashtable: {eqn_table.keys} => {eqn_table.buckets}")
