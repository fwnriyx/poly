'''
Name:       Liang Zheng Kai Lucas & Muhammad Fitri Amir Bin Abdullah
Admin No.:  2222770
Class:      DAAA2B06

DSAA Assignment 2
'''

import os, random, re
# import shutil
from os.path import exists,isfile, isdir, join
from typing import List, Tuple
from Tools.binaryTree import BinaryTree
from Tools.stack import Stack
from Tools.parseTree import ParseTree
    
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
            message = f"Please select your choice: {str(tuple(range(1,len(choice_array)+1))).replace(' ', '') }:\n" + '\n'.join(choices) + '\nEnter choice: '
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
            
    # Function to read data from a file # Improve this
    @staticmethod
    def get_file_data(filename):
        while True:
            try:
                io_file = filename
                if io_file == '':
                    return False , io_file
                assert exists(io_file), '\nInvalid file (doesnt exist)'
                assert isfile(io_file), '\nNot a file'
                assert io_file.endswith('.txt'), '\nMake sure it ends with .txt!'
                with open(io_file, 'r') as f:
                    data = f.read()
                return data, io_file
            except (OSError, Exception) as e:
                print(e)
                return "error", io_file
    
    @staticmethod      
    def tokenize_expression(exp):
        # Use regular expression to tokenize the expression
        # \d+ is one or more digits, \. is a literal dot, \S is one or more non-whitespace characters and | is an OR operator, [a-zA-Z]+ is one or more letters
        pattern = r'\d+\.\d+|\d+|[a-zA-Z]+|\S'
        return re.findall(pattern, exp)
    
    @staticmethod
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
    
    @staticmethod
    def evaluateParseTree(tree, hashtable):
        leftTree = tree.getLeftTree()
        rightTree = tree.getRightTree()
        op = tree.getKey()
        
        if leftTree != None and rightTree != None:
           
            # Replace left tree and right tree if they are variables
            if str(leftTree.getKey()).isalpha():
                try:
                    eqn = hashtable[leftTree.getKey()]
                    tree = ParseTree(eqn)
                    parse_tree = tree.buildParseTree()
                    new_key = Utilities.evaluateParseTree(parse_tree, hashtable)
                    leftTree.setKey(new_key)
                except TypeError:
                    return None
            elif str(rightTree.getKey()).isalpha():
                try:
                    eqn = hashtable[rightTree.getKey()]
                    tree = ParseTree(eqn)
                    parse_tree = tree.buildParseTree()
                    new_key = Utilities.evaluateParseTree(parse_tree, hashtable)
                    leftTree.setKey(new_key)
                except TypeError:
                    return None
            
            # Evaluate Parse Tree  
            if op == '+':
                try:
                    return Utilities.evaluateParseTree(leftTree, hashtable) + Utilities.evaluateParseTree(rightTree, hashtable)
                except TypeError:
                    return None
            elif op == '**':
                try:
                    return Utilities.evaluateParseTree(leftTree, hashtable) ** Utilities.evaluateParseTree(rightTree, hashtable)
                except TypeError:
                    return None
            elif op == '-':
                try:
                    return Utilities.evaluateParseTree(leftTree, hashtable) - Utilities.evaluateParseTree(rightTree, hashtable)
                except TypeError:
                    return None
            elif op == '*':
                try:
                    return Utilities.evaluateParseTree(leftTree, hashtable) * Utilities.evaluateParseTree(rightTree, hashtable)
                except TypeError:
                    return None
            elif op == '/':
                try:
                    return Utilities.evaluateParseTree(leftTree, hashtable) / Utilities.evaluateParseTree(rightTree, hashtable)
                except TypeError:
                    return None
        else:
            return tree.getKey()