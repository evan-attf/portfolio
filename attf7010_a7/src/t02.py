"""
------------------------------------------------------------------------
Checks if all chars are letters
Task 2
------------------------------------------------------------------------
Author: Evan Attfield
ID:     180817010
Email:  attf7010@mylaurier.ca
Last Updated: Nov 15, 2018
------------------------------------------------------------------------
"""
from functions import my_isalpha

s = input('Enter a string to test: ')
alpha = my_isalpha(s)

if alpha == True:
    print('The string is all letters')
else:
    print('The string contains non-letters')