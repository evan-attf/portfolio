"""
------------------------------------------------------------------------
Task 8
Checks for a Leap Year
------------------------------------------------------------------------
Author: Evan Attfield
ID:     180817010
Email:  attf7010@mylaurier.ca
Last Updated: Oct 30, 2018
------------------------------------------------------------------------
"""
from functions import is_leap

year = int(input('Enter a year (>0): '))
result = is_leap(year)

if result == True:
    print('{} is a leap year'.format(year))
else:
    print('{} is a not leap year'.format(year))
    