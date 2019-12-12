"""
------------------------------------------------------------------------
Task 3
------------------------------------------------------------------------
Author: Evan Attfield
ID:     180817010
Email:  attf7010@mylaurier.ca
Last Updated: Sept 26, 2018
------------------------------------------------------------------------
"""

L_COST = 75
S_COST = 50

l_num = int(input('Number of large dogs groomed: '))
s_num = int(input('Number of small dogs groomed: '))

total = (L_COST * l_num) + (S_COST * s_num)
print('Total earned for the day: ${:,.2f}.'.format(total))