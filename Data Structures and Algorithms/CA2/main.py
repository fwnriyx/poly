'''
Name:       Liang Zheng Kai Lucas & Muhammad Fitri Amir Bin Abdullah
Admin No.:  2222770
Class:      DAAA2B06

DSAA Assignment 2
'''

from program import Program

# Application configuration in dictionary format that can be changed.

APP_CONFIG = {'author':
    {'name': 'Lucas(2222770) & Fitri(2222811)', 
    'class': 'DAAA2B06', 
    'adminNo': '2222770'}, 
    'application_welcome': 'ST1507 DSAA: Evaluating and Sorting Assignment Statement ',
    'module_code': 'ST1507'}

# Runs the main program
program = Program(APP_CONFIG)
program.run()