'''
Name:       Liang Zheng Kai Lucas & Muhammad Fitri Amir Bin Abdullah
Admin No.:  2222770
Class:      DAAA2B06

DSAA Assignment 2
'''

import re
from utilities import Utilities
from stack import Stack
from binaryTree import BinaryTree

# ParseTree child class
class ParseTree(BinaryTree):
    def __init__(self, expression):
        self.expression = expression
        super().__init__('?')
        
    def buildParseTree(self):
        tokens = Utilities.tokenize_expression(self.expression)
        tokens = Utilities.exponentConverter(tokens)              
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