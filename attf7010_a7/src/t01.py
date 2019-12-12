"""
------------------------------------------------------------------------
Checks if all chars in a string are digits
Task 1
------------------------------------------------------------------------
Author: Evan Attfield
ID:     180817010
Email:  attf7010@mylaurier.ca
Last Updated: Nov 15, 2018
------------------------------------------------------------------------
"""
from functions import my_isdigit

s = input('Enter a string to test: ')
digits = my_isdigit(s)

if digits == True:
    print('The string is all digits')
else:
    print('The string contains non-digits')