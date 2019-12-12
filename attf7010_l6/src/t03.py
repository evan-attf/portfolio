"""
------------------------------------------------------------------------
Task 3
------------------------------------------------------------------------
Author: Evan Attfield
ID:     180817010
Email:  attf7010@mylaurier.ca
Last Updated: Oct 30, 2018
------------------------------------------------------------------------
"""
from functions import sum_partial_harmonic

num = int(input('Enter n: '))
total = sum_partial_harmonic(num)
print('The sum of the series 1 to 1/3 is: {}'.format(total))