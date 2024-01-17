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
        tokens = exp.split()
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
            elif t in ['+', '-', '*', '/']:
                currentTree.setKey(t)
                currentTree.insertRight('?')
                stack.push(currentTree)
                currentTree = currentTree.getRightTree()
                    
        # RULE 3: If token is number, set key of the current node
        # to that number and return to parent
            elif t not in ['+', '-', '*', '/', ')'] :
                currentTree.setKey(int(t))
                parent = stack.pop()
                currentTree = parent
                
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
exp = '( 2 + ( 4 * 5 ) )'
tree = buildParseTree(exp)
tree.printPreorder(0)
print (f'The expression: {exp} evaluates to: {evaluateParseTree(tree)}')   