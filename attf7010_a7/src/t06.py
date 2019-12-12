"""
------------------------------------------------------------------------
Converts letters in a phone # to digits
Task 6
------------------------------------------------------------------------
Author: Evan Attfield
ID:     180817010
Email:  attf7010@mylaurier.ca
Last Updated: Nov 15, 2018
------------------------------------------------------------------------
"""
from functions import number_convert

number = input('Enter phone number: ')
digits = number_convert(number)

print('Digits: {}'.format(digits))