import re

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
    print(splitExp)
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
        print(tokens)
        tokens = exponentConverter(tokens)
        stack = Stack()
        tree = BinaryTree('*')
        stack.push(tree)
        currentTree = tree
        for t in tokens:
        # RULE 1: If token is '(' add a new node as left child
        # and descend into that node
            if t == '(':
                currentTree.insertLeft('*')
                stack.push(currentTree)
                currentTree = currentTree.getLeftTree()
            #Currently, its going into the right case
            #but for some reason, there is a 2 at the start and a ? instead of a 2 at the end..
            elif t in '**':
                #Make it such that it loops downwards the amount of times the exponent is
                #First, insert asterisk, then insert number, loop that
                idx = tokens.index(t)
                #Loop
                try:
                    timetoLoop = int(tokens[idx+1]) 
                    for i in range(timetoLoop - 1):
                        #Insert asterisk
                        # currentTree.setKey("h")
                        currentTree.insertRight('*')
                        stack.push(currentTree)
                        currentTree = currentTree.getRightTree()
                        print("Inserting asterisk")

                        #Insert right child
                        # currentTree.setKey(tokens[idx - 1])
                        # currentTree.insertRight(tokens[idx - 1])
                        currentTree.insertRight(tokens[idx - 1])
                        stack.push(currentTree)
                        currentTree = currentTree.getRightTree()
                    # #Drop the exponent from the list
                    tokens.remove(tokens[idx+1])
                except ValueError:
                    print("Its a letter!")
                
        # RULE 2: If token is operator set key of current node
        # to that operator and add a new node as right child
        # and descend into that node
            elif t in ['+', '-', '*', '/']:
                print("Wrong part")
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
    
def evaluateParseTree(tree):
        leftTree = tree.getLeftTree()
        rightTree = tree.getRightTree()
        op = tree.getKey()
        
        if leftTree != None and rightTree != None:
            # Add code here to check for variable in equation
            '''
            b=(a+(2*4))
            1. Handle exponents
            
            return evaluateParseTree(leftTree)
            '''
            
            # if op == '*' and leftTree =='*':
            #     return evaluateParseTree(leftTree) ** evaluateParseTree(rightTree)
            # if op == '*' and rightTree =='*':
            #     return evaluateParseTree(leftTree) ** evaluateParseTree(rightTree)
            
            if op == '+':
                return evaluateParseTree(leftTree) + evaluateParseTree(rightTree)
            elif op == '-':
                return evaluateParseTree(leftTree) - evaluateParseTree(rightTree)
            elif op == '*':
                return evaluateParseTree(leftTree) * evaluateParseTree(rightTree)
            elif op == '/':
                return evaluateParseTree(leftTree) / evaluateParseTree(rightTree)
            
        else:
            return tree.getKey()
        
# Main Program
exp = 'a=(apple ** 5)'
eq_idx = exp.index("=") # get idx of equal

# Slicing and storing variable and equation in new vars
variable = exp[:eq_idx]
equation = exp[eq_idx + 1:]


tree = buildParseTree(equation)
tree.printPreorder(0)

print (f'The expression: {exp} evaluates to: {evaluateParseTree(tree)}')  
print (f'{exp}=> {evaluateParseTree(tree)}') 