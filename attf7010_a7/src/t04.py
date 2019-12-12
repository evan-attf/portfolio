"""
------------------------------------------------------------------------
Finds the longest common ending of two string
Task 4
------------------------------------------------------------------------
Author: Evan Attfield
ID:     180817010
Email:  attf7010@mylaurier.ca
Last Updated: Nov 15, 2018
------------------------------------------------------------------------
"""
from functions import common_ending

s1 = input('First string: ')
s2 = input('Second string: ')
common = common_ending(s1, s2)

print('Common ending: {}'.format(common))