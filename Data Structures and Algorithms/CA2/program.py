'''
Name:       Liang Zheng Kai Lucas & Muhammad Fitri Amir Bin Abdullah
Admin No.:  2222770
Class:      DAAA2B06

DSAA Assignment 2
'''

# Imports
import os
from utilities import Utilities
from Tools.hashTable import HashTable
from Tools.parseTree import ParseTree
# from random import shuffle, choice

hashtable = HashTable(1)

class Program:
    # My details
    def __init__(self, config):
        # Load configuration regarding assignment details
        self.__name, self.__admin, self.__class = config['author']['name'], config['author']['adminNo'], config['author']['class']
        self.__module = config['application_welcome']
        self.__module_code = config['module_code']
    
    # Run the main loop/menu of the program. Allow users to select options
    def run(self):
        self.__print_start()
        while True:
            Utilities.press_anywhere()
            options = ["Add/Modify assignment statement", "Display current assignment statements", "Evaluate a single variable", "Read assignment statements from file", "Sort assignment statements", "Exit"]
            user_choice = Utilities.get_choice(choice_array=options)
            if user_choice == 1:
                self.__choice1()
            elif user_choice == 2:
                self.__choice2()
            elif user_choice == 3:
                self.__choice3()
            elif user_choice == 4:
                self.__choice4()
            elif user_choice ==5:
                self.__choice5()
            elif user_choice == 6:
                self.__choice6()
                return
    
    # Print initial banner and assignment details
    def __print_start(self):
        print()
        print('*' * 60)
        print(f'* {self.__module}*')
        print('*' + '-' * 58 + '*')

        print('*',' '*56 ,'*')
        print("""*  -""", 'Done by:', f'{self.__name}', ' '*12, '*')
        print("""*  -""", 'Class:', f'{self.__class}', ' '*37, '*')
        print('*' * 60)
        
    # Option 1: Add/Modify assignment statement
    def __choice1(self):
        
        # Initialize Hashtable of size 1 first
        # Hashtable is dynamic and expands when there is not enough space
        
        # Get statement 
        statement = input("Enter the assignment statement you want to add/modify:\nFor example, a=(1+2)\n").strip()
        
        # ADD INPUT VALIDATION HERE
        # statement = function(statement)
        
        # Separate variable and equation
        equal_idx = statement.index("=")  # get idx of equal
        variable = statement[:equal_idx]
        equation = statement[equal_idx + 1:]
        
        # Store in hashtable
        hashtable[variable] = equation
        # print(f"This is the hashtable: {hashtable.keys} => {hashtable.buckets}\n")
        
    # Option 2: Display current assignment statements
    # Might have to change this to sort results?
    def __choice2(self):
        # Check that there are statements
        if len(hashtable.keys) == 1 and hashtable.keys[0] == None:
            print("There are currently no stored assignments, please add an assignment before continuing.")
            return
        
        print("\nCURRENT ASSIGNMENTS:")
        print("*" * 20)
        
        # Get keys and buckets
        keys = hashtable.keys
        buckets =  hashtable.buckets
        
        # Display results
        for i in range(len(keys)):
            if keys[i] != None:
                # solve eqaution
                eqn = buckets[i]
                tree = ParseTree(eqn)
                parse_tree = tree.buildParseTree()
                solved = Utilities.evaluateParseTree(parse_tree, hashtable)
                print(f'{keys[i]}={eqn}=>{solved}')
    
    # Evaluate a single variable   
    def __choice3(self):
        # Check that there are statements
        if len(hashtable.keys) == 1 and hashtable.keys[0] == None:
            print("There are currently no stored assignments, please add an assignment before continuing.")
            return
             
        variable = input("Please enter the variable you want to evaluate:\n").strip()
        
        # Get bucket
        equation = hashtable[variable]
        
        # Validation for variable input 
        while equation is None:
            variable = input("\nThe variable does not exist\n\nPlease enter the variable you want to evaluate:\n").strip()
            equation = hashtable[variable]
        
        # solve the eqn
        tree = Utilities.buildParseTree(equation)
        solved = Utilities.evaluateParseTree(tree, hashtable)
        
        print(f'\nExpression Tree:')
        tree.printPreorder(0)
        print(f'Value for variable "{variable}" is {solved}')
        
    def __choice4(self):
        filename = input("\nPlease enter the file you want to analyze: ").strip()
        text, file = Utilities.get_file_data(filename)
        if file == '':
            print("No filename was entered.")
            return
        elif text == 'error':
            return
        else:
            return
        
    # Option 6: Exit the Program
    def __choice6(self):
        print()
        print(f'Bye, thanks for using {self.__module_code}/DSAA: Evaluating and Sorting Assignment Statement')