'''
Name:       Liang Zheng Kai Lucas & Muhammad Fitri Amir Bin Abdullah
Admin No.:  2222770
Class:      DAAA2B06

DSAA Assignment 2
'''

# Imports
import os
from utilities import Utilities
# from random import shuffle, choice


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
        print()
        
    
    # Option 6: Exit the Program
    def __choice6(self):
        print()
        print(f'Bye, thanks for using {self.__module_code}/DSAA: Evaluating and Sorting Assignment Statement')