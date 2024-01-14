'''
Name:       Liang Zheng Kai Lucas & Muhammad Fitri Amir Bin Abdullah
Admin No.:  2222770
Class:      DAAA2B06

DSAA Assignment 2
'''

import os,random,re
# import shutil
# from os.path import exists,isfile, isdir, join
from typing import List, Tuple
from Tools.binaryTree import BinaryTree
from Tools.stack import Stack

# General Function Purposes for our main program
class Utilities:
    
    # Function to let users to press any key to continue 
    @staticmethod
    def press_anywhere(): 
        # Allows users to press key to continue
        if os.name == 'nt': # Windows systems
            print('\nPress enter key, to continue....', end=' ')
            os.system('pause >nul') # prevent redirection
            print('\n')
        else:
            os.system("""bash -c 'read -s -n 1 -p "Press Any Key, to continue..."'""")
            print('\n')
            
    # Function to get user's (numeric) choice
    @staticmethod
    def get_choice(choice_array):
        # If user does not enter a proper numeric choice, will prompt them to re-enter
        while True:
            min, max = 1, len(choice_array)
            choices = list(f'\t{idx+1}: {words}' for idx, words in enumerate(choice_array))
            message = f"Please select your choice: {str(tuple(range(1,len(choice_array)+1))).replace(' ', '') }\n" + '\n'.join(choices) + '\nEnter choice: '
            try:
                user_input = int(input(message).strip())
                if user_input >=min and user_input<=max:
                    return user_input
                else:
                    print(f'\nNot an Integer between {min} to {max}. Please choose an appropriate choice.\n')
                    continue
            except Exception:
                print(f'\nNot an Integer between {min} to {max}\n')
                continue
    
    @staticmethod
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
    
    @staticmethod
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
            elif op == '**':
                return evaluateParseTree(leftTree) ** evaluateParseTree(rightTree)
            elif op == '/':
                return evaluateParseTree(leftTree) / evaluateParseTree(rightTree)
        else:
            return tree.getKey()