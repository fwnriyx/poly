'''
Name:       Liang Zheng Kai Lucas & Muhammad Fitri Amir Bin Abdullah
Admin No.:  2222770
Class:      DAAA2B06

DSAA Assignment 2
'''

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
    

'''
Main Program:
leftTree = BinaryTree('Chapter 1',
BinaryTree('Section 1.1'),
BinaryTree('Section 1.2',
BinaryTree('Section 1.2.1'),
None))
rightTree = BinaryTree('Chapter 2',
BinaryTree('Section 2.1'),
BinaryTree('Section 2.2',
BinaryTree('Section 2.2.1'),
BinaryTree('Section 2.2.2')) )
tree = BinaryTree('Contents', leftTree, rightTree)
tree.printPreorder(0)
'''