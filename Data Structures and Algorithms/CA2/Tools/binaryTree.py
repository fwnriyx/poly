'''
Name:       Liang Zheng Kai Lucas & Muhammad Fitri Amir Bin Abdullah
Admin No.:  2222770
Class:      DAAA2B06

DSAA Assignment 2
'''

import re

# BinaryTree Class
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
    
    # def printPreorder(self, level):
    #     print( str(level*'.') + str(self.key))
    #     if self.leftTree != None:
    #         self.leftTree.printPreorder(level+1)
    #     if self.rightTree != None:
    #         self.rightTree.printPreorder(level+1) 
    
    def printPreorder(self, level):
        if self.rightTree != None:
            self.rightTree.printPreorder(level+1)
        print(str(level*'.') + str(self.key))
        if self.leftTree != None:
            self.leftTree.printPreorder(level+1)
        if self.rightTree == None or self.leftTree==None:
            print('hi')