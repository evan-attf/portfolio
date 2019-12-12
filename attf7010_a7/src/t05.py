"""
------------------------------------------------------------------------
Validates an ISBN
Task 5
------------------------------------------------------------------------
Author: Evan Attfield
ID:     180817010
Email:  attf7010@mylaurier.ca
Last Updated: Nov 15, 2018
------------------------------------------------------------------------
"""
from functions import is_valid_isbn

isbn = input('Enter an ISBN: ')
valid = is_valid_isbn(isbn)

if valid == True:
    print('{} is a valid ISBN'.format(isbn))
else:
    print('{} is not a valid ISBN'.format(isbn))