"""
------------------------------------------------------------------------
Looks for a part of a given string
Task 3
------------------------------------------------------------------------
Author: Evan Attfield
ID:     180817010
Email:  attf7010@mylaurier.ca
Last Updated: Nov 15, 2018
------------------------------------------------------------------------
"""
from functions import my_find

s = input('String to search: ')
r = input('String to search for: ')
i = my_find(s, r)

print("'{}' is found at location {} in '{}'".format(r, i, s))